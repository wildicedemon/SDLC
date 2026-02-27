import uuid
from datetime import datetime, timezone
from pathlib import Path

from corpus.config import CorpusSettings
from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.sync.health_checker import check_sync_health


def _setup(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


class TestHealthChecker:
    def test_all_synced_healthy(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        settings = CorpusSettings(
            db_url=tmp_db_url,
            graph_path=str(tmp_path / "graph.json"),
            kilo_api_key="test",
        )

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_artifact(
                artifact_id="art-1",
                title="A1",
                content="content",
                domain_tags="test",
                capability_tags="",
                source_branch="test",
                source_path="test.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )
            repo.create_chunk(
                chunk_id="chunk-1",
                artifact_id="art-1",
                chunk_index=0,
                content="chunk content",
                embedding_synced=True,
            )

        with get_session(engine) as session:
            report = check_sync_health(session, settings=settings)

        assert report.healthy is True
        assert report.vector_synced_pct == 1.0

    def test_unsynced_unhealthy(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        settings = CorpusSettings(
            db_url=tmp_db_url,
            graph_path=str(tmp_path / "graph.json"),
            kilo_api_key="test",
        )

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_artifact(
                artifact_id="art-1",
                title="A1",
                content="content",
                domain_tags="test",
                capability_tags="",
                source_branch="test",
                source_path="test.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )
            repo.create_chunk(
                chunk_id="chunk-1",
                artifact_id="art-1",
                chunk_index=0,
                content="synced",
                embedding_synced=True,
            )
            repo.create_chunk(
                chunk_id="chunk-2",
                artifact_id="art-1",
                chunk_index=1,
                content="not synced",
                embedding_synced=False,
            )

        with get_session(engine) as session:
            report = check_sync_health(session, settings=settings)

        assert report.healthy is False
        assert report.vector_synced_pct == 0.5
