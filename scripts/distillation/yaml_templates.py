from __future__ import annotations

from .constants import AtomType
from .models import KnowledgeAtom

_GAP = "# GAP: insufficient research data to fill this field"


def _atoms_by_type(
    atoms: list[KnowledgeAtom], *types: AtomType
) -> list[KnowledgeAtom]:
    return [a for a in atoms if a.type in types]


def _first_content(atoms: list[KnowledgeAtom], *types: AtomType) -> str:
    filtered = _atoms_by_type(atoms, *types)
    return filtered[0].content if filtered else _GAP


def _content_list(atoms: list[KnowledgeAtom], *types: AtomType) -> list[str]:
    return [a.content for a in _atoms_by_type(atoms, *types)]


def _id_list(atoms: list[KnowledgeAtom], *types: AtomType) -> list[str]:
    return [a.id for a in _atoms_by_type(atoms, *types)]


def _ref(atom: KnowledgeAtom) -> str:
    return f"{atom.content} ({atom.id})"


def _build_gaps(spec: dict, path: str = "") -> list[str]:
    gaps: list[str] = []
    for key, val in spec.items():
        full = f"{path}.{key}" if path else key
        if val == _GAP:
            gaps.append(full)
        elif isinstance(val, dict):
            gaps.extend(_build_gaps(val, full))
        elif isinstance(val, list) and not val:
            gaps.append(f"{full} (empty list)")
    return gaps


def build_mode_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    techniques = _atoms_by_type(atoms, AtomType.TECHNIQUE, AtomType.RECIPE)
    tools = _atoms_by_type(atoms, AtomType.TOOL)
    metrics = _atoms_by_type(atoms, AtomType.METRIC)
    constraints = _atoms_by_type(atoms, AtomType.CONSTRAINT)
    tradeoffs = _atoms_by_type(atoms, AtomType.TRADEOFF)
    failures = _atoms_by_type(atoms, AtomType.FAILURE_MODE)

    role_parts = [a.content for a in techniques[:2]]
    role_def = " ".join(role_parts) if role_parts else _GAP

    enabled_tools = [{a.id: a.content} for a in tools[:5]]
    disabled_tools: list[dict] = []

    skills = [{a.id: a.content} for a in techniques[:5]]

    quality = [_ref(a) for a in metrics[:3]]

    transitions = []
    for a in tradeoffs[:2]:
        transitions.append(
            {"condition": a.content, "target_mode": _GAP, "context_to_pass": _GAP}
        )

    custom = "\n".join(a.content for a in constraints[:3]) if constraints else _GAP

    spec: dict = {
        "mode": name,
        "role_definition": role_def,
        "perspective": _first_content(atoms, AtomType.TECHNIQUE, AtomType.COMBINATION),
        "tools": {"enabled": enabled_tools, "disabled": disabled_tools},
        "context_strategy": _GAP,
        "skills_available": skills,
        "decision_authority": {
            "can_decide": [_ref(a) for a in techniques[:2]] or [_GAP],
            "must_escalate": [_ref(a) for a in failures[:2]] or [_GAP],
        },
        "quality_criteria": quality or [_GAP],
        "transition_triggers": transitions or [{"condition": _GAP, "target_mode": _GAP, "context_to_pass": _GAP}],
        "custom_instructions": custom,
    }
    return spec, _build_gaps(spec)


def build_skill_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    techniques = _atoms_by_type(atoms, AtomType.TECHNIQUE)
    recipes = _atoms_by_type(atoms, AtomType.RECIPE)
    tools = _atoms_by_type(atoms, AtomType.TOOL)
    metrics = _atoms_by_type(atoms, AtomType.METRIC)
    combos = _atoms_by_type(atoms, AtomType.COMBINATION)
    tradeoffs = _atoms_by_type(atoms, AtomType.TRADEOFF)
    anti = _atoms_by_type(atoms, AtomType.ANTI_PATTERN)

    primary = _ref(techniques[0]) if techniques else _GAP

    alternatives = []
    for a in techniques[1:3]:
        alt: dict = {"technique": _ref(a), "use_when": _GAP, "tradeoff": _GAP}
        alternatives.append(alt)
    for a in tradeoffs[:2]:
        alternatives.append({"technique": _GAP, "use_when": a.content, "tradeoff": a.id})

    combo_text = "\n".join(_ref(a) for a in (combos + recipes)[:3]) if (combos or recipes) else _GAP

    procedure: dict = {}
    if recipes:
        lines = recipes[0].content.split("\n")
        for i, line in enumerate(lines, 1):
            procedure[i] = line.strip()
    elif techniques:
        for i, a in enumerate(techniques[:5], 1):
            procedure[i] = a.content
    else:
        procedure[1] = _GAP

    spec: dict = {
        "skill": name,
        "purpose": techniques[0].content[:120] if techniques else (_GAP),
        "technique_stack": {
            "primary": primary,
            "alternatives": alternatives,
            "combination": combo_text,
        },
        "inputs": {"required": [_GAP], "optional": []},
        "procedure": procedure,
        "outputs": [_ref(a) for a in metrics[:2]] or [_GAP],
        "quality_check": _first_content(atoms, AtomType.METRIC),
        "when_to_use": [_ref(a) for a in techniques[:2]] or [_GAP],
        "when_NOT_to_use": [_ref(a) for a in anti[:2]] or [_GAP],
        "cost_profile": {
            "tokens": _GAP,
            "latency": _GAP,
            "when_to_skip": _first_content(atoms, AtomType.TRADEOFF),
        },
    }
    return spec, _build_gaps(spec)


def build_workflow_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    recipes = _atoms_by_type(atoms, AtomType.RECIPE)
    constraints = _atoms_by_type(atoms, AtomType.CONSTRAINT)
    metrics = _atoms_by_type(atoms, AtomType.METRIC)
    failures = _atoms_by_type(atoms, AtomType.FAILURE_MODE)
    techniques = _atoms_by_type(atoms, AtomType.TECHNIQUE)

    phases = []
    source = recipes or techniques
    for i, a in enumerate(source[:4], 1):
        phase: dict = {
            "name": f"phase_{i}",
            "mode": _GAP,
            "skills": [a.id],
            "entry_criteria": _GAP,
            "steps": {j + 1: line.strip() for j, line in enumerate(a.content.split("\n")[:3])},
            "exit_criteria": _GAP,
            "quality_gate": {
                "checks": [_ref(m) for m in metrics[:1]] or [_GAP],
                "on_failure": "escalate",
            },
            "artifacts_produced": [],
        }
        phases.append(phase)

    if not phases:
        phases.append({
            "name": "phase_1",
            "mode": _GAP,
            "skills": [_GAP],
            "entry_criteria": _GAP,
            "steps": {1: _GAP},
            "exit_criteria": _GAP,
            "quality_gate": {"checks": [_GAP], "on_failure": "escalate"},
            "artifacts_produced": [],
        })

    rollback = "\n".join(_ref(a) for a in failures[:2]) if failures else _GAP

    spec: dict = {
        "workflow": name,
        "trigger": _first_content(atoms, AtomType.TECHNIQUE, AtomType.RECIPE),
        "phases": phases,
        "completion_criteria": _first_content(atoms, AtomType.METRIC, AtomType.CONSTRAINT),
        "rollback_plan": rollback,
    }
    return spec, _build_gaps(spec)


def build_rule_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    constraints = _atoms_by_type(atoms, AtomType.CONSTRAINT)
    failures = _atoms_by_type(atoms, AtomType.FAILURE_MODE)
    anti = _atoms_by_type(atoms, AtomType.ANTI_PATTERN)

    constraint_text = "\n".join(_ref(a) for a in constraints[:3]) if constraints else _GAP
    rationale = "\n".join(_ref(a) for a in (failures + anti)[:2]) if (failures or anti) else _GAP

    severity = "critical" if any(a.evidence_strength.value == "STRONG" for a in constraints) else "medium"

    spec: dict = {
        "rule": name,
        "constraint": constraint_text,
        "rationale": rationale,
        "enforcement": {
            "detection": _first_content(atoms, AtomType.FAILURE_MODE, AtomType.TECHNIQUE),
            "response": _first_content(atoms, AtomType.TECHNIQUE, AtomType.RECIPE),
            "severity": severity,
        },
        "exceptions": [{"condition": _GAP, "requires": _GAP}],
    }
    return spec, _build_gaps(spec)


def build_context_strategy_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    techniques = _atoms_by_type(atoms, AtomType.TECHNIQUE)
    metrics = _atoms_by_type(atoms, AtomType.METRIC)
    constraints = _atoms_by_type(atoms, AtomType.CONSTRAINT)
    failures = _atoms_by_type(atoms, AtomType.FAILURE_MODE)
    tradeoffs = _atoms_by_type(atoms, AtomType.TRADEOFF)

    compression = {}
    comp_atoms = [a for a in techniques + tradeoffs if a]
    for i, a in enumerate(comp_atoms[:3], 1):
        compression[i] = _ref(a)
    if not compression:
        compression[1] = _GAP

    spec: dict = {
        "strategy": name,
        "applies_to": [_GAP],
        "window_partition": {
            "system_instructions": "15%",
            "task_context": "30%",
            "relevant_code": "35%",
            "history": "10%",
            "reserved_for_output": "10%",
        },
        "content_selection": {
            "include": [_ref(a) for a in metrics[:2]] or [_GAP],
            "exclude": [_ref(a) for a in _atoms_by_type(atoms, AtomType.ANTI_PATTERN)[:2]] or [_GAP],
        },
        "compression_pipeline": compression,
        "ordering_rules": [_ref(a) for a in constraints[:2]] or [_GAP],
        "refresh_policy": _first_content(atoms, AtomType.TRADEOFF, AtomType.TECHNIQUE),
        "poisoning_checks": [_ref(a) for a in failures[:2]] or [_GAP],
    }
    return spec, _build_gaps(spec)


def build_technique_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    techniques = _atoms_by_type(atoms, AtomType.TECHNIQUE, AtomType.RECIPE)
    failures = _atoms_by_type(atoms, AtomType.FAILURE_MODE)
    tradeoffs = _atoms_by_type(atoms, AtomType.TRADEOFF)
    metrics = _atoms_by_type(atoms, AtomType.METRIC)

    signals = [_ref(a) for a in (failures + tradeoffs)[:2]]

    procedure: dict = {}
    if techniques:
        lines = techniques[0].content.split("\n")
        for i, line in enumerate(lines[:5], 1):
            procedure[i] = line.strip()
    else:
        procedure[1] = _GAP

    spec: dict = {
        "technique": name,
        "situation": _first_content(atoms, AtomType.FAILURE_MODE, AtomType.TRADEOFF),
        "recognition": {"signals": signals or [_GAP]},
        "response": {
            "decision_criteria": _first_content(atoms, AtomType.TRADEOFF),
            "procedure": procedure,
            "success_criteria": _first_content(atoms, AtomType.METRIC),
            "fallback": _first_content(atoms, AtomType.FAILURE_MODE),
        },
    }
    return spec, _build_gaps(spec)


def build_task_decomposition_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    recipes = _atoms_by_type(atoms, AtomType.RECIPE)
    constraints = _atoms_by_type(atoms, AtomType.CONSTRAINT)
    tradeoffs = _atoms_by_type(atoms, AtomType.TRADEOFF)
    metrics = _atoms_by_type(atoms, AtomType.METRIC)

    levels = []
    for a in recipes[:3]:
        levels.append({"level": a.id, "granularity": a.content[:100], "criteria": _GAP})
    if not levels:
        levels.append({"level": _GAP, "granularity": _GAP, "criteria": _GAP})

    checkpoints = []
    for a in metrics[:2]:
        checkpoints.append({"after": _GAP, "verify": _ref(a)})
    if not checkpoints:
        checkpoints.append({"after": _GAP, "verify": _GAP})

    spec: dict = {
        "pattern": name,
        "work_type": _GAP,
        "decomposition": {"levels": levels},
        "dependency_rules": [_ref(a) for a in constraints[:2]] or [_GAP],
        "parallelization": _first_content(atoms, AtomType.TRADEOFF),
        "estimation": _first_content(atoms, AtomType.METRIC),
        "validation_checkpoints": checkpoints,
    }
    return spec, _build_gaps(spec)


def build_mcp_config_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    tools = _atoms_by_type(atoms, AtomType.TOOL)
    constraints = _atoms_by_type(atoms, AtomType.CONSTRAINT)
    failures = _atoms_by_type(atoms, AtomType.FAILURE_MODE)
    tradeoffs = _atoms_by_type(atoms, AtomType.TRADEOFF)

    servers = []
    for a in tools[:5]:
        srv: dict = {
            "name": a.id,
            "purpose": a.content,
            "capabilities_used": [],
            "privileges": {
                "filesystem": "read-only",
                "network": "denied",
                "execution": "sandboxed",
            },
            "when_to_invoke": _GAP,
        }
        servers.append(srv)
    if not servers:
        servers.append({
            "name": _GAP,
            "purpose": _GAP,
            "capabilities_used": [],
            "privileges": {"filesystem": _GAP, "network": _GAP, "execution": _GAP},
            "when_to_invoke": _GAP,
        })

    spec: dict = {
        "configuration": name,
        "applies_to": [_GAP],
        "servers": servers,
        "selection_logic": _first_content(atoms, AtomType.TRADEOFF),
        "fallback": _first_content(atoms, AtomType.FAILURE_MODE, AtomType.TRADEOFF),
        "security_constraints": [_ref(a) for a in constraints[:3]] or [_GAP],
    }
    return spec, _build_gaps(spec)


def build_prompt_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    techniques = _atoms_by_type(atoms, AtomType.TECHNIQUE, AtomType.RECIPE)
    constraints = _atoms_by_type(atoms, AtomType.CONSTRAINT)
    metrics = _atoms_by_type(atoms, AtomType.METRIC)
    anti = _atoms_by_type(atoms, AtomType.ANTI_PATTERN)

    sections = [_ref(a) for a in techniques[:3]]

    spec: dict = {
        "prompt": name,
        "target": _GAP,
        "structure": {
            "sections": sections or [_GAP],
            "context_placement": _first_content(atoms, AtomType.CONSTRAINT, AtomType.TECHNIQUE),
        },
        "instructions": _first_content(atoms, AtomType.TECHNIQUE, AtomType.RECIPE),
        "guardrails": [_ref(a) for a in constraints[:3]] or [_GAP],
        "output_format": _first_content(atoms, AtomType.RECIPE),
        "token_budget": _first_content(atoms, AtomType.METRIC),
    }
    return spec, _build_gaps(spec)


def build_workspace_spec(
    name: str, atoms: list[KnowledgeAtom]
) -> tuple[dict, list[str]]:
    techniques = _atoms_by_type(atoms, AtomType.TECHNIQUE, AtomType.RECIPE)
    constraints = _atoms_by_type(atoms, AtomType.CONSTRAINT)
    failures = _atoms_by_type(atoms, AtomType.FAILURE_MODE)
    tools = _atoms_by_type(atoms, AtomType.TOOL)

    spec: dict = {
        "workspace": name,
        "branch_strategy": _first_content(atoms, AtomType.TECHNIQUE, AtomType.RECIPE),
        "work_tree_management": _first_content(atoms, AtomType.TOOL, AtomType.TECHNIQUE),
        "file_organization": _first_content(atoms, AtomType.RECIPE, AtomType.TECHNIQUE),
        "state_persistence": _first_content(atoms, AtomType.TECHNIQUE),
        "artifact_management": _first_content(atoms, AtomType.TOOL),
        "cleanup": _first_content(atoms, AtomType.CONSTRAINT, AtomType.FAILURE_MODE),
        "conflict_resolution": _first_content(atoms, AtomType.FAILURE_MODE, AtomType.TECHNIQUE),
    }
    return spec, _build_gaps(spec)


BUILDERS: dict[str, callable] = {
    "PC1": build_mode_spec,
    "PC2": build_skill_spec,
    "PC3": build_workflow_spec,
    "PC4": build_prompt_spec,
    "PC5": build_mcp_config_spec,
    "PC6": build_rule_spec,
    "PC7": build_context_strategy_spec,
    "PC8": build_task_decomposition_spec,
    "PC9": build_workspace_spec,
    "PC10": build_technique_spec,
}
