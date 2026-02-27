from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


def record_outcome(session: Session, decision_id: str, outcome: str) -> None:
    repo = CorpusRepository(session)
    repo.create_telemetry_outcome(
        decision_id=decision_id,
        timestamp=datetime.now(timezone.utc).isoformat(),
        outcome=outcome,
    )
