import json
from datetime import datetime, timedelta, timezone

from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import Base
from corpus.db.repository import CorpusRepository
from corpus.telemetry.compactor import compact


def test_superseded_old_artifact_archived(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    old_date = (datetime.now(timezone.utc) - timedelta(days=100)).isoformat()
    repo.create_run(run_id="cr_comp_01", source_branch="test", started_at=old_date, status="completed")
    repo.create_artifact(
        artifact_id="ra_comp_01",
        title="Old",
        content="old content",
        domain_tags=json.dumps(["test"]),
        capability_tags=json.dumps([]),
        source_branch="test",
        source_path="old.md",
        captured_at=old_date,
        run_id="cr_comp_01",
        status="superseded",
    )
    session.flush()

    report = compact(session, max_age_days=90)
    assert report.evaluated == 1
    assert report.archived == 1

    art = repo.get_artifact("ra_comp_01")
    assert art is not None
    assert str(art.status) == "archived"
    session.close()


def test_active_artifact_untouched(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    old_date = (datetime.now(timezone.utc) - timedelta(days=100)).isoformat()
    repo.create_run(run_id="cr_comp_02", source_branch="test", started_at=old_date, status="completed")
    repo.create_artifact(
        artifact_id="ra_comp_02",
        title="Active",
        content="active content",
        domain_tags=json.dumps(["test"]),
        capability_tags=json.dumps([]),
        source_branch="test",
        source_path="active.md",
        captured_at=old_date,
        run_id="cr_comp_02",
        status="active",
    )
    session.flush()

    report = compact(session, max_age_days=90)
    assert report.evaluated == 0
    assert report.archived == 0

    art = repo.get_artifact("ra_comp_02")
    assert art is not None
    assert str(art.status) == "active"
    session.close()
