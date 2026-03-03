"""Multi-format file parser for corpus ingestion.

Supports Markdown, HTML, PDF, and plain-text formats with automatic
format detection based on file extension.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Extension → handler mapping
# ---------------------------------------------------------------------------
_MARKDOWN_EXTS = {".md", ".markdown"}
_HTML_EXTS = {".html", ".htm"}
_PDF_EXTS = {".pdf"}
_TEXT_EXTS = {".txt", ".text", ".log", ".csv"}


@dataclass
class ParsedDocument:
    """Result of parsing a single file."""

    title: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    source_format: str = "unknown"


# ---------------------------------------------------------------------------
# Private format handlers
# ---------------------------------------------------------------------------

def _parse_markdown(path: Path) -> ParsedDocument:
    """Parse a Markdown file, extracting title from the first ``# heading``."""
    text = path.read_text(encoding="utf-8", errors="replace")
    title = path.stem
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            title = stripped[2:].strip()
            break
    return ParsedDocument(
        title=title,
        content=text,
        metadata={"source": str(path)},
        source_format="markdown",
    )


def _parse_html(path: Path) -> ParsedDocument:
    """Parse an HTML file using BeautifulSoup, stripping tags."""
    from bs4 import BeautifulSoup  # type: ignore[import-untyped]

    raw = path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw, "html.parser")

    # Extract title: <title> first, then <h1>
    title = path.stem
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        title = title_tag.string.strip()
    else:
        h1_tag = soup.find("h1")
        if h1_tag:
            title = h1_tag.get_text(strip=True)

    text = soup.get_text(separator="\n", strip=True)
    return ParsedDocument(
        title=title,
        content=text,
        metadata={"source": str(path)},
        source_format="html",
    )


def _parse_pdf(path: Path) -> ParsedDocument:
    """Parse a PDF file using PyMuPDF (fitz), extracting text from all pages."""
    import fitz  # type: ignore[import-untyped]  # pymupdf

    try:
        doc = fitz.open(str(path))
    except Exception as exc:
        raise ValueError(f"Failed to open PDF {path}: {exc}") from exc

    pages_text: list[str] = []
    for page in doc:
        pages_text.append(page.get_text())  # type: ignore[union-attr]

    content = "\n".join(pages_text)

    # Try metadata title, then first heading-like line
    title = path.stem
    pdf_title = doc.metadata.get("title", "") if doc.metadata else ""
    if pdf_title and pdf_title.strip():
        title = pdf_title.strip()
    else:
        # Fallback: first non-empty line that looks like a heading
        for line in content.splitlines():
            stripped = line.strip()
            if stripped and len(stripped) < 200:
                title = stripped
                break

    doc.close()
    return ParsedDocument(
        title=title,
        content=content,
        metadata={"source": str(path), "page_count": len(pages_text)},
        source_format="pdf",
    )


def _parse_text(path: Path) -> ParsedDocument:
    """Parse a plain-text file (txt, log, csv, etc.)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    return ParsedDocument(
        title=path.stem,
        content=text,
        metadata={"source": str(path)},
        source_format="text",
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def parse_file(path: Path) -> ParsedDocument:
    """Auto-detect format from extension and parse the file.

    Parameters
    ----------
    path:
        Filesystem path to the file to parse.

    Returns
    -------
    ParsedDocument
        Parsed content, title, metadata, and detected format.

    Raises
    ------
    FileNotFoundError
        If *path* does not exist.
    ValueError
        If the file is corrupted or unreadable in its detected format.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    suffix = path.suffix.lower()

    if suffix in _MARKDOWN_EXTS:
        logger.info("Parsing Markdown file: %s", path)
        return _parse_markdown(path)

    if suffix in _HTML_EXTS:
        logger.info("Parsing HTML file: %s", path)
        return _parse_html(path)

    if suffix in _PDF_EXTS:
        logger.info("Parsing PDF file: %s", path)
        return _parse_pdf(path)

    if suffix in _TEXT_EXTS:
        logger.info("Parsing text file: %s", path)
        return _parse_text(path)

    # Unknown extension — attempt plain text with a warning
    logger.warning(
        "Unknown extension '%s' for %s — attempting plain-text parse",
        suffix,
        path,
    )
    try:
        return _parse_text(path)
    except Exception:
        raise ValueError(f"Cannot read file with unknown extension: {path}")
