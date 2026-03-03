"""Result reranking for retrieval candidates.

Computes a weighted final score from four signals and sorts
candidates in descending order.

Weights:
  * semantic_score    40 %
  * source_reliability 30 %
  * freshness          20 %
  * task_fit           10 %

Key function: :func:`rerank`.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ScoredChunk:
    """A chunk with multi-dimensional scoring.

    Attributes:
        chunk_id: Identifier for the chunk.
        content: Text content of the chunk.
        semantic_score: Similarity score from vector search.
        source_reliability: Reliability of the chunk's source.
        freshness: Recency score (1.0 = very recent).
        task_fit: How well the chunk fits the current task.
        final_score: Weighted composite score (set by :func:`rerank`).
    """

    chunk_id: str
    content: str
    semantic_score: float = 0.0
    source_reliability: float = 0.0
    freshness: float = 1.0
    task_fit: float = 0.5
    final_score: float = 0.0


def rerank(candidates: list[ScoredChunk], query: str) -> list[ScoredChunk]:
    """Compute final scores and sort candidates in-place.

    Args:
        candidates: Chunks to rerank (modified in-place).
        query: The original query string (reserved for future
            query-aware scoring).

    Returns:
        The same list, sorted by ``final_score`` descending.
    """
    for c in candidates:
        c.final_score = 0.4 * c.semantic_score + 0.3 * c.source_reliability + 0.2 * c.freshness + 0.1 * c.task_fit
    candidates.sort(key=lambda c: c.final_score, reverse=True)
    return candidates
