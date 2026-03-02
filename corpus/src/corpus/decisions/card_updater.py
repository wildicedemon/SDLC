from __future__ import annotations

import json
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


def _parse_tags(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("["):
        try:
            return [t for t in json.loads(raw) if t]
        except (json.JSONDecodeError, TypeError):
            pass
    return [t.strip() for t in raw.split(",") if t.strip()]


def update_impacted_cards(session: Session, run_id: str) -> list[str]:
    repo = CorpusRepository(session)
    artifacts = repo.list_artifacts(run_id=run_id)

    capabilities: set[str] = set()
    for art in artifacts:
        capabilities.update(_parse_tags(str(art.capability_tags)))
        capabilities.update(_parse_tags(str(art.domain_tags)))

    if not capabilities:
        return []

    updated_ids: list[str] = []
    all_cards = repo.list_decision_cards()

    for card in all_cards:
        card_cap = str(card.capability)
        if card_cap not in capabilities:
            continue

        mappings = repo.list_capability_mappings(capability=card_cap)
        source_count = len({str(m.domain) for m in mappings})

        all_artifacts = repo.list_artifacts()
        relevant = [a for a in all_artifacts if card_cap in str(a.domain_tags) or card_cap in str(a.capability_tags)]

        source_diversity = min(source_count / 3.0, 1.0)

        if relevant:
            freshness_values = [int(a.freshness_days or 0) for a in relevant]
            avg_freshness = sum(freshness_values) / len(freshness_values)
            recency = max(0.0, 1.0 - (avg_freshness / 365.0))
        else:
            recency = 0.0

        outcomes = repo.list_outcomes(str(card.decision_id))
        if outcomes:
            successes = sum(1 for o in outcomes if str(o.outcome) == "success")
            downstream_success = successes / len(outcomes)
        else:
            downstream_success = 0.5

        contradiction_penalty = 1.0 if card.has_unresolved_contradiction else 0.0

        confidence = (
            0.3 * source_diversity + 0.3 * recency + 0.2 * downstream_success + 0.2 * (1.0 - contradiction_penalty)
        )
        confidence = max(0.0, min(1.0, confidence))

        card.confidence_score = confidence  # type: ignore[assignment]
        if confidence >= 0.7:
            card.confidence_level = "high"  # type: ignore[assignment]
        elif confidence >= 0.4:
            card.confidence_level = "medium"  # type: ignore[assignment]
        else:
            card.confidence_level = "low"  # type: ignore[assignment]
        card.last_validated_at = datetime.now(timezone.utc).isoformat()  # type: ignore[assignment]

        session.flush()
        updated_ids.append(str(card.decision_id))

    run = repo.get_run(run_id)
    if run is not None:
        run.decisions_impacted = len(updated_ids)  # type: ignore[assignment]
        session.flush()

    return updated_ids
