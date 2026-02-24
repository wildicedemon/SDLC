from __future__ import annotations

import re

from .constants import (
    ANTI_PATTERN_KEYWORDS,
    COMBINATION_KEYWORDS,
    CONSTRAINT_KEYWORDS,
    FAILURE_MODE_KEYWORDS,
    KNOWN_TOOLS,
    METRIC_PATTERN,
    TECHNIQUE_VERBS,
    TRADEOFF_KEYWORDS,
    AtomType,
    EvidenceStrength,
)
from .models import KnowledgeAtom
from .parser import RawAtom

CITATION_RE = re.compile(r"\[(?:paper:)?\d+\]|\[\d+(?:,\s*\d+)*\]")
NUMBERED_STEP_RE = re.compile(r"^\s*\d+[\.\)]\s+", re.MULTILINE)
TOOL_CAPABILITY_RE = re.compile(
    r"\b(?:support|provid|enabl|achiev|deliver|offer|implement|built|designed for"
    r"|capable of|integrat|optimiz|automat)\b",
    re.IGNORECASE,
)
NUMERIC_RE = re.compile(
    r"\d+[\.\d]*\s*[%x×+]"
    r"|\d+\s*[-–]\s*\d+\s*%"
    r"|\d+[\.\d]*\s*(?:percent|reduction|improvement|increase|decrease|"
    r"compression|accuracy|precision|recall|coverage|latency|throughput)",
    re.IGNORECASE,
)
FAILURE_RESPONSE_RE = re.compile(
    r"\b(?:prevent|mitigat|respond|recover|fix|resolv|handl|guard|check|verif|reject|sanitiz|block)\b",
    re.IGNORECASE,
)
MULTI_NAME_RE = re.compile(
    r"\b(?:AST|CFG|DFG|CPG|SSA|index|graph|model|representation|approach|method|algorithm|strategy|pattern)\b",
    re.IGNORECASE,
)


def _count_matches(pattern: re.Pattern[str], text: str) -> int:
    return len(pattern.findall(text))


def _has_tool_mention(text: str) -> str | None:
    for tool in KNOWN_TOOLS:
        if tool.lower() in text.lower():
            return tool
    return None


def _is_recipe(text: str) -> bool:
    steps = NUMBERED_STEP_RE.findall(text)
    if len(steps) >= 3:
        verb_hits = _count_matches(TECHNIQUE_VERBS, text)
        return verb_hits >= 2
    return False


def _detect_type(text: str) -> AtomType | None:
    scores: dict[AtomType, int] = {}

    if _is_recipe(text):
        scores[AtomType.RECIPE] = 100

    if _count_matches(METRIC_PATTERN, text) >= 1:
        scores[AtomType.METRIC] = 60

    tool = _has_tool_mention(text)
    if tool and _count_matches(TOOL_CAPABILITY_RE, text) >= 1:
        scores[AtomType.TOOL] = 55

    if _count_matches(TECHNIQUE_VERBS, text) >= 2:
        scores[AtomType.TECHNIQUE] = 50

    if _count_matches(COMBINATION_KEYWORDS, text) >= 1:
        has_entity = bool(_has_tool_mention(text))
        has_verb = _count_matches(TECHNIQUE_VERBS, text) >= 1
        plus_count = text.count("+")
        multi_names = _count_matches(MULTI_NAME_RE, text)
        if has_entity or has_verb or plus_count >= 1 or multi_names >= 2:
            scores[AtomType.COMBINATION] = 45

    if _count_matches(CONSTRAINT_KEYWORDS, text) >= 1:
        scores[AtomType.CONSTRAINT] = 40

    if _count_matches(FAILURE_MODE_KEYWORDS, text) >= 1:
        has_response = bool(FAILURE_RESPONSE_RE.search(text))
        if has_response:
            scores[AtomType.FAILURE_MODE] = 52

    anti_count = _count_matches(ANTI_PATTERN_KEYWORDS, text)
    if anti_count >= 1:
        scores[AtomType.ANTI_PATTERN] = 53 if anti_count >= 2 else 44

    if _count_matches(TRADEOFF_KEYWORDS, text) >= 1:
        scores[AtomType.TRADEOFF] = 35

    if not scores:
        if tool and len(text) >= 60:
            scores[AtomType.TOOL] = 30
        elif _count_matches(TECHNIQUE_VERBS, text) >= 1 and len(text) >= 80:
            scores[AtomType.TECHNIQUE] = 25

    if not scores:
        return None

    if AtomType.RECIPE in scores:
        return AtomType.RECIPE
    if AtomType.METRIC in scores:
        return AtomType.METRIC
    if AtomType.TECHNIQUE in scores and AtomType.COMBINATION in scores:
        return AtomType.TECHNIQUE

    return max(scores, key=lambda t: scores[t])


def _assess_evidence(text: str) -> EvidenceStrength:
    has_citation = bool(CITATION_RE.search(text))
    has_number = bool(NUMERIC_RE.search(text))
    has_named_source = bool(
        re.search(
            r"\b(?:according to|study|paper|research|benchmark|experiment|survey|measured|reported|demonstrated)\b",
            text,
            re.IGNORECASE,
        )
    )

    if has_citation and has_number:
        return EvidenceStrength.STRONG
    if has_number or has_named_source:
        return EvidenceStrength.MODERATE
    return EvidenceStrength.WEAK


def classify(atom: RawAtom) -> KnowledgeAtom | None:
    text = atom.content
    atom_type = _detect_type(text)
    if atom_type is None:
        return None

    evidence = _assess_evidence(text)

    return KnowledgeAtom(
        id="",
        type=atom_type,
        content=text,
        evidence_strength=evidence,
        sources=[atom.source_path],
        raw_section=atom.raw_section,
    )
