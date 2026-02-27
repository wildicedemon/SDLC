from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.db.models import ResearchArtifact


@dataclass
class CompactionReport:
    evaluated: int = 0
    archived: int = 0


def compact(session: Session, max_age_days: int = 90) -> CompactionReport:
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
