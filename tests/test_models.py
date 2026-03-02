"""Tests for data models."""

import pytest
from pathlib import Path
from datetime import datetime

from distillation.models import (
    KnowledgeAtom,
    AtomType,
    EvidenceStrength,
    Domain,
    SDLCPhase,
    ProductCategory,
    ModeSpec,
    SkillSpec,
    RuleSpec,
    ResearchFile,
    ExtractionRule,
    SystemConfig,
    DistillationConfig,
)


class TestKnowledgeAtom:
    """Test KnowledgeAtom model."""

    def test_create_basic_atom(self):
        """Test creating a basic knowledge atom."""
        atom = KnowledgeAtom(
            id="KA-001",
            type=AtomType.TECHNIQUE,
            content="Tree-sitter: incremental AST parsing, 40+ languages, error recovery",
            evidence_strength=EvidenceStrength.STRONG,
            source=["research/overview.md"],
        )

        assert atom.id == "KA-001"
        assert atom.type == AtomType.TECHNIQUE
        assert "Tree-sitter" in atom.content
        assert atom.evidence_strength == EvidenceStrength.STRONG
        assert "overview.md" in atom.source[0]

    def test_atom_with_domains_and_phases(self):
        """Test atom with domain and phase assignments."""
        atom = KnowledgeAtom(
            id="KA-002",
            type=AtomType.METRIC,
            content="AST-based code search improves precision 60-80% over text-based",
            evidence_strength=EvidenceStrength.MODERATE,
            domains=[Domain.CODE_INTELLIGENCE],
            sdlc_phases=[SDLCPhase.DISCOVERY_ONBOARDING],
            products=[ProductCategory.SKILLS],
        )

        assert Domain.CODE_INTELLIGENCE in atom.domains
        assert SDLCPhase.DISCOVERY_ONBOARDING in atom.sdlc_phases
        assert ProductCategory.SKILLS in atom.products

    def test_atom_string_representation(self):
        """Test string representation of knowledge atom."""
        atom = KnowledgeAtom(
            id="KA-003",
            type=AtomType.CONSTRAINT,
            content="Context window attention degrades 20-40% for mid-context items",
            evidence_strength=EvidenceStrength.STRONG,
        )

        str_repr = str(atom)
        assert "KA-003" in str_repr
        assert "CONSTRAINT" in str_repr
        assert "20-40%" in str_repr

    def test_atom_serialization(self):
        """Test atom serialization and deserialization."""
        original = KnowledgeAtom(
            id="KA-004",
            type=AtomType.TOOL,
            content="Sourcegraph: multi-repo symbol search, sub-second queries",
            evidence_strength=EvidenceStrength.STRONG,
            source=["tools/search.md"],
        )

        # Serialize to dict
        data = original.dict()

        # Deserialize from dict
        restored = KnowledgeAtom(**data)

        assert restored.id == original.id
        assert restored.type == original.type
        assert restored.content == original.content
        assert restored.evidence_strength == original.evidence_strength


class TestProductSpecs:
    """Test product specification models."""

    def test_mode_spec_creation(self):
        """Test creating a mode specification."""
        spec = ModeSpec(
            name="CodeReviewer",
            knowledge_atoms=["KA-001", "KA-002"],
            confidence="HIGH",
            spec_data={
                "role_definition": "Reviews code for quality and security issues",
                "tools": {"enabled": ["ast_parser"], "disabled": ["code_generator"]},
            }
        )

        assert spec.category == ProductCategory.MODES
        assert spec.name == "CodeReviewer"
        assert "KA-001" in spec.knowledge_atoms
        assert spec.confidence == "HIGH"
        assert spec.spec_data["role_definition"] == "Reviews code for quality and security issues"

    def test_skill_spec_creation(self):
        """Test creating a skill specification."""
        spec = SkillSpec(
            name="CodeTraversal",
            knowledge_atoms=["KA-003", "KA-004"],
            confidence="MEDIUM",
            spec_data={
                "purpose": "Navigate and understand code structure",
                "technique_stack": {
                    "primary": "Tree-sitter AST parsing",
                    "alternatives": [{"technique": "Sourcegraph"}]
                }
            }
        )

        assert spec.category == ProductCategory.SKILLS
        assert spec.name == "CodeTraversal"
        assert spec.spec_data["purpose"] == "Navigate and understand code structure"

    def test_rule_spec_creation(self):
        """Test creating a rule specification."""
        spec = RuleSpec(
            name="ContextBoundaries",
            knowledge_atoms=["KA-005"],
            confidence="HIGH",
            spec_data={
                "constraint": "Place critical information at context window boundaries",
                "rationale": "Attention degrades 20-40% for mid-context items",
                "enforcement": {"detection": "content_position_analysis"}
            }
        )

        assert spec.category == ProductCategory.RULES
        assert spec.name == "ContextBoundaries"
        assert "critical information" in spec.spec_data["constraint"]

    def test_spec_yaml_conversion(self):
        """Test converting specs to YAML format."""
        spec = ModeSpec(
            name="TestMode",
            knowledge_atoms=["KA-001"],
            confidence="HIGH",
            spec_data={"test_field": "test_value"}
        )

        yaml_data = spec.to_yaml_dict()
        assert yaml_data["category"] == "PC1"  # MODES
        assert yaml_data["name"] == "TestMode"
        assert yaml_data["test_field"] == "test_value"


class TestResearchModels:
    """Test research processing models."""

    def test_research_file_creation(self):
        """Test creating a research file model."""
        test_path = Path("research/test.md")
        test_content = "# Test Research\n\nThis is test content."

        research_file = ResearchFile(
            path=test_path,
            content=test_content,
            format="md",
            metadata={"title": "Test Research", "author": "Test Author"},
        )

        assert research_file.path == test_path
        assert research_file.content == test_content
        assert research_file.format == "md"
        assert research_file.metadata["title"] == "Test Research"
        assert research_file.filename == "test.md"
        assert research_file.size == len(test_content)

    def test_extraction_rule_creation(self):
        """Test creating an extraction rule."""
        rule = ExtractionRule(
            name="technique_pattern",
            pattern=r"technique:\s*(.+)",
            atom_type="TECHNIQUE",
            priority=1,
            enabled=True,
        )

        assert rule.name == "technique_pattern"
        assert rule.priority == 1
        assert rule.enabled is True

        # Test pattern matching
        assert rule.matches("technique: Tree-sitter parsing")
        assert not rule.matches("This is not a technique")

    def test_extraction_rule_with_regex(self):
        """Test extraction rule with regex patterns."""
        rule = ExtractionRule(
            name="metric_pattern",
            pattern=r"(\d+(?:\.\d+)?)%\s+improvement",
            atom_type="METRIC",
        )

        assert rule.matches("AST parsing shows 35.5% improvement")
        assert rule.matches("Code search shows 60% improvement")
        assert not rule.matches("No percentage here")


class TestConfigModels:
    """Test configuration models."""

    def test_distillation_config_creation(self):
        """Test creating distillation configuration."""
        # Create temporary directories for the test
        import tempfile
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "research"
            output_dir = Path(temp_dir) / "output"
            input_dir.mkdir()
            output_dir.mkdir()

            config = DistillationConfig(
                input_dir=input_dir,
                output_dir=output_dir,
                max_file_size=10 * 1024 * 1024,  # 10MB
                supported_formats=["md", "html", "json"],
                min_evidence_strength="MODERATE",
            )

            assert config.input_dir == input_dir
            assert config.output_dir == output_dir
            assert config.max_file_size == 10 * 1024 * 1024
            assert "md" in config.supported_formats
            assert config.min_evidence_strength == "MODERATE"

    def test_distillation_config_validation(self):
        """Test distillation config validation."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "research"
            output_dir = Path(temp_dir) / "output"
            input_dir.mkdir()
            output_dir.mkdir()

            # Valid config
            config = DistillationConfig(
                input_dir=input_dir,
                output_dir=output_dir,
            )
            assert config.input_dir == input_dir

            # Invalid - non-existent input directory should raise error
            with pytest.raises(ValueError):
                DistillationConfig(
                    input_dir=Path("non_existent_dir"),
                    output_dir=output_dir,
                )

    def test_system_config_creation(self):
        """Test creating complete system configuration."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "research"
            output_dir = Path(temp_dir) / "output"
            input_dir.mkdir()
            output_dir.mkdir()

            distillation_config = DistillationConfig(
                input_dir=input_dir,
                output_dir=output_dir,
            )

            system_config = SystemConfig(
                distillation=distillation_config,
            )

            assert system_config.distillation.input_dir == input_dir
            assert system_config.extraction.context_window == 3  # default value
            assert system_config.validation.enable_schema_validation is True  # default value
            assert system_config.cli.verbose is False  # default value

    def test_system_config_yaml_roundtrip(self):
        """Test YAML serialization and deserialization."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "research"
            output_dir = Path(temp_dir) / "output"
            input_dir.mkdir()
            output_dir.mkdir()

            original_config = SystemConfig(
                distillation=DistillationConfig(
                    input_dir=input_dir,
                    output_dir=output_dir,
                )
            )

            # Serialize to YAML
            yaml_data = original_config.model_dump()

            # Deserialize from YAML
            restored_config = SystemConfig(**yaml_data)

            assert restored_config.distillation.input_dir == original_config.distillation.input_dir
            assert restored_config.distillation.output_dir == original_config.distillation.output_dir