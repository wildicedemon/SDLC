import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from corpus.config import CorpusSettings
from corpus.consolidation.gate_runner import run_gates
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


def _seed_passing_run(repo: CorpusRepository, run_id: str, corpus_root: Path, settings: CorpusSettings) -> None:
    now = datetime.now(timezone.utc).isoformat()
    repo.create_run(run_id=run_id, source_branch="test", started_at=now, status="running")

    research = corpus_root / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    research.mkdir(parents=True, exist_ok=True)
    (research / "overview.md").write_text("# Overview\nContent.\n")

    repo.create_artifact(
        artifact_id="ra_test_01",
        title="Test Artifact",
        content="content",
        domain_tags=json.dumps(["security_architecture"]),
        capability_tags=json.dumps([]),
        source_branch="test",
        source_path="docs/research/01_meta_architecture/security_architecture/overview.md",
        captured_at=now,
        run_id=run_id,
        status="active",
    )

    chunk = repo.create_chunk(
        chunk_id="ac_test_01",
        artifact_id="ra_test_01",
        chunk_index=0,
        content="content",
    )
    chunk.embedding_synced = True  # type: ignore[assignment]
    repo.session.flush()

    Path(settings.graph_path).write_text(
        json.dumps({"directed": False, "multigraph": False, "graph": {}, "nodes": [{"id": "n1"}], "edges": []}),
        encoding="utf-8",
    )


def test_all_gates_pass(_env: tuple[str, CorpusSettings, Path]) -> None:
    db_url, settings, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    run_id = "cr_gate_pass"
    _seed_passing_run(repo, run_id, tmp_path, settings)
    session.flush()

    result = run_gates(session, run_id, corpus_root=str(tmp_path), settings=settings)
    assert result.passed is True
    assert len(result.failures) == 0
    session.close()


def test_unresolved_review_fails_gate(_env: tuple[str, CorpusSettings, Path]) -> None:
    db_url, settings, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    run_id = "cr_gate_review"
    _seed_passing_run(repo, run_id, tmp_path, settings)

    repo.create_artifact(
        artifact_id="ra_test_02",
        title="Second",
        content="content2",
        domain_tags=json.dumps(["security_architecture"]),
        capability_tags=json.dumps([]),
        source_branch="test",
        source_path="docs/research/01_meta_architecture/security_architecture/overview.md",
        captured_at=datetime.now(timezone.utc).isoformat(),
        run_id=run_id,
        status="active",
    )

    repo.create_review_item(
        run_id=run_id,
        item_type="dedup",
        artifact_a_id="ra_test_01",
        artifact_b_id="ra_test_02",
        ai_confidence=0.5,
        ai_recommendation="merge",
    )
    session.flush()

    result = run_gates(session, run_id, corpus_root=str(tmp_path), settings=settings)
    assert result.passed is False
    gate_names = [f.gate for f in result.failures]
    assert "human_review_resolved" in gate_names
    session.close()


def test_broken_reference_fails_gate(_env: tuple[str, CorpusSettings, Path]) -> None:
    db_url, settings, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    run_id = "cr_gate_ref"
    now = datetime.now(timezone.utc).isoformat()
    repo.create_run(run_id=run_id, source_branch="test", started_at=now, status="running")

    research = tmp_path / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    research.mkdir(parents=True, exist_ok=True)
    (research / "overview.md").write_text("# Overview\nSee [link](nonexistent.md).\n")

    repo.create_artifact(
        artifact_id="ra_ref_01",
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

    chunk = repo.create_chunk(chunk_id="ac_ref_01", artifact_id="ra_ref_01", chunk_index=0, content="content")
    chunk.embedding_synced = True  # type: ignore[assignment]
    repo.session.flush()

    Path(settings.graph_path).write_text(
        json.dumps({"directed": False, "multigraph": False, "graph": {}, "nodes": [{"id": "n1"}], "edges": []}),
        encoding="utf-8",
    )

    result = run_gates(session, run_id, corpus_root=str(tmp_path), settings=settings)
    assert result.passed is False
    gate_names = [f.gate for f in result.failures]
    assert "reference_integrity" in gate_names
    session.close()


def test_unhealthy_sync_fails_gate(_env: tuple[str, CorpusSettings, Path]) -> None:
    db_url, settings, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    run_id = "cr_gate_sync"
    now = datetime.now(timezone.utc).isoformat()
    repo.create_run(run_id=run_id, source_branch="test", started_at=now, status="running")

    research = tmp_path / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    research.mkdir(parents=True, exist_ok=True)
    (research / "overview.md").write_text("# Overview\nContent.\n")

    repo.create_artifact(
        artifact_id="ra_sync_01",
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

    repo.create_chunk(chunk_id="ac_sync_01", artifact_id="ra_sync_01", chunk_index=0, content="content")
    session.flush()

    Path(settings.graph_path).write_text(
        json.dumps({"directed": False, "multigraph": False, "graph": {}, "nodes": [{"id": "n1"}], "edges": []}),
        encoding="utf-8",
    )

    result = run_gates(session, run_id, corpus_root=str(tmp_path), settings=settings)
    assert result.passed is False
    gate_names = [f.gate for f in result.failures]
    assert "sync_health" in gate_names
    session.close()


def test_multiple_failures_all_listed(_env: tuple[str, CorpusSettings, Path]) -> None:
    db_url, settings, tmp_path = _env
    engine = create_db_engine(db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    run_id = "cr_gate_multi"
    now = datetime.now(timezone.utc).isoformat()
    repo.create_run(run_id=run_id, source_branch="test", started_at=now, status="running")

    research = tmp_path / "docs" / "research" / "01_meta_architecture" / "security_architecture"
    research.mkdir(parents=True, exist_ok=True)
    (research / "overview.md").write_text("# Overview\nSee [link](nonexistent.md).\n")

    repo.create_artifact(
        artifact_id="ra_multi_01",
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

    repo.create_artifact(
        artifact_id="ra_multi_02",
        title="Second",
        content="content2",
        domain_tags=json.dumps(["security_architecture"]),
        capability_tags=json.dumps([]),
        source_branch="test",
        source_path="docs/research/01_meta_architecture/security_architecture/overview.md",
        captured_at=now,
        run_id=run_id,
        status="active",
    )

    repo.create_review_item(
        run_id=run_id,
        item_type="dedup",
        artifact_a_id="ra_multi_01",
        artifact_b_id="ra_multi_02",
        ai_confidence=0.5,
        ai_recommendation="merge",
    )

    repo.create_chunk(chunk_id="ac_multi_01", artifact_id="ra_multi_01", chunk_index=0, content="content")
    session.flush()

    result = run_gates(session, run_id, corpus_root=str(tmp_path), settings=settings)
    assert result.passed is False
    assert len(result.failures) >= 2
    session.close()
