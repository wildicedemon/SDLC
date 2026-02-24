"""Knowledge atom data models."""

from typing import List, Optional
from pydantic import Field

from .base import (
    AtomType,
    BaseDistillationModel,
    Domain,
    EvidenceStrength,
    ProductCategory,
    SDLCPhase,
)


class KnowledgeAtom(BaseDistillationModel):
    """A single, self-contained piece of actionable knowledge."""

    id: str = Field(..., description="Unique identifier for this knowledge atom")
    type: AtomType = Field(..., description="Type of knowledge atom")
    content: str = Field(..., description="The actual knowledge content (1-5 sentences max)")
    evidence_strength: EvidenceStrength = Field(..., description="Strength of evidence supporting this atom")

    source: List[str] = Field(
        default_factory=list,
        description="Research file path(s) where this was found"
    )

    domains: List[Domain] = Field(
        default_factory=list,
        description="Technical domains this applies to"
    )

    sdlc_phases: List[SDLCPhase] = Field(
        default_factory=list,
        description="SDLC phases this applies to"
    )

    products: List[ProductCategory] = Field(
        default_factory=list,
        description="Product types this feeds"
    )

    def __str__(self) -> str:
        """String representation of the knowledge atom."""
        return f"{self.id} | {self.type} | {self.content} | {self.evidence_strength}"

    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return self.model_dump()

    @classmethod
    def from_dict(cls, data: dict) -> "KnowledgeAtom":
        """Create from dictionary representation."""
        return cls(**data)