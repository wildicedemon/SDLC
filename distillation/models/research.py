"""Research processing models."""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from pydantic import Field

from .base import BaseDistillationModel


class ResearchFile(BaseDistillationModel):
    """Represents a processed research file."""

    path: Path = Field(..., description="Path to the research file")
    content: str = Field(..., description="Raw content of the file")
    format: str = Field(..., description="File format (md, html, json, csv, etc.)")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Extracted metadata (title, author, date, etc.)"
    )
    processed_at: datetime = Field(
        default_factory=datetime.now,
        description="When this file was processed"
    )
    checksum: Optional[str] = Field(None, description="Content checksum for change detection")

    @property
    def filename(self) -> str:
        """Get the filename."""
        return self.path.name

    @property
    def size(self) -> int:
        """Get the content size."""
        return len(self.content)


class ExtractionRule(BaseDistillationModel):
    """Rule for extracting knowledge atoms."""

    name: str = Field(..., description="Rule name")
    pattern: str = Field(..., description="Regex or text pattern to match")
    atom_type: str = Field(..., description="Type of atom this rule extracts")
    priority: int = Field(default=1, description="Rule priority (higher = more important)")
    enabled: bool = Field(default=True, description="Whether this rule is active")

    def matches(self, text: str) -> bool:
        """Check if this rule matches the given text."""
        import re
        return bool(re.search(self.pattern, text, re.IGNORECASE | re.MULTILINE))


class DomainMapping(BaseDistillationModel):
    """Mapping of knowledge to domains."""

    domain: str = Field(..., description="Domain identifier")
    name: str = Field(..., description="Human-readable domain name")
    keywords: List[str] = Field(
        default_factory=list,
        description="Keywords that indicate this domain"
    )
    atom_ids: List[str] = Field(
        default_factory=list,
        description="Knowledge atom IDs in this domain"
    )

    def matches_content(self, content: str) -> bool:
        """Check if content matches this domain's keywords."""
        content_lower = content.lower()
        return any(keyword.lower() in content_lower for keyword in self.keywords)


class PhaseMapping(BaseDistillationModel):
    """Mapping of knowledge to SDLC phases."""

    phase: str = Field(..., description="Phase identifier")
    name: str = Field(..., description="Human-readable phase name")
    description: str = Field(..., description="What happens in this phase")
    keywords: List[str] = Field(
        default_factory=list,
        description="Keywords that indicate this phase"
    )
    atom_ids: List[str] = Field(
        default_factory=list,
        description="Knowledge atom IDs relevant to this phase"
    )

    def matches_content(self, content: str) -> bool:
        """Check if content matches this phase's keywords."""
        content_lower = content.lower()
        return any(keyword.lower() in content_lower for keyword in self.keywords)