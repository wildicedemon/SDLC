"""Sync health monitoring for the vector store and knowledge graph.

Checks two metrics:
* **Vector sync percentage** — fraction of chunks whose embeddings
  have been synced to ChromaDB.
* **Graph node count** — number of nodes in the persisted NetworkX graph.

If any chunks are un-synced, ``healthy`` is set to ``False``.

Key function: :func:`check_sync_health`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.repository import CorpusRepository


@dataclass
class SyncHealthReport:
    """Summary of vector-store and graph health.

    Attributes:
        vector_synced_pct: Fraction (0.0–1.0) of chunks synced to ChromaDB.
        graph_node_count: Number of nodes in the knowledge graph.
        lag_seconds: Reserved for future use (latency metric placeholder).
        healthy: ``True`` when all chunks are synced and graph exists.
    """

    vector_synced_pct: float = 0.0
    graph_node_count: int = 0
    lag_seconds: int = 0
    healthy: bool = True


def check_sync_health(
    session: Session,
    settings: CorpusSettings | None = None,
) -> SyncHealthReport:
    """Assess the sync health of the vector store and knowledge graph.

    Args:
        session: Active SQLAlchemy session.
        settings: Pipeline configuration; loaded from env if ``None``.

    Returns:
        A :class:`SyncHealthReport` summarising sync status.
    """
    if settings is None:
        settings = get_settings()

    repo = CorpusRepository(session)
    report = SyncHealthReport()

    # --- Vector sync percentage ---
    total_chunks = 0
    synced_chunks = 0
    for art in repo.list_artifacts():
        for chunk in repo.list_chunks(artifact_id=str(art.artifact_id)):
            total_chunks += 1
            if chunk.embedding_synced:
                synced_chunks += 1

    report.vector_synced_pct = synced_chunks / total_chunks if total_chunks > 0 else 1.0

    # --- Graph node count ---
    graph_path = Path(settings.graph_path)
    if graph_path.exists():
        import json

        import networkx as nx

        data = json.loads(graph_path.read_text(encoding="utf-8"))
        G = nx.node_link_graph(data)
        report.graph_node_count = G.number_of_nodes()

    # Any un-synced chunks mean the system isn't fully healthy
    if report.vector_synced_pct < 1.0:
        report.healthy = False

    return report
