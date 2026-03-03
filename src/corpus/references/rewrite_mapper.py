"""Path rewrite map generation from database records.

Loads :class:`~corpus.db.models.ReferenceRewriteMap` rows for a given
consolidation run and returns them as lightweight
:class:`RewriteEntry` dataclasses for use by the rewriter.

Key function: :func:`generate_rewrite_map`.
"""

from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from corpus.db.models import ReferenceRewriteMap


@dataclass
class RewriteEntry:
    """A single old-path → new-path mapping.

    Attributes:
        old_path: The original file path before consolidation.
        new_path: The canonical path after consolidation.
        rewritten: Whether all references have been updated.
    """

    old_path: str
    new_path: str
    rewritten: bool = False


def generate_rewrite_map(session: Session, run_id: str) -> list[RewriteEntry]:
    """Load the rewrite map for a consolidation run.

    Args:
        session: Active SQLAlchemy session.
        run_id: Consolidation run to load entries for.

    Returns:
        A list of :class:`RewriteEntry` instances.
    """
    rows = session.query(ReferenceRewriteMap).filter(ReferenceRewriteMap.run_id == run_id).all()
    return [
        RewriteEntry(
            old_path=str(row.old_path),
            new_path=str(row.new_path),
            rewritten=bool(row.rewritten),
        )
        for row in rows
    ]
