from __future__ import annotations

import csv
import io
import re
from dataclasses import dataclass, field
from pathlib import Path

from .constants import DISCARD_CONTENT_PATTERNS, DISCARD_SECTION_PATTERNS

SECTION_SPLIT_RE = re.compile(r"^(#{1,3})\s+", re.MULTILINE)
BULLET_RE = re.compile(r"^\s*[-*]\s+(.+)", re.MULTILINE)
NUMBERED_RE = re.compile(r"^\s*\d+[\.\)]\s+(.+)", re.MULTILINE)
TABLE_ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$", re.MULTILINE)
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
METRIC_RE = re.compile(
    r"\d+[\.\d]*\s*[%x×]"
    r"|\d+\s*[-–]\s*\d+\s*%"
    r"|\d+[\.\d]*\s*(?:percent|reduction|improvement|increase|decrease|"
    r"compression|accuracy|precision|recall|coverage|latency|throughput)",
    re.IGNORECASE,
)
LOW_CONFIDENCE_RE = re.compile(r"confidence[:\s]*low", re.IGNORECASE)
MIN_CONTENT_LENGTH = 40
MIN_BULLET_COUNT_FOR_LOW_CONF = 3


@dataclass
class RawAtom:
    content: str
    source_path: str
    raw_section: str
    section_title: str = ""


def _should_discard_section(title: str, body: str) -> bool:
    for pat in DISCARD_SECTION_PATTERNS:
        if pat.search(title):
            return True
        if pat.search(body[:200]):
            return True
    return False


def _should_discard_content(line: str) -> bool:
    for pat in DISCARD_CONTENT_PATTERNS:
        if pat.search(line):
            return True
    return False


def _is_separator_row(row: str) -> bool:
    cells = [c.strip() for c in row.split("|") if c.strip()]
    return all(re.fullmatch(r":?-+:?", c) for c in cells)


def _split_sections(text: str) -> list[tuple[str, str]]:
    parts: list[tuple[str, str]] = []
    lines = text.split("\n")
    current_title = ""
    current_lines: list[str] = []

    for line in lines:
        m = re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            if current_lines:
                parts.append((current_title, "\n".join(current_lines)))
            current_title = line
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        parts.append((current_title, "\n".join(current_lines)))

    return parts


def _extract_chunks_from_section(title: str, body: str) -> list[str]:
    chunks: list[str] = []
    bullets = BULLET_RE.findall(body)
    numbered = NUMBERED_RE.findall(body)
    table_rows = TABLE_ROW_RE.findall(body)

    table_data: list[str] = []
    for row_text in table_rows:
        if _is_separator_row(row_text):
            continue
        cells = [c.strip() for c in row_text.split("|") if c.strip()]
        row_joined = " | ".join(cells)
        if row_joined and len(row_joined) >= MIN_CONTENT_LENGTH:
            table_data.append(row_joined)
    if table_data:
        chunks.append("\n".join(table_data))

    for b in bullets:
        cleaned = b.strip()
        if _should_discard_content(cleaned):
            continue
        if len(cleaned) >= MIN_CONTENT_LENGTH:
            chunks.append(cleaned)

    for n in numbered:
        cleaned = n.strip()
        if _should_discard_content(cleaned):
            continue
        if len(cleaned) >= MIN_CONTENT_LENGTH:
            chunks.append(cleaned)

    remaining = body
    for pat in (BULLET_RE, NUMBERED_RE, TABLE_ROW_RE):
        remaining = pat.sub("", remaining)
    remaining = remaining.strip()
    if remaining and len(remaining) >= MIN_CONTENT_LENGTH:
        has_bold = bool(BOLD_RE.search(remaining))
        has_metric = bool(METRIC_RE.search(remaining))
        if has_bold or has_metric or len(remaining) >= 80:
            chunks.append(remaining)

    return chunks


def _is_low_confidence_section(title: str, body: str) -> bool:
    if not LOW_CONFIDENCE_RE.search(title) and not LOW_CONFIDENCE_RE.search(body[:200]):
        return False
    bullet_count = len(BULLET_RE.findall(body))
    return bullet_count < MIN_BULLET_COUNT_FOR_LOW_CONF


def _strip_code_fences(text: str) -> str:
    text = re.sub(r"^```\w*\s*\n?", "", text)
    text = re.sub(r"\n?```\s*$", "", text)
    return text


def parse_markdown(text: str, source_path: str) -> list[RawAtom]:
    text = _strip_code_fences(text)
    sections = _split_sections(text)
    atoms: list[RawAtom] = []

    for title, body in sections:
        if _should_discard_section(title, body):
            continue
        if _is_low_confidence_section(title, body):
            continue

        chunks = _extract_chunks_from_section(title, body)
        for chunk in chunks:
            atoms.append(
                RawAtom(
                    content=chunk.strip(),
                    source_path=source_path,
                    raw_section=f"{title}\n{body}".strip(),
                    section_title=title.lstrip("#").strip(),
                )
            )

    return atoms


def parse_csv(text: str, source_path: str) -> list[RawAtom]:
    atoms: list[RawAtom] = []
    reader = csv.DictReader(io.StringIO(text))
    fieldnames = reader.fieldnames or []

    title_col = None
    abstract_col = None
    papers_col = None
    for f in fieldnames:
        fl = f.lower()
        if fl == "title":
            title_col = f
        elif fl == "abstract":
            abstract_col = f
        elif fl == "papers":
            papers_col = f

    if papers_col and not title_col:
        return _parse_nested_csv(text, source_path, papers_col)

    for row in reader:
        parts: list[str] = []
        if title_col and row.get(title_col, "").strip():
            parts.append(row[title_col].strip())
        if abstract_col and row.get(abstract_col, "").strip():
            parts.append(row[abstract_col].strip())

        if not parts:
            all_vals = " ".join(v.strip() for v in row.values() if v and v.strip())
            if len(all_vals) >= MIN_CONTENT_LENGTH:
                parts.append(all_vals)

        content = ". ".join(parts)
        if len(content) >= MIN_CONTENT_LENGTH:
            atoms.append(
                RawAtom(
                    content=content,
                    source_path=source_path,
                    raw_section=content,
                    section_title="",
                )
            )

    return atoms


def _parse_nested_csv(text: str, source_path: str, papers_col: str) -> list[RawAtom]:
    import ast

    atoms: list[RawAtom] = []
    reader = csv.DictReader(io.StringIO(text))
    for row in reader:
        raw = row.get(papers_col, "").strip()
        if not raw:
            continue
        try:
            papers = ast.literal_eval(raw)
        except (ValueError, SyntaxError):
            continue
        if not isinstance(papers, list):
            continue
        for paper in papers:
            if not isinstance(paper, dict):
                continue
            parts: list[str] = []
            if paper.get("title", "").strip():
                parts.append(paper["title"].strip())
            if paper.get("abstract", "").strip():
                parts.append(paper["abstract"].strip())
            content = ". ".join(parts)
            if len(content) >= MIN_CONTENT_LENGTH:
                atoms.append(
                    RawAtom(
                        content=content,
                        source_path=source_path,
                        raw_section=content,
                        section_title=paper.get("title", ""),
                    )
                )
    return atoms


def parse_file(path: Path) -> list[RawAtom]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    source = str(path)
    if path.suffix.lower() == ".csv":
        return parse_csv(text, source)
    return parse_markdown(text, source)
