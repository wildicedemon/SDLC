from __future__ import annotations

from dataclasses import dataclass, field

from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.repository import CorpusRepository
from corpus.references.integrity_validator import validate_integrity
from corpus.sync.health_checker import check_sync_health


@dataclass
class GateFailure:
    gate: str
    detail: str


@dataclass
class GateResult:
    passed: bool = True
    failures: list[GateFailure] = field(default_factory=list)


def run_gates(
    session: Session,
    run_id: str,
    corpus_root: str = ".",
    settings: CorpusSettings | None = None,
) -> GateResult:
    if settings is None:
        settings = get_settings()

    result = GateResult()
    repo = CorpusRepository(session)

    run = repo.get_run(run_id)
    if run is None:
        result.passed = False
        result.failures.append(GateFailure(gate="run_exists", detail=f"Run {run_id} not found"))
        return result

    _gate_capabilities(repo, run_id, result)
    _gate_human_review(repo, run_id, result)
    _gate_classification(repo, run_id, result)
    _gate_reference_integrity(session, run_id, corpus_root, result)
    _gate_sync_health(session, settings, result)

    return result


def _gate_capabilities(repo: CorpusRepository, run_id: str, result: GateResult) -> None:
    artifacts = repo.list_artifacts(run_id=run_id)
    if not artifacts:
        return

    # If no decision cards exist yet (initial run), skip this gate
    all_cards = repo.list_decision_cards()
    if not all_cards:
        return

    import json

    capabilities: set[str] = set()
    for art in artifacts:
        tags = json.loads(str(art.capability_tags)) if art.capability_tags else []
        capabilities.update(tags)

    for cap in capabilities:
        mappings = repo.list_capability_mappings(capability=cap)
        if not mappings:
            result.passed = False
            result.failures.append(
                GateFailure(
                    gate="capability_populated",
                    detail=f"Capability '{cap}' has no decision card mapping after update",
                )
            )


def _gate_human_review(repo: CorpusRepository, run_id: str, result: GateResult) -> None:
    unresolved = repo.list_unresolved_reviews(run_id)
    if unresolved:
        result.passed = False
        result.failures.append(
            GateFailure(
                gate="human_review_resolved",
                detail=f"{len(unresolved)} unresolved human review item(s)",
            )
        )


def _gate_classification(repo: CorpusRepository, run_id: str, result: GateResult) -> None:
    import json

    artifacts = repo.list_artifacts(run_id=run_id)
    for art in artifacts:
        tags = json.loads(str(art.domain_tags)) if art.domain_tags else []
        if not tags:
            result.passed = False
            result.failures.append(
                GateFailure(
                    gate="all_classified",
                    detail=f"Artifact {art.artifact_id} has no domain tags",
                )
            )
            break


def _gate_reference_integrity(session: Session, run_id: str, corpus_root: str, result: GateResult) -> None:
    report = validate_integrity(session, run_id, corpus_root)
    if not report.passed:
        result.passed = False
        broken = len(report.broken_links)
        stale = len(report.stale_paths)
        result.failures.append(
            GateFailure(
                gate="reference_integrity",
                detail=f"{broken} broken link(s), {stale} stale path(s)",
            )
        )


def _gate_sync_health(session: Session, settings: CorpusSettings, result: GateResult) -> None:
    health = check_sync_health(session, settings=settings)
    if not health.healthy:
        result.passed = False
        result.failures.append(
            GateFailure(
                gate="sync_health",
                detail=f"Vector synced: {health.vector_synced_pct:.0%}, graph nodes: {health.graph_node_count}",
            )
        )
