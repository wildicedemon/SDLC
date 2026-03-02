from pathlib import Path

import pytest
from git import Repo

from corpus.consolidation.branch_retirement import retire_branch
from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import Base
from corpus.db.repository import CorpusRepository


@pytest.fixture()
def _env(tmp_path: Path) -> tuple[str, Path]:
    db_path = tmp_path / "data" / "corpus.db"
    db_path.parent.mkdir(parents=True)
    db_url = f"sqlite:///{db_path}"

    git_repo = Repo.init(str(tmp_path / "repo"))
    git_repo.config_writer().set_value("user", "name", "Test").release()
    git_repo.config_writer().set_value("user", "email", "test@test.com").release()

    readme = tmp_path / "repo" / "README.md"
    readme.write_text("# Init\n")
    git_repo.index.add([str(readme)])
    git_repo.index.commit("initial")
    git_repo.create_head("main")

    git_repo.create_head("feature/test-branch")

    return db_url, tmp_path


def test_completed_run_retirement_succeeds(_env: tuple[str, Path]) -> None:
    db_url, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    repo.create_run(
        run_id="cr_retire_ok",
        source_branch="feature/test-branch",
        started_at="2026-01-01T00:00:00",
        status="completed",
    )
    session.flush()

    retire_branch(session, "cr_retire_ok", "archived", repo_path=str(tmp_path / "repo"))
    session.commit()

    run = repo.get_run("cr_retire_ok")
    assert run is not None
    assert str(run.retirement_action) == "archived"

    git_repo = Repo(str(tmp_path / "repo"))
    assert "archive/feature/test-branch" in [t.name for t in git_repo.tags]
    session.close()


def test_non_completed_run_refused(_env: tuple[str, Path]) -> None:
    db_url, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    repo.create_run(
        run_id="cr_retire_fail",
        source_branch="feature/test-branch",
        started_at="2026-01-01T00:00:00",
        status="running",
    )
    session.flush()

    with pytest.raises(ValueError, match="expected 'completed'"):
        retire_branch(session, "cr_retire_fail", "archived", repo_path=str(tmp_path / "repo"))

    session.close()
