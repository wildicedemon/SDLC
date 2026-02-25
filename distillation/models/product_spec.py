"""Product specification models."""

from enum import Enum
from typing import Any, Dict, List, Optional, Union, Literal
from pydantic import Field

from .base import BaseDistillationModel, ProductCategory
from .knowledge_atom import KnowledgeAtom


class ConfidenceLevel(str, Enum):
    """Confidence level for generated specifications."""

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class ProductSpec(BaseDistillationModel):
    """Base class for all product specifications."""

    category: ProductCategory = Field(..., description="Product category")
    name: str = Field(..., description="Name of this specific product instance")
    knowledge_atoms: List[str] = Field(
        default_factory=list,
        description="IDs of knowledge atoms consumed by this product"
    )
    confidence: ConfidenceLevel = Field(..., description="Confidence in this specification")
    gaps: List[str] = Field(
        default_factory=list,
        description="What's missing from research to complete this spec"
    )
    spec_data: Dict[str, Any] = Field(
        default_factory=dict,
        description="The actual specification data (YAML structure)"
    )

    def to_yaml_dict(self) -> Dict[str, Any]:
        """Convert to YAML-serializable dictionary."""
        data = self.model_dump()
        # Ensure enum values are properly converted
        if hasattr(data.get("category"), "value"):
            data["category"] = data["category"].value
        if hasattr(data.get("confidence"), "value"):
            data["confidence"] = data["confidence"].value

        # Flatten spec_data into the main dictionary
        spec_data = data.pop("spec_data", {})
        data.update(spec_data)
        return data


class ModeSpec(ProductSpec):
    """Specification for an agent mode."""

    category: Literal[ProductCategory.MODES] = Field(default=ProductCategory.MODES)

    def __init__(self, **data):
        super().__init__(**data)
        if "mode" not in self.spec_data:
            self.spec_data["mode"] = self.name


class SkillSpec(ProductSpec):
    """Specification for an agent skill."""

    category: Literal[ProductCategory.SKILLS] = Field(default=ProductCategory.SKILLS)

    def __init__(self, **data):
        super().__init__(**data)
        if "skill" not in self.spec_data:
            self.spec_data["skill"] = self.name


class WorkflowSpec(ProductSpec):
    """Specification for a workflow."""

    category: Literal[ProductCategory.WORKFLOWS] = Field(default=ProductCategory.WORKFLOWS)

    def __init__(self, **data):
        super().__init__(**data)
        if "workflow" not in self.spec_data:
            self.spec_data["workflow"] = self.name


class PromptSpec(ProductSpec):
    """Specification for a prompt template."""

    category: Literal[ProductCategory.PROMPTS] = Field(default=ProductCategory.PROMPTS)


class RuleSpec(ProductSpec):
    """Specification for a rule/guardrail."""

    category: Literal[ProductCategory.RULES] = Field(default=ProductCategory.RULES)

    def __init__(self, **data):
        super().__init__(**data)
        if "rule" not in self.spec_data:
            self.spec_data["rule"] = self.name


class ContextStrategySpec(ProductSpec):
    """Specification for a context management strategy."""

    category: Literal[ProductCategory.CONTEXT_STRATEGIES] = Field(default=ProductCategory.CONTEXT_STRATEGIES)

    def __init__(self, **data):
        super().__init__(**data)
        if "strategy" not in self.spec_data:
            self.spec_data["strategy"] = self.name


class TaskDecompositionPatternSpec(ProductSpec):
    """Specification for a task decomposition pattern."""

    category: Literal[ProductCategory.TASK_DECOMPOSITION_PATTERNS] = Field(default=ProductCategory.TASK_DECOMPOSITION_PATTERNS)

    def __init__(self, **data):
        super().__init__(**data)
        if "pattern" not in self.spec_data:
            self.spec_data["pattern"] = self.name


class MCPConfigurationSpec(ProductSpec):
    """Specification for MCP server configuration."""

    category: Literal[ProductCategory.MCP_CONFIGURATIONS] = Field(default=ProductCategory.MCP_CONFIGURATIONS)

    def __init__(self, **data):
        super().__init__(**data)
        if "configuration" not in self.spec_data:
            self.spec_data["configuration"] = self.name


class TechniqueSpec(ProductSpec):
    """Specification for a technique/strategy."""

    category: Literal[ProductCategory.TECHNIQUES_STRATEGIES] = Field(default=ProductCategory.TECHNIQUES_STRATEGIES)

    def __init__(self, **data):
        super().__init__(**data)
        if "technique" not in self.spec_data:
            self.spec_data["technique"] = self.name


class WorkspaceManagementSpec(ProductSpec):
    """Specification for workspace management practices."""

    category: Literal[ProductCategory.WORKSPACE_MANAGEMENT] = Field(default=ProductCategory.WORKSPACE_MANAGEMENT)