"""Product assembly processor for generating specifications from knowledge atoms."""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from dataclasses import dataclass

import yaml

from ..models import (
    ConfidenceLevel,
    Domain,
    KnowledgeAtom,
    MCPConfigurationSpec,
    ModeSpec,
    ProductCategory,
    ProductSpec,
    PromptSpec,
    RuleSpec,
    SDLCPhase,
    SkillSpec,
    TechniqueSpec,
    TaskDecompositionPatternSpec,
    WorkflowSpec,
    WorkspaceManagementSpec,
    ContextStrategySpec,
)


@dataclass
class TemplateField:
    """Represents a field in a product template."""

    name: str
    required: bool = False
    default_value: Any = None
    description: str = ""
    validation_rules: List[str] = None

    def __post_init__(self):
        if self.validation_rules is None:
            self.validation_rules = []


@dataclass
class ProductTemplate:
    """Template for generating a product specification."""

    category: ProductCategory
    name: str
    fields: Dict[str, TemplateField]
    spec_class: type[ProductSpec]

    def validate_spec_data(self, spec_data: Dict[str, Any]) -> List[str]:
        """Validate spec data against template requirements."""
        errors = []

        # Check required fields
        for field_name, field in self.fields.items():
            if field.required and field_name not in spec_data:
                if field.default_value is not None:
                    spec_data[field_name] = field.default_value
                else:
                    errors.append(f"Required field '{field_name}' is missing")

        # Apply validation rules
        for field_name, field in self.fields.items():
            if field_name in spec_data and field.validation_rules:
                value = spec_data[field_name]
                for rule in field.validation_rules:
                    if not self.validate_rule(value, rule):
                        errors.append(f"Field '{field_name}' failed validation rule: {rule}")

        return errors

    def validate_rule(self, value: Any, rule: str) -> bool:
        """Apply a validation rule to a value."""
        if rule == "non_empty":
            return bool(value)
        elif rule == "list_non_empty":
            return isinstance(value, list) and len(value) > 0
        elif rule == "dict_non_empty":
            return isinstance(value, dict) and len(value) > 0
        elif rule.startswith("min_length:"):
            min_len = int(rule.split(":")[1])
            return len(str(value)) >= min_len
        elif rule.startswith("max_length:"):
            max_len = int(rule.split(":")[1])
            return len(str(value)) <= max_len
        return True


class ProductAssembler:
    """Assembles product specifications from knowledge atoms using templates."""

    def __init__(self, templates_dir: Optional[Path] = None):
        """Initialize the product assembler.

        Args:
            templates_dir: Directory containing template files. If None, uses default.
        """
        self.templates_dir = templates_dir or Path(__file__).parent.parent / "templates"
        self.templates_dir.mkdir(exist_ok=True)

        # Initialize templates
        self.templates = self._load_templates()

        # Template registry
        self.template_registry: Dict[ProductCategory, ProductTemplate] = {}

        # Load all product templates
        self._initialize_template_registry()

    def _load_templates(self) -> Dict[str, Dict[str, Any]]:
        """Load template definitions from YAML files."""
        templates = {}

        # Define template files to load
        template_files = {
            "modes.yaml": ProductCategory.MODES,
            "skills.yaml": ProductCategory.SKILLS,
            "workflows.yaml": ProductCategory.WORKFLOWS,
            "prompts.yaml": ProductCategory.PROMPTS,
            "mcp_configurations.yaml": ProductCategory.MCP_CONFIGURATIONS,
            "rules.yaml": ProductCategory.RULES,
            "context_strategies.yaml": ProductCategory.CONTEXT_STRATEGIES,
            "task_decomposition_patterns.yaml": ProductCategory.TASK_DECOMPOSITION_PATTERNS,
            "workspace_management.yaml": ProductCategory.WORKSPACE_MANAGEMENT,
            "techniques_strategies.yaml": ProductCategory.TECHNIQUES_STRATEGIES,
        }

        for template_file, category in template_files.items():
            template_path = self.templates_dir / template_file
            if template_path.exists():
                with open(template_path, 'r', encoding='utf-8') as f:
                    template_data = yaml.safe_load(f)
                    templates[category] = template_data
            else:
                # Create default template if it doesn't exist
                templates[category] = self._create_default_template(category)

        return templates

    def _create_default_template(self, category: ProductCategory) -> Dict[str, Any]:
        """Create a default template for a product category."""
        # This will be implemented when we create the template files
        return {
            "name": f"{category.value} Template",
            "fields": {},
            "structure": {}
        }

    def _initialize_template_registry(self):
        """Initialize the template registry with ProductTemplate objects."""
        spec_class_map = {
            ProductCategory.MODES: ModeSpec,
            ProductCategory.SKILLS: SkillSpec,
            ProductCategory.WORKFLOWS: WorkflowSpec,
            ProductCategory.PROMPTS: PromptSpec,
            ProductCategory.MCP_CONFIGURATIONS: MCPConfigurationSpec,
            ProductCategory.RULES: RuleSpec,
            ProductCategory.CONTEXT_STRATEGIES: ContextStrategySpec,
            ProductCategory.TASK_DECOMPOSITION_PATTERNS: TaskDecompositionPatternSpec,
            ProductCategory.WORKSPACE_MANAGEMENT: WorkspaceManagementSpec,
            ProductCategory.TECHNIQUES_STRATEGIES: TechniqueSpec,
        }

        for category, template_data in self.templates.items():
            fields = {}

            # Parse field definitions
            for field_name, field_config in template_data.get("fields", {}).items():
                fields[field_name] = TemplateField(
                    name=field_name,
                    required=field_config.get("required", False),
                    default_value=field_config.get("default"),
                    description=field_config.get("description", ""),
                    validation_rules=field_config.get("validation", [])
                )

            self.template_registry[category] = ProductTemplate(
                category=category,
                name=template_data.get("name", f"{category} Template"),
                fields=fields,
                spec_class=spec_class_map[category]
            )

    def assemble_spec(
        self,
        category: ProductCategory,
        name: str,
        knowledge_atoms: List[KnowledgeAtom],
        **kwargs
    ) -> ProductSpec:
        """Assemble a product specification from knowledge atoms.

        Args:
            category: Product category to generate
            name: Name of the specific product instance
            knowledge_atoms: Knowledge atoms to consume
            **kwargs: Additional context for assembly

        Returns:
            ProductSpec: The assembled product specification
        """
        if category not in self.template_registry:
            raise ValueError(f"No template available for category: {category}")

        template = self.template_registry[category]

        # Extract relevant atoms for this category
        relevant_atoms = self._filter_atoms_for_category(knowledge_atoms, category)

        # Generate spec data using template
        spec_data = self._generate_spec_data(template, relevant_atoms, name, **kwargs)

        # Validate the generated spec
        validation_errors = template.validate_spec_data(spec_data)
        if validation_errors:
            # Log warnings but don't fail - specs can be incomplete
            print(f"Warning: Validation errors for {name}: {validation_errors}")

        # Calculate confidence
        confidence = self._calculate_confidence(relevant_atoms)

        # Identify gaps
        gaps = self._identify_gaps(template, spec_data, relevant_atoms)

        # Create the spec instance
        spec = template.spec_class(
            name=name,
            knowledge_atoms=[atom.id for atom in relevant_atoms],
            confidence=confidence,
            gaps=gaps,
            spec_data=spec_data
        )

        return spec

    def _filter_atoms_for_category(
        self,
        atoms: List[KnowledgeAtom],
        category: ProductCategory
    ) -> List[KnowledgeAtom]:
        """Filter knowledge atoms relevant to a specific product category."""
        relevant_atoms = []

        for atom in atoms:
            # Direct product mapping
            if category in atom.products:
                relevant_atoms.append(atom)
                continue

            # Domain-based relevance (atoms from domains that feed this product type)
            domain_to_category_map = {
                Domain.AGENT_ARCHITECTURE: [ProductCategory.MODES],
                Domain.TASK_MANAGEMENT: [ProductCategory.WORKFLOWS, ProductCategory.TASK_DECOMPOSITION_PATTERNS],
                Domain.CONTEXT_ENGINEERING: [ProductCategory.CONTEXT_STRATEGIES, ProductCategory.PROMPTS],
                Domain.MEMORY_SYSTEMS: [ProductCategory.CONTEXT_STRATEGIES],
                Domain.CODE_INTELLIGENCE: [ProductCategory.SKILLS],
                Domain.TESTING_VALIDATION: [ProductCategory.SKILLS, ProductCategory.WORKFLOWS],
                Domain.SECURITY_GUARDRAILS: [ProductCategory.RULES, ProductCategory.MCP_CONFIGURATIONS],
                Domain.MODEL_MANAGEMENT: [ProductCategory.MODES, ProductCategory.SKILLS],
                Domain.CI_CD_DEVOPS: [ProductCategory.WORKFLOWS],
                Domain.WORKSPACE_MANAGEMENT: [ProductCategory.WORKSPACE_MANAGEMENT],
                Domain.HUMAN_INTERACTION: [ProductCategory.MODES],
                Domain.SELF_IMPROVEMENT: [ProductCategory.TECHNIQUES_STRATEGIES],
            }

            relevant_categories = domain_to_category_map.get(atom.domains[0] if atom.domains else None, [])
            if category in relevant_categories:
                relevant_atoms.append(atom)

        return relevant_atoms

    def _generate_spec_data(
        self,
        template: ProductTemplate,
        atoms: List[KnowledgeAtom],
        name: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Generate specification data using the template and atoms."""
        spec_data = {}

        # Group atoms by type for easier processing
        atoms_by_type = {}
        for atom in atoms:
            if atom.type not in atoms_by_type:
                atoms_by_type[atom.type] = []
            atoms_by_type[atom.type].append(atom)

        # Generate each field based on template
        for field_name, field in template.fields.items():
            value = self._generate_field_value(field_name, field, atoms, atoms_by_type, name, **kwargs)
            if value is not None:
                spec_data[field_name] = value

        return spec_data

    def _generate_field_value(
        self,
        field_name: str,
        field: TemplateField,
        atoms: List[KnowledgeAtom],
        atoms_by_type: Dict[str, List[KnowledgeAtom]],
        name: str,
        **kwargs
    ) -> Any:
        """Generate a value for a specific template field."""
        # This is a simplified implementation - in practice, this would be much more sophisticated
        # with specific logic for each field type and product category

        if field_name == "purpose" and atoms:
            # Generate purpose from strongest TECHNIQUE atoms
            technique_atoms = atoms_by_type.get("TECHNIQUE", [])
            if technique_atoms:
                # Sort by evidence strength
                sorted_atoms = sorted(technique_atoms, key=lambda x: ["WEAK", "MODERATE", "STRONG"].index(x.evidence_strength))
                return f"Apply {sorted_atoms[-1].content[:100]}..."

        elif field_name in ["procedure", "steps", "technique_stack"]:
            # Generate procedural content from RECIPE and TECHNIQUE atoms
            recipe_atoms = atoms_by_type.get("RECIPE", [])
            technique_atoms = atoms_by_type.get("TECHNIQUE", [])

            steps = []
            for atom in recipe_atoms + technique_atoms:
                # Extract step-like content
                content = atom.content
                if "step" in content.lower() or "1." in content or "2." in content:
                    steps.append(content)

            if steps:
                return "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps[:5]))  # Limit to 5 steps

        elif field_name in ["constraint", "rationale"]:
            # Generate from CONSTRAINT and FAILURE_MODE atoms
            constraint_atoms = atoms_by_type.get("CONSTRAINT", [])
            failure_atoms = atoms_by_type.get("FAILURE_MODE", [])

            if constraint_atoms:
                return constraint_atoms[0].content
            elif failure_atoms:
                return f"Prevents: {failure_atoms[0].content}"

        elif field_name == "tools":
            # Generate from TOOL atoms
            tool_atoms = atoms_by_type.get("TOOL", [])
            if tool_atoms:
                tools = []
                for atom in tool_atoms:
                    # Extract tool name and capability
                    content = atom.content
                    if ":" in content:
                        tool_name = content.split(":")[0].strip()
                        capability = content.split(":")[1].strip()
                        tools.append({tool_name: f"Used for: {capability}"})
                return {"enabled": tools[:3]}  # Limit to 3 tools

        # For other fields, use default or return None
        return field.default_value

    def _calculate_confidence(self, atoms: List[KnowledgeAtom]) -> ConfidenceLevel:
        """Calculate confidence level for a specification based on atom evidence."""
        if not atoms:
            return ConfidenceLevel.LOW

        # Count evidence strengths
        strong_count = sum(1 for atom in atoms if atom.evidence_strength == "STRONG")
        moderate_count = sum(1 for atom in atoms if atom.evidence_strength == "MODERATE")
        weak_count = sum(1 for atom in atoms if atom.evidence_strength == "WEAK")

        total = len(atoms)

        # Calculate weighted score
        score = (strong_count * 3 + moderate_count * 2 + weak_count * 1) / (total * 3)

        if score >= 0.8:
            return ConfidenceLevel.HIGH
        elif score >= 0.5:
            return ConfidenceLevel.MEDIUM
        else:
            return ConfidenceLevel.LOW

    def _identify_gaps(
        self,
        template: ProductTemplate,
        spec_data: Dict[str, Any],
        atoms: List[KnowledgeAtom]
    ) -> List[str]:
        """Identify gaps in the specification."""
        gaps = []

        # Check for missing required fields
        for field_name, field in template.fields.items():
            if field.required and field_name not in spec_data:
                gaps.append(f"Missing required field: {field_name}")

        # Check for insufficient atom coverage
        if len(atoms) < 2:
            gaps.append("Insufficient knowledge atoms for robust specification")

        # Check for weak evidence
        weak_atoms = [atom for atom in atoms if atom.evidence_strength == "WEAK"]
        if len(weak_atoms) > len(atoms) * 0.5:
            gaps.append("Majority of supporting evidence is weak")

        return gaps

    def validate_spec(self, spec: ProductSpec) -> List[str]:
        """Validate a product specification."""
        if spec.category not in self.template_registry:
            return [f"No template available for category: {spec.category}"]

        template = self.template_registry[spec.category]
        return template.validate_spec_data(spec.spec_data)

    def export_spec(self, spec: ProductSpec, output_path: Path) -> None:
        """Export a specification to a YAML file."""
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(spec.to_yaml_dict(), f, default_flow_style=False, sort_keys=False)