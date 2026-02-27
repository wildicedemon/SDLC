from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.repository import CorpusRepository


@dataclass
class SyncHealthReport:
    vector_synced_pct: float = 0.0
    graph_node_count: int = 0
    lag_seconds: int = 0
    healthy: bool = True


def check_sync_health(
    session: Session,
    settings: CorpusSettings | None = None,
) -> SyncHealthReport:
    if settings is None:
        settings = get_settings()

    repo = CorpusRepository(session)
    report = SyncHealthReport()

    total_chunks = 0
    synced_chunks = 0
    for art in repo.list_artifacts():
        for chunk in repo.list_chunks(artifact_id=str(art.artifact_id)):
            total_chunks += 1
            if chunk.embedding_synced:
                synced_chunks += 1

    report.vector_synced_pct = synced_chunks / total_chunks if total_chunks > 0 else 1.0

    graph_path = Path(settings.graph_path)
    if graph_path.exists():
        import json

        import networkx as nx

        data = json.loads(graph_path.read_text(encoding="utf-8"))
        G = nx.node_link_graph(data)
        report.graph_node_count = G.number_of_nodes()

    if report.vector_synced_pct < 1.0:
        report.healthy = False

    return report
