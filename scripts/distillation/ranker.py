from __future__ import annotations

import re
from collections import defaultdict

from .constants import AtomType, EvidenceStrength
from .models import KnowledgeAtom

_EVIDENCE_ORDER = {
    EvidenceStrength.STRONG: 0,
    EvidenceStrength.MODERATE: 1,
    EvidenceStrength.WEAK: 2,
}

_AGENT_KEYWORDS = re.compile(
    r"\b(?:agent|multi-agent|autonomous|orchestrat|delegat|mode switch|handoff|"
    r"context window|prompt inject|hallucin|token budget|MCP|tool call|"
    r"self-heal|auto-learn|confidence-based|model rout)\b",
    re.IGNORECASE,
)

_SPECIFIC_INDICATORS = re.compile(
    r"\d+[\.\d]*\s*[%x×]"
    r"|step\s*\d"
    r"|1\.\s"
    r"|\b(?:parse|build|construct|generate|verify|extract)\b",
    re.IGNORECASE,
)


def _specificity_score(atom: KnowledgeAtom) -> int:
    return len(_SPECIFIC_INDICATORS.findall(atom.content))


def _agent_specificity_score(atom: KnowledgeAtom) -> int:
    return len(_AGENT_KEYWORDS.findall(atom.content))


def rank(atoms: list[KnowledgeAtom]) -> list[KnowledgeAtom]:
    by_type: dict[AtomType, list[KnowledgeAtom]] = defaultdict(list)
    for atom in atoms:
        by_type[atom.type].append(atom)

    for group in by_type.values():
        group.sort(
            key=lambda a: (
                _EVIDENCE_ORDER.get(a.evidence_strength, 3),
                -_specificity_score(a),
                -_agent_specificity_score(a),
            )
        )

    result: list[KnowledgeAtom] = []
    counter = 1
    for atom_type in AtomType:
        for atom in by_type.get(atom_type, []):
            atom.id = f"KA-{counter:03d}"
            result.append(atom)
            counter += 1

    return result
