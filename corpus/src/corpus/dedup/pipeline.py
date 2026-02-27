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
    if settings is None:
        settings = get_settings()

    repo = CorpusRepository(session)
    artifacts = repo.list_artifacts(run_id=run_id)

    all_chunks = []
    for art in artifacts:
        all_chunks.extend(repo.list_chunks(artifact_id=str(art.artifact_id)))

    report = DedupReport(run_id=run_id)

    candidates = generate_candidates(all_chunks, threshold=settings.dedup_l1_threshold)
    report.candidates = candidates
    report.candidate_count = len(candidates)

    if not candidates:
        return report

    confirmed, disagreements = filter_candidates(
        candidates,
        threshold=settings.dedup_l2_threshold,
        embed_fn=embed_fn,
    )
    report.confirmed = confirmed
    report.confirmed_dups = len(confirmed)
    report.disagreements = disagreements

    if candidates:
        report.l3_rate = len(disagreements) / len(candidates)
    if report.l3_rate > settings.l3_rate_alert_threshold:
        report.l3_rate_alert = True
        logger.warning(
            "L3 arbitration rate %.1f%% exceeds threshold %.1f%%",
            report.l3_rate * 100,
            settings.l3_rate_alert_threshold * 100,
        )

    if disagreements:
        if arbitrate_fn is not None:
            arb_results = arbitrate_fn(disagreements)  # type: ignore[operator]
        else:
            arb_results = arbitrate(
                disagreements,
                base_url=settings.llm_base_url,
                api_key=settings.kilo_api_key,
                model=settings.llm_model,
            )
        report.arbitration_results = arb_results
        report.arbitrated = len(arb_results)

        all_fallback = all(r.recommendation == "human_review" for r in arb_results)
        if all_fallback and arb_results:
            report.arbitration_fallback = True

        for result in arb_results:
            if result.confidence < settings.arbitration_confidence_min or result.recommendation == "human_review":
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
    chunk = repo.get_chunk(chunk_id)
    if chunk is not None:
        return str(chunk.artifact_id)
    artifacts = repo.list_artifacts(run_id=run_id)
    if artifacts:
        return str(artifacts[0].artifact_id)
    return None
