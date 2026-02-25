"""Domain mapping processor for organizing knowledge atoms by technical domains."""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass

from ..models import (
    Domain,
    KnowledgeAtom,
    AtomType,
    EvidenceStrength,
)


@dataclass
class DomainMappingRule:
    """Rule for mapping atoms to domains based on content patterns."""

    domain: Domain
    keywords: List[str]
    atom_types: List[AtomType]
    priority: int = 1
    enabled: bool = True

    def matches(self, atom: KnowledgeAtom) -> bool:
        """Check if this rule matches the given atom."""
        if atom.type not in self.atom_types:
            return False

        content_lower = atom.content.lower()
        return any(keyword.lower() in content_lower for keyword in self.keywords)


@dataclass
class DomainSpec:
    """Specification for a technical domain."""

    domain: Domain
    name: str
    description: str
    key_concerns: List[str]
    cross_domain_links: Dict[Domain, str]  # domain -> relationship description


class DomainMapper:
    """Maps knowledge atoms to technical domains and manages domain relationships."""

    def __init__(self):
        """Initialize the domain mapper with all domain specifications and mapping rules."""
        self.domain_specs = self._load_domain_specs()
        self.mapping_rules = self._load_mapping_rules()

    def _load_domain_specs(self) -> Dict[Domain, DomainSpec]:
        """Load specifications for all 12 technical domains."""
        return {
            Domain.AGENT_ARCHITECTURE: DomainSpec(
                domain=Domain.AGENT_ARCHITECTURE,
                name="Agent Architecture & Orchestration",
                description="What agents are, how they're structured, how they coordinate, how they're specialized.",
                key_concerns=[
                    "Agent design patterns (hierarchical, swarm, debate, MoA)",
                    "Mode definitions and mode switching",
                    "Agent lifecycle states and state machines",
                    "Trust scoring, performance scoring, consensus mechanisms",
                    "Delegation patterns and handoff protocols",
                    "Deadlock/livelock detection and recovery"
                ],
                cross_domain_links={
                    Domain.TASK_MANAGEMENT: "Agent orchestration depends on task decomposition",
                    Domain.CONTEXT_ENGINEERING: "Agent modes require specific context strategies",
                    Domain.SECURITY_GUARDRAILS: "Agent trust scoring prevents adversarial behavior"
                }
            ),

            Domain.TASK_MANAGEMENT: DomainSpec(
                domain=Domain.TASK_MANAGEMENT,
                name="Task Management & Decomposition",
                description="How work is broken down, sequenced, tracked, and validated.",
                key_concerns=[
                    "Task decomposition hierarchies (initiative → phase → task → atomic action)",
                    "Dependency detection and resolution",
                    "Parallelization strategies",
                    "Commit generation and branch management",
                    "Conflict resolution for concurrent agent work",
                    "Work tree lifecycle management"
                ],
                cross_domain_links={
                    Domain.AGENT_ARCHITECTURE: "Task management requires agent coordination",
                    Domain.WORKSPACE_MANAGEMENT: "Task execution requires workspace organization",
                    Domain.SELF_IMPROVEMENT: "Task performance enables optimization loops"
                }
            ),

            Domain.CONTEXT_ENGINEERING: DomainSpec(
                domain=Domain.CONTEXT_ENGINEERING,
                name="Context & Prompt Engineering",
                description="How agents receive information and how that information is managed.",
                key_concerns=[
                    "Context window optimization and partitioning",
                    "Compression techniques (ranked by ratio vs. quality)",
                    "Prompt structure and ordering (attention research)",
                    "Anti-hallucination prompt patterns",
                    "Context poisoning detection",
                    "Token budget management",
                    "Context refresh and rotation for long tasks"
                ],
                cross_domain_links={
                    Domain.AGENT_ARCHITECTURE: "Context strategies are mode-specific",
                    Domain.CODE_INTELLIGENCE: "Code context requires specialized compression",
                    Domain.SECURITY_GUARDRAILS: "Context poisoning requires detection mechanisms"
                }
            ),

            Domain.MEMORY_SYSTEMS: DomainSpec(
                domain=Domain.MEMORY_SYSTEMS,
                name="Memory & Knowledge Systems",
                description="How agents store, retrieve, and learn from information across sessions.",
                key_concerns=[
                    "Short-term working memory",
                    "Persistent memory architecture",
                    "Vector DB strategies",
                    "Knowledge graphs",
                    "Auto-learning systems",
                    "Cross-session retrieval"
                ],
                cross_domain_links={
                    Domain.CONTEXT_ENGINEERING: "Memory systems provide context history",
                    Domain.CODE_INTELLIGENCE: "Code knowledge requires specialized indexing",
                    Domain.SELF_IMPROVEMENT: "Learning systems enable adaptation"
                }
            ),

            Domain.CODE_INTELLIGENCE: DomainSpec(
                domain=Domain.CODE_INTELLIGENCE,
                name="Code Intelligence & Representations",
                description="How agents understand, navigate, and analyze code.",
                key_concerns=[
                    "Code representations (AST, CFG, DFG, CPG, SSA)",
                    "Symbol indexing and code search",
                    "Semantic diffing",
                    "Taint tracking",
                    "Schema inference",
                    "Repo grokking / full code graph systems",
                    "Tool evaluations (Tree-sitter, Sourcegraph, CodeQL, Semgrep, Joern)"
                ],
                cross_domain_links={
                    Domain.CONTEXT_ENGINEERING: "Code context requires intelligence tools",
                    Domain.SECURITY_GUARDRAILS: "Code analysis enables security scanning",
                    Domain.TESTING_VALIDATION: "Code understanding enables test generation"
                }
            ),

            Domain.TESTING_VALIDATION: DomainSpec(
                domain=Domain.TESTING_VALIDATION,
                name="Testing & Validation",
                description="How agents verify their own work and the quality of generated code.",
                key_concerns=[
                    "Test generation techniques (unit, integration, E2E)",
                    "Mutation testing for AI-generated tests",
                    "Quality gates and validation pipelines",
                    "Behavioral testing and property-based testing",
                    "Multi-stage verification workflows",
                    "Happy/sad path validation"
                ],
                cross_domain_links={
                    Domain.CODE_INTELLIGENCE: "Testing requires code analysis",
                    Domain.SECURITY_GUARDRAILS: "Validation includes security checks",
                    Domain.SELF_IMPROVEMENT: "Test results enable quality improvement"
                }
            ),

            Domain.SECURITY_GUARDRAILS: DomainSpec(
                domain=Domain.SECURITY_GUARDRAILS,
                name="Security & Guardrails",
                description="How the system protects against adversarial inputs, hallucinations, and unsafe outputs.",
                key_concerns=[
                    "Prompt injection defense",
                    "Hallucination detection and prevention (rates, techniques)",
                    "Package verification (slopsquatting)",
                    "Sandboxing and isolation",
                    "MCP privilege isolation",
                    "Context poisoning attack vectors and defense",
                    "Secret management"
                ],
                cross_domain_links={
                    Domain.CONTEXT_ENGINEERING: "Security requires context validation",
                    Domain.AGENT_ARCHITECTURE: "Guardrails constrain agent behavior",
                    Domain.CODE_INTELLIGENCE: "Security scanning requires code analysis"
                }
            ),

            Domain.MODEL_MANAGEMENT: DomainSpec(
                domain=Domain.MODEL_MANAGEMENT,
                name="Model Management & Routing",
                description="How the system selects, switches, and optimizes model usage.",
                key_concerns=[
                    "Model capability matrices",
                    "Confidence-based routing",
                    "Cost-aware model selection",
                    "Temperature optimization",
                    "Fallback strategies",
                    "Multi-model adversarial review",
                    "Hallucination profiling per model"
                ],
                cross_domain_links={
                    Domain.AGENT_ARCHITECTURE: "Model routing enables agent specialization",
                    Domain.SECURITY_GUARDRAILS: "Model selection affects security properties",
                    Domain.SELF_IMPROVEMENT: "Model performance enables optimization"
                }
            ),

            Domain.CI_CD_DEVOPS: DomainSpec(
                domain=Domain.CI_CD_DEVOPS,
                name="CI/CD & DevOps",
                description="How the system integrates with build, deploy, and operations infrastructure.",
                key_concerns=[
                    "Self-healing pipelines",
                    "Canary/blue-green deployments",
                    "Pipeline optimization",
                    "Container orchestration for agents",
                    "Observability integration"
                ],
                cross_domain_links={
                    Domain.WORKSPACE_MANAGEMENT: "CI/CD requires workspace organization",
                    Domain.TESTING_VALIDATION: "Pipelines include automated testing",
                    Domain.SECURITY_GUARDRAILS: "DevOps includes security scanning"
                }
            ),

            Domain.WORKSPACE_MANAGEMENT: DomainSpec(
                domain=Domain.WORKSPACE_MANAGEMENT,
                name="Workspace & Infrastructure Management",
                description="How agents organize files, branches, environments, and resources.",
                key_concerns=[
                    "Branch strategies for multi-agent work",
                    "Work tree management",
                    "File organization during task execution",
                    "State persistence",
                    "Artifact management",
                    "Cleanup protocols",
                    "Environment provisioning"
                ],
                cross_domain_links={
                    Domain.TASK_MANAGEMENT: "Workspace management supports task execution",
                    Domain.CI_CD_DEVOPS: "Infrastructure management enables deployment",
                    Domain.AGENT_ARCHITECTURE: "Workspace organization affects agent coordination"
                }
            ),

            Domain.HUMAN_INTERACTION: DomainSpec(
                domain=Domain.HUMAN_INTERACTION,
                name="Human Interaction",
                description="How agents collaborate with humans.",
                key_concerns=[
                    "Escalation triggers and thresholds",
                    "Approval gateways",
                    "Confidence-based handoff criteria",
                    "Explainable plan visualization",
                    "Notification systems"
                ],
                cross_domain_links={
                    Domain.AGENT_ARCHITECTURE: "Human interaction requires agent communication",
                    Domain.SECURITY_GUARDRAILS: "Human approval prevents automated risks",
                    Domain.SELF_IMPROVEMENT: "Human feedback enables learning"
                }
            ),

            Domain.SELF_IMPROVEMENT: DomainSpec(
                domain=Domain.SELF_IMPROVEMENT,
                name="Self-Improvement & Optimization",
                description="How the system improves its own performance over time.",
                key_concerns=[
                    "Prompt optimization loops",
                    "Agent performance regression detection",
                    "Workflow A/B testing",
                    "Cost optimization feedback",
                    "Skill enable/disable for token efficiency"
                ],
                cross_domain_links={
                    Domain.AGENT_ARCHITECTURE: "Self-improvement requires agent introspection",
                    Domain.MODEL_MANAGEMENT: "Optimization affects model selection",
                    Domain.TASK_MANAGEMENT: "Performance metrics enable task optimization"
                }
            ),
        }

    def _load_mapping_rules(self) -> List[DomainMappingRule]:
        """Load rules for mapping atoms to domains based on content analysis."""
        return [
            # Agent Architecture rules
            DomainMappingRule(
                domain=Domain.AGENT_ARCHITECTURE,
                keywords=["agent", "orchestration", "coordination", "specialization", "mode", "trust scoring", "consensus", "delegation", "handoff", "deadlock", "livelock"],
                atom_types=[AtomType.TECHNIQUE, AtomType.CONSTRAINT, AtomType.FAILURE_MODE, AtomType.RECIPE],
                priority=10
            ),

            # Task Management rules
            DomainMappingRule(
                domain=Domain.TASK_MANAGEMENT,
                keywords=["task", "decomposition", "dependency", "parallelization", "commit", "branch", "conflict", "resolution", "work tree", "lifecycle"],
                atom_types=[AtomType.TECHNIQUE, AtomType.CONSTRAINT, AtomType.FAILURE_MODE, AtomType.RECIPE],
                priority=9
            ),

            # Context Engineering rules
            DomainMappingRule(
                domain=Domain.CONTEXT_ENGINEERING,
                keywords=["context", "window", "compression", "prompt", "attention", "hallucination", "poisoning", "token", "budget", "refresh", "rotation"],
                atom_types=[AtomType.TECHNIQUE, AtomType.METRIC, AtomType.CONSTRAINT, AtomType.TOOL, AtomType.COMBINATION, AtomType.FAILURE_MODE],
                priority=8
            ),

            # Memory Systems rules
            DomainMappingRule(
                domain=Domain.MEMORY_SYSTEMS,
                keywords=["memory", "persistent", "vector", "database", "knowledge", "graph", "learning", "retrieval", "session"],
                atom_types=[AtomType.TECHNIQUE, AtomType.TOOL, AtomType.CONSTRAINT, AtomType.COMBINATION],
                priority=7
            ),

            # Code Intelligence rules
            DomainMappingRule(
                domain=Domain.CODE_INTELLIGENCE,
                keywords=["ast", "cfg", "dfg", "cpg", "ssa", "symbol", "indexing", "semantic", "diffing", "taint", "tracking", "schema", "inference", "repo", "grokking", "tree-sitter", "sourcegraph", "codeql", "semgrep", "joern"],
                atom_types=[AtomType.TECHNIQUE, AtomType.TOOL, AtomType.METRIC, AtomType.COMBINATION, AtomType.RECIPE],
                priority=9
            ),

            # Testing & Validation rules
            DomainMappingRule(
                domain=Domain.TESTING_VALIDATION,
                keywords=["test", "validation", "generation", "mutation", "quality", "gate", "behavioral", "property", "verification", "happy", "sad", "path"],
                atom_types=[AtomType.TECHNIQUE, AtomType.METRIC, AtomType.CONSTRAINT, AtomType.RECIPE, AtomType.COMBINATION],
                priority=8
            ),

            # Security & Guardrails rules
            DomainMappingRule(
                domain=Domain.SECURITY_GUARDRAILS,
                keywords=["security", "guardrail", "injection", "hallucination", "package", "verification", "slopsquatting", "sandboxing", "isolation", "privilege", "poisoning", "attack", "secret", "management"],
                atom_types=[AtomType.TECHNIQUE, AtomType.CONSTRAINT, AtomType.FAILURE_MODE, AtomType.TOOL, AtomType.ANTI_PATTERN],
                priority=10
            ),

            # Model Management rules
            DomainMappingRule(
                domain=Domain.MODEL_MANAGEMENT,
                keywords=["model", "routing", "capability", "matrix", "confidence", "cost", "temperature", "fallback", "adversarial", "review", "profiling"],
                atom_types=[AtomType.TECHNIQUE, AtomType.METRIC, AtomType.CONSTRAINT, AtomType.TRADEOFF, AtomType.COMBINATION],
                priority=7
            ),

            # CI/CD & DevOps rules
            DomainMappingRule(
                domain=Domain.CI_CD_DEVOPS,
                keywords=["ci/cd", "devops", "pipeline", "canary", "blue-green", "deployment", "container", "orchestration", "observability", "self-healing"],
                atom_types=[AtomType.TECHNIQUE, AtomType.TOOL, AtomType.RECIPE, AtomType.CONSTRAINT],
                priority=6
            ),

            # Workspace Management rules
            DomainMappingRule(
                domain=Domain.WORKSPACE_MANAGEMENT,
                keywords=["workspace", "branch", "strategy", "work tree", "file", "organization", "state", "persistence", "artifact", "cleanup", "environment", "provisioning"],
                atom_types=[AtomType.TECHNIQUE, AtomType.CONSTRAINT, AtomType.RECIPE, AtomType.FAILURE_MODE],
                priority=7
            ),

            # Human Interaction rules
            DomainMappingRule(
                domain=Domain.HUMAN_INTERACTION,
                keywords=["human", "interaction", "escalation", "approval", "handoff", "explainable", "visualization", "notification", "collaboration"],
                atom_types=[AtomType.TECHNIQUE, AtomType.CONSTRAINT, AtomType.METRIC, AtomType.RECIPE],
                priority=6
            ),

            # Self-Improvement rules
            DomainMappingRule(
                domain=Domain.SELF_IMPROVEMENT,
                keywords=["improvement", "optimization", "regression", "detection", "a/b", "testing", "feedback", "learning", "adaptation", "performance"],
                atom_types=[AtomType.TECHNIQUE, AtomType.METRIC, AtomType.CONSTRAINT, AtomType.RECIPE, AtomType.COMBINATION],
                priority=8
            ),
        ]

    def map_atoms_to_domains(self, atoms: List[KnowledgeAtom]) -> Dict[Domain, List[KnowledgeAtom]]:
        """Map knowledge atoms to their relevant technical domains.

        Args:
            atoms: List of knowledge atoms to map.

        Returns:
            Dictionary mapping domains to lists of atoms assigned to each domain.
        """
        domain_atoms: Dict[Domain, List[KnowledgeAtom]] = {
            domain: [] for domain in Domain
        }

        for atom in atoms:
            # Reset domains for this atom
            atom.domains = []

            # Apply mapping rules in priority order
            matched_domains = set()
            for rule in sorted(self.mapping_rules, key=lambda r: r.priority, reverse=True):
                if rule.enabled and rule.matches(atom):
                    if rule.domain not in matched_domains:
                        matched_domains.add(rule.domain)
                        atom.domains.append(rule.domain)
                        domain_atoms[rule.domain].append(atom)

            # If no domains matched, assign to a default catch-all
            if not atom.domains:
                # Use content analysis to find best fit
                best_domain = self._find_best_domain_fit(atom)
                if best_domain:
                    atom.domains.append(best_domain)
                    domain_atoms[best_domain].append(atom)

        return domain_atoms

    def _find_best_domain_fit(self, atom: KnowledgeAtom) -> Optional[Domain]:
        """Find the best domain fit for an atom that didn't match any rules."""
        content_lower = atom.content.lower()

        # Simple keyword-based fallback mapping
        domain_keywords = {
            Domain.AGENT_ARCHITECTURE: ["agent", "orchestrate", "coordinate"],
            Domain.TASK_MANAGEMENT: ["task", "decompose", "dependency"],
            Domain.CONTEXT_ENGINEERING: ["context", "prompt", "token"],
            Domain.CODE_INTELLIGENCE: ["code", "ast", "parse", "analyze"],
            Domain.SECURITY_GUARDRAILS: ["security", "safe", "protect", "guard"],
            Domain.TESTING_VALIDATION: ["test", "validate", "verify"],
        }

        best_score = 0
        best_domain = None

        for domain, keywords in domain_keywords.items():
            score = sum(1 for keyword in keywords if keyword in content_lower)
            if score > best_score:
                best_score = score
                best_domain = domain

        return best_domain if best_score > 0 else None

    def rank_atoms_in_domains(self, domain_atoms: Dict[Domain, List[KnowledgeAtom]]) -> Dict[Domain, List[KnowledgeAtom]]:
        """Rank atoms within each domain by evidence strength and relevance.

        Args:
            domain_atoms: Dictionary mapping domains to their atoms.

        Returns:
            Dictionary with atoms ranked within each domain.
        """
        ranked_domains = {}

        for domain, atoms in domain_atoms.items():
            if not atoms:
                ranked_domains[domain] = []
                continue

            # Sort by evidence strength (STRONG > MODERATE > WEAK), then by type priority
            type_priority = {
                AtomType.CONSTRAINT: 10,
                AtomType.FAILURE_MODE: 9,
                AtomType.TECHNIQUE: 8,
                AtomType.METRIC: 7,
                AtomType.TOOL: 6,
                AtomType.COMBINATION: 5,
                AtomType.RECIPE: 4,
                AtomType.ANTI_PATTERN: 3,
                AtomType.TRADEOFF: 2,
            }

            def sort_key(atom: KnowledgeAtom) -> tuple:
                strength_order = {"STRONG": 3, "MODERATE": 2, "WEAK": 1}
                return (
                    strength_order.get(atom.evidence_strength, 0),
                    type_priority.get(atom.type, 0),
                    -len(atom.content)  # Prefer more detailed content
                )

            ranked_atoms = sorted(atoms, key=sort_key, reverse=True)
            ranked_domains[domain] = ranked_atoms

        return ranked_domains

    def identify_cross_domain_links(self, domain_atoms: Dict[Domain, List[KnowledgeAtom]]) -> Dict[Domain, Dict[Domain, List[KnowledgeAtom]]]:
        """Identify atoms that are relevant to multiple domains.

        Args:
            domain_atoms: Dictionary mapping domains to their atoms.

        Returns:
            Dictionary mapping source domains to target domains with shared atoms.
        """
        cross_links: Dict[Domain, Dict[Domain, List[KnowledgeAtom]]] = {}

        # Get all atoms and their domain assignments
        all_atoms = []
        for atoms in domain_atoms.values():
            all_atoms.extend(atoms)

        for atom in all_atoms:
            if len(atom.domains) > 1:
                # This atom belongs to multiple domains
                for source_domain in atom.domains:
                    if source_domain not in cross_links:
                        cross_links[source_domain] = {}

                    for target_domain in atom.domains:
                        if target_domain != source_domain:
                            if target_domain not in cross_links[source_domain]:
                                cross_links[source_domain][target_domain] = []
                            cross_links[source_domain][target_domain].append(atom)

        return cross_links

    def generate_gap_report(self, domain_atoms: Dict[Domain, List[KnowledgeAtom]]) -> Dict[Domain, Dict[str, any]]:
        """Generate gap analysis report for each domain.

        Args:
            domain_atoms: Dictionary mapping domains to their atoms.

        Returns:
            Gap analysis report with coverage assessment and missing areas.
        """
        gap_report = {}

        for domain in Domain:
            atoms = domain_atoms.get(domain, [])
            domain_spec = self.domain_specs[domain]

            # Analyze coverage by atom type
            type_coverage = {}
            for atom_type in AtomType:
                type_atoms = [a for a in atoms if a.type == atom_type]
                type_coverage[atom_type] = {
                    "count": len(type_atoms),
                    "strong_evidence": len([a for a in type_atoms if a.evidence_strength == "STRONG"]),
                    "moderate_evidence": len([a for a in type_atoms if a.evidence_strength == "MODERATE"]),
                    "weak_evidence": len([a for a in type_atoms if a.evidence_strength == "WEAK"]),
                }

            # Identify key concern coverage
            concern_coverage = {}
            for concern in domain_spec.key_concerns:
                # Simple keyword matching for concern coverage
                concern_lower = concern.lower()
                relevant_atoms = []
                for atom in atoms:
                    atom_content_lower = atom.content.lower()
                    # Check if concern keywords appear in atom content
                    concern_keywords = concern_lower.split()
                    if any(keyword in atom_content_lower for keyword in concern_keywords):
                        relevant_atoms.append(atom)

                concern_coverage[concern] = {
                    "atoms_count": len(relevant_atoms),
                    "has_strong_evidence": any(a.evidence_strength == "STRONG" for a in relevant_atoms),
                    "sample_atoms": [a.id for a in relevant_atoms[:3]]  # First 3 atom IDs
                }

            # Calculate overall coverage score
            total_atoms = len(atoms)
            strong_atoms = len([a for a in atoms if a.evidence_strength == "STRONG"])
            coverage_score = strong_atoms / max(total_atoms, 1)  # Avoid division by zero

            gap_report[domain] = {
                "total_atoms": total_atoms,
                "strong_evidence_atoms": strong_atoms,
                "coverage_score": coverage_score,
                "type_coverage": type_coverage,
                "concern_coverage": concern_coverage,
                "gaps": self._identify_domain_gaps(domain, atoms, domain_spec)
            }

        return gap_report

    def _identify_domain_gaps(self, domain: Domain, atoms: List[KnowledgeAtom], domain_spec: DomainSpec) -> List[str]:
        """Identify gaps in domain coverage."""
        gaps = []

        # Check for missing atom types
        present_types = set(atom.type for atom in atoms)
        missing_types = set(AtomType) - present_types
        if missing_types:
            gaps.append(f"Missing atom types: {', '.join(t.value for t in missing_types)}")

        # Check for low evidence strength
        weak_atoms = [a for a in atoms if a.evidence_strength == "WEAK"]
        if len(weak_atoms) > len(atoms) * 0.5:  # More than 50% weak evidence
            gaps.append("High proportion of weak evidence atoms - needs stronger research backing")

        # Check concern coverage
        poorly_covered_concerns = []
        for concern in domain_spec.key_concerns:
            concern_atoms = []
            concern_lower = concern.lower()
            for atom in atoms:
                atom_content_lower = atom.content.lower()
                concern_keywords = concern_lower.split()
                if any(keyword in atom_content_lower for keyword in concern_keywords):
                    concern_atoms.append(atom)

            if len(concern_atoms) == 0:
                poorly_covered_concerns.append(concern[:50] + "..." if len(concern) > 50 else concern)

        if poorly_covered_concerns:
            gaps.append(f"Poorly covered concerns: {', '.join(poorly_covered_concerns)}")

        # Check cross-domain isolation
        multi_domain_atoms = [a for a in atoms if len(a.domains) > 1]
        if len(multi_domain_atoms) < len(atoms) * 0.1:  # Less than 10% cross-domain
            gaps.append("Low cross-domain connectivity - may indicate domain isolation")

        return gaps

    def get_domain_summary(self, domain: Domain, atoms: List[KnowledgeAtom]) -> Dict[str, any]:
        """Generate a summary report for a specific domain.

        Args:
            domain: The domain to summarize.
            atoms: Atoms assigned to this domain.

        Returns:
            Summary dictionary with key metrics and ranked atoms.
        """
        if domain not in self.domain_specs:
            return {}

        domain_spec = self.domain_specs[domain]

        # Get ranked atoms
        ranked_atoms = self.rank_atoms_in_domains({domain: atoms}).get(domain, [])

        # Group by type for summary
        atoms_by_type = {}
        for atom in ranked_atoms:
            if atom.type not in atoms_by_type:
                atoms_by_type[atom.type] = []
            atoms_by_type[atom.type].append(atom)

        return {
            "domain": domain,
            "name": domain_spec.name,
            "description": domain_spec.description,
            "total_atoms": len(atoms),
            "atoms_by_type": {k: len(v) for k, v in atoms_by_type.items()},
            "key_techniques": [
                {
                    "id": atom.id,
                    "content": atom.content[:100] + "..." if len(atom.content) > 100 else atom.content,
                    "evidence": atom.evidence_strength
                }
                for atom in ranked_atoms[:5]  # Top 5
            ],
            "cross_domain_links": domain_spec.cross_domain_links
        }