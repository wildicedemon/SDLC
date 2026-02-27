import json

import pytest
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError

from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import (
    ArtifactChunk,
    Base,
    ConsolidationRun,
    ResearchArtifact,
)

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


@pytest.fixture()
def engine(tmp_db_url: str):  # type: ignore[no-untyped-def]
    eng = create_db_engine(tmp_db_url)
    Base.metadata.create_all(eng)
    return eng


def test_create_all_creates_10_tables(engine) -> None:  # type: ignore[no-untyped-def]
    inspector = inspect(engine)
    tables = set(inspector.get_table_names())
    assert EXPECTED_TABLES.issubset(tables), f"Missing tables: {EXPECTED_TABLES - tables}"
    assert len(EXPECTED_TABLES) == 10


def test_artifact_without_run_id_fk_raises(engine) -> None:  # type: ignore[no-untyped-def]
    session = make_session_factory(engine)()
    try:
        artifact = ResearchArtifact(
            artifact_id="ra_test_001",
            title="Test",
            content="content",
            domain_tags=json.dumps(["test"]),
            capability_tags=json.dumps(["cap"]),
            source_branch="test-branch",
            source_path="test/path.md",
            captured_at="2026-01-01T00:00:00",
            run_id="nonexistent_run",
            status="active",
        )
        session.add(artifact)
        with pytest.raises(IntegrityError):
            session.flush()
    finally:
        session.rollback()
        session.close()


def test_consolidation_run_invalid_status_raises(engine) -> None:  # type: ignore[no-untyped-def]
    session = make_session_factory(engine)()
    try:
        run = ConsolidationRun(
            run_id="cr_test_001",
            source_branch="test-branch",
            started_at="2026-01-01T00:00:00",
            status="invalid",
        )
        session.add(run)
        with pytest.raises(IntegrityError):
            session.flush()
    finally:
        session.rollback()
        session.close()


def test_duplicate_chunk_index_raises(engine) -> None:  # type: ignore[no-untyped-def]
    session = make_session_factory(engine)()
    try:
        run = ConsolidationRun(
            run_id="cr_dup_test",
            source_branch="test-branch",
            started_at="2026-01-01T00:00:00",
            status="pending",
        )
        session.add(run)
        session.flush()

        artifact = ResearchArtifact(
            artifact_id="ra_dup_test",
            title="Test",
            content="content",
            domain_tags=json.dumps(["test"]),
            capability_tags=json.dumps(["cap"]),
            source_branch="test-branch",
            source_path="test/path.md",
            captured_at="2026-01-01T00:00:00",
            run_id="cr_dup_test",
            status="active",
        )
        session.add(artifact)
        session.flush()

        chunk1 = ArtifactChunk(
            chunk_id="chunk_001",
            artifact_id="ra_dup_test",
            chunk_index=0,
            content="first chunk",
        )
        chunk2 = ArtifactChunk(
            chunk_id="chunk_002",
            artifact_id="ra_dup_test",
            chunk_index=0,
            content="duplicate index",
        )
        session.add(chunk1)
        session.flush()
        session.add(chunk2)
        with pytest.raises(IntegrityError):
            session.flush()
    finally:
        session.rollback()
        session.close()
