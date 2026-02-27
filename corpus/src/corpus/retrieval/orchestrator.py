from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.repository import CorpusRepository
from corpus.retrieval.formatter import format_response
from corpus.retrieval.reranker import ScoredChunk, rerank
from corpus.retrieval.symbolic_filter import extract_constraints


@dataclass
class RetrievalResponse:
    content: str = ""
    depth: str = "L1"
    confidence: float = 0.0
    provenance: list[str] = field(default_factory=list)
    escalation_reason: str | None = None


def query(
    session: Session,
    question: str,
    depth_override: str | None = None,
    settings: CorpusSettings | None = None,
) -> RetrievalResponse:
    if settings is None:
        settings = get_settings()

    repo = CorpusRepository(session)
    constraints = extract_constraints(question)

    clean_query = question
    for d in constraints.domains:
        clean_query = clean_query.replace(f"[domain:{d}]", "").strip()
    for c in constraints.capabilities:
        clean_query = clean_query.replace(f"[capability:{c}]", "").strip()

    scored_chunks: list[ScoredChunk] = []
    try:
        import chromadb

        client = chromadb.PersistentClient(path=settings.chroma_dir)
        collection = client.get_collection("corpus_chunks")
        results = collection.query(query_texts=[clean_query], n_results=20)

        if results and results["documents"] and results["documents"][0]:
            distances = results["distances"][0] if results.get("distances") else []
            for i, doc in enumerate(results["documents"][0]):
                cid = results["ids"][0][i] if results["ids"] else f"chunk-{i}"
                dist = distances[i] if i < len(distances) else 1.0
                semantic = max(0.0, 1.0 - dist)
                scored_chunks.append(ScoredChunk(chunk_id=cid, content=doc, semantic_score=semantic))
    except Exception:
        pass

    graph_path = Path(settings.graph_path)
    if graph_path.exists() and scored_chunks:
        try:
            import networkx as nx

            data = json.loads(graph_path.read_text(encoding="utf-8"))
            G = nx.node_link_graph(data)
            expanded_ids: set[str] = set()
            for sc in scored_chunks[:5]:
                if G.has_node(sc.chunk_id):
                    for neighbor in G.neighbors(sc.chunk_id):
                        expanded_ids.add(neighbor)
        except Exception:
            pass

    rerank(scored_chunks, clean_query)

    all_cards = repo.list_decision_cards()
    matched_cards = []

    if constraints.domains or constraints.capabilities:
        for card in all_cards:
            cap = str(card.capability)
            if cap in constraints.domains or cap in constraints.capabilities:
                matched_cards.append(card)
    else:
        for card in all_cards:
            cap = str(card.capability).lower()
            if cap in clean_query.lower() or clean_query.lower() in str(card.question).lower():
                matched_cards.append(card)

    if not matched_cards and all_cards:
        matched_cards = all_cards[:3]

    best_confidence = 0.0
    if matched_cards:
        best_confidence = max(float(c.confidence_score) for c in matched_cards)

    escalation_reason = None
    if depth_override:
        depth = depth_override
    else:
        depth = "L1"
        has_contradiction = any(c.has_unresolved_contradiction for c in matched_cards)
        if has_contradiction or best_confidence < 0.50:
            depth = "L3"
            escalation_reason = (
                "unresolved contradiction" if has_contradiction else f"low confidence ({best_confidence:.2f})"
            )
        elif best_confidence < 0.70:
            depth = "L2"
            escalation_reason = f"moderate confidence ({best_confidence:.2f})"

    formatted = format_response(matched_cards, depth)
    provenance = [str(c.provenance_refs) for c in matched_cards if c.provenance_refs]

    # When no decision cards exist, fall back to showing top vector-search results
    if not matched_cards and scored_chunks:
        parts = ["## Relevant Knowledge Chunks\n"]
        for sc in scored_chunks[:10]:
            score_pct = sc.final_score * 100 if sc.final_score else sc.semantic_score * 100
            parts.append(f"**[{score_pct:.0f}% match]** (chunk: {sc.chunk_id})\n{sc.content[:500]}\n---\n")
        formatted = "\n".join(parts)
        best_confidence = max(
            (sc.final_score or sc.semantic_score for sc in scored_chunks[:10]),
            default=0.0,
        )
        escalation_reason = None
        depth = depth_override or "L1"

    return RetrievalResponse(
        content=formatted,
        depth=depth,
        confidence=best_confidence,
        provenance=provenance,
        escalation_reason=escalation_reason,
    )
