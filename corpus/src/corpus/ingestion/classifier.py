from __future__ import annotations

import re
from dataclasses import dataclass, field

DOMAIN_DIRECTORIES: dict[str, list[str]] = {
    "01_meta_architecture": [
        "economic_optimization_modeling",
        "governance_compliance",
        "security_architecture",
        "system_design_philosophy",
    ],
    "02_agent_orchestration": [
        "agent_system_design",
        "distributed_orchestration",
        "task_architecture",
    ],
    "03_context_memory_intelligence": [
        "context_management",
        "knowledge_representation",
        "memory_systems",
        "reasoning_architecture",
    ],
    "04_code_intelligence": [
        "code_exploration",
        "refactoring_optimization",
        "specification_design",
    ],
    "05_sdlc_automation": [
        "cicd_devops",
        "observability_feedback_loops",
        "testing_architecture",
    ],
    "06_data_infrastructure": [
        "database_data_engineering",
        "infrastructure_engineering",
    ],
    "07_human_interaction": [
        "human_in_the_loop_systems",
    ],
    "08_model_management": [
        "model_capability_management",
    ],
    "09_research_discipline": [
        "research_benchmarking_framework",
    ],
    "10_scaling_enterprise": [
        "ecosystem_intelligence",
        "large_codebase_handling",
    ],
    "11_advanced_runtime": [
        "autonomous_runtime_systems",
    ],
    "12_self_improvement": [
        "system_self_improvement",
    ],
}

# ---------------------------------------------------------------------------
# Research prefixes — both primary and Kimi-Research mirror
# ---------------------------------------------------------------------------
_RESEARCH_PREFIXES = (
    "docs/research/",
    "Kimi-Research/docs/research/",
)

# Special directories inside a research root
_SPECIAL_RESEARCH_DIRS: dict[str, str] = {
    "_distilled": "distilled",
    "_extractions": "extractions",
    "_indices": "indices",
    "_progress": "progress",
    "00_meta": "meta",
    "03_indices": "indices",
}

# Top-level knowledge directories outside docs/research/
_KNOWLEDGE_PREFIXES: dict[str, str] = {
    "distilled/": "distilled",
    "distillation/": "distillation",
    "docs/distilled/": "distilled",
    "docs/distillation/": "distillation",
    "Kimi-Research/research/": "kimi_research",
}

_META_DIR = "00_meta"
_INDICES_DIR = "03_indices"


def _make_research_patterns(prefix: str) -> tuple[re.Pattern[str], re.Pattern[str], re.Pattern[str], re.Pattern[str]]:
    escaped = re.escape(prefix)
    domain = re.compile(rf"^{escaped}(\d{{2}}_[^/]+)/([^/]+)/(.+)$")
    meta = re.compile(rf"^{escaped}00_meta/(.+)$")
    indices = re.compile(rf"^{escaped}03_indices/(.+)$")
    special = re.compile(rf"^{escaped}(_[^/]+)/(.+)$")
    return domain, meta, indices, special


_RESEARCH_PATTERNS = [
    (prefix, *_make_research_patterns(prefix)) for prefix in _RESEARCH_PREFIXES
]


@dataclass
class Classification:
    domain_tags: list[str] = field(default_factory=list)
    capability_tags: list[str] = field(default_factory=list)
    is_classified: bool = False


def _normalize_path(path: str) -> str:
    return path.replace("\\", "/")


def _capability_from_filename(filename: str) -> str | None:
    stem = filename.rsplit(".", 1)[0] if "." in filename else filename
    if stem in ("overview", "patterns", "comparisons", "references", "README"):
        return None
    if stem.startswith("perplexityai_research_overview"):
        return None
    return stem


def classify(path: str) -> Classification:
    path = _normalize_path(path)

    # ------------------------------------------------------------------
    # 1. Try each research prefix (docs/research/, Kimi-Research/docs/research/)
    # ------------------------------------------------------------------
    for prefix, domain_pat, meta_pat, indices_pat, special_pat in _RESEARCH_PATTERNS:
        if not path.startswith(prefix):
            continue

        # Meta directory
        m = meta_pat.match(path)
        if m:
            return Classification(
                domain_tags=["meta"],
                capability_tags=[],
                is_classified=True,
            )

        # Indices directory
        m = indices_pat.match(path)
        if m:
            return Classification(
                domain_tags=["indices"],
                capability_tags=[],
                is_classified=True,
            )

        # Special underscore directories (_distilled, _extractions, _indices, _progress)
        m = special_pat.match(path)
        if m:
            special_dir = m.group(1)
            tag = _SPECIAL_RESEARCH_DIRS.get(special_dir, special_dir.lstrip("_"))
            filename = m.group(2).split("/")[-1]
            cap = _capability_from_filename(filename)
            return Classification(
                domain_tags=[tag],
                capability_tags=[cap] if cap else [],
                is_classified=True,
            )

        # Standard domain pattern (NN_domain/subdomain/file)
        m = domain_pat.match(path)
        if m:
            top_dir = m.group(1)
            subdomain = m.group(2)
            filename = m.group(3).split("/")[-1]

            if top_dir in DOMAIN_DIRECTORIES:
                known_subs = DOMAIN_DIRECTORIES[top_dir]
                if subdomain in known_subs:
                    cap = _capability_from_filename(filename)
                    capability_tags = [cap] if cap else []
                    return Classification(
                        domain_tags=[subdomain],
                        capability_tags=capability_tags,
                        is_classified=True,
                    )

        # Root-level files inside a research prefix (e.g. docs/research/index.md)
        rel = path[len(prefix):]
        if "/" not in rel:
            cap = _capability_from_filename(rel)
            return Classification(
                domain_tags=["research_root"],
                capability_tags=[cap] if cap else [],
                is_classified=True,
            )

        # Files matched the prefix but fell through — still classify as research
        first_dir = rel.split("/")[0]
        tag = _SPECIAL_RESEARCH_DIRS.get(first_dir, first_dir)
        filename = rel.split("/")[-1]
        cap = _capability_from_filename(filename)
        return Classification(
            domain_tags=[tag],
            capability_tags=[cap] if cap else [],
            is_classified=True,
        )

    # ------------------------------------------------------------------
    # 2. Top-level knowledge directories (distilled/, distillation/, etc.)
    # ------------------------------------------------------------------
    for kprefix, tag in _KNOWLEDGE_PREFIXES.items():
        if path.startswith(kprefix):
            filename = path.split("/")[-1]
            cap = _capability_from_filename(filename)
            return Classification(
                domain_tags=[tag],
                capability_tags=[cap] if cap else [],
                is_classified=True,
            )

    # ------------------------------------------------------------------
    # 3. Unclassified
    # ------------------------------------------------------------------
    return Classification()
