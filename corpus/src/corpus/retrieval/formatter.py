from __future__ import annotations

from corpus.db.models import DecisionCard


def format_response(decisions: list[DecisionCard], depth: str) -> str:
    if not decisions:
        return "No matching decisions found."

    parts: list[str] = []
    for card in decisions:
        if depth == "L0":
            parts.append(
                f"## {card.question}\n"
                f"**Recommendation**: {card.recommendation}\n"
                f"**Confidence**: {card.confidence_score} ({card.confidence_level})\n"
                f"**Rationale**: {card.confidence_explanation or 'N/A'}\n"
            )
        elif depth == "L1":
            parts.append(
                f"## {card.question}\n"
                f"**Recommendation**: {card.recommendation}\n"
                f"**Confidence**: {card.confidence_score} ({card.confidence_level})\n"
                f"**Alternatives**: {card.alternatives or 'None'}\n"
                f"**Constraints**: {card.constraints or 'None'}\n"
                f"**Contradiction**: {'YES' if card.has_unresolved_contradiction else 'No'}\n"
                f"**Provenance**: {card.provenance_refs}\n"
            )
        elif depth == "L2":
            parts.append(
                f"## {card.question}\n"
                f"**Recommendation**: {card.recommendation}\n"
                f"**Confidence**: {card.confidence_score} ({card.confidence_level})\n"
                f"**Alternatives**: {card.alternatives or 'None'}\n"
                f"**Constraints**: {card.constraints or 'None'}\n"
                f"**Contradiction**: {'YES' if card.has_unresolved_contradiction else 'No'}\n"
                f"**Provenance**: {card.provenance_refs}\n"
                f"**Revisit Triggers**: {card.revisit_triggers or 'None'}\n"
                f"**Last Validated**: {card.last_validated_at}\n"
            )
        else:
            parts.append(
                f"## {card.question}\n"
                f"**Recommendation**: {card.recommendation}\n"
                f"**Confidence**: {card.confidence_score} ({card.confidence_level})\n"
                f"**Explanation**: {card.confidence_explanation or 'N/A'}\n"
                f"**Alternatives**: {card.alternatives or 'None'}\n"
                f"**Constraints**: {card.constraints or 'None'}\n"
                f"**Contradiction**: {'YES' if card.has_unresolved_contradiction else 'No'}\n"
                f"**Provenance**: {card.provenance_refs}\n"
                f"**Revisit Triggers**: {card.revisit_triggers or 'None'}\n"
                f"**Last Validated**: {card.last_validated_at}\n"
                f"**Status**: {card.status}\n"
                f"**Decision ID**: {card.decision_id}\n"
            )

    return "\n".join(parts)
