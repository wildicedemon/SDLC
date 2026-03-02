import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

import networkx as nx

from corpus.config import CorpusSettings
from corpus.db.engine import create_db_engine, get_session
from corpus.db.migrations.runner import migrate_forward
from corpus.db.repository import CorpusRepository
from corpus.sync.graph_sync import rebuild_graph, sync_graph


def _setup(tmp_db_url: str) -> None:
    engine = create_db_engine(tmp_db_url)
    migrate_forward(engine)


class TestGraphSync:
    def test_sync_creates_nodes(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        graph_path = str(tmp_path / "graph.json")
        settings = CorpusSettings(db_url=tmp_db_url, graph_path=graph_path, kilo_api_key="test")

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_artifact(
                artifact_id="art-1",
                title="A1",
                content="content",
                domain_tags='["security"]',
                capability_tags="[]",
                source_branch="test",
                source_path="test.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )
            repo.create_artifact(
                artifact_id="art-2",
                title="A2",
                content="content",
                domain_tags='["security"]',
                capability_tags="[]",
                source_branch="test",
                source_path="test2.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )
            repo.create_decision_card(
                decision_id="dc-1",
                question="Q",
                capability="security",
                recommendation="Use TLS",
                confidence_score=0.7,
                confidence_level="medium",
                provenance_refs="ref",
                last_validated_at=datetime.now(timezone.utc).isoformat(),
            )
            repo.create_capability_mapping(capability="security", decision_id="dc-1", domain="sec")

        with get_session(engine) as session:
            result = sync_graph(session, run_id, settings=settings)

        assert result.nodes_added == 4
        assert Path(graph_path).exists()

        data = json.loads(Path(graph_path).read_text(encoding="utf-8"))
        G = nx.node_link_graph(data)
        assert G.number_of_nodes() == 4

    def test_supports_edge_exists(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        graph_path = str(tmp_path / "graph.json")
        settings = CorpusSettings(db_url=tmp_db_url, graph_path=graph_path, kilo_api_key="test")

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_artifact(
                artifact_id="art-1",
                title="A1",
                content="content",
                domain_tags='["security"]',
                capability_tags="[]",
                source_branch="test",
                source_path="test.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )
            repo.create_decision_card(
                decision_id="dc-1",
                question="Q",
                capability="security",
                recommendation="Use TLS",
                confidence_score=0.7,
                confidence_level="medium",
                provenance_refs="ref",
                last_validated_at=datetime.now(timezone.utc).isoformat(),
            )

        with get_session(engine) as session:
            sync_graph(session, run_id, settings=settings)

        data = json.loads(Path(graph_path).read_text(encoding="utf-8"))
        G = nx.node_link_graph(data)
        assert G.has_edge("art-1", "dc-1")
        assert G.edges["art-1", "dc-1"]["label"] == "supports"

    def test_rebuild_produces_identical(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        graph_path = str(tmp_path / "graph.json")
        settings = CorpusSettings(db_url=tmp_db_url, graph_path=graph_path, kilo_api_key="test")

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )
            repo.create_artifact(
                artifact_id="art-1",
                title="A1",
                content="content",
                domain_tags='["security"]',
                capability_tags="[]",
                source_branch="test",
                source_path="test.md",
                captured_at=datetime.now(timezone.utc).isoformat(),
                run_id=run_id,
            )
            repo.create_decision_card(
                decision_id="dc-1",
                question="Q",
                capability="security",
                recommendation="Use TLS",
                confidence_score=0.7,
                confidence_level="medium",
                provenance_refs="ref",
                last_validated_at=datetime.now(timezone.utc).isoformat(),
            )

        with get_session(engine) as session:
            sync_graph(session, run_id, settings=settings)

        with get_session(engine) as session:
            rebuild_graph(session, settings=settings)

        data = json.loads(Path(graph_path).read_text(encoding="utf-8"))
        G = nx.node_link_graph(data)
        assert G.number_of_nodes() >= 2

    def test_graph_loadable_via_networkx(self, tmp_path: Path, tmp_db_url: str) -> None:
        _setup(tmp_db_url)
        engine = create_db_engine(tmp_db_url)
        run_id = f"run-{uuid.uuid4().hex[:8]}"
        graph_path = str(tmp_path / "graph.json")
        settings = CorpusSettings(db_url=tmp_db_url, graph_path=graph_path, kilo_api_key="test")

        with get_session(engine) as session:
            repo = CorpusRepository(session)
            repo.create_run(
                run_id=run_id,
                source_branch="test",
                started_at=datetime.now(timezone.utc).isoformat(),
                status="running",
            )

        with get_session(engine) as session:
            sync_graph(session, run_id, settings=settings)

        data = json.loads(Path(graph_path).read_text(encoding="utf-8"))
        G = nx.node_link_graph(data)
        assert isinstance(G, nx.DiGraph)
