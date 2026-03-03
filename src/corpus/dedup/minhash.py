"""MinHash LSH deduplication — Layer 1 of the 3-layer dedup pipeline.

Uses `datasketch <https://ekzhu.com/datasketch/>`_ to build a
MinHash Locality-Sensitive Hashing index over artifact chunks.
Chunks whose estimated Jaccard similarity exceeds a configurable
threshold are emitted as :class:`CandidatePair` instances for
further verification by Layer 2 (embeddings).

Key function: :func:`generate_candidates`.
"""

from __future__ import annotations

from dataclasses import dataclass

from datasketch import MinHash, MinHashLSH

from corpus.db.models import ArtifactChunk


@dataclass
class CandidatePair:
    """A pair of chunks flagged as potential duplicates by MinHash LSH.

    Attributes:
        chunk_a_id: ID of the first chunk.
        chunk_b_id: ID of the second chunk.
        chunk_a_content: Text content of the first chunk.
        chunk_b_content: Text content of the second chunk.
        estimated_jaccard: MinHash-estimated Jaccard similarity.
    """

    chunk_a_id: str
    chunk_b_id: str
    chunk_a_content: str
    chunk_b_content: str
    estimated_jaccard: float


def _make_minhash(text: str, num_perm: int = 128) -> MinHash:
    """Create a MinHash signature from whitespace-delimited tokens.

    Args:
        text: Input text to hash.
        num_perm: Number of permutation functions (controls accuracy).

    Returns:
        A populated :class:`~datasketch.MinHash` object.
    """
    m = MinHash(num_perm=num_perm)
    for word in text.lower().split():
        m.update(word.encode("utf-8"))
    return m


def generate_candidates(
    chunks: list[ArtifactChunk],
    threshold: float = 0.5,
) -> list[CandidatePair]:
    """Identify near-duplicate chunk pairs using MinHash LSH.

    All chunks are inserted into an LSH index.  Each chunk is then
    queried against the index, and pairs exceeding *threshold* are
    returned.  Duplicate and self-match pairs are suppressed.

    Args:
        chunks: Artifact chunks to compare.
        threshold: Minimum Jaccard similarity to consider a pair a
            candidate (default ``0.5``).

    Returns:
        A deduplicated list of :class:`CandidatePair` instances.
    """
    if not chunks:
        return []

    num_perm = 128
    lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)
    minhashes: dict[str, MinHash] = {}
    content_map: dict[str, str] = {}

    for chunk in chunks:
        cid = str(chunk.chunk_id)
        content = str(chunk.content)
        mh = _make_minhash(content, num_perm)
        minhashes[cid] = mh
        content_map[cid] = content
        try:
            lsh.insert(cid, mh)
        except ValueError:
            # Duplicate key — skip silently
            pass

    # Track seen pairs by sorted ID tuple to avoid duplicates
    seen: set[tuple[str, str]] = set()
    pairs: list[CandidatePair] = []

    for cid, mh in minhashes.items():
        results = lsh.query(mh)
        for other_id in results:
            if other_id == cid:
                continue
            key = tuple(sorted((cid, other_id)))
            if key in seen:
                continue
            seen.add(key)  # type: ignore[arg-type]
            jaccard = minhashes[cid].jaccard(minhashes[other_id])
            pairs.append(
                CandidatePair(
                    chunk_a_id=key[0],
                    chunk_b_id=key[1],
                    chunk_a_content=content_map[key[0]],
                    chunk_b_content=content_map[key[1]],
                    estimated_jaccard=jaccard,
                )
            )

    return pairs
