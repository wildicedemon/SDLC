from enum import Enum
from typing import List, Dict, Any
from pydantic import BaseModel, Field


class AtomType(str, Enum):
    TECHNIQUE = "TECHNIQUE"
    METRIC = "METRIC"
    CONSTRAINT = "CONSTRAINT"
    TOOL = "TOOL"
    COMBINATION = "COMBINATION"
    FAILURE_MODE = "FAILURE_MODE"
    ANTI_PATTERN = "ANTI_PATTERN"
    TRADEOFF = "TRADEOFF"
    RECIPE = "RECIPE"


class EvidenceStrength(str, Enum):
    STRONG = "STRONG"
    MODERATE = "MODERATE"
    WEAK = "WEAK"


class KnowledgeAtom(BaseModel):
    id: str = Field(description="Unique identifier, e.g., KA-047")
    type: AtomType
    content: str = Field(description="The actual knowledge, 1-5 sentences max")
    evidence_strength: EvidenceStrength
    source: List[str] = Field(description="Research file path(s) where this was found")
    domains: List[str] = Field(
        description="Which technical domains this applies to (D1-D12)"
    )
    sdlc_phases: List[str] = Field(
        description="Which lifecycle phases this applies to (P1-P8)"
    )
    products: List[str] = Field(description="Which product types this feeds (PC1-PC10)")


# Prong 2 Domain Output


class RankedAtom(BaseModel):
    atom_id: str
    summary: str
    evidence_strength: EvidenceStrength


class KeyConstraint(BaseModel):
    atom_id: str
    constraint: str


class KeyTool(BaseModel):
    atom_id: str
    tool: str
    evaluated_capability: str


class CombinationRecipe(BaseModel):
    atom_id: str
    description: str


class FailureMode(BaseModel):
    atom_id: str
    what_breaks: str
    how_to_detect: str
    how_to_respond: str


class CrossDomainLink(BaseModel):
    atom_id: str
    relevant_domains: List[str]


class DomainOutput(BaseModel):
    domain: str
    knowledge_atoms: List[str]
    key_techniques: List[RankedAtom]
    key_constraints: List[KeyConstraint]
    key_tools: List[KeyTool]
    combination_recipes: List[CombinationRecipe]
    failure_modes: List[FailureMode]
    cross_domain_links: List[CrossDomainLink]
    gaps: List[str]


# Prong 3 SDLC Phase Output


class PhaseStep(BaseModel):
    step_number: int
    description: str
    atom_ids: List[str]


class PhaseTransition(BaseModel):
    target_phase: str
    condition: str
    is_fallback: bool = False


class PhaseOutput(BaseModel):
    phase: str
    description: str = Field(alias="WHAT THE AGENT IS DOING", default="")
    knowledge_atoms: List[str]
    techniques_to_use: List[PhaseStep]
    constraints_in_effect: List[str]
    tools_needed: List[str]
    failure_modes_to_watch_for: List[str]
    transitions: List[PhaseTransition]


# Prong 4 Spec Templates


class ProductSpec(BaseModel):
    product: str
    instance: str
    knowledge_atoms_consumed: List[str]
    draft_spec: Any  # Can be a more specific type depending on the product
    confidence: str  # HIGH, MEDIUM, LOW
    gaps: List[str]


# PC1: Mode Spec
class TransitionTrigger(BaseModel):
    condition: str
    target_mode: str
    context_to_pass: str


class ModeDecisionAuthority(BaseModel):
    can_decide: List[str]
    must_escalate: List[str]


class ModeTools(BaseModel):
    enabled: Dict[str, str]  # tool: why
    disabled: Dict[str, str]  # tool: why


class ModeSpec(BaseModel):
    mode: str
    role_definition: str
    perspective: str
    tools: ModeTools
    context_strategy: str
    skills_available: Dict[str, str]  # skill: when to invoke
    decision_authority: ModeDecisionAuthority
    quality_criteria: List[str]
    transition_triggers: List[TransitionTrigger]
    custom_instructions: str


# PC2: Skill Spec
class AlternativeTechnique(BaseModel):
    technique: str
    use_when: str
    tradeoff: str


class SkillTechniqueStack(BaseModel):
    primary: str
    alternatives: List[AlternativeTechnique]
    combination: str


class SkillInputs(BaseModel):
    required: List[str]
    optional: List[str]


class SkillCostProfile(BaseModel):
    tokens: str
    latency: str
    when_to_skip: str


class SkillSpec(BaseModel):
    skill: str
    purpose: str
    technique_stack: SkillTechniqueStack
    inputs: SkillInputs
    procedure: Dict[int, str]
    outputs: List[str]
    quality_check: str
    when_to_use: List[str]
    when_not_to_use: List[str]
    cost_profile: SkillCostProfile


# PC3: Workflow Spec
class WorkflowQualityGate(BaseModel):
    checks: List[str]
    on_failure: str  # retry, escalate, rollback


class WorkflowPhase(BaseModel):
    name: str
    mode: str
    skills: List[str]
    entry_criteria: List[str]
    steps: Dict[int, str]
    exit_criteria: List[str]
    quality_gate: WorkflowQualityGate
    artifacts_produced: List[str]


class WorkflowSpec(BaseModel):
    workflow: str
    trigger: str
    phases: List[WorkflowPhase]
    completion_criteria: List[str]
    rollback_plan: str


# PC6: Rule Spec
class RuleEnforcement(BaseModel):
    detection: str
    response: str
    severity: str


class RuleException(BaseModel):
    condition: str
    requires: str


class RuleSpec(BaseModel):
    rule: str
    constraint: str
    rationale: str
    enforcement: RuleEnforcement
    exceptions: List[RuleException]


# PC7: Context Strategy Spec
class WindowPartition(BaseModel):
    system_instructions: str
    task_context: str
    relevant_code: str
    history: str
    reserved_for_output: str


class ContentSelection(BaseModel):
    include: List[str]
    exclude: List[str]


class ContextStrategySpec(BaseModel):
    strategy: str
    applies_to: List[str]
    window_partition: WindowPartition
    content_selection: ContentSelection
    compression_pipeline: Dict[int, str]
    ordering_rules: List[str]
    refresh_policy: str
    poisoning_checks: List[str]


# Technique Spec
class TechniqueRecognition(BaseModel):
    signals: List[str]


class TechniqueResponse(BaseModel):
    decision_criteria: str
    procedure: Dict[int, str]
    success_criteria: str
    fallback: str


class TechniqueSpec(BaseModel):
    technique: str
    situation: str
    recognition: TechniqueRecognition
    response: TechniqueResponse


# Task Decomposition Pattern
class DecompositionLevel(BaseModel):
    level: str
    granularity: str
    criteria: str


class Decomposition(BaseModel):
    levels: List[DecompositionLevel]


class ValidationCheckpoint(BaseModel):
    after: str
    verify: str


class TaskDecompositionPatternSpec(BaseModel):
    pattern: str
    work_type: str
    decomposition: Decomposition
    dependency_rules: str
    parallelization: str
    estimation: str
    validation_checkpoints: List[ValidationCheckpoint]


# MCP Configuration
class McpPrivileges(BaseModel):
    filesystem: str
    network: str
    execution: str


class McpServerConfig(BaseModel):
    name: str
    purpose: str
    capabilities_used: List[str]
    privileges: McpPrivileges
    when_to_invoke: str


class McpConfigurationSpec(BaseModel):
    configuration: str
    applies_to: str
    servers: List[McpServerConfig]
    selection_logic: str
    fallback: str
    security_constraints: List[str]
