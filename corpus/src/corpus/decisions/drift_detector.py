from __future__ import annotations

import uuid
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository
from corpus.decisions.card_updater import _parse_tags


def detect_drift(
    session: Session,
    run_id: str,
    previous_scores: dict[str, float],
) -> list[str]:
    repo = CorpusRepository(session)
    created_ids: list[str] = []

    for decision_id, old_score in previous_scores.items():
        card = repo.get_decision_card(decision_id)
        if card is None:
            continue

        new_score = float(card.confidence_score)
        delta = new_score - old_score

        if abs(delta) > 0.1:
            event_id = f"drift-{uuid.uuid4().hex[:8]}"
            repo.create_drift_event(
                event_id=event_id,
                decision_id=decision_id,
                trigger="confidence_drop" if delta < 0 else "confidence_increase",
                confidence_delta=delta,
                affected_sections="confidence_score",
                status="pending_revalidation",
                run_id=run_id,
                created_at=datetime.now(timezone.utc).isoformat(),
            )
            created_ids.append(event_id)

        artifacts = repo.list_artifacts(run_id=run_id)
        card_cap = str(card.capability)
        contradicting = [
            a
            for a in artifacts
            if "contradict" in str(a.content).lower()
            and (card_cap in _parse_tags(str(a.domain_tags)) or card_cap in _parse_tags(str(a.capability_tags)))
        ]
        if contradicting:
            card.has_unresolved_contradiction = True  # type: ignore[assignment]
            session.flush()

            if abs(delta) <= 0.1:
                event_id = f"drift-{uuid.uuid4().hex[:8]}"
                repo.create_drift_event(
                    event_id=event_id,
                    decision_id=decision_id,
                    trigger="contradiction",
                    confidence_delta=delta,
                    affected_sections="has_unresolved_contradiction",
                    status="pending_revalidation",
                    run_id=run_id,
                    created_at=datetime.now(timezone.utc).isoformat(),
                )
                created_ids.append(event_id)

    run = repo.get_run(run_id)
    if run is not None:
        run.drift_events_count = len(created_ids)  # type: ignore[assignment]
        session.flush()

    return created_ids
