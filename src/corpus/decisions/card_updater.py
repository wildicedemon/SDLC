"""Confidence recalculation for decision cards.

After new artifacts are ingested, this module re-scores every
decision card whose capability overlaps with the new evidence.
The composite confidence score is a weighted blend of:

* **Source diversity** (30 %) — how many distinct domains contribute.
* **Recency** (30 %) — average freshness of relevant artifacts.
* **Downstream success** (20 %) — telemetry success rate.
* **Contradiction penalty** (20 %) — penalises unresolved conflicts.

Key function: :func:`update_impacted_cards`.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


def _parse_tags(raw: str) -> list[str]:
    """Parse a tag string that may be JSON-array or comma-separated.

    Args:
        raw: Raw tag string (e.g. ``'["a","b"]'`` or ``'a, b'``).

    Returns:
        A list of non-empty tag strings.
    """
    raw = raw.strip()
    if raw.startswith("["):
        try:
            return [t for t in json.loads(raw) if t]
        except (json.JSONDecodeError, TypeError):
            pass
    return [t.strip() for t in raw.split(",") if t.strip()]


def update_impacted_cards(session: Session, run_id: str) -> list[str]:
    """Recalculate confidence for every card whose capability overlaps new artifacts.

    Iterates over all decision cards and checks whether their
    ``capability`` appears in any artifact's domain or capability tags
    within the given run.  Matching cards receive an updated composite
    confidence score and have their ``last_validated_at`` timestamp
    refreshed.

    The run's ``decisions_impacted`` counter is updated at the end.

    Args:
        session: Active SQLAlchemy session.
        run_id: Consolidation run whose artifacts provide new evidence.

    Returns:
        List of decision-card IDs that were recalculated.
    """
    repo = CorpusRepository(session)
    artifacts = repo.list_artifacts(run_id=run_id)

    # Collect all capabilities and domains from newly ingested artifacts
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

        # --- Source diversity: how many distinct domains map to this capability ---
        mappings = repo.list_capability_mappings(capability=card_cap)
        source_count = len({str(m.domain) for m in mappings})

        # Collect all artifacts whose tags reference this capability
        all_artifacts = repo.list_artifacts()
        relevant = [a for a in all_artifacts if card_cap in str(a.domain_tags) or card_cap in str(a.capability_tags)]

        # Normalise source diversity to [0, 1] (3 sources → full score)
        source_diversity = min(source_count / 3.0, 1.0)

        # --- Recency: average artifact freshness (newer → higher) ---
        if relevant:
            freshness_values = [int(a.freshness_days or 0) for a in relevant]
            avg_freshness = sum(freshness_values) / len(freshness_values)
            recency = max(0.0, 1.0 - (avg_freshness / 365.0))
        else:
            recency = 0.0

        # --- Downstream success rate from telemetry outcomes ---
        outcomes = repo.list_outcomes(str(card.decision_id))
        if outcomes:
            successes = sum(1 for o in outcomes if str(o.outcome) == "success")
            downstream_success = successes / len(outcomes)
        else:
            downstream_success = 0.5  # neutral prior when no telemetry exists

        # --- Contradiction penalty ---
        contradiction_penalty = 1.0 if card.has_unresolved_contradiction else 0.0

        # Weighted composite score
        confidence = (
            0.3 * source_diversity + 0.3 * recency + 0.2 * downstream_success + 0.2 * (1.0 - contradiction_penalty)
        )
        confidence = max(0.0, min(1.0, confidence))

        # Update the card in-place
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

    # Record how many cards were impacted on the run itself
    run = repo.get_run(run_id)
    if run is not None:
        run.decisions_impacted = len(updated_ids)  # type: ignore[assignment]
        session.flush()

    return updated_ids
