"""Content normalizer and chunker for research artifacts.

Splits markdown content at ``## `` (H2) heading boundaries, extracts
the document title from the first ``# `` heading, and writes the
result to a canonical path on disk.  If the target file already
exists the new content is **appended** (merged) rather than
overwriting, and the combined text is re-chunked.

Key function: :func:`normalize`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

# Splits before every line that starts with "## " (H2 heading)
_HEADING_PATTERN = re.compile(r"(?=^## )", re.MULTILINE)


@dataclass
class NormalizedResult:
    """Output of the :func:`normalize` function.

    Attributes:
        chunks: Ordered list of text chunks split on H2 headings.
        title: The document title extracted from the first ``#`` heading.
        merged: ``True`` if the content was appended to an existing file.
    """

    chunks: list[str] = field(default_factory=list)
    title: str = ""
    merged: bool = False


def _extract_title(content: str) -> str:
    """Return the text of the first H1 (``# ``) heading, or empty string."""
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return ""


def _split_chunks(content: str) -> list[str]:
    """Split *content* into chunks at every H2 heading boundary."""
    parts = _HEADING_PATTERN.split(content)
    return [p for p in parts if p.strip()]


def normalize(
    content: str,
    domain: str,
    canonical_path: str,
) -> NormalizedResult:
    """Normalize and persist research content to a canonical location.

    If *canonical_path* already exists the incoming *content* is
    appended to the existing text and the combined document is
    re-split into chunks.

    Args:
        content: Raw markdown text to normalize.
        domain: Domain tag (currently unused but reserved for
            future domain-specific normalisation).
        canonical_path: Filesystem path where the normalised output is
            written.

    Returns:
        A :class:`NormalizedResult` with the extracted title, chunks,
        and a flag indicating whether a merge occurred.
    """
    title = _extract_title(content)
    chunks = _split_chunks(content)

    target = Path(canonical_path)
    merged = False

    if target.exists():
        # Append new content below existing text, then re-chunk
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
