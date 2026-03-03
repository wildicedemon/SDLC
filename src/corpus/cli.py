from pathlib import Path

import click


@click.group()
def cli() -> None:
    """Corpus — Hybrid corpus management system."""


@cli.command()
def init() -> None:
    """Initialize DB, run migrations, create data dirs."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine
    from corpus.db.migrations.runner import migrate_forward

    settings = get_settings()
    settings.ensure_data_dirs()
    engine = create_db_engine(settings.db_url)
    applied = migrate_forward(engine)
    if applied:
        click.echo(f"Applied migrations: {', '.join(applied)}")
    else:
        click.echo("Database already up to date.")


@cli.command()
@click.option("--rollback", is_flag=True, help="Rollback last migration.")
def migrate(rollback: bool) -> None:
    """Run pending schema migrations."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine
    from corpus.db.migrations.runner import migrate_forward, migrate_rollback

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    if rollback:
        rolled = migrate_rollback(engine)
        if rolled:
            click.echo(f"Rolled back migration: {rolled}")
        else:
            click.echo("Nothing to roll back.")
    else:
        applied = migrate_forward(engine)
        if applied:
            click.echo(f"Applied migrations: {', '.join(applied)}")
        else:
            click.echo("Database already up to date.")


@cli.command()
@click.argument("source")
@click.option("--base", default="main", help="Base branch to diff against.")
@click.option("--repo-path", default=".", help="Path to the git repository.")
def ingest(source: str, base: str, repo_path: str) -> None:
    """Ingest artifacts from a branch or worktree."""
    import sys

    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.db.repository import CorpusRepository
    from corpus.ingestion.pipeline import run_ingest

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        result = run_ingest(repo, repo_path, source, base, corpus_root=repo_path)

    if result.failed:
        click.echo("Ingestion FAILED — unclassified files:")
        for f in result.unclassified_files:
            click.echo(f"  {f}")
        click.echo(f"Run ID: {result.run_id} (status=failed)")
        sys.exit(1)

    click.echo(f"Ingested {result.artifacts_ingested} artifacts, {result.chunks_created} chunks.")
    if result.unclassified_files:
        click.echo(f"Skipped {len(result.unclassified_files)} unclassified files.")
    click.echo(f"Run ID: {result.run_id}")


@cli.command()
@click.argument("run_id")
def dedup(run_id: str) -> None:
    """Run 3-layer dedup pipeline for a consolidation run."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.dedup.pipeline import run_dedup

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        report = run_dedup(session, run_id, settings=settings)

    click.echo(f"Dedup complete for run {run_id}:")
    click.echo(f"  Candidates: {report.candidate_count}")
    click.echo(f"  Confirmed dups: {report.confirmed_dups}")
    click.echo(f"  Arbitrated: {report.arbitrated}")
    click.echo(f"  Human queued: {report.human_queued}")
    click.echo(f"  L3 rate: {report.l3_rate:.1%}")
    if report.l3_rate_alert:
        click.echo("  WARNING: L3 rate exceeds threshold")
    if report.arbitration_fallback:
        click.echo("  WARNING: Arbitration fallback — all disagreements routed to human queue")


@cli.command("update-decisions")
@click.argument("run_id")
def update_decisions(run_id: str) -> None:
    """Recompute impacted DecisionCards and indices."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.db.repository import CorpusRepository
    from corpus.decisions.card_updater import update_impacted_cards
    from corpus.decisions.drift_detector import detect_drift
    from corpus.decisions.index_updater import update_indices

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        all_cards = repo.list_decision_cards()
        previous_scores = {str(c.decision_id): float(c.confidence_score) for c in all_cards}

        updated_ids = update_impacted_cards(session, run_id)
        update_indices(session, updated_ids)
        drift_ids = detect_drift(session, run_id, previous_scores)

    click.echo(f"Updated {len(updated_ids)} decision cards.")
    click.echo(f"Drift events created: {len(drift_ids)}")


@cli.command("generate-decisions")
@click.argument("run_id")
@click.option("--domain", multiple=True, help="Specific domain(s) to generate for. Omit for all.")
@click.option("--dry-run", is_flag=True, help="Show what would be generated without calling LLM.")
def generate_decisions_cmd(run_id: str, domain: tuple[str, ...], dry_run: bool) -> None:
    """Generate DecisionCards from ingested artifacts using LLM deep research."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.decisions.generator import generate_decisions

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        report = generate_decisions(
            session,
            run_id,
            settings=settings,
            domains=list(domain) if domain else None,
            dry_run=dry_run,
        )

    click.echo(f"\nGenerated: {report.generated}")
    click.echo(f"Skipped (existing): {report.skipped_existing}")
    click.echo(f"Skipped (structural): {report.skipped_structural}")
    click.echo(f"Failed: {report.failed}")
    if report.details:
        click.echo("\nDetails:")
        for d in report.details:
            click.echo(f"  {d}")


@cli.command("check-references")
@click.argument("run_id")
@click.option("--corpus-root", default=".", help="Path to the corpus root.")
def check_references(run_id: str, corpus_root: str) -> None:
    """Validate reference integrity for a run."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.references.integrity_validator import validate_integrity
    from corpus.references.rewrite_mapper import generate_rewrite_map
    from corpus.references.rewriter import rewrite_references

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        rmap = generate_rewrite_map(session, run_id)
        rewrites = rewrite_references(rmap, corpus_root)
        report = validate_integrity(session, run_id, corpus_root)

    click.echo(f"Rewrites applied: {rewrites}")
    click.echo(f"Integrity check: {'PASSED' if report.passed else 'FAILED'}")
    click.echo(f"  Total checked: {report.total_checked}")
    if report.broken_links:
        click.echo(f"  Broken links: {len(report.broken_links)}")
        for link in report.broken_links:
            click.echo(f"    {link}")
    if report.stale_paths:
        click.echo(f"  Stale paths: {len(report.stale_paths)}")
        for p in report.stale_paths:
            click.echo(f"    {p}")


@cli.command("sync-derived")
@click.argument("run_id")
def sync_derived(run_id: str) -> None:
    """Sync vector + graph layers from relational."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.sync.graph_sync import sync_graph
    from corpus.sync.vector_sync import sync_vectors

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        vr = sync_vectors(session, run_id, settings=settings)
        gr = sync_graph(session, run_id, settings=settings)

    click.echo(f"Vectors synced: {vr.synced}/{vr.total}")
    click.echo(f"Graph nodes added: {gr.nodes_added}, edges added: {gr.edges_added}")


@cli.command()
@click.argument("run_id")
@click.option("--corpus-root", default=".", help="Path to the corpus root.")
def complete(run_id: str, corpus_root: str) -> None:
    """Run all gates and mark run complete/fail."""
    from corpus.config import get_settings
    from corpus.consolidation.run_controller import complete_run
    from corpus.db.engine import create_db_engine, get_session

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        passed = complete_run(session, run_id, corpus_root=corpus_root, settings=settings)

    if passed:
        click.echo(f"Run {run_id} completed successfully.")
    else:
        click.echo(f"Run {run_id} FAILED gates. See remediation_report for details.")


@cli.command()
@click.argument("source")
@click.option("--base", default="main", help="Base branch to diff against.")
@click.option("--repo-path", default=".", help="Path to the git repository.")
def run(source: str, base: str, repo_path: str) -> None:
    """Full pipeline: ingest -> dedup -> update -> check -> sync -> complete."""
    import sys

    from corpus.config import get_settings
    from corpus.consolidation.run_controller import complete_run
    from corpus.db.engine import create_db_engine, get_session
    from corpus.db.repository import CorpusRepository
    from corpus.decisions.card_updater import update_impacted_cards
    from corpus.decisions.drift_detector import detect_drift
    from corpus.decisions.index_updater import update_indices
    from corpus.dedup.pipeline import run_dedup
    from corpus.ingestion.pipeline import run_ingest
    from corpus.references.integrity_validator import validate_integrity
    from corpus.references.rewrite_mapper import generate_rewrite_map
    from corpus.references.rewriter import rewrite_references
    from corpus.sync.graph_sync import sync_graph
    from corpus.sync.vector_sync import sync_vectors

    settings = get_settings()
    engine = create_db_engine(settings.db_url)

    with get_session(engine) as session:
        repo = CorpusRepository(session)

        click.echo("Step 1/6: Ingesting...")
        ingest_result = run_ingest(repo, repo_path, source, base, corpus_root=repo_path)
        if ingest_result.failed:
            click.echo(f"Ingestion FAILED: {len(ingest_result.unclassified_files)} unclassified files")
            sys.exit(1)
        run_id = ingest_result.run_id
        n_art = ingest_result.artifacts_ingested
        n_chk = ingest_result.chunks_created
        click.echo(f"  Ingested {n_art} artifacts, {n_chk} chunks (run={run_id})")
        if ingest_result.unclassified_files:
            click.echo(f"  Skipped {len(ingest_result.unclassified_files)} unclassified files")

        click.echo("Step 2/6: Dedup...")
        dedup_report = run_dedup(session, run_id, settings=settings)
        click.echo(f"  Candidates: {dedup_report.candidate_count}, Confirmed: {dedup_report.confirmed_dups}")

        click.echo("Step 3/6: Updating decisions...")
        all_cards = repo.list_decision_cards()
        prev_scores = {str(c.decision_id): float(c.confidence_score) for c in all_cards}
        updated_ids = update_impacted_cards(session, run_id)
        update_indices(session, updated_ids)
        detect_drift(session, run_id, prev_scores)
        click.echo(f"  Updated {len(updated_ids)} cards")

        click.echo("Step 4/6: Checking references...")
        rmap = generate_rewrite_map(session, run_id)
        rewrite_references(rmap, repo_path)
        validate_integrity(session, run_id, repo_path)

        click.echo("Step 5/6: Syncing derived layers...")
        sync_vectors(session, run_id, settings=settings)
        sync_graph(session, run_id, settings=settings)

        click.echo("Step 6/6: Running completion gates...")
        passed = complete_run(session, run_id, corpus_root=repo_path, settings=settings)

    if passed:
        click.echo(f"Pipeline complete. Run {run_id} PASSED all gates.")
    else:
        click.echo(f"Pipeline finished. Run {run_id} FAILED gates.")
        sys.exit(1)


@cli.group()
def review() -> None:
    """Manage human review queue."""


@review.command("list")
@click.option("--run-id", default=None, help="Filter by run ID.")
def review_list(run_id: str | None) -> None:
    """List unresolved human review items."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.db.models import HumanReviewQueue
    from corpus.db.repository import CorpusRepository

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        if run_id:
            items = repo.list_unresolved_reviews(run_id)
        else:
            items = list(session.query(HumanReviewQueue).filter(HumanReviewQueue.disposition.is_(None)).all())

    if not items:
        click.echo("No unresolved review items.")
        return

    for item in items:
        click.echo(
            f"  [{item.id}] run={item.run_id} type={item.item_type} "
            f"a={item.artifact_a_id} b={item.artifact_b_id} "
            f"confidence={item.ai_confidence} rec={item.ai_recommendation}"
        )


@review.command("resolve")
@click.argument("item_id", type=int)
@click.argument("disposition")
def review_resolve(item_id: int, disposition: str) -> None:
    """Resolve a review item with a disposition."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.db.repository import CorpusRepository

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        item = repo.resolve_review(item_id, disposition)

    if item is None:
        click.echo(f"Review item {item_id} not found.")
    else:
        click.echo(f"Resolved review item {item_id} with disposition: {disposition}")


@cli.command()
@click.argument("question")
@click.option("--depth", type=click.Choice(["L0", "L1", "L2", "L3"]), default=None, help="Retrieval depth.")
def query(question: str, depth: str | None) -> None:
    """Run a retrieval query."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.retrieval.orchestrator import query as run_query

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        resp = run_query(session, question, depth_override=depth, settings=settings)

    click.echo(f"Depth: {resp.depth} | Confidence: {resp.confidence:.2f}")
    if resp.escalation_reason:
        click.echo(f"Escalation: {resp.escalation_reason}")
    click.echo(resp.content)


@cli.command("rebuild-vectors")
def rebuild_vectors() -> None:
    """Full vector rebuild from relational."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.sync.vector_sync import rebuild_vectors as _rebuild

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        result = _rebuild(session, settings=settings)
    click.echo(f"Rebuilt vectors: {result.synced}/{result.total}")


@cli.command("rebuild-graph")
def rebuild_graph() -> None:
    """Full graph rebuild from relational."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.sync.graph_sync import rebuild_graph as _rebuild

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        result = _rebuild(session, settings=settings)
    click.echo(f"Rebuilt graph: {result.nodes_added} nodes, {result.edges_added} edges")


@cli.group()
def telemetry() -> None:
    """Telemetry and calibration commands."""


@telemetry.command("record")
@click.argument("decision_id")
@click.argument("outcome")
def telemetry_record(decision_id: str, outcome: str) -> None:
    """Record a decision outcome."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.telemetry.collector import record_outcome

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        record_outcome(session, decision_id, outcome)
    click.echo(f"Recorded outcome '{outcome}' for decision {decision_id}.")


@telemetry.command("calibrate")
def telemetry_calibrate() -> None:
    """Recompute confidence calibration."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.telemetry.calibrator import calibrate

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        report = calibrate(session)
    click.echo(f"Evaluated: {report.decisions_evaluated}, Recalibrated: {report.decisions_recalibrated}")
    for did, old, new in report.adjustments:
        click.echo(f"  {did}: {old:.2f} -> {new:.2f}")


@telemetry.command("metrics")
def telemetry_metrics() -> None:
    """Print operational metrics."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.telemetry.metrics import compute_metrics

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        m = compute_metrics(session)
    click.echo(f"Runs: {m.total_runs} ({m.completed_runs} completed)")
    click.echo(f"Artifacts: {m.total_artifacts}, Chunks: {m.total_chunks}")
    click.echo(f"Decisions: {m.total_decisions}, Drift events: {m.total_drift_events}")
    click.echo(f"Unresolved reviews: {m.unresolved_reviews}")
    click.echo(f"Contradiction density: {m.contradiction_density:.1%}")
    click.echo(f"Vector synced: {m.vector_synced_pct:.1%}")


@cli.command()
def status() -> None:
    """Show current run status, queue, sync health."""
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.db.models import ConsolidationRun, HumanReviewQueue
    from corpus.sync.health_checker import check_sync_health
    from corpus.telemetry.metrics import compute_metrics

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    with get_session(engine) as session:
        last_run = session.query(ConsolidationRun).order_by(ConsolidationRun.started_at.desc()).first()
        last_run_info = None
        if last_run:
            last_run_info = (str(last_run.run_id), str(last_run.status))
        unresolved = session.query(HumanReviewQueue).filter(HumanReviewQueue.disposition.is_(None)).count()
        health = check_sync_health(session, settings=settings)
        m = compute_metrics(session)

    if last_run_info:
        click.echo(f"Last run: {last_run_info[0]} (status={last_run_info[1]})")
    else:
        click.echo("No runs found.")
    click.echo(f"Human review queue: {unresolved} unresolved")
    click.echo(f"Sync health: {'HEALTHY' if health.healthy else 'UNHEALTHY'} (vectors={health.vector_synced_pct:.0%})")
    click.echo(f"Totals: {m.total_runs} runs, {m.total_artifacts} artifacts, {m.total_decisions} decisions")


@cli.command()
@click.option("--dir", "watch_dir", default=None, help="Directory to watch for new files (default: CORPUS_WATCH_DIR or C:\\Users\\Ice\\scrape)")
@click.option("--poll-interval", default=None, type=float, help="Seconds between poll cycles (default: 2.0)")
def watch(watch_dir: str | None, poll_interval: float | None) -> None:
    """Watch a drop-folder for new files and auto-ingest them."""
    import logging

    from corpus.config import get_settings
    from corpus.ingestion.watcher import watch as run_watch

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

    settings = get_settings()
    resolved_dir = Path(watch_dir) if watch_dir else Path(settings.watch_dir)
    resolved_interval = poll_interval if poll_interval is not None else settings.poll_interval

    click.echo(f"Watching {resolved_dir} (poll every {resolved_interval}s)")
    click.echo("Press Ctrl+C to stop.")
    run_watch(resolved_dir, poll_interval=resolved_interval)


@cli.command("ingest-file")
@click.argument("file_path", type=click.Path(exists=True, path_type=Path))
def ingest_file_cmd(file_path: Path) -> None:
    """Ingest a single file into the corpus."""
    import uuid
    from datetime import datetime, timezone

    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine, get_session
    from corpus.db.migrations.runner import migrate_forward
    from corpus.db.repository import CorpusRepository
    from corpus.ingestion.parsers import parse_file
    from corpus.ingestion.pipeline import ingest_file

    settings = get_settings()
    settings.ensure_data_dirs()
    engine = create_db_engine(settings.db_url)
    migrate_forward(engine)

    click.echo(f"Parsing {file_path} …")
    parsed = parse_file(file_path)
    click.echo(f"  Format: {parsed.source_format}, Title: {parsed.title}")

    with get_session(engine) as session:
        repo = CorpusRepository(session)

        run_id = f"cr_file_{uuid.uuid4().hex[:8]}"
        now = datetime.now(timezone.utc).isoformat()
        repo.create_run(
            run_id=run_id,
            source_branch="file",
            started_at=now,
            status="running",
        )

        ingest_file(
            file_path=file_path,
            content=parsed.content,
            title=parsed.title,
            metadata=parsed.metadata,
            session=session,
            run_id=run_id,
        )

        repo.update_run_status(run_id, "completed")

    click.echo(f"Ingested {file_path} (run={run_id})")
