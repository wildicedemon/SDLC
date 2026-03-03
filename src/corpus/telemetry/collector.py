"""Telemetry outcome recording.

Provides a thin helper to persist ``success`` or ``failure``
outcomes for individual decision cards.  These records are later
aggregated by the calibrator to adjust confidence scores.

Key function: :func:`record_outcome`.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


def record_outcome(session: Session, decision_id: str, outcome: str) -> None:
    """Persist a telemetry outcome for a decision card.

    Args:
        session: Active SQLAlchemy session.
        decision_id: The decision card this outcome relates to.
        outcome: Either ``"success"`` or ``"failure"``.
    """
    repo = CorpusRepository(session)
    repo.create_telemetry_outcome(
        decision_id=decision_id,
        timestamp=datetime.now(timezone.utc).isoformat(),
        outcome=outcome,
    )
