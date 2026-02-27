from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from corpus.dedup.minhash import CandidatePair


@dataclass
class ConfirmedDup:
    chunk_a_id: str
    chunk_b_id: str
    cosine_similarity: float


@dataclass
class Disagreement:
    chunk_a_id: str
    chunk_b_id: str
    chunk_a_content: str
    chunk_b_content: str
    jaccard: float
    cosine_similarity: float


EmbedFn = type[None] | object


def _cosine_sim(a: NDArray[np.float32], b: NDArray[np.float32]) -> float:
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
    if not pairs:
        return [], []

    if embed_fn is None:
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer("all-MiniLM-L6-v2")
        embed_fn = model.encode

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
