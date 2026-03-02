from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from corpus.db.models import ReferenceRewriteMap


@dataclass
class RewriteEntry:
    old_path: str
    new_path: str
    rewritten: bool = False


def generate_rewrite_map(session: Session, run_id: str) -> list[RewriteEntry]:
    rows = session.query(ReferenceRewriteMap).filter(ReferenceRewriteMap.run_id == run_id).all()
    return [
        RewriteEntry(
            old_path=str(row.old_path),
            new_path=str(row.new_path),
            rewritten=bool(row.rewritten),
        )
        for row in rows
    ]
