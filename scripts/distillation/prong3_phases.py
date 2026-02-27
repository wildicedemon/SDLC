from __future__ import annotations

from pathlib import Path

from .constants import (
    PHASE_NAMES,
    AtomType,
    SDLCPhase,
)
from .models import KnowledgeAtom, PhaseSpec


PHASE_DESCRIPTIONS: dict[str, str] = {
    "P1": "The agent is encountering a new or unfamiliar codebase — scanning, mapping dependencies, and building an initial understanding of the architecture.",
    "P2": "The agent is deciding what to build and how — decomposing tasks, sequencing dependencies, and selecting architecture and branch strategies.",
    "P3": "The agent is writing code — generating implementations, managing context windows, verifying packages, and adhering to style conventions.",
    "P4": "The agent is verifying that code works correctly — generating tests, running quality gates, performing mutation testing, and security scanning.",
    "P5": "The agent is reviewing code (its own or another agent's) — traversing changes, running semantic diffs, detecting anti-patterns, and assessing impact.",
    "P6": "The agent is diagnosing and fixing problems — performing root cause analysis, recognizing error patterns, and applying automated repair strategies.",
    "P7": "The agent is deploying code to environments — interacting with CI/CD pipelines, executing canary/blue-green strategies, and verifying health checks.",
    "P8": "The agent is maintaining running systems — detecting incidents, monitoring performance, managing dependency updates, and identifying technical debt.",
}

PHASE_TRANSITIONS: dict[str, dict[str, str]] = {
    "P1": {
        "Exit to P2 when": "Codebase structure, dependencies, and entry points are mapped",
        "Fallback to P1 when": "New unfamiliar module or dependency discovered during later phases",
    },
    "P2": {
        "Exit to P3 when": "Task decomposition complete and implementation plan approved",
        "Fallback to P1 when": "Significant unknowns discovered requiring deeper codebase exploration",
    },
    "P3": {
        "Exit to P4 when": "Implementation complete and ready for verification",
        "Fallback to P2 when": "Requirements or architecture need re-evaluation",
    },
    "P4": {
        "Exit to P5 when": "All quality gates pass and test coverage meets thresholds",
        "Fallback to P3 when": "Tests reveal implementation defects requiring code changes",
    },
    "P5": {
        "Exit to P7 when": "Review approved with no blocking issues",
        "Fallback to P3 when": "Review identifies issues requiring implementation changes",
        "Fallback to P6 when": "Review reveals bugs needing investigation",
    },
    "P6": {
        "Exit to P3 when": "Root cause identified and fix strategy determined",
        "Fallback to P1 when": "Bug involves unfamiliar code area requiring fresh discovery",
    },
    "P7": {
        "Exit to P8 when": "Deployment verified and health checks pass",
        "Fallback to P6 when": "Deployment failure or health check failure requiring diagnosis",
    },
    "P8": {
        "Exit to P6 when": "Incident detected requiring debugging",
        "Exit to P2 when": "Maintenance reveals need for new feature or significant refactor",
    },
}

STEP_LABELS: dict[str, list[str]] = {
    "P1": [
        "Scan codebase structure and entry points",
        "Map dependencies and external integrations",
        "Extract architecture patterns and API surfaces",
        "Identify gaps between current and desired state",
    ],
    "P2": [
        "Decompose work into task hierarchy",
        "Sequence dependencies and identify parallelization",
        "Select architecture approach and branch strategy",
        "Estimate resource requirements (tokens, time, cost)",
    ],
    "P3": [
        "Set up context window with relevant code and specs",
        "Generate code following project conventions",
        "Verify packages and imports against registry",
        "Run incremental validation during implementation",
    ],
    "P4": [
        "Generate test cases (unit, integration, E2E)",
        "Execute quality gate checks",
        "Run mutation testing on generated tests",
        "Perform security scanning and performance profiling",
    ],
    "P5": [
        "Traverse code changes using semantic diff",
        "Analyze change impact across codebase",
        "Detect anti-patterns and security issues",
        "Verify review checklist and refactoring opportunities",
    ],
    "P6": [
        "Collect error context and reproduce the issue",
        "Perform root cause analysis with code traversal",
        "Apply automated repair strategies",
        "Verify fix and check for regressions",
    ],
    "P7": [
        "Prepare deployment artifacts and configuration",
        "Execute deployment strategy (canary/blue-green)",
        "Verify health checks and rollback readiness",
        "Manage feature flags and release gates",
    ],
    "P8": [
        "Monitor system performance and health",
        "Detect and respond to incidents",
        "Manage dependency updates and security patches",
        "Identify technical debt and optimization targets",
    ],
}


def _atoms_for_phase(atoms: list[KnowledgeAtom], phase_key: str) -> list[KnowledgeAtom]:
    return [a for a in atoms if phase_key in a.sdlc_phases]


def _filter_by_type(atoms: list[KnowledgeAtom], atom_type: AtomType) -> list[KnowledgeAtom]:
    return [a for a in atoms if a.type == atom_type]


def _build_phase_spec(
    phase_key: str,
    phase_atoms: list[KnowledgeAtom],
) -> PhaseSpec:
    phase_enum = SDLCPhase(phase_key)
    name = PHASE_NAMES[phase_key]
    description = PHASE_DESCRIPTIONS.get(phase_key, "")

    techniques = _filter_by_type(phase_atoms, AtomType.TECHNIQUE)
    recipes = _filter_by_type(phase_atoms, AtomType.RECIPE)
    technique_atoms = techniques + recipes

    steps = STEP_LABELS.get(phase_key, [])
    techniques_by_step: dict[str, list[str]] = {}
    for i, label in enumerate(steps):
        step_key = f"Step {i + 1} — {label}"
        chunk_size = max(1, len(technique_atoms) // max(len(steps), 1))
        start = i * chunk_size
        end = start + chunk_size if i < len(steps) - 1 else len(technique_atoms)
        techniques_by_step[step_key] = [a.id for a in technique_atoms[start:end]]

    constraints = [a.id for a in _filter_by_type(phase_atoms, AtomType.CONSTRAINT)]
    tools = [a.id for a in _filter_by_type(phase_atoms, AtomType.TOOL)]
    failure_modes = [
        a.id
        for a in phase_atoms
        if a.type in (AtomType.FAILURE_MODE, AtomType.ANTI_PATTERN)
    ]
    transitions = PHASE_TRANSITIONS.get(phase_key, {})

    return PhaseSpec(
        phase=phase_enum,
        name=name,
        description=description,
        atom_ids=[a.id for a in phase_atoms],
        techniques_by_step=techniques_by_step,
        constraints=constraints,
        tools=tools,
        failure_modes=failure_modes,
        transitions=transitions,
    )


def _render_phase_markdown(spec: PhaseSpec, atoms_by_id: dict[str, KnowledgeAtom]) -> str:
    lines: list[str] = []
    lines.append(f"# {spec.phase.value}: {spec.name}")
    lines.append("")
    lines.append(f"**WHAT THE AGENT IS DOING**: {spec.description}")
    lines.append("")

    lines.append(f"## Knowledge Atoms ({len(spec.atom_ids)} total)")
    lines.append("")
    for aid in spec.atom_ids:
        atom = atoms_by_id.get(aid)
        if atom:
            lines.append(f"- `{aid}` [{atom.type.value}] ({atom.evidence_strength.value}) — {atom.content[:120]}")
        else:
            lines.append(f"- `{aid}`")
    lines.append("")

    lines.append("## Techniques to Use (ranked, by step)")
    lines.append("")
    for step_label, atom_ids in spec.techniques_by_step.items():
        lines.append(f"### {step_label}")
        if atom_ids:
            for aid in atom_ids:
                atom = atoms_by_id.get(aid)
                if atom:
                    lines.append(f"- `{aid}` ({atom.evidence_strength.value}) — {atom.content[:120]}")
                else:
                    lines.append(f"- `{aid}`")
        else:
            lines.append("- *(no atoms mapped to this step)*")
        lines.append("")

    lines.append("## Constraints in Effect")
    lines.append("")
    if spec.constraints:
        for aid in spec.constraints:
            atom = atoms_by_id.get(aid)
            if atom:
                lines.append(f"- `{aid}` — {atom.content[:150]}")
            else:
                lines.append(f"- `{aid}`")
    else:
        lines.append("- *(no constraints identified for this phase)*")
    lines.append("")

    lines.append("## Tools Needed")
    lines.append("")
    if spec.tools:
        for aid in spec.tools:
            atom = atoms_by_id.get(aid)
            if atom:
                lines.append(f"- `{aid}` — {atom.content[:150]}")
            else:
                lines.append(f"- `{aid}`")
    else:
        lines.append("- *(no tools identified for this phase)*")
    lines.append("")

    lines.append("## Failure Modes to Watch For")
    lines.append("")
    if spec.failure_modes:
        for aid in spec.failure_modes:
            atom = atoms_by_id.get(aid)
            if atom:
                lines.append(f"- `{aid}` [{atom.type.value}] — {atom.content[:150]}")
            else:
                lines.append(f"- `{aid}`")
    else:
        lines.append("- *(no failure modes identified for this phase)*")
    lines.append("")

    lines.append("## Transitions")
    lines.append("")
    if spec.transitions:
        for condition, target in spec.transitions.items():
            lines.append(f"- **{condition}**: {target}")
    else:
        lines.append("- *(no transitions defined)*")
    lines.append("")

    return "\n".join(lines)


PHASE_FILE_NAMES: dict[str, str] = {
    "P1": "P1_discovery_onboarding.md",
    "P2": "P2_planning_design.md",
    "P3": "P3_implementation.md",
    "P4": "P4_testing_verification.md",
    "P5": "P5_code_review.md",
    "P6": "P6_debugging_error_recovery.md",
    "P7": "P7_deployment_release.md",
    "P8": "P8_maintenance_monitoring.md",
}


def generate_phase_specs(
    atoms: list[KnowledgeAtom],
    output_dir: Path,
) -> list[PhaseSpec]:
    phases_dir = output_dir / "phases"
    phases_dir.mkdir(parents=True, exist_ok=True)

    atoms_by_id: dict[str, KnowledgeAtom] = {a.id: a for a in atoms}

    specs: list[PhaseSpec] = []
    for phase_key in [p.value for p in SDLCPhase]:
        phase_atoms = _atoms_for_phase(atoms, phase_key)
        spec = _build_phase_spec(phase_key, phase_atoms)
        specs.append(spec)

        md_content = _render_phase_markdown(spec, atoms_by_id)
        filename = PHASE_FILE_NAMES[phase_key]
        (phases_dir / filename).write_text(md_content, encoding="utf-8")

    return specs
