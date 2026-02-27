import uuid
from datetime import datetime, timezone
from pathlib import Path

import chromadb

from corpus.config import CorpusSettings
from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.sync.vector_sync import rebuild_vectors, sync_vectors


def _setup(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


def _seed(session: object, run_id: str, chunk_count: int = 3) -> None:
    repo = CorpusRepository(session)  # type: ignore[arg-type]
    repo.create_run(
        run_id=run_id,
        source_branch="test",
        started_at=datetime.now(timezone.utc).isoformat(),
        status="running",
    )
    art_id = f"art-{uuid.uuid4().hex[:8]}"
    repo.create_artifact(
        artifact_id=art_id,
        title="Test",
        content="test",
        domain_tags="test",
        capability_tags="",
        source_branch="test",
        source_path="test.md",
        captured_at=datetime.now(timezone.utc).isoformat(),
        run_id=run_id,
    )
    for i in range(chunk_count):
        repo.create_chunk(
            chunk_id=f"chunk-{uuid.uuid4().hex[:8]}",
            artifact_id=art_id,
            chunk_index=i,
            content=f"Chunk content number {i} with unique words for embedding.",
        )


class TestVectorSync:
    def test_sync_embeds_chunks(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        chroma_dir = str(tmp_path / "chroma")
        settings = CorpusSettings(db_url=tmp_db_url, chroma_dir=chroma_dir, kilo_api_key="test")

        with get_session(engine) as session:
            _seed(session, run_id, chunk_count=3)

        with get_session(engine) as session:
            result = sync_vectors(session, run_id, settings=settings)

        assert result.synced == 3
        assert result.total == 3

        client = chromadb.PersistentClient(path=chroma_dir)
        collection = client.get_collection("corpus_chunks")
        assert collection.count() == 3

    def test_synced_flag_set(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        chroma_dir = str(tmp_path / "chroma")
        settings = CorpusSettings(db_url=tmp_db_url, chroma_dir=chroma_dir, kilo_api_key="test")

        with get_session(engine) as session:
            _seed(session, run_id, chunk_count=3)

        with get_session(engine) as session:
            sync_vectors(session, run_id, settings=settings)

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            for art in repo.list_artifacts(run_id=run_id):
                for chunk in repo.list_chunks(artifact_id=str(art.artifact_id)):
                    assert chunk.embedding_synced is True

    def test_rebuild_matches_incremental(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        chroma_dir = str(tmp_path / "chroma")
        settings = CorpusSettings(db_url=tmp_db_url, chroma_dir=chroma_dir, kilo_api_key="test")

        with get_session(engine) as session:
            _seed(session, run_id, chunk_count=3)

        with get_session(engine) as session:
            sync_vectors(session, run_id, settings=settings)

        with get_session(engine) as session:
            rebuild_result = rebuild_vectors(session, settings=settings)

        assert rebuild_result.synced == 3

        client = chromadb.PersistentClient(path=chroma_dir)
        collection = client.get_collection("corpus_chunks")
        assert collection.count() == 3
