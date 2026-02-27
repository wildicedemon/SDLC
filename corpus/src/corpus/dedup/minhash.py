from __future__ import annotations

from dataclasses import dataclass

from datasketch import MinHash, MinHashLSH

from corpus.db.models import ArtifactChunk


@dataclass
class CandidatePair:
    chunk_a_id: str
    chunk_b_id: str
    chunk_a_content: str
    chunk_b_content: str
    estimated_jaccard: float


def _make_minhash(text: str, num_perm: int = 128) -> MinHash:
    m = MinHash(num_perm=num_perm)
    for word in text.lower().split():
        m.update(word.encode("utf-8"))
    return m


def generate_candidates(
    chunks: list[ArtifactChunk],
    threshold: float = 0.5,
) -> list[CandidatePair]:
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
            pass

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
