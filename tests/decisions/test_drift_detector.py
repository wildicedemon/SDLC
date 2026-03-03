import uuid
from datetime import datetime, timezone

from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.decisions.drift_detector import detect_drift


def _setup(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


class TestDriftDetector:
    def test_confidence_drop_creates_event(self, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_decision_card(
                decision_id="d1",
                question="Q",
                capability="security",
                recommendation="Use X",
                confidence_score=0.6,
                confidence_level="medium",
                provenance_refs="ref1",
                last_validated_at=datetime.now(timezone.utc).isoformat(),
            )

        with get_session(engine) as session:
            ids = detect_drift(session, run_id, {"d1": 0.8})
            assert len(ids) >= 1
            repo = CorpusRepository(session)
            event = repo.get_drift_event(ids[0])
            assert event is not None
            assert str(event.trigger) == "confidence_drop"

    def test_contradiction_sets_flag(self, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_decision_card(
                decision_id="d1",
                question="Q",
                capability="security",
                recommendation="Use X",
                confidence_score=0.7,
                confidence_level="medium",
                provenance_refs="ref1",
                last_validated_at=datetime.now(timezone.utc).isoformat(),
            )
            repo.create_artifact(
                artifact_id="art-contra",
                title="Contradicting",
                content="This contradicts existing security recommendation",
                domain_tags="security",
                capability_tags="",
                source_branch="test",
                source_path="contra.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )

        with get_session(engine) as session:
            detect_drift(session, run_id, {"d1": 0.7})
            repo = CorpusRepository(session)
            card = repo.get_decision_card("d1")
            assert card is not None
            assert card.has_unresolved_contradiction is True

    def test_no_change_no_event(self, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_decision_card(
                decision_id="d1",
                question="Q",
                capability="security",
                recommendation="Use X",
                confidence_score=0.7,
                confidence_level="medium",
                provenance_refs="ref1",
                last_validated_at=datetime.now(timezone.utc).isoformat(),
            )

        with get_session(engine) as session:
            ids = detect_drift(session, run_id, {"d1": 0.7})
            assert len(ids) == 0
