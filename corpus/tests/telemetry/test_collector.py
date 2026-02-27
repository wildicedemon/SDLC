from corpus.db.engine import create_db_engine, make_session_factory
from corpus.db.models import Base, TelemetryOutcome
from corpus.db.repository import CorpusRepository
from corpus.telemetry.collector import record_outcome


def test_record_outcome_persists(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    repo.create_decision_card(
        decision_id="dc_coll_01",
        question="test?",
        capability="test_cap",
        recommendation="use X",
        confidence_score=0.8,
        confidence_level="high",
        provenance_refs="[]",
        last_validated_at="2026-01-01",
        status="active",
    )
    session.flush()

    record_outcome(session, "dc_coll_01", "success")
    session.flush()

    rows = session.query(TelemetryOutcome).filter_by(decision_id="dc_coll_01").all()
    assert len(rows) == 1
    assert str(rows[0].outcome) == "success"
    assert rows[0].timestamp is not None
    session.close()


def test_multiple_outcomes_for_same_decision(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    Base.metadata.create_all(engine)
    session = make_session_factory(engine)()
    repo = CorpusRepository(session)

    repo.create_decision_card(
        decision_id="dc_coll_02",
        question="test?",
        capability="test_cap",
        recommendation="use X",
        confidence_score=0.8,
        confidence_level="high",
        provenance_refs="[]",
        last_validated_at="2026-01-01",
        status="active",
    )
    session.flush()

    record_outcome(session, "dc_coll_02", "success")
    record_outcome(session, "dc_coll_02", "failure")
    record_outcome(session, "dc_coll_02", "success")
    session.flush()

    outcomes = repo.list_outcomes("dc_coll_02")
    assert len(outcomes) == 3
    session.close()
