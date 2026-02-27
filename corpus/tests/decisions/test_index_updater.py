from datetime import datetime, timezone

from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.decisions.index_updater import update_indices


def _setup(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


class TestIndexUpdater:
    def test_new_mapping_created(self, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_decision_card(
                decision_id="d1",
                question="Q",
                capability="security",
                recommendation="Use X",
                confidence_score=0.7,
                confidence_level="medium",
                provenance_refs="domain_a",
                last_validated_at=datetime.now(timezone.utc).isoformat(),
            )

        with get_session(engine) as session:
            update_indices(session, ["d1"])
            repo = CorpusRepository(session)
            mappings = repo.list_capability_mappings(capability="security")
            assert len(mappings) == 1
            assert str(mappings[0].decision_id) == "d1"

    def test_existing_mapping_not_duplicated(self, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_decision_card(
                decision_id="d1",
                question="Q",
                capability="security",
                recommendation="Use X",
                confidence_score=0.7,
                confidence_level="medium",
                provenance_refs="domain_a",
                last_validated_at=datetime.now(timezone.utc).isoformat(),
            )
            repo.create_capability_mapping(
                capability="security",
                decision_id="d1",
                domain="domain_a",
            )

        with get_session(engine) as session:
            update_indices(session, ["d1"])
            repo = CorpusRepository(session)
            mappings = repo.list_capability_mappings(capability="security")
            assert len(mappings) == 1
