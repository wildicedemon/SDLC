from pathlib import Path

import pytest
from git import Repo

from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import ArtifactChunk, Base, ConsolidationRun, ResearchArtifact
from corpus.db.repository import CorpusRepository
from corpus.ingestion.pipeline import run_ingest


@pytest.fixture()
def _classified_repo(tmp_path: Path) -> tuple[Path, str, str]:
    repo = Repo.init(str(tmp_path))
    repo.config_writer().set_value("user", "name", "Test").release()
    repo.config_writer().set_value("user", "email", "test@test.com").release()

    base_dir = tmp_path / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    base_dir.mkdir(parents=True)
    (base_dir / "existing.md").write_text("# Existing\nBase content.\n")
    repo.index.add([str(base_dir / "existing.md")])
    repo.index.commit("initial")
    repo.create_head("main")

    branch = "feature/add-artifacts"
    repo.create_head(branch)
    repo.heads[branch].checkout()

    (base_dir / "patterns.md").write_text("# Patterns\n\n## Section A\n\nPattern A.\n\n## Section B\n\nPattern B.\n")
    dir2 = tmp_path / "docs" / "research" / "09_research_discipline" / "research_benchmarking_framework"
    dir2.mkdir(parents=True)
    (dir2 / "overview.md").write_text("# Overview\n\nBenchmarking.\n")
    repo.index.add([str(base_dir / "patterns.md"), str(dir2 / "overview.md")])
    repo.index.commit("add artifacts")

    db_path = tmp_path / "data"
    db_path.mkdir()
    db_url = f"sqlite:///{db_path / 'corpus.db'}"

    return tmp_path, branch, db_url


@pytest.fixture()
def _unclassified_repo(tmp_path: Path) -> tuple[Path, str, str]:
    repo = Repo.init(str(tmp_path))
    repo.config_writer().set_value("user", "name", "Test").release()
    repo.config_writer().set_value("user", "email", "test@test.com").release()

    readme = tmp_path / "README.md"
    readme.write_text("# Readme\n")
    repo.index.add([str(readme)])
    repo.index.commit("initial")
    repo.create_head("main")

    branch = "feature/unclassified"
    repo.create_head(branch)
    repo.heads[branch].checkout()

    bad = tmp_path / "random" / "unknown"
    bad.mkdir(parents=True)
    (bad / "file.md").write_text("# Unknown\nThis file is not in a known domain.\n")
    repo.index.add([str(bad / "file.md")])
    repo.index.commit("add unclassified file")

    db_path = tmp_path / "data"
    db_path.mkdir()
    db_url = f"sqlite:///{db_path / 'corpus.db'}"

    return tmp_path, branch, db_url


def test_ingest_creates_run_and_artifacts(
    _classified_repo: tuple[Path, str, str],
) -> None:
    repo_path, branch, db_url = _classified_repo
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    result = run_ingest(repo, str(repo_path), branch, "main", corpus_root=str(repo_path))
    session.commit()

    assert not result.failed
    assert result.artifacts_ingested == 2
    assert result.chunks_created >= 2

    runs = session.query(ConsolidationRun).all()
    assert len(runs) == 1
    assert runs[0].status == "running"

    artifacts = session.query(ResearchArtifact).filter_by(run_id=result.run_id).all()
    assert len(artifacts) == 2

    chunks = session.query(ArtifactChunk).all()
    assert len(chunks) >= 2

    session.close()


def test_ingest_with_unclassified_fails(
    _unclassified_repo: tuple[Path, str, str],
) -> None:
    repo_path, branch, db_url = _unclassified_repo
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    result = run_ingest(repo, str(repo_path), branch, "main", corpus_root=str(repo_path))
    session.commit()

    assert result.failed
    assert len(result.unclassified_files) > 0

    run = session.query(ConsolidationRun).filter_by(run_id=result.run_id).one()
    assert run.status == "failed"

    session.close()
