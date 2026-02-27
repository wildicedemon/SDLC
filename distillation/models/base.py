"""Base models and enums for the research distillation system."""

from enum import Enum
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, ConfigDict


class EvidenceStrength(str, Enum):
    """Strength of evidence supporting a knowledge atom."""

    STRONG = "STRONG"
    MODERATE = "MODERATE"
    WEAK = "WEAK"


class AtomType(str, Enum):
    """Types of knowledge atoms that can be extracted."""

    TECHNIQUE = "TECHNIQUE"
    METRIC = "METRIC"
    CONSTRAINT = "CONSTRAINT"
    TOOL = "TOOL"
    COMBINATION = "COMBINATION"
    FAILURE_MODE = "FAILURE_MODE"
    ANTI_PATTERN = "ANTI_PATTERN"
    TRADEOFF = "TRADEOFF"
    RECIPE = "RECIPE"


class Domain(str, Enum):
    """Technical domains for organizing knowledge atoms."""

    AGENT_ARCHITECTURE = "D1"
    TASK_MANAGEMENT = "D2"
    CONTEXT_ENGINEERING = "D3"
    MEMORY_SYSTEMS = "D4"
    CODE_INTELLIGENCE = "D5"
    TESTING_VALIDATION = "D6"
    SECURITY_GUARDRAILS = "D7"
    MODEL_MANAGEMENT = "D8"
    CI_CD_DEVOPS = "D9"
    WORKSPACE_MANAGEMENT = "D10"
    HUMAN_INTERACTION = "D11"
    SELF_IMPROVEMENT = "D12"


class SDLCPhase(str, Enum):
    """Software development lifecycle phases."""

    DISCOVERY_ONBOARDING = "P1"
    PLANNING_DESIGN = "P2"
    IMPLEMENTATION = "P3"
    TESTING_VERIFICATION = "P4"
    CODE_REVIEW = "P5"
    DEBUGGING_RECOVERY = "P6"
    DEPLOYMENT_RELEASE = "P7"
    MAINTENANCE_MONITORING = "P8"


class ProductCategory(str, Enum):
    """Categories of products that can be generated."""

    MODES = "PC1"
    SKILLS = "PC2"
    WORKFLOWS = "PC3"
    PROMPTS = "PC4"
    MCP_CONFIGURATIONS = "PC5"
    RULES = "PC6"
    CONTEXT_STRATEGIES = "PC7"
    TASK_DECOMPOSITION_PATTERNS = "PC8"
    WORKSPACE_MANAGEMENT = "PC9"
    TECHNIQUES_STRATEGIES = "PC10"


class BaseDistillationModel(BaseModel):
    """Base class for all distillation models with common configuration."""

    model_config = ConfigDict(
        use_enum_values=True,
        validate_assignment=True,
        extra="forbid",
    )