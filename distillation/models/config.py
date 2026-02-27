"""Configuration models."""

from pathlib import Path
from typing import Dict, List, Optional, Any
from pydantic import Field, field_validator

from .base import BaseDistillationModel


class DistillationConfig(BaseDistillationModel):
    """Main configuration for the distillation system."""

    # Input/Output paths
    input_dir: Path = Field(..., description="Directory containing research files")
    output_dir: Path = Field(default=Path("output"), description="Directory for generated outputs")

    # Processing options
    max_file_size: int = Field(
        default=10 * 1024 * 1024,  # 10MB
        description="Maximum file size to process (bytes)"
    )
    supported_formats: List[str] = Field(
        default_factory=lambda: ["md", "markdown", "html", "json", "csv", "txt"],
        description="Supported file formats"
    )

    # Extraction settings
    min_evidence_strength: str = Field(
        default="MODERATE",
        description="Minimum evidence strength to extract"
    )
    deduplication_threshold: float = Field(
        default=0.85,
        description="Similarity threshold for deduplication (0-1)"
    )

    # Processing pipeline
    enable_async: bool = Field(default=True, description="Enable asynchronous processing")
    max_concurrent_files: int = Field(default=4, description="Maximum concurrent file processing")

    # Logging
    log_level: str = Field(default="INFO", description="Logging level")
    log_file: Optional[Path] = Field(None, description="Path to log file")

    @field_validator('input_dir')
    @classmethod
    def input_dir_must_exist(cls, v):
        """Validate that input directory exists."""
        if not v.exists():
            raise ValueError(f"Input directory does not exist: {v}")
        if not v.is_dir():
            raise ValueError(f"Input path is not a directory: {v}")
        return v

    @field_validator('output_dir')
    @classmethod
    def output_dir_is_created(cls, v):
        """Ensure output directory can be created."""
        v.mkdir(parents=True, exist_ok=True)
        return v


class ExtractionConfig(BaseDistillationModel):
    """Configuration for the extraction process."""

    rules_file: Optional[Path] = Field(None, description="Path to custom extraction rules")
    custom_patterns: Dict[str, str] = Field(
        default_factory=dict,
        description="Custom regex patterns for atom types"
    )
    context_window: int = Field(
        default=3,
        description="Number of sentences before/after to include as context"
    )
    min_content_length: int = Field(
        default=10,
        description="Minimum content length for extraction"
    )
    max_content_length: int = Field(
        default=1000,
        description="Maximum content length for extraction"
    )


class TemplateConfig(BaseDistillationModel):
    """Configuration for template processing."""

    template_dir: Path = Field(
        default=Path("distillation/templates"),
        description="Directory containing YAML templates"
    )
    custom_templates: Dict[str, Path] = Field(
        default_factory=dict,
        description="Custom template paths by product type"
    )

    @field_validator('template_dir')
    @classmethod
    def template_dir_validation(cls, v):
        """Validate template directory."""
        if v.exists() and not v.is_dir():
            raise ValueError(f"Template path is not a directory: {v}")
        return v


class ValidationConfig(BaseDistillationModel):
    """Configuration for validation and quality checks."""

    enable_schema_validation: bool = Field(
        default=True,
        description="Enable JSON schema validation for specs"
    )
    enable_cross_reference_check: bool = Field(
        default=True,
        description="Enable cross-reference validation"
    )
    enable_gap_analysis: bool = Field(
        default=True,
        description="Enable gap analysis reporting"
    )
    min_confidence_threshold: str = Field(
        default="LOW",
        description="Minimum confidence level to accept"
    )


class CLIConfig(BaseDistillationModel):
    """Configuration for CLI interface."""

    verbose: bool = Field(default=False, description="Enable verbose output")
    quiet: bool = Field(default=False, description="Suppress non-error output")
    progress_bar: bool = Field(default=True, description="Show progress bars")
    color_output: bool = Field(default=True, description="Enable colored output")


class SystemConfig(BaseDistillationModel):
    """Complete system configuration."""

    distillation: DistillationConfig = Field(..., description="Core distillation settings")
    extraction: ExtractionConfig = Field(default_factory=ExtractionConfig, description="Extraction settings")
    templates: TemplateConfig = Field(default_factory=TemplateConfig, description="Template settings")
    validation: ValidationConfig = Field(default_factory=ValidationConfig, description="Validation settings")
    cli: CLIConfig = Field(default_factory=CLIConfig, description="CLI settings")

    @classmethod
    def from_yaml(cls, path: Path) -> "SystemConfig":
        """Load configuration from YAML file."""
        import yaml
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls(**data)

    def to_yaml(self, path: Path) -> None:
        """Save configuration to YAML file."""
        import yaml
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(self.model_dump(), f, default_flow_style=False, sort_keys=False)