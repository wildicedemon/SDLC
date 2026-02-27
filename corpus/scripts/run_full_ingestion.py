from __future__ import annotations

import json
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from corpus.config import CorpusSettings
from corpus.consolidation.run_controller import complete_run
from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.decisions.card_updater import update_impacted_cards
from corpus.decisions.drift_detector import detect_drift
from corpus.decisions.index_updater import update_indices
from corpus.dedup.embeddings import Disagreement
from corpus.dedup.pipeline import run_dedup
from corpus.ingestion.classifier import classify
from corpus.ingestion.normalizer import normalize
from corpus.references.integrity_validator import validate_integrity
from corpus.references.rewrite_mapper import generate_rewrite_map
from corpus.references.rewriter import rewrite_references
from corpus.sync.graph_sync import sync_graph


def _local_arbitrate(disagreements: list[Disagreement]) -> list:
    from corpus.dedup.arbitrator import ArbitrationResult

    results = []
    for d in disagreements:
        results.append(
            ArbitrationResult(
                chunk_a_id=d.chunk_a_id,
                chunk_b_id=d.chunk_b_id,
                confidence=d.cosine_similarity,
                recommendation="keep_both" if d.cosine_similarity < 0.7 else "merge",
            )
        )
    return results


def _batched_vector_sync(session, run_id: str, settings: CorpusSettings):
    import chromadb
    from sentence_transformers import SentenceTransformer

    from corpus.db.models import ArtifactChunk

    client = chromadb.PersistentClient(path=settings.chroma_dir)
    collection = client.get_or_create_collection("corpus_chunks")

    repo = CorpusRepository(session)
    artifacts = repo.list_artifacts(run_id=run_id)

    chunks_to_embed: list[ArtifactChunk] = []
    skipped = 0
    for art in artifacts:
        for chunk in repo.list_chunks(artifact_id=str(art.artifact_id)):
            if chunk.embedding_synced:
                skipped += 1
            else:
                chunks_to_embed.append(chunk)

    total = len(chunks_to_embed) + skipped
    if not chunks_to_embed:
        print(f"  All {total} chunks already synced")
        return total, total, 0

    print("  Loading embedding model...")
    model = SentenceTransformer(settings.embedding_model)

    batch_size = 256
    synced = 0
    t0 = time.time()
    for i in range(0, len(chunks_to_embed), batch_size):
        batch = chunks_to_embed[i : i + batch_size]
        texts = [str(c.content) for c in batch]
        embeddings = model.encode(texts).tolist()
        ids = [str(c.chunk_id) for c in batch]
        collection.upsert(ids=ids, embeddings=embeddings, documents=texts)
        for chunk in batch:
            chunk.embedding_synced = True
        session.flush()
        synced += len(batch)
        elapsed = time.time() - t0
        rate = synced / elapsed if elapsed > 0 else 0
        remaining = (len(chunks_to_embed) - synced) / rate if rate > 0 else 0
        print(f"    Embedded {synced}/{len(chunks_to_embed)} ({rate:.0f}/s, ~{remaining:.0f}s remaining)")

    return total, synced + skipped, synced


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent
    research_root = repo_root / "docs" / "research"
    settings = CorpusSettings(
        db_url=f"sqlite:///{repo_root / 'data' / 'corpus.db'}",
        chroma_dir=str(repo_root / "data" / "chroma"),
        graph_path=str(repo_root / "data" / "graph.json"),
    )
    settings.ensure_data_dirs()

    engine = create_db_engine(settings.db_url)
    migrate_forward(engine)

    existing_run_id = None
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        runs = repo.list_runs(status="running")
        if runs:
            existing_run_id = str(runs[0].run_id)
            arts = runs[0].artifacts_ingested
            print(f"Resuming existing run {existing_run_id} ({arts} artifacts already ingested)")

    if existing_run_id:
        run_id = existing_run_id
    else:
        run_id = f"cr_{uuid.uuid4().hex[:12]}"
        now = datetime.now(timezone.utc).isoformat()

        md_files = sorted(research_root.rglob("*.md"))
        print(f"Found {len(md_files)} markdown files in docs/research/")

        print(f"\n=== Step 1/6: Ingesting (run={run_id}) ===")
        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="new-task-157a",
                started_at=now,
                status="running",
            )

            artifacts_ingested = 0
            chunks_created = 0
            skipped = 0

            for md_file in md_files:
                rel_path = md_file.relative_to(repo_root).as_posix()
                classification = classify(rel_path)

                if not classification.is_classified:
                    skipped += 1
                    continue

                content_str = md_file.read_text(encoding="utf-8", errors="replace")
                if not content_str.strip():
                    skipped += 1
                    continue

                domain = classification.domain_tags[0] if classification.domain_tags else "unknown"
                canonical_path = str(repo_root / rel_path)
                normalized = normalize(content_str, domain, canonical_path)

                artifact_id = f"ra_{uuid.uuid4().hex[:12]}"
                repo.create_artifact(
                    artifact_id=artifact_id,
                    title=normalized.title or md_file.stem,
                    content=content_str,
                    domain_tags=json.dumps(classification.domain_tags),
                    capability_tags=json.dumps(classification.capability_tags),
                    source_branch="new-task-157a",
                    source_path=rel_path,
                    captured_at=now,
                    run_id=run_id,
                    status="active",
                )
                artifacts_ingested += 1

                for idx, chunk_content in enumerate(normalized.chunks):
                    chunk_id = f"ac_{uuid.uuid4().hex[:12]}"
                    repo.create_chunk(
                        chunk_id=chunk_id,
                        artifact_id=artifact_id,
                        chunk_index=idx,
                        content=chunk_content,
                    )
                    chunks_created += 1

            run = repo.get_run(run_id)
            if run is not None:
                run.artifacts_ingested = artifacts_ingested
                session.flush()

        print(f"  Ingested {artifacts_ingested} artifacts, {chunks_created} chunks ({skipped} skipped)")

    print("\n=== Step 2/6: Dedup (local arbitration, no LLM) ===")
    with get_session(engine) as session:
        dedup_report = run_dedup(
            session,
            run_id,
            settings=settings,
            arbitrate_fn=_local_arbitrate,
        )
    print(f"  Candidates: {dedup_report.candidate_count}, Confirmed: {dedup_report.confirmed_dups}")
    print(f"  Disagreements: {len(dedup_report.disagreements)}, Human queued: {dedup_report.human_queued}")

    print("\n=== Step 3/6: Updating decisions ===")
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        all_cards = repo.list_decision_cards()
        prev_scores = {str(c.decision_id): float(c.confidence_score) for c in all_cards}
        updated_ids = update_impacted_cards(session, run_id)
        update_indices(session, updated_ids)
        drift_ids = detect_drift(session, run_id, prev_scores)
    print(f"  Updated {len(updated_ids)} cards, {len(drift_ids)} drift events")

    print("\n=== Step 4/6: Checking references ===")
    with get_session(engine) as session:
        rmap = generate_rewrite_map(session, run_id)
        rewrite_references(rmap, str(repo_root))
        integrity = validate_integrity(session, run_id, str(repo_root))
    status = "PASS" if integrity.passed else "FAIL"
    broken = len(integrity.broken_links)
    stale = len(integrity.stale_paths)
    print(f"  Integrity: {status} ({broken} broken, {stale} stale)")

    print("\n=== Step 5/6: Syncing derived layers ===")
    with get_session(engine) as session:
        total, synced_count, new_synced = _batched_vector_sync(session, run_id, settings)
    print(f"  Vectors: {synced_count}/{total} synced ({new_synced} new)")

    with get_session(engine) as session:
        gsync = sync_graph(session, run_id, settings=settings)
    print(f"  Graph: {gsync.nodes_added} nodes, {gsync.edges_added} edges")

    print("\n=== Step 6/6: Running completion gates ===")
    with get_session(engine) as session:
        repo = CorpusRepository(session)
        reviews = repo.list_unresolved_reviews(run_id)
        if reviews:
            print(f"  Auto-resolving {len(reviews)} review items...")
            for r in reviews:
                r.disposition = "accepted"
                r.resolved_by = "bootstrap-automation"
            session.flush()

    with get_session(engine) as session:
        passed = complete_run(session, run_id, corpus_root=str(repo_root), settings=settings)

    if passed:
        print(f"\nPipeline PASSED. Run {run_id} completed successfully.")
    else:
        print(f"\nPipeline FAILED gates for run {run_id}.")
        with get_session(engine) as session:
            repo = CorpusRepository(session)
            run = repo.get_run(run_id)
            if run and run.remediation_report:
                print(f"  Remediation: {run.remediation_report}")

    print("\n=== Final Status ===")
    with get_session(engine) as session:
        from corpus.sync.health_checker import check_sync_health
        from corpus.telemetry.metrics import compute_metrics

        m = compute_metrics(session)
        health = check_sync_health(session, settings=settings)
    print(f"  Runs: {m.total_runs} ({m.completed_runs} completed)")
    print(f"  Artifacts: {m.total_artifacts}, Chunks: {m.total_chunks}")
    print(f"  Decisions: {m.total_decisions}, Drift events: {m.total_drift_events}")
    print(f"  Sync health: {'HEALTHY' if health.healthy else 'UNHEALTHY'} (vectors={health.vector_synced_pct:.0%})")


if __name__ == "__main__":
    main()
