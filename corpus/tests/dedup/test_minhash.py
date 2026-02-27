from corpus.db.models import ArtifactChunk
from corpus.dedup.minhash import generate_candidates


def _make_chunk(chunk_id: str, content: str) -> ArtifactChunk:
    return ArtifactChunk(
        chunk_id=chunk_id,
        content=content,
        artifact_id="art-1",
        chunk_index=0,
        embedding_synced=False,
    )


class TestMinhash:
    def test_identical_chunks_generate_candidate(self) -> None:
        text = "the quick brown fox jumps over the lazy dog " * 10
        c1 = _make_chunk("c1", text)
        c2 = _make_chunk("c2", text)
        pairs = generate_candidates([c1, c2], threshold=0.5)
        assert len(pairs) == 1
        assert {pairs[0].chunk_a_id, pairs[0].chunk_b_id} == {"c1", "c2"}

    def test_completely_different_chunks_no_candidate(self) -> None:
        c1 = _make_chunk("c1", "alpha bravo charlie delta echo foxtrot golf hotel india")
        c2 = _make_chunk("c2", "one two three four five six seven eight nine ten eleven twelve")
        pairs = generate_candidates([c1, c2], threshold=0.5)
        assert len(pairs) == 0

    def test_near_duplicate_generates_candidate(self) -> None:
        base = "the quick brown fox jumps over the lazy dog near the riverbank"
        words = base.split()
        modified = words[: int(len(words) * 0.8)] + ["modified", "text", "here"]
        c1 = _make_chunk("c1", " ".join(words * 5))
        c2 = _make_chunk("c2", " ".join(modified * 5))
        pairs = generate_candidates([c1, c2], threshold=0.3)
        assert len(pairs) >= 1
