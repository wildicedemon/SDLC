import pytest

from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import Base
from corpus.db.repository import CorpusRepository
from corpus.ingestion.path_mapper import record_mapping


@pytest.fixture()
def repo(tmp_db_url: str) -> CorpusRepository:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    r = CorpusRepository(session)
    r.create_run(
        run_id="cr_pm_test",
        source_branch="test-branch",
        started_at="2026-01-01T00:00:00",
        status="running",
    )
    return r


def test_record_mapping_persists(repo: CorpusRepository) -> None:
    record_mapping(repo, "old/path.md", "new/path.md", "cr_pm_test")
    repo.session.flush()

    from corpus.db.models import ReferenceRewriteMap

    rows = repo.session.query(ReferenceRewriteMap).filter_by(run_id="cr_pm_test").all()
    assert len(rows) == 1
    assert rows[0].old_path == "old/path.md"
    assert rows[0].new_path == "new/path.md"
    assert rows[0].rewritten is False


def test_multiple_mappings_for_same_run(repo: CorpusRepository) -> None:
    record_mapping(repo, "a.md", "b.md", "cr_pm_test")
    record_mapping(repo, "c.md", "d.md", "cr_pm_test")
    record_mapping(repo, "e.md", "f.md", "cr_pm_test")
    repo.session.flush()

    from corpus.db.models import ReferenceRewriteMap

    rows = repo.session.query(ReferenceRewriteMap).filter_by(run_id="cr_pm_test").all()
    assert len(rows) == 3
