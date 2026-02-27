import uuid
from datetime import datetime, timezone

from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.decisions.card_updater import update_impacted_cards


def _setup(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


def _seed_card(
    repo: CorpusRepository,
    decision_id: str,
    capability: str,
    confidence: float = 0.5,
) -> None:
    repo.create_decision_card(
        decision_id=decision_id,
        question=f"Q about {capability}",
        capability=capability,
        recommendation="Use X",
        confidence_score=confidence,
        confidence_level="medium",
        provenance_refs="ref1",
        last_validated_at=datetime.now(timezone.utc).isoformat(),
    )


def _seed_run_and_artifact(
    repo: CorpusRepository,
    run_id: str,
    domain_tags: str,
    content: str = "test content",
) -> str:
    repo.create_run(
        run_id=run_id,
        source_branch="test",
        started_at=datetime.now(timezone.utc).isoformat(),
        status="running",
    )
    art_id = f"art-{uuid.uuid4().hex[:8]}"
    repo.create_artifact(
        artifact_id=art_id,
        title="Test",
        content=content,
        domain_tags=domain_tags,
        capability_tags="",
        source_branch="test",
        source_path="test.md",
        captured_at=datetime.now(timezone.utc).isoformat(),
        run_id=run_id,
    )
    return art_id


class TestCardUpdater:
    def test_diverse_sources_high_confidence(self, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "security")
            _seed_card(repo, "d2", "security")
            _seed_card(repo, "d3", "security")
            _seed_run_and_artifact(repo, run_id, "security")
            repo.create_capability_mapping(capability="security", decision_id="d1", domain="domain_a")
            repo.create_capability_mapping(capability="security", decision_id="d2", domain="domain_b")
            repo.create_capability_mapping(capability="security", decision_id="d3", domain="domain_c")

        with get_session(engine) as session:
            updated = update_impacted_cards(session, run_id)
            assert "d1" in updated
            repo = CorpusRepository(session)
            card = repo.get_decision_card("d1")
            assert card is not None
            assert float(card.confidence_score) > 0.5

    def test_single_source_stale_low_confidence(self, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "testing")
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_artifact(
                artifact_id="art-stale",
                title="Old",
                content="old content",
                domain_tags="testing",
                capability_tags="",
                source_branch="test",
                source_path="old.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
                freshness_days=400,
            )

        with get_session(engine) as session:
            updated = update_impacted_cards(session, run_id)
            assert "d1" in updated
            repo = CorpusRepository(session)
            card = repo.get_decision_card("d1")
            assert card is not None
            assert float(card.confidence_score) < 0.5

    def test_only_related_cards_updated(self, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "security")
            _seed_card(repo, "d2", "unrelated_topic", confidence=0.9)
            _seed_run_and_artifact(repo, run_id, "security")

        with get_session(engine) as session:
            updated = update_impacted_cards(session, run_id)
            assert "d1" in updated
            assert "d2" not in updated
            repo = CorpusRepository(session)
            card2 = repo.get_decision_card("d2")
            assert card2 is not None
            assert float(card2.confidence_score) == 0.9
