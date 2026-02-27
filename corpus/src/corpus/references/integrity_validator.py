from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


@dataclass
class IntegrityReport:
    broken_links: list[str] = field(default_factory=list)
    stale_paths: list[str] = field(default_factory=list)
    total_checked: int = 0
    passed: bool = True


_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def validate_integrity(session: Session, run_id: str, corpus_root: str) -> IntegrityReport:
    report = IntegrityReport()
    root = Path(corpus_root)

    research_dir = root / "docs" / "research"
    if research_dir.exists():
        for md_file in research_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            for match in _LINK_RE.finditer(content):
                link_target = match.group(2)
                if link_target.startswith("http://") or link_target.startswith("https://"):
                    continue
                if link_target.startswith("#"):
                    continue

                report.total_checked += 1
                resolved = (md_file.parent / link_target).resolve()
                if not resolved.exists():
                    location = f"{md_file}:{link_target}"
                    report.broken_links.append(location)
                    report.passed = False

    repo = CorpusRepository(session)
    artifacts = repo.list_artifacts(run_id=run_id)
    for art in artifacts:
        source_path = str(art.source_path)
        report.total_checked += 1
        full_path = root / source_path
        if not full_path.exists():
            report.stale_paths.append(source_path)
            report.passed = False

    return report
