from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.models import ArtifactChunk
from corpus.db.repository import CorpusRepository

_CHROMA_BATCH_SIZE = 5000


@dataclass
class SyncResult:
    synced: int = 0
    skipped: int = 0
    total: int = 0


def _batched_upsert(collection: object, ids: list[str], embeddings: list[list[float]], texts: list[str]) -> None:
    """Upsert in batches to stay within ChromaDB's max batch size."""
    for i in range(0, len(ids), _CHROMA_BATCH_SIZE):
        batch_ids = ids[i : i + _CHROMA_BATCH_SIZE]
        batch_emb = embeddings[i : i + _CHROMA_BATCH_SIZE]
        batch_txt = texts[i : i + _CHROMA_BATCH_SIZE]
        collection.upsert(ids=batch_ids, embeddings=batch_emb, documents=batch_txt)  # type: ignore[union-attr]


def sync_vectors(
    session: Session,
    run_id: str,
    settings: CorpusSettings | None = None,
) -> SyncResult:
    if settings is None:
        settings = get_settings()

    import chromadb

    client = chromadb.PersistentClient(path=settings.chroma_dir)
    collection = client.get_or_create_collection("corpus_chunks")

    repo = CorpusRepository(session)
    artifacts = repo.list_artifacts(run_id=run_id)

    result = SyncResult()
    chunks_to_embed: list[ArtifactChunk] = []

    for art in artifacts:
        for chunk in repo.list_chunks(artifact_id=str(art.artifact_id)):
            result.total += 1
            if chunk.embedding_synced:
                result.skipped += 1
                continue
            chunks_to_embed.append(chunk)

    if not chunks_to_embed:
        return result

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(settings.embedding_model)
    texts = [str(c.content) for c in chunks_to_embed]
    embeddings = model.encode(texts).tolist()

    ids = [str(c.chunk_id) for c in chunks_to_embed]
    _batched_upsert(collection, ids, embeddings, texts)

    for chunk in chunks_to_embed:
        chunk.embedding_synced = True  # type: ignore[assignment]
    session.flush()

    result.synced = len(chunks_to_embed)
    return result


def rebuild_vectors(session: Session, settings: CorpusSettings | None = None) -> SyncResult:
    if settings is None:
        settings = get_settings()

    import chromadb

    client = chromadb.PersistentClient(path=settings.chroma_dir)
    try:
        client.delete_collection("corpus_chunks")
    except Exception:
        pass
    collection = client.get_or_create_collection("corpus_chunks")

    repo = CorpusRepository(session)
    all_chunks = []
    for art in repo.list_artifacts():
        all_chunks.extend(repo.list_chunks(artifact_id=str(art.artifact_id)))

    result = SyncResult(total=len(all_chunks))
    if not all_chunks:
        return result

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(settings.embedding_model)
    texts = [str(c.content) for c in all_chunks]
    embeddings = model.encode(texts).tolist()

    ids = [str(c.chunk_id) for c in all_chunks]
    _batched_upsert(collection, ids, embeddings, texts)

    for chunk in all_chunks:
        chunk.embedding_synced = True  # type: ignore[assignment]
    session.flush()

    result.synced = len(all_chunks)
    return result
