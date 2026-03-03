import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from corpus.config import CorpusSettings
from corpus.consolidation.run_controller import complete_run
from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import Base
from corpus.db.repository import CorpusRepository


@pytest.fixture()
def _env(tmp_path: Path) -> tuple[str, CorpusSettings, Path]:
    db_path = tmp_path / "data" / "corpus.db"
    db_path.parent.mkdir(parents=True)
    chroma_dir = tmp_path / "data" / "chroma"
    chroma_dir.mkdir(parents=True)
    graph_path = tmp_path / "data" / "graph.json"
    db_url = f"sqlite:///{db_path}"

    settings = CorpusSettings(
        db_url=db_url,
        chroma_dir=str(chroma_dir),
        graph_path=str(graph_path),
    )
    return db_url, settings, tmp_path


def test_gates_pass_run_completed(_env: tuple[str, CorpusSettings, Path]) -> None:
    db_url, settings, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    run_id = "cr_ctrl_pass"
    now = datetime.now(timezone.utc).isoformat()
    repo.create_run(run_id=run_id, source_branch="test", started_at=now, status="running")

    research = tmp_path / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    research.mkdir(parents=True, exist_ok=True)
    (research / "overview.md").write_text("# Overview\nContent.\n")

    repo.create_artifact(
        artifact_id="ra_ctrl_01",
        title="Test",
        content="content",
        domain_tags=json.dumps(["security_architecture"]),
        capability_tags=json.dumps([]),
        source_branch="test",
        source_path="docs/research/01_meta_architecture/security_architecture/overview.md",
        captured_at=now,
        run_id=run_id,
        status="active",
    )
    chunk = repo.create_chunk(chunk_id="ac_ctrl_01", artifact_id="ra_ctrl_01", chunk_index=0, content="content")
    chunk.embedding_synced = True  # type: ignore[assignment]
    session.flush()

    Path(settings.graph_path).write_text(
        json.dumps({"directed": False, "multigraph": False, "graph": {}, "nodes": [{"id": "n1"}], "edges": []}),
        encoding="utf-8",
    )

    passed = complete_run(session, run_id, corpus_root=str(tmp_path), settings=settings)
    session.commit()

    assert passed is True
    run = repo.get_run(run_id)
    assert run is not None
    assert str(run.status) == "completed"
    assert run.completed_at is not None
    session.close()


def test_gates_fail_run_failed(_env: tuple[str, CorpusSettings, Path]) -> None:
    db_url, settings, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    run_id = "cr_ctrl_fail"
    now = datetime.now(timezone.utc).isoformat()
    repo.create_run(run_id=run_id, source_branch="test", started_at=now, status="running")

    research = tmp_path / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    research.mkdir(parents=True, exist_ok=True)
    (research / "overview.md").write_text("# Overview\nContent.\n")

    repo.create_artifact(
        artifact_id="ra_ctrl_f1",
        title="Test",
        content="content",
        domain_tags=json.dumps(["security_architecture"]),
        capability_tags=json.dumps([]),
        source_branch="test",
        source_path="docs/research/01_meta_architecture/security_architecture/overview.md",
        captured_at=now,
        run_id=run_id,
        status="active",
    )

    repo.create_chunk(chunk_id="ac_ctrl_f1", artifact_id="ra_ctrl_f1", chunk_index=0, content="content")
    session.flush()

    passed = complete_run(session, run_id, corpus_root=str(tmp_path), settings=settings)
    session.commit()

    assert passed is False
    run = repo.get_run(run_id)
    assert run is not None
    assert str(run.status) == "failed"
    assert run.remediation_report is not None
    assert len(str(run.remediation_report)) > 0
    session.close()
