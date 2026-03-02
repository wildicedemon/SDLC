import numpy as np

from corpus.dedup.embeddings import filter_candidates
from corpus.dedup.minhash import CandidatePair


def _mock_embed_similar(texts: list[str]) -> list[list[float]]:
    vecs = []
    for i, _ in enumerate(texts):
        base = np.ones(384, dtype=np.float32) * 0.5
        base[i % 384] += 0.01 * i
        vecs.append(base.tolist())
    return vecs


def _mock_embed_dissimilar(texts: list[str]) -> list[list[float]]:
    vecs = []
    for i, _ in enumerate(texts):
        v = np.zeros(384, dtype=np.float32)
        v[i % 384] = 1.0
        vecs.append(v.tolist())
    return vecs


class TestEmbeddings:
    def test_similar_pair_confirmed(self) -> None:
        pair = CandidatePair(
            chunk_a_id="c1",
            chunk_b_id="c2",
            chunk_a_content="the quick brown fox",
            chunk_b_content="the quick brown fox jumps",
            estimated_jaccard=0.8,
        )
        confirmed, disagreements = filter_candidates([pair], threshold=0.85, embed_fn=_mock_embed_similar)
        assert len(confirmed) == 1
        assert confirmed[0].cosine_similarity >= 0.85

    def test_dissimilar_pair_disagreement(self) -> None:
        pair = CandidatePair(
            chunk_a_id="c1",
            chunk_b_id="c2",
            chunk_a_content="alpha bravo charlie",
            chunk_b_content="delta echo foxtrot",
            estimated_jaccard=0.6,
        )
        confirmed, disagreements = filter_candidates([pair], threshold=0.85, embed_fn=_mock_embed_dissimilar)
        assert len(disagreements) == 1
        assert disagreements[0].cosine_similarity < 0.85
