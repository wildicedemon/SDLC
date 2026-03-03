"""Response formatting for retrieval results.

Renders matched decision cards as markdown at varying detail levels:

* **L0** — recommendation + confidence only.
* **L1** — adds alternatives, constraints, contradiction flag, provenance.
* **L2** — adds revisit triggers and last-validated timestamp.
* **L3** — full card dump including status, explanation, and decision ID.

Key function: :func:`format_response`.
"""

from __future__ import annotations

from corpus.db.models import DecisionCard


def format_response(decisions: list[DecisionCard], depth: str) -> str:
    """Format a list of decision cards as a markdown string.

    The amount of detail included depends on *depth*:

    * ``L0`` — minimal (question, recommendation, confidence).
    * ``L1`` — standard (adds alternatives, constraints, provenance).
    * ``L2`` — extended (adds revisit triggers, timestamps).
    * ``L3`` (or anything else) — full card dump.

    Args:
        decisions: Decision cards to render.
        depth: Detail level (``L0``, ``L1``, ``L2``, or ``L3``).

    Returns:
        A markdown-formatted string, or a "no results" message
        when *decisions* is empty.
    """
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
            # L3 or any unrecognised depth — full dump
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
