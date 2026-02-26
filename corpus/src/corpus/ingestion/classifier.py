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

_RESEARCH_PREFIX = "docs/research/"

_META_DIR = "00_meta"
_INDICES_DIR = "03_indices"

_DOMAIN_PATTERN = re.compile(
    r"^docs/research/(\d{2}_[^/]+)/([^/]+)/(.+)$"
)
_META_PATTERN = re.compile(
    r"^docs/research/00_meta/(.+)$"
)
_INDICES_PATTERN = re.compile(
    r"^docs/research/03_indices/(.+)$"
)


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

    if not path.startswith(_RESEARCH_PREFIX):
        return Classification()

    m = _META_PATTERN.match(path)
    if m:
        return Classification(
            domain_tags=["meta"],
            capability_tags=[],
            is_classified=True,
        )

    m = _INDICES_PATTERN.match(path)
    if m:
        return Classification(
            domain_tags=["indices"],
            capability_tags=[],
            is_classified=True,
        )

    m = _DOMAIN_PATTERN.match(path)
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

    return Classification()
