"""SDLC Phase assignment processor for mapping knowledge atoms to development lifecycle phases."""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass

from ..models import (
    SDLCPhase,
    KnowledgeAtom,
    AtomType,
    Domain,
)


@dataclass
class PhaseAssignmentRule:
    """Rule for assigning atoms to SDLC phases based on content and domain."""

    phase: SDLCPhase
    keywords: List[str]
    domains: List[Domain]
    atom_types: List[AtomType]
    priority: int = 1
    enabled: bool = True

    def matches(self, atom: KnowledgeAtom) -> bool:
        """Check if this rule matches the given atom."""
        # Check atom type
        if atom.type not in self.atom_types:
            return False

        # Check domain overlap
        if self.domains and not any(domain in atom.domains for domain in self.domains):
            return False

        # Check content keywords
        content_lower = atom.content.lower()
        return any(keyword.lower() in content_lower for keyword in self.keywords)


@dataclass
class PhaseSpec:
    """Specification for an SDLC phase."""

    phase: SDLCPhase
    name: str
    description: str
    what_agent_is_doing: str
    key_activities: List[str]
    transitions: Dict[str, str]  # condition -> next_phase description


class PhaseAssigner:
    """Assigns knowledge atoms to SDLC phases and manages phase relationships."""

    def __init__(self):
        """Initialize the phase assigner with all phase specifications and assignment rules."""
        self.phase_specs = self._load_phase_specs()
        self.assignment_rules = self._load_assignment_rules()

    def _load_phase_specs(self) -> Dict[SDLCPhase, PhaseSpec]:
        """Load specifications for all 8 SDLC phases."""
        return {
            SDLCPhase.DISCOVERY_ONBOARDING: PhaseSpec(
                phase=SDLCPhase.DISCOVERY_ONBOARDING,
                name="Discovery & Onboarding",
                description="The agent is encountering a new or unfamiliar codebase.",
                what_agent_is_doing="Analyzing and understanding the codebase structure, dependencies, and patterns.",
                key_activities=[
                    "Codebase scanning and repo grokking",
                    "Dependency mapping",
                    "Architecture extraction",
                    "API surface discovery",
                    "Entrypoint and endpoint mapping",
                    "Pattern recognition in existing code",
                    "Gap analysis between current and desired state"
                ],
                transitions={
                    "sufficient_understanding": "Move to P2 when codebase structure is understood",
                    "major_gaps_found": "Stay in P1 and request additional context or clarification"
                }
            ),

            SDLCPhase.PLANNING_DESIGN: PhaseSpec(
                phase=SDLCPhase.PLANNING_DESIGN,
                name="Planning & Design",
                description="The agent is deciding what to build and how.",
                what_agent_is_doing="Creating implementation plans, breaking down work, and designing solutions.",
                key_activities=[
                    "Task decomposition patterns",
                    "Dependency sequencing",
                    "Architecture decision making",
                    "Specification creation",
                    "Risk assessment",
                    "Resource estimation (tokens, time, cost)",
                    "Branch strategy selection"
                ],
                transitions={
                    "plan_complete": "Move to P3 when implementation plan is finalized",
                    "unclear_requirements": "Return to P1 for additional discovery",
                    "high_risk_identified": "May require human approval before proceeding"
                }
            ),

            SDLCPhase.IMPLEMENTATION: PhaseSpec(
                phase=SDLCPhase.IMPLEMENTATION,
                name="Implementation",
                description="The agent is writing code.",
                what_agent_is_doing="Generating, modifying, and validating code according to specifications.",
                key_activities=[
                    "Code generation techniques and quality assurance",
                    "Context window management during coding",
                    "Anti-hallucination during code generation",
                    "Package verification",
                    "Style adherence",
                    "Incremental validation during writing",
                    "Model selection for coding tasks"
                ],
                transitions={
                    "code_complete": "Move to P4 for testing and verification",
                    "implementation_blocked": "May return to P2 for plan adjustment",
                    "quality_issues": "Stay in P3 and fix issues before proceeding"
                }
            ),

            SDLCPhase.TESTING_VERIFICATION: PhaseSpec(
                phase=SDLCPhase.TESTING_VERIFICATION,
                name="Testing & Verification",
                description="The agent is verifying that code works correctly.",
                what_agent_is_doing="Running tests, validating functionality, and ensuring quality standards.",
                key_activities=[
                    "Test generation techniques",
                    "Quality gate execution",
                    "Multi-stage validation",
                    "Behavioral verification",
                    "Mutation testing",
                    "Performance profiling",
                    "Security scanning"
                ],
                transitions={
                    "tests_pass": "Move to P5 for code review",
                    "test_failures": "Return to P3 for fixes",
                    "quality_gates_fail": "Stay in P4 and address issues"
                }
            ),

            SDLCPhase.CODE_REVIEW: PhaseSpec(
                phase=SDLCPhase.CODE_REVIEW,
                name="Code Review",
                description="The agent is reviewing code (its own or another agent's).",
                what_agent_is_doing="Analyzing code quality, identifying issues, and suggesting improvements.",
                key_activities=[
                    "Code traversal for review (representations needed)",
                    "Semantic diffing for change understanding",
                    "Security-focused review (taint analysis)",
                    "Anti-pattern detection",
                    "Refactoring opportunity identification",
                    "Review checklist execution"
                ],
                transitions={
                    "review_complete": "Move to P6 if issues found, or P7 for deployment",
                    "major_issues": "Return to P3 for fixes",
                    "minor_improvements": "May stay in P5 for quick fixes or proceed"
                }
            ),

            SDLCPhase.DEBUGGING_RECOVERY: PhaseSpec(
                phase=SDLCPhase.DEBUGGING_RECOVERY,
                name="Debugging & Error Recovery",
                description="The agent is diagnosing and fixing problems.",
                what_agent_is_doing="Investigating failures, identifying root causes, and implementing fixes.",
                key_activities=[
                    "Root cause analysis techniques",
                    "Error pattern recognition",
                    "Automated repair strategies",
                    "Regression detection",
                    "Context management during debugging (preserving investigation state)",
                    "Model switching for difficult diagnosis"
                ],
                transitions={
                    "issue_resolved": "Return to appropriate previous phase",
                    "unresolvable": "Escalate to human or move to P7 with known issues",
                    "systemic_problem": "May require returning to P1 for broader analysis"
                }
            ),

            SDLCPhase.DEPLOYMENT_RELEASE: PhaseSpec(
                phase=SDLCPhase.DEPLOYMENT_RELEASE,
                name="Deployment & Release",
                description="The agent is deploying code to environments.",
                what_agent_is_doing="Managing deployment processes, environment configuration, and release coordination.",
                key_activities=[
                    "CI/CD pipeline interaction",
                    "Canary/blue-green strategies",
                    "Rollback procedures",
                    "Health check verification",
                    "Feature flag management"
                ],
                transitions={
                    "deployment_success": "Move to P8 for maintenance and monitoring",
                    "deployment_failure": "Execute rollback and return to P6",
                    "partial_success": "May proceed with monitoring or rollback decision"
                }
            ),

            SDLCPhase.MAINTENANCE_MONITORING: PhaseSpec(
                phase=SDLCPhase.MAINTENANCE_MONITORING,
                name="Maintenance & Monitoring",
                description="The agent is maintaining running systems.",
                what_agent_is_doing="Monitoring system health, handling maintenance tasks, and responding to issues.",
                key_activities=[
                    "Incident detection and response",
                    "Performance monitoring",
                    "Dependency update management",
                    "Technical debt identification",
                    "Self-healing pipeline triggers"
                ],
                transitions={
                    "new_requirements": "May return to P1 for new feature development",
                    "system_issues": "Move to P6 for debugging and recovery",
                    "maintenance_complete": "Continue monitoring or prepare for next cycle"
                }
            ),
        }

    def _load_assignment_rules(self) -> List[PhaseAssignmentRule]:
        """Load rules for assigning atoms to SDLC phases."""
        return [
            # P1: Discovery & Onboarding rules
            PhaseAssignmentRule(
                phase=SDLCPhase.DISCOVERY_ONBOARDING,
                keywords=["discovery", "onboarding", "codebase", "scanning", "repo", "grokking", "dependency", "mapping", "architecture", "extraction", "api", "surface", "entrypoint", "endpoint", "pattern", "recognition", "gap", "analysis"],
                domains=[Domain.CODE_INTELLIGENCE, Domain.WORKSPACE_MANAGEMENT],
                atom_types=[AtomType.TECHNIQUE, AtomType.TOOL, AtomType.RECIPE, AtomType.COMBINATION],
                priority=9
            ),

            # P2: Planning & Design rules
            PhaseAssignmentRule(
                phase=SDLCPhase.PLANNING_DESIGN,
                keywords=["planning", "design", "task", "decomposition", "dependency", "sequencing", "architecture", "decision", "specification", "risk", "assessment", "estimation", "resource", "token", "time", "cost", "branch", "strategy"],
                domains=[Domain.TASK_MANAGEMENT, Domain.AGENT_ARCHITECTURE],
                atom_types=[AtomType.TECHNIQUE, AtomType.CONSTRAINT, AtomType.METRIC, AtomType.RECIPE],
                priority=8
            ),

            # P3: Implementation rules
            PhaseAssignmentRule(
                phase=SDLCPhase.IMPLEMENTATION,
                keywords=["implementation", "coding", "generation", "modification", "validation", "context", "window", "hallucination", "package", "verification", "style", "adherence", "incremental", "model", "selection"],
                domains=[Domain.CONTEXT_ENGINEERING, Domain.CODE_INTELLIGENCE, Domain.SECURITY_GUARDRAILS],
                atom_types=[AtomType.TECHNIQUE, AtomType.CONSTRAINT, AtomType.TOOL, AtomType.FAILURE_MODE, AtomType.ANTI_PATTERN],
                priority=9
            ),

            # P4: Testing & Verification rules
            PhaseAssignmentRule(
                phase=SDLCPhase.TESTING_VERIFICATION,
                keywords=["testing", "verification", "test", "generation", "quality", "gate", "validation", "behavioral", "property", "mutation", "performance", "profiling", "security", "scanning"],
                domains=[Domain.TESTING_VALIDATION, Domain.SECURITY_GUARDRAILS, Domain.CODE_INTELLIGENCE],
                atom_types=[AtomType.TECHNIQUE, AtomType.METRIC, AtomType.TOOL, AtomType.RECIPE, AtomType.COMBINATION],
                priority=8
            ),

            # P5: Code Review rules
            PhaseAssignmentRule(
                phase=SDLCPhase.CODE_REVIEW,
                keywords=["review", "code", "traversal", "semantic", "diffing", "security", "taint", "analysis", "anti-pattern", "refactoring", "checklist"],
                domains=[Domain.CODE_INTELLIGENCE, Domain.SECURITY_GUARDRAILS, Domain.TESTING_VALIDATION],
                atom_types=[AtomType.TECHNIQUE, AtomType.TOOL, AtomType.METRIC, AtomType.COMBINATION, AtomType.RECIPE],
                priority=7
            ),

            # P6: Debugging & Error Recovery rules
            PhaseAssignmentRule(
                phase=SDLCPhase.DEBUGGING_RECOVERY,
                keywords=["debugging", "error", "recovery", "diagnosis", "root", "cause", "analysis", "repair", "regression", "investigation", "model", "switching"],
                domains=[Domain.CODE_INTELLIGENCE, Domain.CONTEXT_ENGINEERING, Domain.MODEL_MANAGEMENT],
                atom_types=[AtomType.TECHNIQUE, AtomType.TOOL, AtomType.FAILURE_MODE, AtomType.RECIPE, AtomType.COMBINATION],
                priority=8
            ),

            # P7: Deployment & Release rules
            PhaseAssignmentRule(
                phase=SDLCPhase.DEPLOYMENT_RELEASE,
                keywords=["deployment", "release", "ci/cd", "pipeline", "canary", "blue-green", "rollback", "health", "check", "feature", "flag"],
                domains=[Domain.CI_CD_DEVOPS, Domain.WORKSPACE_MANAGEMENT],
                atom_types=[AtomType.TECHNIQUE, AtomType.TOOL, AtomType.RECIPE, AtomType.CONSTRAINT, AtomType.FAILURE_MODE],
                priority=7
            ),

            # P8: Maintenance & Monitoring rules
            PhaseAssignmentRule(
                phase=SDLCPhase.MAINTENANCE_MONITORING,
                keywords=["maintenance", "monitoring", "incident", "detection", "response", "performance", "dependency", "update", "technical", "debt", "self-healing"],
                domains=[Domain.CI_CD_DEVOPS, Domain.SELF_IMPROVEMENT, Domain.SECURITY_GUARDRAILS],
                atom_types=[AtomType.TECHNIQUE, AtomType.METRIC, AtomType.TOOL, AtomType.CONSTRAINT, AtomType.RECIPE],
                priority=6
            ),

            # Cross-phase rules for general techniques
            PhaseAssignmentRule(
                phase=SDLCPhase.DISCOVERY_ONBOARDING,  # Default fallback
                keywords=["analysis", "understanding", "exploration", "mapping", "discovery"],
                domains=[],  # Any domain
                atom_types=[AtomType.TECHNIQUE, AtomType.TOOL],
                priority=1  # Low priority fallback
            ),
        ]

    def assign_atoms_to_phases(self, atoms: List[KnowledgeAtom]) -> Dict[SDLCPhase, List[KnowledgeAtom]]:
        """Assign knowledge atoms to their relevant SDLC phases.

        Args:
            atoms: List of knowledge atoms to assign.

        Returns:
            Dictionary mapping phases to lists of atoms assigned to each phase.
        """
        phase_atoms: Dict[SDLCPhase, List[KnowledgeAtom]] = {
            phase: [] for phase in SDLCPhase
        }

        for atom in atoms:
            # Reset phases for this atom
            atom.sdlc_phases = []

            # Apply assignment rules in priority order
            matched_phases = set()
            for rule in sorted(self.assignment_rules, key=lambda r: r.priority, reverse=True):
                if rule.enabled and rule.matches(atom):
                    if rule.phase not in matched_phases:
                        matched_phases.add(rule.phase)
                        atom.sdlc_phases.append(rule.phase)
                        phase_atoms[rule.phase].append(atom)

            # If no phases matched, assign to a default based on content analysis
            if not atom.sdlc_phases:
                default_phase = self._find_default_phase(atom)
                if default_phase:
                    atom.sdlc_phases.append(default_phase)
                    phase_atoms[default_phase].append(atom)

        return phase_atoms

    def _find_default_phase(self, atom: KnowledgeAtom) -> Optional[SDLCPhase]:
        """Find a default phase assignment for atoms that don't match specific rules."""
        content_lower = atom.content.lower()

        # Early phases
        if any(word in content_lower for word in ["understand", "analyze", "explore", "discover", "map", "scan"]):
            return SDLCPhase.DISCOVERY_ONBOARDING

        # Planning phases
        if any(word in content_lower for word in ["plan", "design", "decide", "estimate", "risk", "architecture"]):
            return SDLCPhase.PLANNING_DESIGN

        # Implementation phases
        if any(word in content_lower for word in ["implement", "code", "write", "generate", "create", "build"]):
            return SDLCPhase.IMPLEMENTATION

        # Testing phases
        if any(word in content_lower for word in ["test", "verify", "validate", "check", "quality"]):
            return SDLCPhase.TESTING_VERIFICATION

        # Review/Debug phases
        if any(word in content_lower for word in ["review", "debug", "fix", "error", "issue", "problem"]):
            return SDLCPhase.DEBUGGING_RECOVERY

        # Deployment phases
        if any(word in content_lower for word in ["deploy", "release", "pipeline", "environment"]):
            return SDLCPhase.DEPLOYMENT_RELEASE

        # Default to discovery if nothing else matches
        return SDLCPhase.DISCOVERY_ONBOARDING

    def rank_atoms_in_phases(self, phase_atoms: Dict[SDLCPhase, List[KnowledgeAtom]]) -> Dict[SDLCPhase, List[KnowledgeAtom]]:
        """Rank atoms within each phase by relevance and evidence strength.

        Args:
            phase_atoms: Dictionary mapping phases to their atoms.

        Returns:
            Dictionary with atoms ranked within each phase.
        """
        ranked_phases = {}

        for phase, atoms in phase_atoms.items():
            if not atoms:
                ranked_phases[phase] = []
                continue

            # Sort by: evidence strength, then by phase specificity, then by content length
            def sort_key(atom: KnowledgeAtom) -> tuple:
                strength_order = {"STRONG": 3, "MODERATE": 2, "WEAK": 1}

                # Phase specificity score (atoms with multiple phases are less specific)
                specificity_score = 1.0 / max(len(atom.sdlc_phases), 1)

                return (
                    strength_order.get(atom.evidence_strength, 0),
                    specificity_score,
                    -len(atom.content)  # Prefer more detailed content
                )

            ranked_atoms = sorted(atoms, key=sort_key, reverse=True)
            ranked_phases[phase] = ranked_atoms

        return ranked_phases

    def get_phase_sequence(self, phase_atoms: Dict[SDLCPhase, List[KnowledgeAtom]]) -> List[Dict[str, any]]:
        """Generate a sequenced workflow of phases with their key techniques.

        Args:
            phase_atoms: Dictionary mapping phases to their atoms.

        Returns:
            List of phase dictionaries with sequencing information.
        """
        phase_order = [
            SDLCPhase.DISCOVERY_ONBOARDING,
            SDLCPhase.PLANNING_DESIGN,
            SDLCPhase.IMPLEMENTATION,
            SDLCPhase.TESTING_VERIFICATION,
            SDLCPhase.CODE_REVIEW,
            SDLCPhase.DEBUGGING_RECOVERY,
            SDLCPhase.DEPLOYMENT_RELEASE,
            SDLCPhase.MAINTENANCE_MONITORING,
        ]

        sequence = []

        for phase in phase_order:
            atoms = phase_atoms.get(phase, [])
            if not atoms:
                continue

            phase_spec = self.phase_specs[phase]
            ranked_atoms = self.rank_atoms_in_phases({phase: atoms})[phase]

            # Group techniques by step order
            techniques_by_step = self._organize_techniques_by_steps(phase, ranked_atoms)

            phase_info = {
                "phase": phase,
                "name": phase_spec.name,
                "description": phase_spec.what_agent_is_doing,
                "total_atoms": len(atoms),
                "techniques_by_step": techniques_by_step,
                "constraints": [a for a in ranked_atoms if a.type == AtomType.CONSTRAINT][:3],  # Top 3
                "tools_needed": [a for a in ranked_atoms if a.type == AtomType.TOOL][:3],  # Top 3
                "failure_modes": [a for a in ranked_atoms if a.type == AtomType.FAILURE_MODE][:3],  # Top 3
                "transitions": phase_spec.transitions
            }

            sequence.append(phase_info)

        return sequence

    def _organize_techniques_by_steps(self, phase: SDLCPhase, atoms: List[KnowledgeAtom]) -> Dict[str, List[KnowledgeAtom]]:
        """Organize techniques into logical step sequences for a phase."""
        techniques = [a for a in atoms if a.type in [AtomType.TECHNIQUE, AtomType.RECIPE, AtomType.COMBINATION]]

        if not techniques:
            return {}

        # Define step sequences for each phase
        phase_steps = {
            SDLCPhase.DISCOVERY_ONBOARDING: {
                "Step 1 - Initial Scanning": ["scan", "map", "explore", "discover"],
                "Step 2 - Structure Analysis": ["analyze", "parse", "extract", "understand"],
                "Step 3 - Pattern Recognition": ["identify", "recognize", "classify", "categorize"],
                "Step 4 - Gap Assessment": ["assess", "evaluate", "compare", "validate"]
            },
            SDLCPhase.PLANNING_DESIGN: {
                "Step 1 - Requirements Analysis": ["analyze", "understand", "clarify", "define"],
                "Step 2 - Task Decomposition": ["decompose", "break", "split", "organize"],
                "Step 3 - Dependency Mapping": ["identify", "map", "sequence", "order"],
                "Step 4 - Risk Assessment": ["assess", "evaluate", "estimate", "mitigate"]
            },
            SDLCPhase.IMPLEMENTATION: {
                "Step 1 - Context Setup": ["prepare", "configure", "initialize", "setup"],
                "Step 2 - Code Generation": ["generate", "write", "create", "implement"],
                "Step 3 - Incremental Validation": ["validate", "check", "verify", "test"],
                "Step 4 - Quality Assurance": ["review", "refactor", "optimize", "clean"]
            },
            SDLCPhase.TESTING_VERIFICATION: {
                "Step 1 - Test Planning": ["plan", "design", "strategy", "approach"],
                "Step 2 - Test Generation": ["generate", "create", "write", "automate"],
                "Step 3 - Test Execution": ["run", "execute", "perform", "validate"],
                "Step 4 - Results Analysis": ["analyze", "review", "assess", "report"]
            },
            SDLCPhase.CODE_REVIEW: {
                "Step 1 - Code Examination": ["examine", "analyze", "review", "inspect"],
                "Step 2 - Issue Identification": ["identify", "detect", "find", "spot"],
                "Step 3 - Impact Assessment": ["assess", "evaluate", "measure", "quantify"],
                "Step 4 - Recommendations": ["recommend", "suggest", "propose", "advise"]
            },
            SDLCPhase.DEBUGGING_RECOVERY: {
                "Step 1 - Problem Identification": ["identify", "reproduce", "isolate", "characterize"],
                "Step 2 - Root Cause Analysis": ["analyze", "investigate", "trace", "diagnose"],
                "Step 3 - Solution Development": ["develop", "design", "create", "formulate"],
                "Step 4 - Fix Implementation": ["implement", "apply", "deploy", "execute"]
            },
            SDLCPhase.DEPLOYMENT_RELEASE: {
                "Step 1 - Pre-deployment Checks": ["check", "validate", "verify", "test"],
                "Step 2 - Deployment Execution": ["deploy", "release", "push", "publish"],
                "Step 3 - Health Verification": ["monitor", "check", "validate", "confirm"],
                "Step 4 - Rollback Preparation": ["prepare", "plan", "backup", "document"]
            },
            SDLCPhase.MAINTENANCE_MONITORING: {
                "Step 1 - System Monitoring": ["monitor", "watch", "observe", "track"],
                "Step 2 - Issue Detection": ["detect", "identify", "alert", "notify"],
                "Step 3 - Problem Resolution": ["resolve", "fix", "repair", "restore"],
                "Step 4 - Preventive Maintenance": ["prevent", "optimize", "update", "improve"]
            }
        }

        steps_config = phase_steps.get(phase, {})
        if not steps_config:
            # Fallback: put all techniques in a single step
            return {"General Techniques": techniques[:5]}  # Top 5

        # Assign techniques to steps based on keyword matching
        steps_with_techniques = {}
        assigned_technique_ids = set()

        for step_name, step_keywords in steps_config.items():
            step_techniques = []
            for technique in techniques:
                if technique.id in assigned_technique_ids:
                    continue

                content_lower = technique.content.lower()
                if any(keyword in content_lower for keyword in step_keywords):
                    step_techniques.append(technique)
                    assigned_technique_ids.add(technique.id)

            if step_techniques:
                # Sort by evidence strength within the step
                step_techniques.sort(key=lambda t: {"STRONG": 3, "MODERATE": 2, "WEAK": 1}.get(t.evidence_strength, 0), reverse=True)
                steps_with_techniques[step_name] = step_techniques

        # Add any remaining techniques to a general step
        remaining_techniques = [t for t in techniques if t.id not in assigned_technique_ids]
        if remaining_techniques:
            remaining_techniques.sort(key=lambda t: {"STRONG": 3, "MODERATE": 2, "WEAK": 1}.get(t.evidence_strength, 0), reverse=True)
            steps_with_techniques["Additional Techniques"] = remaining_techniques[:3]  # Top 3

        return steps_with_techniques

    def get_phase_summary(self, phase: SDLCPhase, atoms: List[KnowledgeAtom]) -> Dict[str, any]:
        """Generate a summary report for a specific phase.

        Args:
            phase: The phase to summarize.
            atoms: Atoms assigned to this phase.

        Returns:
            Summary dictionary with key metrics and organized content.
        """
        if phase not in self.phase_specs:
            return {}

        phase_spec = self.phase_specs[phase]

        # Get ranked atoms
        ranked_atoms = self.rank_atoms_in_phases({phase: atoms}).get(phase, [])

        # Group by type
        atoms_by_type = {}
        for atom in ranked_atoms:
            if atom.type not in atoms_by_type:
                atoms_by_type[atom.type] = []
            atoms_by_type[atom.type].append(atom)

        # Get techniques organized by steps
        techniques_by_step = self._organize_techniques_by_steps(phase, ranked_atoms)

        return {
            "phase": phase,
            "name": phase_spec.name,
            "what_agent_is_doing": phase_spec.what_agent_is_doing,
            "total_atoms": len(atoms),
            "atoms_by_type": {k: len(v) for k, v in atoms_by_type.items()},
            "techniques_by_step": {
                step: [{"id": t.id, "content": t.content[:80] + "..." if len(t.content) > 80 else t.content, "evidence": t.evidence_strength}
                      for t in techniques]
                for step, techniques in techniques_by_step.items()
            },
            "key_constraints": [
                {"id": atom.id, "content": atom.content}
                for atom in atoms_by_type.get(AtomType.CONSTRAINT, [])[:3]
            ],
            "tools_needed": [
                {"id": atom.id, "content": atom.content}
                for atom in atoms_by_type.get(AtomType.TOOL, [])[:3]
            ],
            "failure_modes": [
                {"id": atom.id, "content": atom.content}
                for atom in atoms_by_type.get(AtomType.FAILURE_MODE, [])[:3]
            ],
            "transitions": phase_spec.transitions
        }
