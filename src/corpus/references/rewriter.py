"""Markdown link rewriting based on path rewrite maps.

Scans all ``.md`` files under well-known corpus directories and
replaces markdown link targets that match old paths with their
new canonical locations.

Key function: :func:`rewrite_references`.
"""

from __future__ import annotations

import re
from pathlib import Path

from corpus.references.rewrite_mapper import RewriteEntry


def rewrite_references(rewrite_map: list[RewriteEntry], corpus_root: str) -> int:
    """Apply path rewrites to markdown links across the corpus.

    For each entry in the *rewrite_map*, builds a regex that matches
    ``[text](old_path)`` and substitutes ``[text](new_path)``.

    Only files under ``docs/research``, ``docs/research/03_indices``,
    and ``docs/research/00_meta/run_reports`` are scanned.

    Args:
        rewrite_map: Entries describing old→new path mappings.
        corpus_root: Filesystem root of the corpus repository.

    Returns:
        The total number of link substitutions performed.
    """
    if not rewrite_map:
        return 0

    root = Path(corpus_root)
    count = 0

    # Collect markdown files from known corpus directories
    md_files: list[Path] = []
    for search_dir in ["docs/research", "docs/research/03_indices", "docs/research/00_meta/run_reports"]:
        d = root / search_dir
        if d.exists():
            md_files.extend(d.rglob("*.md"))

    # Deduplicate by resolved path (handles symlinks / overlapping globs)
    seen: set[Path] = set()
    unique_files: list[Path] = []
    for f in md_files:
        resolved = f.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique_files.append(f)

    for entry in rewrite_map:
        old_escaped = re.escape(entry.old_path)
        # Match markdown links whose target is the old path
        pattern = re.compile(r"\[([^\]]*)\]\(" + old_escaped + r"\)")

        for md_file in unique_files:
            content = md_file.read_text(encoding="utf-8")
            escaped_new = entry.new_path.replace("\\", "/")
            new_content, n = pattern.subn(rf"[\1]({escaped_new})", content)
            if n > 0:
                md_file.write_text(new_content, encoding="utf-8")
                count += n

    return count
