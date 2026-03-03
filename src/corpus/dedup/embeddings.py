"""Embedding-based deduplication — Layer 2 of the 3-layer dedup pipeline.

Takes :class:`~corpus.dedup.minhash.CandidatePair` instances from
Layer 1 (MinHash) and computes cosine similarity between their
sentence-transformer embeddings.  Pairs that exceed the cosine
threshold are confirmed as duplicates; those that don't become
:class:`Disagreement` instances sent to Layer 3 (LLM arbitration).

Key function: :func:`filter_candidates`.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from corpus.dedup.minhash import CandidatePair


@dataclass
class ConfirmedDup:
    """A pair confirmed as duplicate by embedding similarity.

    Attributes:
        chunk_a_id: ID of the first chunk.
        chunk_b_id: ID of the second chunk.
        cosine_similarity: Cosine similarity of their embeddings.
    """

    chunk_a_id: str
    chunk_b_id: str
    cosine_similarity: float


@dataclass
class Disagreement:
    """A pair where MinHash flagged a candidate but embeddings disagree.

    Sent to Layer 3 (LLM arbitration) for resolution.

    Attributes:
        chunk_a_id: ID of the first chunk.
        chunk_b_id: ID of the second chunk.
        chunk_a_content: Text of the first chunk (for the LLM prompt).
        chunk_b_content: Text of the second chunk (for the LLM prompt).
        jaccard: Original MinHash Jaccard estimate.
        cosine_similarity: The below-threshold cosine similarity.
    """

    chunk_a_id: str
    chunk_b_id: str
    chunk_a_content: str
    chunk_b_content: str
    jaccard: float
    cosine_similarity: float


# Typing alias — any callable that maps list[str] → array-like
EmbedFn = type[None] | object


def _cosine_sim(a: NDArray[np.float32], b: NDArray[np.float32]) -> float:
    """Compute cosine similarity between two vectors.

    Returns 0.0 when either vector has zero magnitude.
    """
    dot = float(np.dot(a, b))
    norm = float(np.linalg.norm(a) * np.linalg.norm(b))
    if norm == 0:
        return 0.0
    return dot / norm


def filter_candidates(
    pairs: list[CandidatePair],
    threshold: float = 0.85,
    embed_fn: object | None = None,
) -> tuple[list[ConfirmedDup], list[Disagreement]]:
    """Partition candidate pairs into confirmed duplicates and disagreements.

    Embeddings are computed in a single batch for efficiency.  If no
    *embed_fn* is supplied, a default ``all-MiniLM-L6-v2`` model is
    loaded via ``sentence-transformers``.

    Args:
        pairs: Candidate pairs from Layer 1 (MinHash).
        threshold: Cosine similarity above which a pair is confirmed
            as duplicate (default ``0.85``).
        embed_fn: Optional callable ``(list[str]) -> array-like``.

    Returns:
        A tuple of ``(confirmed, disagreements)`` lists.
    """
    if not pairs:
        return [], []

    # Lazy-load a sentence-transformer model when no embed_fn provided
    if embed_fn is None:
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer("all-MiniLM-L6-v2")
        embed_fn = model.encode

    # Collect unique chunks to avoid redundant embedding calls
    all_texts: list[str] = []
    text_index: dict[str, int] = {}
    for pair in pairs:
        for cid, content in [
            (pair.chunk_a_id, pair.chunk_a_content),
            (pair.chunk_b_id, pair.chunk_b_content),
        ]:
            if cid not in text_index:
                text_index[cid] = len(all_texts)
                all_texts.append(content)

    # Batch-embed all unique texts at once
    embeddings = embed_fn(all_texts)  # type: ignore[operator]

    confirmed: list[ConfirmedDup] = []
    disagreements: list[Disagreement] = []

    for pair in pairs:
        idx_a = text_index[pair.chunk_a_id]
        idx_b = text_index[pair.chunk_b_id]
        cos = _cosine_sim(
            np.array(embeddings[idx_a], dtype=np.float32),
            np.array(embeddings[idx_b], dtype=np.float32),
        )
        if cos >= threshold:
            confirmed.append(
                ConfirmedDup(
                    chunk_a_id=pair.chunk_a_id,
                    chunk_b_id=pair.chunk_b_id,
                    cosine_similarity=cos,
                )
            )
        else:
            disagreements.append(
                Disagreement(
                    chunk_a_id=pair.chunk_a_id,
                    chunk_b_id=pair.chunk_b_id,
                    chunk_a_content=pair.chunk_a_content,
                    chunk_b_content=pair.chunk_b_content,
                    jaccard=pair.estimated_jaccard,
                    cosine_similarity=cos,
                )
            )

    return confirmed, disagreements
