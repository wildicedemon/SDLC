from __future__ import annotations

from corpus.db.repository import CorpusRepository


def record_mapping(
    repo: CorpusRepository,
    old_path: str,
    new_path: str,
    run_id: str,
) -> None:
    repo.create_rewrite_map_entry(
        run_id=run_id,
        old_path=old_path,
        new_path=new_path,
        rewritten=False,
    )
