import json
from datetime import datetime, timezone

from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import Base
from corpus.db.repository import CorpusRepository
from corpus.telemetry.metrics import compute_metrics


def test_metrics_returns_all_fields(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    now = datetime.now(timezone.utc).isoformat()
    repo.create_run(run_id="cr_met_01", source_branch="test", started_at=now, status="completed")
    repo.create_artifact(
        artifact_id="ra_met_01",
        title="Test",
        content="content",
        domain_tags=json.dumps(["test"]),
        capability_tags=json.dumps([]),
        source_branch="test",
        source_path="test.md",
        captured_at=now,
        run_id="cr_met_01",
        status="active",
    )
    repo.create_chunk(chunk_id="ac_met_01", artifact_id="ra_met_01", chunk_index=0, content="content")
    session.flush()

    m = compute_metrics(session)
    assert m.total_runs == 1
    assert m.completed_runs == 1
    assert m.total_artifacts == 1
    assert m.total_chunks == 1
    assert isinstance(m.contradiction_density, float)
    assert isinstance(m.vector_synced_pct, float)
    session.close()
