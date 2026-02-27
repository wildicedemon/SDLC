from corpus.retrieval.reranker import ScoredChunk, rerank


class TestReranker:
    def test_high_reliability_ranks_above(self) -> None:
        c1 = ScoredChunk(chunk_id="c1", content="a", semantic_score=0.5, source_reliability=0.9, freshness=1.0)
        c2 = ScoredChunk(chunk_id="c2", content="b", semantic_score=0.5, source_reliability=0.1, freshness=0.2)
        ranked = rerank([c2, c1], "query")
        assert ranked[0].chunk_id == "c1"

    def test_deterministic(self) -> None:
        chunks = [
            ScoredChunk(chunk_id="c1", content="a", semantic_score=0.8),
            ScoredChunk(chunk_id="c2", content="b", semantic_score=0.5),
        ]
        r1 = [c.chunk_id for c in rerank(list(chunks), "q")]
        r2 = [c.chunk_id for c in rerank(list(chunks), "q")]
        assert r1 == r2
