from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import networkx as nx
from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.repository import CorpusRepository
from corpus.decisions.card_updater import _parse_tags


@dataclass
class SyncResult:
    nodes_added: int = 0
    edges_added: int = 0


def sync_graph(
    session: Session,
    run_id: str,
    settings: CorpusSettings | None = None,
) -> SyncResult:
    if settings is None:
        settings = get_settings()

    graph_path = Path(settings.graph_path)
    if graph_path.exists():
        data = json.loads(graph_path.read_text(encoding="utf-8"))
        G = nx.node_link_graph(data)
    else:
        G = nx.DiGraph()

    repo = CorpusRepository(session)
    result = SyncResult()

    artifacts = repo.list_artifacts(run_id=run_id)
    for art in artifacts:
        aid = str(art.artifact_id)
        if not G.has_node(aid):
            G.add_node(aid, type="artifact", title=str(art.title))
            result.nodes_added += 1

    all_cards = repo.list_decision_cards()
    for card in all_cards:
        did = str(card.decision_id)
        if not G.has_node(did):
            G.add_node(did, type="decision", capability=str(card.capability))
            result.nodes_added += 1

    mappings = repo.list_capability_mappings()
    caps: set[str] = set()
    for m in mappings:
        cap = str(m.capability)
        if cap not in caps:
            caps.add(cap)
            if not G.has_node(cap):
                G.add_node(cap, type="capability")
                result.nodes_added += 1

    for art in artifacts:
        aid = str(art.artifact_id)
        tags = _parse_tags(str(art.domain_tags)) + _parse_tags(str(art.capability_tags))
        for card in all_cards:
            if str(card.capability) in tags:
                if not G.has_edge(aid, str(card.decision_id)):
                    G.add_edge(aid, str(card.decision_id), label="supports")
                    result.edges_added += 1

    for m in mappings:
        did = str(m.decision_id)
        cap = str(m.capability)
        if not G.has_edge(did, cap):
            G.add_edge(did, cap, label="addresses")
            result.edges_added += 1

    graph_path.parent.mkdir(parents=True, exist_ok=True)
    data = nx.node_link_data(G)
    graph_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    return result


def rebuild_graph(session: Session, settings: CorpusSettings | None = None) -> SyncResult:
    if settings is None:
        settings = get_settings()

    G = nx.DiGraph()
    repo = CorpusRepository(session)
    result = SyncResult()

    for art in repo.list_artifacts():
        aid = str(art.artifact_id)
        G.add_node(aid, type="artifact", title=str(art.title))
        result.nodes_added += 1

    for card in repo.list_decision_cards():
        did = str(card.decision_id)
        G.add_node(did, type="decision", capability=str(card.capability))
        result.nodes_added += 1

    mappings = repo.list_capability_mappings()
    caps: set[str] = set()
    for m in mappings:
        cap = str(m.capability)
        if cap not in caps:
            caps.add(cap)
            G.add_node(cap, type="capability")
            result.nodes_added += 1

    all_cards = repo.list_decision_cards()
    for art in repo.list_artifacts():
        aid = str(art.artifact_id)
        tags = _parse_tags(str(art.domain_tags)) + _parse_tags(str(art.capability_tags))
        for card in all_cards:
            if str(card.capability) in tags:
                G.add_edge(aid, str(card.decision_id), label="supports")
                result.edges_added += 1

    for m in mappings:
        G.add_edge(str(m.decision_id), str(m.capability), label="addresses")
        result.edges_added += 1

    graph_path = Path(settings.graph_path)
    graph_path.parent.mkdir(parents=True, exist_ok=True)
    data = nx.node_link_data(G)
    graph_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    return result
