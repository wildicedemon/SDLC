from __future__ import annotations

from .constants import (
    DOMAIN_KEYWORDS,
    PHASE_KEYWORDS,
    PRODUCT_KEYWORDS,
    Domain,
    ProductCategory,
    SDLCPhase,
)
from .models import KnowledgeAtom

_MATCH_THRESHOLD = 2

_FALLBACK_DOMAIN = Domain.D1.value
_FALLBACK_PHASE = SDLCPhase.P3.value
_FALLBACK_PRODUCT = ProductCategory.PC10.value


def _match_keywords(
    text: str,
    vocabularies: dict[str, list[str]],
    threshold: int = _MATCH_THRESHOLD,
) -> list[str]:
    text_lower = text.lower()
    matched: list[str] = []
    scores: list[tuple[str, int]] = []
    for key, keywords in vocabularies.items():
        hits = sum(1 for kw in keywords if kw.lower() in text_lower)
        if hits >= threshold:
            matched.append(key)
        if hits > 0:
            scores.append((key, hits))
    if not matched and scores:
        scores.sort(key=lambda s: s[1], reverse=True)
        matched.append(scores[0][0])
    return matched


def _tag_domains(atom: KnowledgeAtom) -> list[str]:
    matches = _match_keywords(atom.content, DOMAIN_KEYWORDS)
    if not matches:
        matches = _match_keywords(atom.raw_section, DOMAIN_KEYWORDS)
    return matches if matches else [_FALLBACK_DOMAIN]


def _tag_phases(atom: KnowledgeAtom) -> list[str]:
    matches = _match_keywords(atom.content, PHASE_KEYWORDS)
    if not matches:
        matches = _match_keywords(atom.raw_section, PHASE_KEYWORDS)
    return matches if matches else [_FALLBACK_PHASE]


def _tag_products(atom: KnowledgeAtom) -> list[str]:
    matches = _match_keywords(atom.content, PRODUCT_KEYWORDS)
    if not matches:
        matches = _match_keywords(atom.raw_section, PRODUCT_KEYWORDS)
    return matches if matches else [_FALLBACK_PRODUCT]


def tag(atoms: list[KnowledgeAtom]) -> list[KnowledgeAtom]:
    for atom in atoms:
        atom.domains = _tag_domains(atom)
        atom.sdlc_phases = _tag_phases(atom)
        atom.products = _tag_products(atom)
    return atoms
