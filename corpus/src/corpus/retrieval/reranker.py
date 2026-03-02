from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ScoredChunk:
    chunk_id: str
    content: str
    semantic_score: float = 0.0
    source_reliability: float = 0.0
    freshness: float = 1.0
    task_fit: float = 0.5
    final_score: float = 0.0


def rerank(candidates: list[ScoredChunk], query: str) -> list[ScoredChunk]:
    for c in candidates:
        c.final_score = 0.4 * c.semantic_score + 0.3 * c.source_reliability + 0.2 * c.freshness + 0.1 * c.task_fit
    candidates.sort(key=lambda c: c.final_score, reverse=True)
    return candidates
