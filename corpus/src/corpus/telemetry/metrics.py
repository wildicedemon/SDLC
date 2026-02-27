from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from corpus.db.models import (
    ArtifactChunk,
    ConsolidationRun,
    DecisionCard,
    DriftEvent,
    HumanReviewQueue,
    ResearchArtifact,
)


@dataclass
class OperationalMetrics:
    total_runs: int = 0
    completed_runs: int = 0
    total_artifacts: int = 0
    total_chunks: int = 0
    total_decisions: int = 0
    total_drift_events: int = 0
    unresolved_reviews: int = 0
    contradiction_density: float = 0.0
    vector_synced_pct: float = 0.0


def compute_metrics(session: Session) -> OperationalMetrics:
    m = OperationalMetrics()

    m.total_runs = session.query(ConsolidationRun).count()
    m.completed_runs = session.query(ConsolidationRun).filter(ConsolidationRun.status == "completed").count()
    m.total_artifacts = session.query(ResearchArtifact).count()
    m.total_chunks = session.query(ArtifactChunk).count()
    m.total_decisions = session.query(DecisionCard).count()
    m.total_drift_events = session.query(DriftEvent).count()
    m.unresolved_reviews = session.query(HumanReviewQueue).filter(HumanReviewQueue.disposition.is_(None)).count()

    if m.total_decisions > 0:
        contradicted = session.query(DecisionCard).filter(DecisionCard.has_unresolved_contradiction.is_(True)).count()
        m.contradiction_density = contradicted / m.total_decisions

    synced = session.query(ArtifactChunk).filter(ArtifactChunk.embedding_synced.is_(True)).count()
    m.vector_synced_pct = synced / m.total_chunks if m.total_chunks > 0 else 1.0

    return m
