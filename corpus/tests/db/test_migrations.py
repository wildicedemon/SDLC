import pytest
from sqlalchemy import inspect, text

from corpus.db.engine import create_db_engine
from corpus.db.migrations.runner import migrate_forward, migrate_rollback

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
    return create_db_engine(tmp_db_url)


def test_migrate_forward_creates_tables_and_tracks_version(engine) -> None:  # type: ignore[no-untyped-def]
    applied = migrate_forward(engine)
    assert "001_initial" in applied

    inspector = inspect(engine)
    tables = set(inspector.get_table_names())
    assert EXPECTED_TABLES.issubset(tables)

    with engine.connect() as conn:
        rows = conn.execute(text("SELECT version FROM _schema_versions")).fetchall()
    versions = [r[0] for r in rows]
    assert "001_initial" in versions


def test_migrate_rollback_removes_tables(engine) -> None:  # type: ignore[no-untyped-def]
    migrate_forward(engine)
    rolled = migrate_rollback(engine)
    assert rolled == "001_initial"

    inspector = inspect(engine)
    tables = set(inspector.get_table_names())
    remaining = EXPECTED_TABLES & tables
    assert len(remaining) == 0, f"Tables still present after rollback: {remaining}"

    with engine.connect() as conn:
        rows = conn.execute(text("SELECT version FROM _schema_versions")).fetchall()
    assert len(rows) == 0


def test_remigrate_after_rollback_restores_tables(engine) -> None:  # type: ignore[no-untyped-def]
    migrate_forward(engine)
    migrate_rollback(engine)
    applied = migrate_forward(engine)
    assert "001_initial" in applied

    inspector = inspect(engine)
    tables = set(inspector.get_table_names())
    assert EXPECTED_TABLES.issubset(tables)
