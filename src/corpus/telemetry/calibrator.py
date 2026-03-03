"""Confidence calibration based on telemetry outcomes.

Compares each decision card's stored confidence score against the
actual success rate derived from telemetry outcomes.  When the
gap exceeds a threshold (default 5 %), the score is adjusted to
match observed reality.

Key function: :func:`calibrate`.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


@dataclass
class CalibrationReport:
    """Summary of a calibration pass.

    Attributes:
        decisions_evaluated: Cards with enough outcomes to evaluate.
        decisions_recalibrated: Cards whose score was adjusted.
        adjustments: Tuples of ``(decision_id, old_score, new_score)``.
    """

    decisions_evaluated: int = 0
    decisions_recalibrated: int = 0
    adjustments: list[tuple[str, float, float]] = field(default_factory=list)


def calibrate(session: Session, min_outcomes: int = 5) -> CalibrationReport:
    """Recalibrate confidence scores from real-world telemetry.

    Only decision cards with at least *min_outcomes* telemetry
    records are evaluated.  If the observed success rate differs
    from the stored confidence score by more than 5 %, the score
    is overwritten with the success rate (clamped to [0, 1]).

    Args:
        session: Active SQLAlchemy session.
        min_outcomes: Minimum number of outcomes required before
            recalibrating a card.

    Returns:
        A :class:`CalibrationReport` detailing what was changed.
    """
    repo = CorpusRepository(session)
    report = CalibrationReport()

    cards = repo.list_decision_cards()
    for card in cards:
        decision_id = str(card.decision_id)
        outcomes = repo.list_outcomes(decision_id)
        if len(outcomes) < min_outcomes:
            continue

        report.decisions_evaluated += 1
        successes = sum(1 for o in outcomes if str(o.outcome) == "success")
        success_rate = successes / len(outcomes)

        old_score = float(card.confidence_score)
        delta = abs(success_rate - old_score)

        # Only adjust when observed reality differs meaningfully
        if delta > 0.05:
            new_score = max(0.0, min(1.0, success_rate))
            card.confidence_score = new_score  # type: ignore[assignment]
            session.flush()
            report.decisions_recalibrated += 1
            report.adjustments.append((decision_id, old_score, new_score))

    return report
