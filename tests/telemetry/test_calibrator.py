from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import Base
from corpus.db.repository import CorpusRepository
from corpus.telemetry.calibrator import calibrate
from corpus.telemetry.collector import record_outcome


def _seed_decision(repo: CorpusRepository, decision_id: str, confidence: float) -> None:
    repo.create_decision_card(
        decision_id=decision_id,
        question="test?",
        capability="test_cap",
        recommendation="use X",
        confidence_score=confidence,
        confidence_level="high" if confidence >= 0.7 else "low",
        provenance_refs="[]",
        last_validated_at="2026-01-01",
        status="active",
    )


def test_calibrate_with_enough_outcomes(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    _seed_decision(repo, "dc_cal_01", 0.5)
    session.flush()

    for _ in range(4):
        record_outcome(session, "dc_cal_01", "success")
    record_outcome(session, "dc_cal_01", "failure")
    session.flush()

    report = calibrate(session, min_outcomes=5)
    assert report.decisions_evaluated == 1
    assert report.decisions_recalibrated == 1
    assert len(report.adjustments) == 1
    _, old, new = report.adjustments[0]
    assert abs(new - 0.8) < 0.01
    session.close()


def test_calibrate_below_threshold_skipped(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    _seed_decision(repo, "dc_cal_02", 0.8)
    session.flush()

    for _ in range(3):
        record_outcome(session, "dc_cal_02", "success")
    session.flush()

    report = calibrate(session, min_outcomes=5)
    assert report.decisions_evaluated == 0
    assert report.decisions_recalibrated == 0
    session.close()


def test_calibrate_small_delta_not_recalibrated(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    _seed_decision(repo, "dc_cal_03", 0.80)
    session.flush()

    for _ in range(4):
        record_outcome(session, "dc_cal_03", "success")
    record_outcome(session, "dc_cal_03", "failure")
    session.flush()

    report = calibrate(session, min_outcomes=5)
    assert report.decisions_evaluated == 1
    assert report.decisions_recalibrated == 0
    session.close()
