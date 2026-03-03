"""Operational metrics computation for the corpus pipeline.

Aggregates high-level counters and percentages across the entire
database — runs, artifacts, chunks, decisions, drift events,
review queue, contradiction density, and vector-sync coverage.

Key function: :func:`compute_metrics`.
"""

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
    """Snapshot of corpus-wide operational health.

    Attributes:
        total_runs: Total number of consolidation runs.
        completed_runs: Runs in ``completed`` status.
        total_artifacts: Total research artifacts in the database.
        total_chunks: Total artifact chunks.
        total_decisions: Total decision cards.
        total_drift_events: Total drift events ever created.
        unresolved_reviews: Human-review items still pending.
        contradiction_density: Fraction of decisions with unresolved
            contradictions (0.0–1.0).
        vector_synced_pct: Fraction of chunks synced to ChromaDB.
    """

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
    """Compute a full set of operational metrics from the database.

    All counts are performed via direct SQLAlchemy queries for
    efficiency (no Python-side filtering).

    Args:
        session: Active SQLAlchemy session.

    Returns:
        An :class:`OperationalMetrics` snapshot.
    """
    m = OperationalMetrics()

    m.total_runs = session.query(ConsolidationRun).count()
    m.completed_runs = session.query(ConsolidationRun).filter(ConsolidationRun.status == "completed").count()
    m.total_artifacts = session.query(ResearchArtifact).count()
    m.total_chunks = session.query(ArtifactChunk).count()
    m.total_decisions = session.query(DecisionCard).count()
    m.total_drift_events = session.query(DriftEvent).count()
    m.unresolved_reviews = session.query(HumanReviewQueue).filter(HumanReviewQueue.disposition.is_(None)).count()

    # Contradiction density: fraction of decisions flagged
    if m.total_decisions > 0:
        contradicted = session.query(DecisionCard).filter(DecisionCard.has_unresolved_contradiction.is_(True)).count()
        m.contradiction_density = contradicted / m.total_decisions

    # Vector sync coverage
    synced = session.query(ArtifactChunk).filter(ArtifactChunk.embedding_synced.is_(True)).count()
    m.vector_synced_pct = synced / m.total_chunks if m.total_chunks > 0 else 1.0

    return m
