from datetime import datetime, timezone

from corpus.config import CorpusSettings
from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.retrieval.orchestrator import query


def _setup(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


def _seed_card(
    repo: CorpusRepository,
    decision_id: str,
    capability: str,
    confidence: float,
    contradiction: bool = False,
) -> None:
    repo.create_decision_card(
        decision_id=decision_id,
        question=f"How to {capability}?",
        capability=capability,
        recommendation=f"Use best {capability}",
        confidence_score=confidence,
        confidence_level="high" if confidence >= 0.7 else ("medium" if confidence >= 0.4 else "low"),
        has_unresolved_contradiction=contradiction,
        provenance_refs="ref1",
        last_validated_at=datetime.now(timezone.utc).isoformat(),
    )


class TestOrchestrator:
    def test_high_confidence_l1(self, tmp_path: object, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(
            db_url=tmp_db_url,
            chroma_dir=str(tmp_path) + "/chroma",  # type: ignore[operator]
            graph_path=str(tmp_path) + "/graph.json",  # type: ignore[operator]
            kilo_api_key="test",
        )

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "security", 0.85)

        with get_session(engine) as session:
            resp = query(session, "security", settings=settings)

        assert resp.depth == "L1"
        assert resp.escalation_reason is None

    def test_moderate_confidence_escalates_l2(self, tmp_path: object, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(
            db_url=tmp_db_url,
            chroma_dir=str(tmp_path) + "/chroma",  # type: ignore[operator]
            graph_path=str(tmp_path) + "/graph.json",  # type: ignore[operator]
            kilo_api_key="test",
        )

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "security", 0.65)

        with get_session(engine) as session:
            resp = query(session, "security", settings=settings)

        assert resp.depth == "L2"
        assert resp.escalation_reason is not None

    def test_low_confidence_escalates_l3(self, tmp_path: object, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(
            db_url=tmp_db_url,
            chroma_dir=str(tmp_path) + "/chroma",  # type: ignore[operator]
            graph_path=str(tmp_path) + "/graph.json",  # type: ignore[operator]
            kilo_api_key="test",
        )

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "security", 0.40)

        with get_session(engine) as session:
            resp = query(session, "security", settings=settings)

        assert resp.depth == "L3"

    def test_contradiction_escalates_l3(self, tmp_path: object, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(
            db_url=tmp_db_url,
            chroma_dir=str(tmp_path) + "/chroma",  # type: ignore[operator]
            graph_path=str(tmp_path) + "/graph.json",  # type: ignore[operator]
            kilo_api_key="test",
        )

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "security", 0.90, contradiction=True)

        with get_session(engine) as session:
            resp = query(session, "security", settings=settings)

        assert resp.depth == "L3"

    def test_explicit_depth_overrides(self, tmp_path: object, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(
            db_url=tmp_db_url,
            chroma_dir=str(tmp_path) + "/chroma",  # type: ignore[operator]
            graph_path=str(tmp_path) + "/graph.json",  # type: ignore[operator]
            kilo_api_key="test",
        )

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "security", 0.40)

        with get_session(engine) as session:
            resp = query(session, "security", depth_override="L0", settings=settings)

        assert resp.depth == "L0"

    def test_provenance_non_empty(self, tmp_path: object, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        settings = CorpusSettings(
            db_url=tmp_db_url,
            chroma_dir=str(tmp_path) + "/chroma",  # type: ignore[operator]
            graph_path=str(tmp_path) + "/graph.json",  # type: ignore[operator]
            kilo_api_key="test",
        )

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            _seed_card(repo, "d1", "security", 0.85)

        with get_session(engine) as session:
            resp = query(session, "security", settings=settings)

        assert len(resp.provenance) >= 1
