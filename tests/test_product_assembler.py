"""Tests for ProductAssembler and template system."""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch

from distillation.models import (
    KnowledgeAtom,
    AtomType,
    EvidenceStrength,
    Domain,
    ProductCategory,
    ConfidenceLevel,
    ModeSpec,
    SkillSpec,
    RuleSpec,
)
from distillation.processors.product_assembler import ProductAssembler, TemplateField, ProductTemplate


class TestTemplateField:
    """Test TemplateField functionality."""

    def test_field_creation(self):
        """Test creating a template field."""
        field = TemplateField(
            name="test_field",
            required=True,
            description="A test field",
            validation_rules=["non_empty", "min_length:5"]
        )

        assert field.name == "test_field"
        assert field.required is True
        assert field.description == "A test field"
        assert "non_empty" in field.validation_rules

    def test_validation_rules(self):
        """Test field validation rules."""
        field = TemplateField(
            name="test",
            validation_rules=["non_empty", "min_length:3", "max_length:10"]
        )

        # Should pass
        assert field._validate_rule("hello", "non_empty")
        assert field._validate_rule("hello", "min_length:3")
        assert field._validate_rule("hello", "max_length:10")

        # Should fail
        assert not field._validate_rule("", "non_empty")
        assert not field._validate_rule("hi", "min_length:3")
        assert not field._validate_rule("this_is_too_long", "max_length:10")


class TestProductTemplate:
    """Test ProductTemplate functionality."""

    def test_template_creation(self):
        """Test creating a product template."""
        fields = {
            "name": TemplateField("name", required=True, validation_rules=["non_empty"]),
            "description": TemplateField("description", validation_rules=["min_length:10"])
        }

        template = ProductTemplate(
            category=ProductCategory.MODES,
            name="Test Template",
            fields=fields,
            spec_class=ModeSpec
        )

        assert template.category == ProductCategory.MODES
        assert template.name == "Test Template"
        assert len(template.fields) == 2

    def test_spec_validation(self):
        """Test specification data validation."""
        fields = {
            "required_field": TemplateField("required_field", required=True, validation_rules=["non_empty"]),
            "optional_field": TemplateField("optional_field", validation_rules=["min_length:5"])
        }

        template = ProductTemplate(
            category=ProductCategory.MODES,
            name="Test Template",
            fields=fields,
            spec_class=ModeSpec
        )

        # Valid spec data
        valid_data = {
            "required_field": "test value",
            "optional_field": "valid"
        }
        errors = template.validate_spec_data(valid_data)
        assert len(errors) == 0

        # Invalid spec data - missing required field
        invalid_data = {"optional_field": "valid"}
        errors = template.validate_spec_data(invalid_data)
        assert len(errors) > 0
        assert "required_field" in errors[0]

        # Invalid spec data - validation rule failure
        invalid_data2 = {
            "required_field": "test",
            "optional_field": "hi"  # Too short
        }
        errors = template.validate_spec_data(invalid_data2)
        assert len(errors) > 0


class TestProductAssembler:
    """Test ProductAssembler functionality."""

    @pytest.fixture
    def sample_atoms(self):
        """Create sample knowledge atoms for testing."""
        return [
            KnowledgeAtom(
                id="KA-001",
                type=AtomType.TECHNIQUE,
                content="Tree-sitter provides incremental AST parsing for 40+ languages with error recovery",
                evidence_strength=EvidenceStrength.STRONG,
                domains=[Domain.CODE_INTELLIGENCE],
                products=[ProductCategory.SKILLS]
            ),
            KnowledgeAtom(
                id="KA-002",
                type=AtomType.METRIC,
                content="AST-based search improves precision by 60-80% over text-based methods",
                evidence_strength=EvidenceStrength.MODERATE,
                domains=[Domain.CODE_INTELLIGENCE],
                products=[ProductCategory.SKILLS]
            ),
            KnowledgeAtom(
                id="KA-003",
                type=AtomType.CONSTRAINT,
                content="Context window attention degrades 20-40% for mid-context items",
                evidence_strength=EvidenceStrength.STRONG,
                domains=[Domain.CONTEXT_ENGINEERING],
                products=[ProductCategory.CONTEXT_STRATEGIES]
            ),
            KnowledgeAtom(
                id="KA-004",
                type=AtomType.TOOL,
                content="Sourcegraph: multi-repo symbol search, sub-second queries across million-line codebases",
                evidence_strength=EvidenceStrength.STRONG,
                domains=[Domain.CODE_INTELLIGENCE],
                products=[ProductCategory.SKILLS]
            )
        ]

    @pytest.fixture
    def temp_templates_dir(self):
        """Create a temporary directory with template files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            templates_path = Path(temp_dir)

            # Create a minimal skills template
            skills_template = {
                "name": "Skills Template",
                "fields": {
                    "purpose": {
                        "required": True,
                        "validation": ["non_empty"]
                    },
                    "technique_stack": {
                        "required": True,
                        "validation": ["dict_non_empty"]
                    }
                }
            }

            import yaml
            with open(templates_path / "skills.yaml", 'w') as f:
                yaml.dump(skills_template, f)

            yield templates_path

    def test_assembler_initialization(self, temp_templates_dir):
        """Test ProductAssembler initialization."""
        assembler = ProductAssembler(templates_dir=temp_templates_dir)

        assert assembler.templates_dir == temp_templates_dir
        assert ProductCategory.SKILLS in assembler.template_registry

    def test_atom_filtering(self, sample_atoms):
        """Test filtering atoms for specific product categories."""
        assembler = ProductAssembler()

        # Test filtering for SKILLS category
        skill_atoms = assembler._filter_atoms_for_category(sample_atoms, ProductCategory.SKILLS)
        assert len(skill_atoms) == 3  # KA-001, KA-002, KA-004 have SKILLS in products

        # Test filtering for CONTEXT_STRATEGIES category
        context_atoms = assembler._filter_atoms_for_category(sample_atoms, ProductCategory.CONTEXT_STRATEGIES)
        assert len(context_atoms) == 1  # KA-003 has CONTEXT_STRATEGIES in products

    def test_confidence_calculation(self, sample_atoms):
        """Test confidence level calculation."""
        assembler = ProductAssembler()

        # Test with mixed evidence strengths
        confidence = assembler._calculate_confidence(sample_atoms)
        # 2 STRONG + 1 MODERATE + 1 MODERATE = score should be around 0.75 (MEDIUM)
        assert confidence in [ConfidenceLevel.MEDIUM, ConfidenceLevel.HIGH]

        # Test with all strong evidence
        strong_atoms = [atom for atom in sample_atoms if atom.evidence_strength == EvidenceStrength.STRONG]
        confidence = assembler._calculate_confidence(strong_atoms)
        assert confidence == ConfidenceLevel.HIGH

        # Test with weak evidence
        weak_atoms = [KnowledgeAtom(
            id="KA-005",
            type=AtomType.TECHNIQUE,
            content="Some technique",
            evidence_strength=EvidenceStrength.WEAK
        )]
        confidence = assembler._calculate_confidence(weak_atoms)
        assert confidence == ConfidenceLevel.LOW

    def test_gap_identification(self, temp_templates_dir, sample_atoms):
        """Test gap identification in specifications."""
        assembler = ProductAssembler(templates_dir=temp_templates_dir)

        template = assembler.template_registry[ProductCategory.SKILLS]
        spec_data = {"purpose": "Test purpose"}  # Missing required technique_stack

        gaps = assembler._identify_gaps(template, spec_data, sample_atoms)

        assert len(gaps) > 0
        assert any("technique_stack" in gap for gap in gaps)

    def test_spec_assembly(self, temp_templates_dir, sample_atoms):
        """Test end-to-end specification assembly."""
        assembler = ProductAssembler(templates_dir=temp_templates_dir)

        # Create a complete spec data for testing
        spec_data = {
            "purpose": "Navigate and understand code structure",
            "technique_stack": {
                "primary": "Tree-sitter AST parsing",
                "alternatives": []
            }
        }

        # Mock the _generate_spec_data method to return our test data
        with patch.object(assembler, '_generate_spec_data', return_value=spec_data):
            spec = assembler.assemble_spec(
                category=ProductCategory.SKILLS,
                name="Code Traversal Skill",
                knowledge_atoms=sample_atoms
            )

            assert isinstance(spec, SkillSpec)
            assert spec.name == "Code Traversal Skill"
            assert spec.category == ProductCategory.SKILLS
            assert len(spec.knowledge_atoms) > 0
            assert spec.confidence in [ConfidenceLevel.LOW, ConfidenceLevel.MEDIUM, ConfidenceLevel.HIGH]

    def test_spec_validation(self, temp_templates_dir):
        """Test specification validation."""
        assembler = ProductAssembler(templates_dir=temp_templates_dir)

        # Create a valid spec
        spec = SkillSpec(
            name="Test Skill",
            knowledge_atoms=["KA-001"],
            confidence=ConfidenceLevel.HIGH,
            gaps=[],
            spec_data={
                "purpose": "Test purpose",
                "technique_stack": {"primary": "test technique"}
            }
        )

        errors = assembler.validate_spec(spec)
        assert len(errors) == 0

        # Create an invalid spec (missing required field)
        invalid_spec = SkillSpec(
            name="Invalid Skill",
            knowledge_atoms=["KA-001"],
            confidence=ConfidenceLevel.HIGH,
            gaps=[],
            spec_data={
                "purpose": "Test purpose"
                # Missing technique_stack
            }
        )

        errors = assembler.validate_spec(invalid_spec)
        assert len(errors) > 0

    def test_spec_export(self, temp_templates_dir, tmp_path):
        """Test specification export to YAML."""
        assembler = ProductAssembler(templates_dir=temp_templates_dir)

        spec = SkillSpec(
            name="Test Skill",
            knowledge_atoms=["KA-001", "KA-002"],
            confidence=ConfidenceLevel.HIGH,
            gaps=["Minor gap"],
            spec_data={
                "purpose": "Test skill purpose",
                "technique_stack": {"primary": "test technique"}
            }
        )

        output_path = tmp_path / "test_skill.yaml"
        assembler.export_spec(spec, output_path)

        assert output_path.exists()

        # Verify the exported YAML contains expected content
        import yaml
        with open(output_path, 'r') as f:
            exported_data = yaml.safe_load(f)

        assert exported_data["name"] == "Test Skill"
        assert exported_data["category"] == "PC2"  # SKILLS
        assert "purpose" in exported_data
        assert exported_data["confidence"] == "HIGH"
        assert len(exported_data["gaps"]) == 1

    def test_field_value_generation(self, sample_atoms):
        """Test field value generation from atoms."""
        assembler = ProductAssembler()

        # Test purpose generation
        purpose = assembler._generate_field_value(
            "purpose", TemplateField("purpose"), sample_atoms[:1],  # TECHNIQUE atom
            {"TECHNIQUE": sample_atoms[:1]}, "Test Skill"
        )
        assert purpose is not None
        assert "Apply" in purpose

        # Test tool generation
        tools = assembler._generate_field_value(
            "tools", TemplateField("tools"), sample_atoms,  # Include TOOL atom
            {"TOOL": [sample_atoms[3]]}, "Test Skill"  # KA-004 is TOOL
        )
        assert tools is not None
        assert "enabled" in tools

        # Test constraint generation
        constraint = assembler._generate_field_value(
            "constraint", TemplateField("constraint"), sample_atoms,  # Include CONSTRAINT atom
            {"CONSTRAINT": [sample_atoms[2]]}, "Test Rule"  # KA-003 is CONSTRAINT
        )
        assert constraint is not None
        assert "Context window" in constraint