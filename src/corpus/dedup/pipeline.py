"""Three-layer deduplication orchestration pipeline.

Coordinates the three dedup layers in sequence:

1. **Layer 1 — MinHash LSH** (:func:`~corpus.dedup.minhash.generate_candidates`):
   fast token-level Jaccard similarity to surface candidate pairs.
2. **Layer 2 — Embeddings** (:func:`~corpus.dedup.embeddings.filter_candidates`):
   semantic cosine similarity to confirm or reject candidates.
3. **Layer 3 — LLM Arbitration** (:func:`~corpus.dedup.arbitrator.arbitrate`):
   asks an LLM to resolve any L1/L2 disagreements.

Pairs that the LLM routes to ``human_review`` are enqueued in the
:class:`~corpus.db.models.HumanReviewQueue`.

Key function: :func:`run_dedup`.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.repository import CorpusRepository
from corpus.dedup.arbitrator import ArbitrationResult, arbitrate
from corpus.dedup.embeddings import ConfirmedDup, Disagreement, filter_candidates
from corpus.dedup.minhash import CandidatePair, generate_candidates

logger = logging.getLogger(__name__)


@dataclass
class DedupReport:
    """Summary report produced by :func:`run_dedup`.

    Attributes:
        run_id: Consolidation run this report belongs to.
        candidate_count: Number of L1 candidate pairs found.
        confirmed_dups: Pairs confirmed as duplicates by L2.
        arbitrated: Number of pairs sent through L3 arbitration.
        human_queued: Pairs routed to the human review queue.
        l3_rate: Fraction of L1 candidates that reached L3.
        l3_rate_alert: ``True`` if *l3_rate* exceeds the alert threshold.
        arbitration_fallback: ``True`` if every L3 result was ``human_review``.
        candidates: Raw L1 candidate pairs.
        confirmed: L2-confirmed duplicate pairs.
        disagreements: L1/L2 disagreement pairs.
        arbitration_results: L3 arbitration outcomes.
    """

    run_id: str
    candidate_count: int = 0
    confirmed_dups: int = 0
    arbitrated: int = 0
    human_queued: int = 0
    l3_rate: float = 0.0
    l3_rate_alert: bool = False
    arbitration_fallback: bool = False
    candidates: list[CandidatePair] = field(default_factory=list)
    confirmed: list[ConfirmedDup] = field(default_factory=list)
    disagreements: list[Disagreement] = field(default_factory=list)
    arbitration_results: list[ArbitrationResult] = field(default_factory=list)


def run_dedup(
    session: Session,
    run_id: str,
    settings: CorpusSettings | None = None,
    embed_fn: object | None = None,
    arbitrate_fn: object | None = None,
) -> DedupReport:
    """Execute the full 3-layer dedup pipeline for a consolidation run.

    Args:
        session: Active SQLAlchemy session.
        run_id: ID of the consolidation run whose artifacts to dedup.
        settings: Pipeline configuration; loaded from env if ``None``.
        embed_fn: Optional override for the embedding function.
        arbitrate_fn: Optional override for the arbitration function.

    Returns:
        A :class:`DedupReport` with counts and detailed pair lists.
    """
    if settings is None:
        settings = get_settings()

    repo = CorpusRepository(session)
    artifacts = repo.list_artifacts(run_id=run_id)

    # Collect all chunks across artifacts for this run
    all_chunks = []
    for art in artifacts:
        all_chunks.extend(repo.list_chunks(artifact_id=str(art.artifact_id)))

    report = DedupReport(run_id=run_id)

    # --- Layer 1: MinHash LSH candidate generation ---
    candidates = generate_candidates(all_chunks, threshold=settings.dedup_l1_threshold)
    report.candidates = candidates
    report.candidate_count = len(candidates)

    if not candidates:
        return report

    # --- Layer 2: Embedding-based confirmation ---
    confirmed, disagreements = filter_candidates(
        candidates,
        threshold=settings.dedup_l2_threshold,
        embed_fn=embed_fn,
    )
    report.confirmed = confirmed
    report.confirmed_dups = len(confirmed)
    report.disagreements = disagreements

    # Calculate L3 escalation rate and alert if too high
    if candidates:
        report.l3_rate = len(disagreements) / len(candidates)
    if report.l3_rate > settings.l3_rate_alert_threshold:
        report.l3_rate_alert = True
        logger.warning(
            "L3 arbitration rate %.1f%% exceeds threshold %.1f%%",
            report.l3_rate * 100,
            settings.l3_rate_alert_threshold * 100,
        )

    # --- Layer 3: LLM / auto arbitration ---
    if disagreements:
        if arbitrate_fn is not None:
            arb_results = arbitrate_fn(disagreements)  # type: ignore[operator]
        else:
            arb_results = arbitrate(
                disagreements,
                base_url=settings.llm_base_url,
                api_key=settings.kilo_api_key,
                model=settings.llm_model,
                max_calls=settings.max_arbitration_calls,
            )
        report.arbitration_results = arb_results
        report.arbitrated = len(arb_results)

        # Detect total fallback — every result routed to human review
        all_fallback = all(r.recommendation == "human_review" for r in arb_results)
        if all_fallback and arb_results:
            report.arbitration_fallback = True

        # Enqueue human-review items in the review queue
        for result in arb_results:
            if result.recommendation == "human_review":
                art_a = _find_artifact_for_chunk(repo, result.chunk_a_id, run_id)
                art_b = _find_artifact_for_chunk(repo, result.chunk_b_id, run_id)
                if art_a and art_b:
                    repo.create_review_item(
                        run_id=run_id,
                        item_type="dedup_disagreement",
                        artifact_a_id=art_a,
                        artifact_b_id=art_b,
                        ai_confidence=result.confidence,
                        ai_recommendation=result.recommendation,
                    )
                    report.human_queued += 1

    return report


def _find_artifact_for_chunk(repo: CorpusRepository, chunk_id: str, run_id: str) -> str | None:
    """Resolve a chunk ID to its parent artifact ID.

    Falls back to the first artifact in the run if the chunk's own
    artifact reference cannot be found (defensive fallback).

    Args:
        repo: The corpus repository.
        chunk_id: The chunk to look up.
        run_id: Current consolidation run (for fallback).

    Returns:
        The artifact ID string, or ``None`` if nothing could be resolved.
    """
    chunk = repo.get_chunk(chunk_id)
    if chunk is not None:
        return str(chunk.artifact_id)
    # Fallback: return the first artifact in this run
    artifacts = repo.list_artifacts(run_id=run_id)
    if artifacts:
        return str(artifacts[0].artifact_id)
    return None
