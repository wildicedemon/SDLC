"""Link integrity validation for the consolidated corpus.

Scans all markdown files under ``docs/research/`` for relative
links and verifies that each target exists on disk.  Also confirms
that every artifact's ``source_path`` still resolves.

Key function: :func:`validate_integrity`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


@dataclass
class IntegrityReport:
    """Summary of link-integrity checks.

    Attributes:
        broken_links: List of ``"file:target"`` strings for broken relative links.
        stale_paths: Artifact source paths that no longer exist on disk.
        total_checked: Total number of links / paths inspected.
        passed: ``True`` only when no broken links or stale paths were found.
    """

    broken_links: list[str] = field(default_factory=list)
    stale_paths: list[str] = field(default_factory=list)
    total_checked: int = 0
    passed: bool = True


# Matches markdown links: [text](target)
_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def validate_integrity(session: Session, run_id: str, corpus_root: str) -> IntegrityReport:
    """Check that all relative links and artifact paths resolve.

    Two-phase check:

    1. **Link scan** — walk every ``.md`` file under
       ``<corpus_root>/docs/research/``, extract relative markdown
       links (skipping ``http(s)://`` and ``#`` anchors), and verify
       the target exists on disk.
    2. **Artifact path check** — for each artifact in the run, confirm
       its ``source_path`` resolves under *corpus_root*.

    Args:
        session: Active SQLAlchemy session.
        run_id: Consolidation run to verify artifacts for.
        corpus_root: Filesystem root of the corpus repository.

    Returns:
        An :class:`IntegrityReport` summarising any issues.
    """
    report = IntegrityReport()
    root = Path(corpus_root)

    # --- Phase 1: scan markdown links ---
    research_dir = root / "docs" / "research"
    if research_dir.exists():
        for md_file in research_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            for match in _LINK_RE.finditer(content):
                link_target = match.group(2)
                # Skip external and anchor-only links
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

    # --- Phase 2: artifact source-path existence ---
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
