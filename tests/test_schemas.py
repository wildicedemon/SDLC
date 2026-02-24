import pytest
from pydantic import ValidationError
from scripts.distillation.schemas import (
    KnowledgeAtom,
    AtomType,
    EvidenceStrength,
    DomainOutput,
    PhaseOutput,
    ModeSpec,
    SkillSpec,
)


def test_knowledge_atom_valid():
    atom = KnowledgeAtom(
        id="KA-001",
        type=AtomType.TOOL,
        content="Tree-sitter: incremental AST parsing, 40+ languages, error recovery, de facto standard",
        evidence_strength=EvidenceStrength.STRONG,
        source=["knowledge_representation/overview.md"],
        domains=["D5"],
        sdlc_phases=["P1", "P3", "P5"],
        products=["PC2"],
    )
    assert atom.id == "KA-001"
    assert atom.type == AtomType.TOOL


def test_knowledge_atom_invalid_type():
    with pytest.raises(ValidationError):
        KnowledgeAtom(
            id="KA-002",
            type="INVALID_TYPE",
            content="Invalid type",
            evidence_strength=EvidenceStrength.STRONG,
            source=[],
            domains=[],
            sdlc_phases=[],
            products=[],
        )


def test_domain_output_valid():
    domain_output = DomainOutput(
        domain="D5",
        knowledge_atoms=["KA-001", "KA-004"],
        key_techniques=[
            {
                "atom_id": "KA-001",
                "summary": "Tree-sitter for AST",
                "evidence_strength": "STRONG",
            }
        ],
        key_constraints=[],
        key_tools=[
            {
                "atom_id": "KA-004",
                "tool": "Sourcegraph",
                "evaluated_capability": "multi-repo symbol search",
            }
        ],
        combination_recipes=[],
        failure_modes=[],
        cross_domain_links=[{"atom_id": "KA-005", "relevant_domains": ["D7"]}],
        gaps=["Needs more info on X"],
    )
    assert domain_output.domain == "D5"
    assert len(domain_output.key_techniques) == 1


def test_phase_output_valid():
    phase_output = PhaseOutput(
        phase="P1",
        **{"WHAT THE AGENT IS DOING": "Initial codebase understanding"},
        knowledge_atoms=["KA-001", "KA-002"],
        techniques_to_use=[
            {"step_number": 1, "description": "Parse codebase", "atom_ids": ["KA-001"]}
        ],
        constraints_in_effect=[],
        tools_needed=["KA-004"],
        failure_modes_to_watch_for=[],
        transitions=[
            {
                "target_phase": "P2",
                "condition": "Understanding complete",
                "is_fallback": False,
            }
        ]
    )
    assert phase_output.phase == "P1"
    assert (
        getattr(phase_output, "WHAT THE AGENT IS DOING", phase_output.description)
        == "Initial codebase understanding"
    )


def test_skill_spec_valid():
    skill = SkillSpec(
        skill="code_traversal",
        purpose="Navigate and understand code structure",
        technique_stack={
            "primary": "Tree-sitter AST parsing",
            "alternatives": [
                {
                    "technique": "LSIF offline index",
                    "use_when": "Pre-indexed codebase",
                    "tradeoff": "Faster queries but no real-time updates",
                }
            ],
            "combination": "Tier 1: AST + Symbol Index",
        },
        inputs={
            "required": ["Target file(s)", "Task type"],
            "optional": ["Existing symbol index"],
        },
        procedure={1: "Parse target file(s) with Tree-sitter", 2: "Query symbol index"},
        outputs=["Code structure map", "Symbol reference graph"],
        quality_check="Verify all referenced symbols resolved",
        when_to_use=["Agent needs to understand unfamiliar code"],
        when_not_to_use=["Simple text search is sufficient"],
        cost_profile={
            "tokens": "LOW",
            "latency": "Tier 1 fast",
            "when_to_skip": "Single-file edits",
        },
    )
    assert skill.skill == "code_traversal"
    assert len(skill.procedure) == 2


def test_mode_spec_valid():
    mode = ModeSpec(
        mode="coder",
        role_definition="Writes code based on specs",
        perspective="Focus on correctness and style",
        tools={
            "enabled": {"editor": "to edit files"},
            "disabled": {"bash": "not needed"},
        },
        context_strategy="default_context",
        skills_available={"code_traversal": "when analyzing"},
        decision_authority={
            "can_decide": ["variable names"],
            "must_escalate": ["architecture changes"],
        },
        quality_criteria=["tests pass"],
        transition_triggers=[
            {
                "condition": "code complete",
                "target_mode": "tester",
                "context_to_pass": "file paths",
            }
        ],
        custom_instructions="Do your best",
    )
    assert mode.mode == "coder"
    assert mode.tools.enabled["editor"] == "to edit files"
