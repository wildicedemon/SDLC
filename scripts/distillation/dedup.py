from __future__ import annotations

import hashlib
import re
from collections import defaultdict

from .models import KnowledgeAtom


_CITATION_STRIP_RE = re.compile(r"\[(?:paper:)?\d+(?:,\s*\d+)*\]")
_WHITESPACE_RE = re.compile(r"\s+")


def _normalize(text: str) -> str:
    t = text.lower()
    t = _CITATION_STRIP_RE.sub("", t)
    t = _WHITESPACE_RE.sub(" ", t).strip()
    return t


def _content_hash(text: str) -> str:
    return hashlib.sha256(_normalize(text).encode("utf-8")).hexdigest()


_EVIDENCE_RANK = {"STRONG": 0, "MODERATE": 1, "WEAK": 2}


def _pick_best(group: list[KnowledgeAtom]) -> KnowledgeAtom:
    group.sort(
        key=lambda a: (
            _EVIDENCE_RANK.get(a.evidence_strength.value, 3),
            -len(a.content),
        )
    )
    best = group[0]

    merged_sources: list[str] = []
    seen: set[str] = set()
    for atom in group:
        for src in atom.sources:
            if src not in seen:
                seen.add(src)
                merged_sources.append(src)
    best.sources = merged_sources

    if len(group) > 1:
        for other in group[1:]:
            if len(other.raw_section) > len(best.raw_section):
                best.raw_section = other.raw_section

    best.content_hash = _content_hash(best.content)
    return best


def deduplicate(atoms: list[KnowledgeAtom]) -> list[KnowledgeAtom]:
    groups: dict[str, list[KnowledgeAtom]] = defaultdict(list)
    for atom in atoms:
        h = _content_hash(atom.content)
        atom.content_hash = h
        groups[h].append(atom)

    result: list[KnowledgeAtom] = []
    for group in groups.values():
        result.append(_pick_best(group))
    return result
