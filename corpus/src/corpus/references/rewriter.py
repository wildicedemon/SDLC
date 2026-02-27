from __future__ import annotations

import re
from pathlib import Path

from corpus.references.rewrite_mapper import RewriteEntry


def rewrite_references(rewrite_map: list[RewriteEntry], corpus_root: str) -> int:
    if not rewrite_map:
        return 0

    root = Path(corpus_root)
    count = 0

    md_files: list[Path] = []
    for search_dir in ["docs/research", "docs/research/03_indices", "docs/research/00_meta/run_reports"]:
        d = root / search_dir
        if d.exists():
            md_files.extend(d.rglob("*.md"))

    seen: set[Path] = set()
    unique_files: list[Path] = []
    for f in md_files:
        resolved = f.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique_files.append(f)

    for entry in rewrite_map:
        old_escaped = re.escape(entry.old_path)
        pattern = re.compile(r"\[([^\]]*)\]\(" + old_escaped + r"\)")

        for md_file in unique_files:
            content = md_file.read_text(encoding="utf-8")
            escaped_new = entry.new_path.replace("\\", "/")
            new_content, n = pattern.subn(rf"[\1]({escaped_new})", content)
            if n > 0:
                md_file.write_text(new_content, encoding="utf-8")
                count += n

    return count
