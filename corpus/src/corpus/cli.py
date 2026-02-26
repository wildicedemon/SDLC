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
    click.echo(f"Run ID: {result.run_id}")


@cli.command()
@click.argument("run_id")
def dedup(run_id: str) -> None:
    """Run 3-layer dedup pipeline for a consolidation run."""
    click.echo(f"corpus dedup {run_id}: not yet implemented")


@cli.command("update-decisions")
@click.argument("run_id")
def update_decisions(run_id: str) -> None:
    """Recompute impacted DecisionCards and indices."""
    click.echo(f"corpus update-decisions {run_id}: not yet implemented")


@cli.command("check-references")
@click.argument("run_id")
def check_references(run_id: str) -> None:
    """Validate reference integrity for a run."""
    click.echo(f"corpus check-references {run_id}: not yet implemented")


@cli.command("sync-derived")
@click.argument("run_id")
def sync_derived(run_id: str) -> None:
    """Sync vector + graph layers from relational."""
    click.echo(f"corpus sync-derived {run_id}: not yet implemented")


@cli.command()
@click.argument("run_id")
def complete(run_id: str) -> None:
    """Run all gates and mark run complete/fail."""
    click.echo(f"corpus complete {run_id}: not yet implemented")


@cli.command()
@click.argument("source")
def run(source: str) -> None:
    """Full pipeline: ingest -> dedup -> update -> check -> sync -> complete."""
    click.echo(f"corpus run {source}: not yet implemented")


@cli.group()
def review() -> None:
    """Manage human review queue."""


@review.command("list")
def review_list() -> None:
    """List unresolved human review items."""
    click.echo("corpus review list: not yet implemented")


@review.command("resolve")
@click.argument("item_id")
@click.argument("disposition")
def review_resolve(item_id: str, disposition: str) -> None:
    """Resolve a review item with a disposition."""
    click.echo(f"corpus review resolve {item_id} {disposition}: not yet implemented")


@cli.command()
@click.argument("question")
@click.option("--depth", type=click.Choice(["L0", "L1", "L2", "L3"]), default="L1", help="Retrieval depth.")
def query(question: str, depth: str) -> None:
    """Run a retrieval query."""
    click.echo(f"corpus query (depth={depth}): not yet implemented")


@cli.command("rebuild-vectors")
def rebuild_vectors() -> None:
    """Full vector rebuild from relational."""
    click.echo("corpus rebuild-vectors: not yet implemented")


@cli.command("rebuild-graph")
def rebuild_graph() -> None:
    """Full graph rebuild from relational."""
    click.echo("corpus rebuild-graph: not yet implemented")


@cli.group()
def telemetry() -> None:
    """Telemetry and calibration commands."""


@telemetry.command("record")
@click.argument("decision_id")
@click.argument("outcome")
def telemetry_record(decision_id: str, outcome: str) -> None:
    """Record a decision outcome."""
    click.echo(f"corpus telemetry record {decision_id} {outcome}: not yet implemented")


@telemetry.command("calibrate")
def telemetry_calibrate() -> None:
    """Recompute confidence calibration."""
    click.echo("corpus telemetry calibrate: not yet implemented")


@telemetry.command("metrics")
def telemetry_metrics() -> None:
    """Print operational metrics."""
    click.echo("corpus telemetry metrics: not yet implemented")


@cli.command()
def status() -> None:
    """Show current run status, queue, sync health."""
    click.echo("corpus status: not yet implemented")
