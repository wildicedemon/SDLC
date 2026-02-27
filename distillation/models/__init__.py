"""Data models for the research distillation system."""

from .base import (
    AtomType,
    BaseDistillationModel,
    Domain,
    EvidenceStrength,
    ProductCategory,
    SDLCPhase,
)
from .config import (
    CLIConfig,
    DistillationConfig,
    ExtractionConfig,
    SystemConfig,
    TemplateConfig,
    ValidationConfig,
)
from .knowledge_atom import KnowledgeAtom
from .product_spec import (
    ConfidenceLevel,
    ContextStrategySpec,
    MCPConfigurationSpec,
    ModeSpec,
    ProductSpec,
    PromptSpec,
    RuleSpec,
    SkillSpec,
    TaskDecompositionPatternSpec,
    TechniqueSpec,
    WorkflowSpec,
    WorkspaceManagementSpec,
)
from .research import (
    DomainMapping,
    ExtractionRule,
    PhaseMapping,
    ResearchFile,
)

__all__ = [
    # Base models
    "AtomType",
    "BaseDistillationModel",
    "Domain",
    "EvidenceStrength",
    "ProductCategory",
    "SDLCPhase",

    # Knowledge atoms
    "KnowledgeAtom",

    # Product specs
    "ConfidenceLevel",
    "ContextStrategySpec",
    "MCPConfigurationSpec",
    "ModeSpec",
    "ProductSpec",
    "PromptSpec",
    "RuleSpec",
    "SkillSpec",
    "TaskDecompositionPatternSpec",
    "TechniqueSpec",
    "WorkflowSpec",
    "WorkspaceManagementSpec",

    # Research processing
    "DomainMapping",
    "ExtractionRule",
    "PhaseMapping",
    "ResearchFile",

    # Configuration
    "CLIConfig",
    "DistillationConfig",
    "ExtractionConfig",
    "SystemConfig",
    "TemplateConfig",
    "ValidationConfig",
]