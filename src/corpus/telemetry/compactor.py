"""Data compaction for superseded research artifacts.

Transitions old, *superseded* artifacts to *archived* status once
they exceed a configurable age threshold.  This keeps the active
corpus lean and reduces noise in dedup and retrieval.

Key function: :func:`compact`.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.db.models import ResearchArtifact


@dataclass
class CompactionReport:
    """Summary of a compaction pass.

    Attributes:
        evaluated: Number of superseded artifacts inspected.
        archived: Number of artifacts transitioned to ``archived``.
    """

    evaluated: int = 0
    archived: int = 0


def compact(session: Session, max_age_days: int = 90) -> CompactionReport:
    """Archive superseded artifacts older than *max_age_days*.

    Only artifacts with ``status='superseded'`` are considered.
    Their ``captured_at`` timestamp is compared against the current
    UTC time; those exceeding the threshold are moved to ``archived``.

    Args:
        session: Active SQLAlchemy session.
        max_age_days: Maximum age in days before archiving.

    Returns:
        A :class:`CompactionReport` with counts.
    """
    report = CompactionReport()
    now = datetime.now(timezone.utc)

    artifacts = session.query(ResearchArtifact).filter(ResearchArtifact.status == "superseded").all()

    for art in artifacts:
        report.evaluated += 1
        captured_at = str(art.captured_at)
        try:
            captured = datetime.fromisoformat(captured_at)
            if captured.tzinfo is None:
                captured = captured.replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            continue

        age_days = (now - captured).days
        if age_days > max_age_days:
            art.status = "archived"  # type: ignore[assignment]
            report.archived += 1

    session.flush()
    return report
