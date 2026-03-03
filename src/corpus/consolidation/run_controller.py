"""Run lifecycle management for consolidation runs.

Orchestrates the final stage of a pipeline run: executes quality
gates, marks the run as ``completed`` on success, or ``failed``
with a remediation report on failure.

Key function: :func:`complete_run`.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from corpus.config import CorpusSettings, get_settings
from corpus.consolidation.gate_runner import run_gates
from corpus.db.repository import CorpusRepository


def complete_run(
    session: Session,
    run_id: str,
    corpus_root: str = ".",
    settings: CorpusSettings | None = None,
) -> bool:
    """Finalize a consolidation run by executing quality gates.

    If all gates pass the run is marked ``completed`` and its
    ``completed_at`` timestamp is set.  Otherwise the run is marked
    ``failed`` and a human-readable ``remediation_report`` is stored.

    Args:
        session: Active SQLAlchemy session.
        run_id: ID of the run to finalise.
        corpus_root: Filesystem root of the corpus (for integrity checks).
        settings: Pipeline configuration; loaded from env if ``None``.

    Returns:
        ``True`` if all gates passed, ``False`` otherwise.
    """
    if settings is None:
        settings = get_settings()

    repo = CorpusRepository(session)
    gate_result = run_gates(session, run_id, corpus_root=corpus_root, settings=settings)

    if gate_result.passed:
        run = repo.get_run(run_id)
        if run is not None:
            run.status = "completed"  # type: ignore[assignment]
            run.completed_at = datetime.now(timezone.utc).isoformat()  # type: ignore[assignment]
            session.flush()
        return True

    # Build a semicolon-delimited failure summary for the report
    details = "; ".join(f"[{f.gate}] {f.detail}" for f in gate_result.failures)
    run = repo.get_run(run_id)
    if run is not None:
        run.status = "failed"  # type: ignore[assignment]
        run.remediation_report = details  # type: ignore[assignment]
        session.flush()
    return False
