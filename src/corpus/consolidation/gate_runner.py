"""Quality gate checking for consolidation runs.

Executes a battery of post-pipeline checks (gates) to verify that
the corpus is in a consistent state before a run is marked complete.

Gates:
* **capability_populated** — every capability tag has a decision-card mapping.
* **human_review_resolved** — no unresolved human-review items remain.
* **all_classified** — every artifact has at least one domain tag.
* **reference_integrity** — all markdown links resolve on disk.
* **sync_health** — vector store and graph are sufficiently synced.

Key function: :func:`run_gates`.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.db.repository import CorpusRepository
from corpus.references.integrity_validator import validate_integrity
from corpus.sync.health_checker import check_sync_health


@dataclass
class GateFailure:
    """A single quality-gate failure.

    Attributes:
        gate: Name of the gate that failed.
        detail: Human-readable explanation.
    """

    gate: str
    detail: str


@dataclass
class GateResult:
    """Aggregate result of all quality gates.

    Attributes:
        passed: ``True`` only when every gate passed.
        failures: List of individual gate failures.
    """

    passed: bool = True
    failures: list[GateFailure] = field(default_factory=list)


def run_gates(
    session: Session,
    run_id: str,
    corpus_root: str = ".",
    settings: CorpusSettings | None = None,
) -> GateResult:
    """Execute all quality gates for a consolidation run.

    Each gate appends to ``result.failures`` and sets
    ``result.passed = False`` when it detects an issue.

    Args:
        session: Active SQLAlchemy session.
        run_id: ID of the consolidation run to verify.
        corpus_root: Filesystem root for integrity checks.
        settings: Pipeline configuration; loaded from env if ``None``.

    Returns:
        A :class:`GateResult` summarising pass/fail status.
    """
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
    """Check that every artifact capability has a decision-card mapping."""
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
    """Verify all human-review items are resolved."""
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
    """Ensure every artifact has at least one domain tag."""
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
            break  # One failure is enough to flag the gate


def _gate_reference_integrity(session: Session, run_id: str, corpus_root: str, result: GateResult) -> None:
    """Run the link-integrity validator and propagate any failures."""
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
    """Verify vector-store and graph-sync health metrics."""
    health = check_sync_health(session, settings=settings)
    if not health.healthy:
        result.passed = False
        result.failures.append(
            GateFailure(
                gate="sync_health",
                detail=f"Vector synced: {health.vector_synced_pct:.0%}, graph nodes: {health.graph_node_count}",
            )
        )
