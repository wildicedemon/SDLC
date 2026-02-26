import json

from sqlalchemy import inspect

from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.migrations.runner import migrate_forward, migrate_rollback
from corpus.db.models import Base
from corpus.db.repository import CorpusRepository

EXPECTED_TABLES = {
    "consolidation_runs",
    "research_artifacts",
    "artifact_chunks",
    "decision_cards",
    "drift_events",
    "reference_rewrite_maps",
    "reference_integrity_reports",
    "human_review_queue",
    "capability_mappings",
    "telemetry_outcomes",
}


def test_full_roundtrip(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)

    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    run = repo.create_run(
        run_id="cr_rt_001",
        source_branch="feature/test",
        started_at="2026-01-01T00:00:00",
        status="running",
    )

    art1 = repo.create_artifact(
        artifact_id="ra_rt_001",
        title="Artifact 1",
        content="Content 1",
        domain_tags=json.dumps(["security"]),
        capability_tags=json.dumps(["auth"]),
        source_branch="feature/test",
        source_path="docs/research/01/patterns.md",
        captured_at="2026-01-01T00:00:00",
        run_id="cr_rt_001",
        status="active",
    )
    art2 = repo.create_artifact(
        artifact_id="ra_rt_002",
        title="Artifact 2",
        content="Content 2",
        domain_tags=json.dumps(["testing"]),
        capability_tags=json.dumps(["e2e"]),
        source_branch="feature/test",
        source_path="docs/research/02/overview.md",
        captured_at="2026-01-01T00:00:00",
        run_id="cr_rt_001",
        status="active",
    )

    for i in range(3):
        repo.create_chunk(
            chunk_id=f"chunk_rt_{i}",
            artifact_id="ra_rt_001" if i < 2 else "ra_rt_002",
            chunk_index=i if i < 2 else 0,
            content=f"Chunk content {i}",
        )

    card = repo.create_decision_card(
        decision_id="dc_rt_001",
        question="Which auth?",
        capability="auth",
        recommendation=json.dumps({"summary": "Use OAuth2"}),
        confidence_score=0.9,
        confidence_level="high",
        provenance_refs=json.dumps(["ra_rt_001"]),
        last_validated_at="2026-01-01T00:00:00",
        status="active",
    )

    repo.create_capability_mapping(capability="auth", decision_id="dc_rt_001", domain="security")

    repo.create_drift_event(
        event_id="de_rt_001",
        decision_id="dc_rt_001",
        trigger="new_conflicting_artifact",
        confidence_delta=-0.1,
        status="pending_revalidation",
        run_id="cr_rt_001",
        created_at="2026-01-01T00:00:00",
    )

    session.commit()

    assert repo.get_run("cr_rt_001") is not None
    assert repo.get_artifact("ra_rt_001") is not None
    assert repo.get_artifact("ra_rt_002") is not None
    assert len(repo.list_chunks(artifact_id="ra_rt_001")) == 2
    assert len(repo.list_chunks(artifact_id="ra_rt_002")) == 1
    assert repo.get_decision_card("dc_rt_001") is not None
    assert len(repo.list_capability_mappings(capability="auth")) == 1
    assert repo.get_drift_event("de_rt_001") is not None

    session.close()


def test_rollback_and_remigrate(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)

    session = make_session_factory(engine)()
    repo = CorpusRepository(session)
    repo.create_run(run_id="cr_x", source_branch="x", started_at="2026-01-01T00:00:00", status="pending")
    session.commit()
    session.close()

    migrate_rollback(engine)
    inspector = inspect(engine)
    tables = set(inspector.get_table_names())
    remaining = EXPECTED_TABLES & tables
    assert len(remaining) == 0

    migrate_forward(engine)
    inspector = inspect(engine)
    tables = set(inspector.get_table_names())
    assert EXPECTED_TABLES.issubset(tables)

    session2 = make_session_factory(engine)()
    repo2 = CorpusRepository(session2)
    assert len(repo2.list_runs()) == 0
    session2.close()
