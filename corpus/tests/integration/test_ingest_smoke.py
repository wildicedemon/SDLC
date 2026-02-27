import json
from pathlib import Path

import pytest
from git import Repo

from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.ingestion.pipeline import run_ingest


@pytest.fixture()
def ingest_repo(tmp_path: Path) -> tuple[Path, str, str]:
    repo_dir = tmp_path / "repo"
    repo_dir.mkdir()
    repo = Repo.init(str(repo_dir))
    repo.config_writer().set_value("user", "name", "Test").release()
    repo.config_writer().set_value("user", "email", "test@test.com").release()

    readme = repo_dir / "README.md"
    readme.write_text("# Repo root")
    repo.index.add([str(readme)])
    repo.index.commit("initial commit")
    repo.create_head("main")

    branch_name = "feature/ingest-smoke"
    repo.create_head(branch_name)
    repo.heads[branch_name].checkout()

    arch_dir = repo_dir / "docs" / "research" / "01_meta_architecture"
    sec_dir = arch_dir / "security_architecture"
    sec_dir.mkdir(parents=True)

    (sec_dir / "patterns.md").write_text(
        "# Security Patterns\n\n## Pattern A\nContent for pattern A.\n\n## Pattern B\nContent for pattern B.\n"
    )
    (sec_dir / "threat_modeling.md").write_text("# Threat Modeling\n\n## Overview\nThreat modeling overview.\n")

    design_dir = arch_dir / "system_design_philosophy"
    design_dir.mkdir(parents=True)
    (design_dir / "overview.md").write_text("# System Design Philosophy\n\nDesign content here.\n")

    research_dir = repo_dir / "docs" / "research" / "09_research_discipline" / "research_benchmarking_framework"
    research_dir.mkdir(parents=True)
    (research_dir / "overview.md").write_text(
        "# Research Benchmarking\n\n## Metrics\nBenchmark metrics.\n\n## Methodology\nHow to benchmark.\n"
    )

    repo.index.add(
        [
            str(sec_dir / "patterns.md"),
            str(sec_dir / "threat_modeling.md"),
            str(design_dir / "overview.md"),
            str(research_dir / "overview.md"),
        ]
    )
    repo.index.commit("add research artifacts")

    db_path = tmp_path / "data" / "corpus.db"
    db_path.parent.mkdir(parents=True)
    db_url = f"sqlite:///{db_path}"

    return repo_dir, branch_name, db_url


def test_ingest_creates_run(ingest_repo: tuple[Path, str, str]) -> None:
    repo_dir, branch, db_url = ingest_repo
    engine = create_db_engine(db_url)
    migrate_forward(engine)

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        result = run_ingest(repo, str(repo_dir), branch, "main", corpus_root=str(repo_dir))

    assert not result.failed
    assert result.artifacts_ingested >= 4

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        runs = repo.list_runs()
        assert len(runs) == 1
        assert runs[0].artifacts_ingested >= 4


def test_ingest_artifacts_have_domain_tags(ingest_repo: tuple[Path, str, str]) -> None:
    repo_dir, branch, db_url = ingest_repo
    engine = create_db_engine(db_url)
    migrate_forward(engine)

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        result = run_ingest(repo, str(repo_dir), branch, "main", corpus_root=str(repo_dir))

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        artifacts = repo.list_artifacts(run_id=result.run_id)
        assert len(artifacts) == 4
        for art in artifacts:
            tags = json.loads(art.domain_tags)
            assert len(tags) > 0, f"Artifact {art.artifact_id} has empty domain_tags"


def test_ingest_creates_chunks(ingest_repo: tuple[Path, str, str]) -> None:
    repo_dir, branch, db_url = ingest_repo
    engine = create_db_engine(db_url)
    migrate_forward(engine)

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        result = run_ingest(repo, str(repo_dir), branch, "main", corpus_root=str(repo_dir))

    assert result.chunks_created >= 4

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        artifacts = repo.list_artifacts(run_id=result.run_id)
        total_chunks = 0
        for art in artifacts:
            chunks = repo.list_chunks(artifact_id=art.artifact_id)
            assert len(chunks) >= 1, f"Artifact {art.artifact_id} has 0 chunks"
            total_chunks += len(chunks)
        assert total_chunks >= 4


def test_ingest_no_unclassified(ingest_repo: tuple[Path, str, str]) -> None:
    repo_dir, branch, db_url = ingest_repo
    engine = create_db_engine(db_url)
    migrate_forward(engine)

    with get_session(engine) as session:
        repo = CorpusRepository(session)
        result = run_ingest(repo, str(repo_dir), branch, "main", corpus_root=str(repo_dir))

    assert not result.failed
    assert len(result.unclassified_files) == 0
