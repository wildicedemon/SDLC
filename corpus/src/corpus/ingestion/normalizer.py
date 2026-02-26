from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

_HEADING_PATTERN = re.compile(r"(?=^## )", re.MULTILINE)


@dataclass
class NormalizedResult:
    chunks: list[str] = field(default_factory=list)
    title: str = ""
    merged: bool = False


def _extract_title(content: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return ""


def _split_chunks(content: str) -> list[str]:
    parts = _HEADING_PATTERN.split(content)
    return [p for p in parts if p.strip()]


def normalize(
    content: str,
    domain: str,
    canonical_path: str,
) -> NormalizedResult:
    title = _extract_title(content)
    chunks = _split_chunks(content)

    target = Path(canonical_path)
    merged = False

    if target.exists():
        existing = target.read_text(encoding="utf-8")
        combined = existing.rstrip("\n") + "\n\n" + content.lstrip("\n")
        target.write_text(combined, encoding="utf-8")
        chunks = _split_chunks(combined)
        title = _extract_title(combined) or title
        merged = True
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    return NormalizedResult(chunks=chunks, title=title, merged=merged)
