from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from .constants import (
    DOMAIN_NAMES,
    AtomType,
    Domain,
    EvidenceStrength,
)
from .models import DomainSpec, KnowledgeAtom

_EVIDENCE_ORDER = {
    EvidenceStrength.STRONG: 0,
    EvidenceStrength.MODERATE: 1,
    EvidenceStrength.WEAK: 2,
}

_DOMAIN_FILE_NAMES: dict[str, str] = {
    "D1": "D01_agent_architecture.md",
    "D2": "D02_task_management.md",
    "D3": "D03_context_prompt_engineering.md",
    "D4": "D04_memory_knowledge_systems.md",
    "D5": "D05_code_intelligence.md",
    "D6": "D06_testing_validation.md",
    "D7": "D07_security_guardrails.md",
    "D8": "D08_model_management.md",
    "D9": "D09_cicd_devops.md",
    "D10": "D10_workspace_infrastructure.md",
    "D11": "D11_human_interaction.md",
    "D12": "D12_self_improvement.md",
}

_EXPECTED_TYPES: dict[str, list[AtomType]] = {
    key: [
        AtomType.TECHNIQUE,
        AtomType.CONSTRAINT,
        AtomType.TOOL,
        AtomType.COMBINATION,
        AtomType.RECIPE,
        AtomType.FAILURE_MODE,
        AtomType.METRIC,
        AtomType.TRADEOFF,
    ]
    for key in DOMAIN_NAMES
}


def _sort_by_evidence(atoms: list[KnowledgeAtom]) -> list[KnowledgeAtom]:
    return sorted(atoms, key=lambda a: _EVIDENCE_ORDER.get(a.evidence_strength, 3))


def _one_line(atom: KnowledgeAtom, max_len: int = 120) -> str:
    text = atom.content.replace("\n", " ").strip()
    if len(text) > max_len:
        text = text[: max_len - 3] + "..."
    return text


def _build_domain_spec(
    domain_key: str,
    atoms: list[KnowledgeAtom],
    all_atoms_by_id: dict[str, KnowledgeAtom],
) -> DomainSpec:
    sorted_atoms = _sort_by_evidence(atoms)
    atom_ids = [a.id for a in sorted_atoms]

    by_type: dict[AtomType, list[KnowledgeAtom]] = defaultdict(list)
    for a in sorted_atoms:
        by_type[a.type].append(a)

    key_techniques = [a.id for a in by_type.get(AtomType.TECHNIQUE, [])]
    key_techniques += [a.id for a in by_type.get(AtomType.RECIPE, [])]
    key_constraints = [a.id for a in by_type.get(AtomType.CONSTRAINT, [])]
    key_tools = [a.id for a in by_type.get(AtomType.TOOL, [])]
    combination_recipes = [a.id for a in by_type.get(AtomType.COMBINATION, [])]
    failure_modes = [a.id for a in by_type.get(AtomType.FAILURE_MODE, [])]
    failure_modes += [a.id for a in by_type.get(AtomType.ANTI_PATTERN, [])]

    cross_domain_links: dict[str, list[str]] = {}
    for a in sorted_atoms:
        other_domains = [d for d in a.domains if d != domain_key]
        if other_domains:
            cross_domain_links[a.id] = other_domains

    present_types = set(by_type.keys())
    gaps: list[str] = []
    for expected in _EXPECTED_TYPES.get(domain_key, []):
        if expected not in present_types:
            gaps.append(f"No {expected.value} atoms found")
    if len(atoms) < 3:
        gaps.append(f"Thin coverage: only {len(atoms)} atom(s)")

    return DomainSpec(
        domain=Domain(domain_key),
        name=DOMAIN_NAMES[domain_key],
        atom_ids=atom_ids,
        key_techniques=key_techniques,
        key_constraints=key_constraints,
        key_tools=key_tools,
        combination_recipes=combination_recipes,
        failure_modes=failure_modes,
        cross_domain_links=cross_domain_links,
        gaps=gaps,
    )


def _render_domain_md(
    spec: DomainSpec,
    atoms_by_id: dict[str, KnowledgeAtom],
) -> str:
    lines: list[str] = []
    lines.append(f"# DOMAIN: {spec.domain.value} — {spec.name}")
    lines.append("")

    lines.append(f"## KNOWLEDGE ATOMS ({len(spec.atom_ids)} total, ranked by evidence strength)")
    lines.append("")
    for aid in spec.atom_ids:
        a = atoms_by_id.get(aid)
        if a:
            lines.append(f"- `{aid}` [{a.type.value}] [{a.evidence_strength.value}]")
    lines.append("")

    if spec.key_techniques:
        lines.append("## KEY TECHNIQUES (ranked)")
        lines.append("")
        for i, aid in enumerate(spec.key_techniques, 1):
            a = atoms_by_id.get(aid)
            if a:
                lines.append(f"{i}. `{aid}` — {_one_line(a)} — {a.evidence_strength.value}")
        lines.append("")

    if spec.key_constraints:
        lines.append("## KEY CONSTRAINTS")
        lines.append("")
        for aid in spec.key_constraints:
            a = atoms_by_id.get(aid)
            if a:
                lines.append(f"- `{aid}` — {_one_line(a)}")
        lines.append("")

    if spec.key_tools:
        lines.append("## KEY TOOLS")
        lines.append("")
        for aid in spec.key_tools:
            a = atoms_by_id.get(aid)
            if a:
                lines.append(f"- `{aid}` — {_one_line(a)} — {a.evidence_strength.value}")
        lines.append("")

    if spec.combination_recipes:
        lines.append("## COMBINATION RECIPES")
        lines.append("")
        for aid in spec.combination_recipes:
            a = atoms_by_id.get(aid)
            if a:
                lines.append(f"- `{aid}` — {_one_line(a)}")
        lines.append("")

    if spec.failure_modes:
        lines.append("## FAILURE MODES")
        lines.append("")
        for aid in spec.failure_modes:
            a = atoms_by_id.get(aid)
            if a:
                lines.append(f"- `{aid}` — {_one_line(a)}")
        lines.append("")

    if spec.cross_domain_links:
        lines.append("## CROSS-DOMAIN LINKS")
        lines.append("")
        for aid, other_domains in spec.cross_domain_links.items():
            domain_names = [f"{d} ({DOMAIN_NAMES.get(d, d)})" for d in other_domains]
            lines.append(f"- `{aid}` also relevant to {', '.join(domain_names)}")
        lines.append("")

    lines.append("## GAPS")
    lines.append("")
    if spec.gaps:
        for gap in spec.gaps:
            lines.append(f"- {gap}")
    else:
        lines.append("- No gaps identified")
    lines.append("")

    return "\n".join(lines)


def generate_domain_specs(
    atoms: list[KnowledgeAtom],
    output_dir: Path,
) -> list[DomainSpec]:
    domains_dir = output_dir / "domains"
    domains_dir.mkdir(parents=True, exist_ok=True)

    atoms_by_id: dict[str, KnowledgeAtom] = {a.id: a for a in atoms}

    by_domain: dict[str, list[KnowledgeAtom]] = defaultdict(list)
    for a in atoms:
        for d in a.domains:
            by_domain[d].append(a)

    specs: list[DomainSpec] = []
    for domain_key in sorted(DOMAIN_NAMES.keys(), key=lambda k: int(k[1:])):
        domain_atoms = by_domain.get(domain_key, [])
        spec = _build_domain_spec(domain_key, domain_atoms, atoms_by_id)
        specs.append(spec)

        md_content = _render_domain_md(spec, atoms_by_id)
        filename = _DOMAIN_FILE_NAMES[domain_key]
        (domains_dir / filename).write_text(md_content, encoding="utf-8")

    return specs
