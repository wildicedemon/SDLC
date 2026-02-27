from __future__ import annotations

from dataclasses import dataclass, field

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


@dataclass
class CalibrationReport:
    decisions_evaluated: int = 0
    decisions_recalibrated: int = 0
    adjustments: list[tuple[str, float, float]] = field(default_factory=list)


def calibrate(session: Session, min_outcomes: int = 5) -> CalibrationReport:
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

        if delta > 0.05:
            new_score = max(0.0, min(1.0, success_rate))
            card.confidence_score = new_score  # type: ignore[assignment]
            session.flush()
            report.decisions_recalibrated += 1
            report.adjustments.append((decision_id, old_score, new_score))

    return report
