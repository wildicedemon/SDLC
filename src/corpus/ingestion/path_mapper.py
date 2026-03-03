"""Path rewrite mapper for ingestion.

Records the mapping from an artifact's original source path to its
new canonical location so that downstream reference-rewriting can
update links in other documents.

Key function: :func:`record_mapping`.
"""

from __future__ import annotations

from corpus.db.repository import CorpusRepository


def record_mapping(
    repo: CorpusRepository,
    old_path: str,
    new_path: str,
    run_id: str,
) -> None:
    """Persist a source→canonical path mapping for a consolidation run.

    The entry is initially marked as *not yet rewritten*; the
    reference-rewriting phase later flips the flag once all links
    that reference ``old_path`` have been updated.

    Args:
        repo: The corpus data-access repository.
        old_path: Original path of the artifact in the source branch.
        new_path: Canonical destination path after normalisation.
        run_id: The consolidation run this mapping belongs to.
    """
    repo.create_rewrite_map_entry(
        run_id=run_id,
        old_path=old_path,
        new_path=new_path,
        rewritten=False,
    )
