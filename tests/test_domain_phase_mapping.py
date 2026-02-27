"""Tests for domain mapping and phase assignment functionality."""

import pytest
from unittest.mock import Mock

from distillation.models import (
    KnowledgeAtom,
    AtomType,
    EvidenceStrength,
    Domain,
    SDLCPhase,
)
from distillation.processors import DomainMapper, PhaseAssigner


class TestDomainMapper:
    """Test cases for DomainMapper functionality."""

    @pytest.fixture
    def domain_mapper(self):
        """Create a DomainMapper instance for testing."""
        return DomainMapper()

    @pytest.fixture
    def sample_atoms(self):
        """Create sample knowledge atoms for testing."""
        return [
            KnowledgeAtom(
                id="KA-001",
                type=AtomType.TECHNIQUE,
                content="Tree-sitter enables incremental AST parsing with 40+ language support and error recovery",
                evidence_strength=EvidenceStrength.STRONG,
                source=["research/code_intelligence.md"]
            ),
            KnowledgeAtom(
                id="KA-002",
                type=AtomType.METRIC,
                content="AST-based code search improves precision by 60-80% over text-based methods",
                evidence_strength=EvidenceStrength.MODERATE,
                source=["research/search_techniques.md"]
            ),
            KnowledgeAtom(
                id="KA-003",
                type=AtomType.CONSTRAINT,
                content="Context window attention degrades 20-40% for mid-context items",
                evidence_strength=EvidenceStrength.STRONG,
                source=["research/attention_mechanisms.md"]
            ),
            KnowledgeAtom(
                id="KA-004",
                type=AtomType.TOOL,
                content="Sourcegraph provides multi-repo symbol search with sub-second queries across million-line codebases",
                evidence_strength=EvidenceStrength.STRONG,
                source=["research/code_search_tools.md"]
            ),
            KnowledgeAtom(
                id="KA-005",
                type=AtomType.FAILURE_MODE,
                content="19.7% of AI-recommended packages are fabricated and fail registry verification",
                evidence_strength=EvidenceStrength.MODERATE,
                source=["research/package_security.md"]
            ),
            KnowledgeAtom(
                id="KA-006",
                type=AtomType.TECHNIQUE,
                content="Chain-of-verification: generate answer → extract claims → verify each independently → produce final answer",
                evidence_strength=EvidenceStrength.STRONG,
                source=["research/verification_techniques.md"]
            ),
        ]

    def test_domain_specs_loaded(self, domain_mapper):
        """Test that all 12 domain specifications are loaded."""
        assert len(domain_mapper.domain_specs) == 12
        assert Domain.AGENT_ARCHITECTURE in domain_mapper.domain_specs
        assert Domain.SELF_IMPROVEMENT in domain_mapper.domain_specs

    def test_mapping_rules_loaded(self, domain_mapper):
        """Test that mapping rules are loaded."""
        assert len(domain_mapper.mapping_rules) > 0
        # Check that rules have proper structure
        for rule in domain_mapper.mapping_rules:
            assert rule.domain in Domain
            assert isinstance(rule.keywords, list)
            assert isinstance(rule.atom_types, list)

    def test_map_atoms_to_domains(self, domain_mapper, sample_atoms):
        """Test mapping atoms to domains."""
        domain_atoms = domain_mapper.map_atoms_to_domains(sample_atoms)

        # Check that atoms were assigned to domains
        total_assigned = sum(len(atoms) for atoms in domain_atoms.values())
        assert total_assigned >= len(sample_atoms)  # Some atoms may be assigned to multiple domains

        # Check that specific atoms are assigned to expected domains
        code_intelligence_atoms = domain_atoms.get(Domain.CODE_INTELLIGENCE, [])
        assert len(code_intelligence_atoms) > 0

        context_engineering_atoms = domain_atoms.get(Domain.CONTEXT_ENGINEERING, [])
        assert len(context_engineering_atoms) > 0

    def test_rank_atoms_in_domains(self, domain_mapper, sample_atoms):
        """Test ranking atoms within domains."""
        domain_atoms = domain_mapper.map_atoms_to_domains(sample_atoms)
        ranked_domains = domain_mapper.rank_atoms_in_domains(domain_atoms)

        # Check that ranking preserves all atoms
        for domain in domain_atoms:
            assert len(ranked_domains[domain]) == len(domain_atoms[domain])

        # Check that strong evidence atoms come first (when they exist)
        for domain, atoms in ranked_domains.items():
            if atoms:
                # First atom should have highest evidence strength
                first_strength = atoms[0].evidence_strength
                for atom in atoms[1:]:
                    # Later atoms should not have higher strength than first
                    assert {"STRONG": 3, "MODERATE": 2, "WEAK": 1}[atom.evidence_strength] <= {"STRONG": 3, "MODERATE": 2, "WEAK": 1}[first_strength]

    def test_identify_cross_domain_links(self, domain_mapper, sample_atoms):
        """Test identification of cross-domain relationships."""
        domain_atoms = domain_mapper.map_atoms_to_domains(sample_atoms)
        cross_links = domain_mapper.identify_cross_domain_links(domain_atoms)

        # Should identify some cross-domain relationships
        # (This is a basic test - actual cross-links depend on atom assignments)
        assert isinstance(cross_links, dict)

    def test_generate_gap_report(self, domain_mapper, sample_atoms):
        """Test gap report generation."""
        domain_atoms = domain_mapper.map_atoms_to_domains(sample_atoms)
        gap_report = domain_mapper.generate_gap_report(domain_atoms)

        assert len(gap_report) == 12  # All domains
        for domain in Domain:
            assert domain in gap_report
            domain_report = gap_report[domain]
            assert "total_atoms" in domain_report
            assert "coverage_score" in domain_report
            assert "gaps" in domain_report

    def test_get_domain_summary(self, domain_mapper, sample_atoms):
        """Test domain summary generation."""
        # Assign domains to sample atoms for testing
        sample_atoms[0].domains = [Domain.CODE_INTELLIGENCE]
        sample_atoms[1].domains = [Domain.CODE_INTELLIGENCE]
        sample_atoms[2].domains = [Domain.CONTEXT_ENGINEERING]

        summary = domain_mapper.get_domain_summary(Domain.CODE_INTELLIGENCE, [sample_atoms[0], sample_atoms[1]])

        assert summary["domain"] == Domain.CODE_INTELLIGENCE
        assert "total_atoms" in summary
        assert "key_techniques" in summary
        assert "cross_domain_links" in summary


class TestPhaseAssigner:
    """Test cases for PhaseAssigner functionality."""

    @pytest.fixture
    def phase_assigner(self):
        """Create a PhaseAssigner instance for testing."""
        return PhaseAssigner()

    @pytest.fixture
    def sample_atoms(self):
        """Create sample knowledge atoms for testing."""
        return [
            KnowledgeAtom(
                id="KA-001",
                type=AtomType.TECHNIQUE,
                content="Use Tree-sitter for incremental AST parsing during codebase analysis",
                evidence_strength=EvidenceStrength.STRONG,
                domains=[Domain.CODE_INTELLIGENCE],
                source=["research/code_intelligence.md"]
            ),
            KnowledgeAtom(
                id="KA-002",
                type=AtomType.TECHNIQUE,
                content="Implement chain-of-verification to validate AI-generated code",
                evidence_strength=EvidenceStrength.STRONG,
                domains=[Domain.SECURITY_GUARDRAILS],
                source=["research/verification_techniques.md"]
            ),
            KnowledgeAtom(
                id="KA-003",
                type=AtomType.TOOL,
                content="Sourcegraph enables multi-repo symbol search for code understanding",
                evidence_strength=EvidenceStrength.STRONG,
                domains=[Domain.CODE_INTELLIGENCE],
                source=["research/code_search_tools.md"]
            ),
            KnowledgeAtom(
                id="KA-004",
                type=AtomType.CONSTRAINT,
                content="Never deploy code with unverified package dependencies",
                evidence_strength=EvidenceStrength.STRONG,
                domains=[Domain.SECURITY_GUARDRAILS],
                source=["research/package_security.md"]
            ),
            KnowledgeAtom(
                id="KA-005",
                type=AtomType.RECIPE,
                content="1. Parse code with AST 2. Build CFG 3. Apply taint analysis 4. Generate security report",
                evidence_strength=EvidenceStrength.MODERATE,
                domains=[Domain.CODE_INTELLIGENCE, Domain.SECURITY_GUARDRAILS],
                source=["research/security_scanning.md"]
            ),
        ]

    def test_phase_specs_loaded(self, phase_assigner):
        """Test that all 8 phase specifications are loaded."""
        assert len(phase_assigner.phase_specs) == 8
        assert SDLCPhase.DISCOVERY_ONBOARDING in phase_assigner.phase_specs
        assert SDLCPhase.MAINTENANCE_MONITORING in phase_assigner.phase_specs

    def test_assignment_rules_loaded(self, phase_assigner):
        """Test that assignment rules are loaded."""
        assert len(phase_assigner.assignment_rules) > 0
        # Check that rules have proper structure
        for rule in phase_assigner.assignment_rules:
            assert rule.phase in SDLCPhase
            assert isinstance(rule.keywords, list)
            assert isinstance(rule.domains, list) or rule.domains is None
            assert isinstance(rule.atom_types, list)

    def test_assign_atoms_to_phases(self, phase_assigner, sample_atoms):
        """Test assigning atoms to phases."""
        phase_atoms = phase_assigner.assign_atoms_to_phases(sample_atoms)

        # Check that atoms were assigned to phases
        total_assigned = sum(len(atoms) for atoms in phase_atoms.values())
        assert total_assigned >= len(sample_atoms)  # Some atoms may be assigned to multiple phases

        # Check that specific atoms are assigned to expected phases
        discovery_atoms = phase_atoms.get(SDLCPhase.DISCOVERY_ONBOARDING, [])
        implementation_atoms = phase_atoms.get(SDLCPhase.IMPLEMENTATION, [])
        security_atoms = phase_atoms.get(SDLCPhase.TESTING_VERIFICATION, [])

        # At least some atoms should be assigned
        assert len(discovery_atoms) + len(implementation_atoms) + len(security_atoms) > 0

    def test_rank_atoms_in_phases(self, phase_assigner, sample_atoms):
        """Test ranking atoms within phases."""
        phase_atoms = phase_assigner.assign_atoms_to_phases(sample_atoms)
        ranked_phases = phase_assigner.rank_atoms_in_phases(phase_atoms)

        # Check that ranking preserves all atoms
        for phase in phase_atoms:
            assert len(ranked_phases[phase]) == len(phase_atoms[phase])

    def test_get_phase_sequence(self, phase_assigner, sample_atoms):
        """Test phase sequence generation."""
        phase_atoms = phase_assigner.assign_atoms_to_phases(sample_atoms)
        sequence = phase_assigner.get_phase_sequence(phase_atoms)

        # Should return a list of phase dictionaries
        assert isinstance(sequence, list)

        # Check that phases are in correct order
        phase_order = [SDLCPhase.DISCOVERY_ONBOARDING, SDLCPhase.PLANNING_DESIGN,
                      SDLCPhase.IMPLEMENTATION, SDLCPhase.TESTING_VERIFICATION,
                      SDLCPhase.CODE_REVIEW, SDLCPhase.DEBUGGING_RECOVERY,
                      SDLCPhase.DEPLOYMENT_RELEASE, SDLCPhase.MAINTENANCE_MONITORING]

        if sequence:  # Only check order if we have phases
            sequence_phases = [item["phase"] for item in sequence]
            # Check that the phases appear in the expected order
            expected_indices = []
            for phase in sequence_phases:
                if phase in phase_order:
                    expected_indices.append(phase_order.index(phase))

            # Indices should be non-decreasing (phases in order)
            assert expected_indices == sorted(expected_indices)

    def test_get_phase_summary(self, phase_assigner, sample_atoms):
        """Test phase summary generation."""
        # Assign phases to sample atoms for testing
        sample_atoms[0].sdlc_phases = [SDLCPhase.DISCOVERY_ONBOARDING]
        sample_atoms[1].sdlc_phases = [SDLCPhase.IMPLEMENTATION]
        sample_atoms[2].sdlc_phases = [SDLCPhase.DISCOVERY_ONBOARDING]

        summary = phase_assigner.get_phase_summary(SDLCPhase.DISCOVERY_ONBOARDING,
                                                 [sample_atoms[0], sample_atoms[2]])

        assert summary["phase"] == SDLCPhase.DISCOVERY_ONBOARDING
        assert "total_atoms" in summary
        assert "techniques_by_step" in summary
        assert "key_constraints" in summary
        assert "tools_needed" in summary


class TestIntegration:
    """Integration tests for domain and phase mapping together."""

    def test_full_pipeline(self):
        """Test the complete domain and phase mapping pipeline."""
        # Create sample atoms
        atoms = [
            KnowledgeAtom(
                id="KA-001",
                type=AtomType.TECHNIQUE,
                content="Tree-sitter AST parsing for code analysis and understanding",
                evidence_strength=EvidenceStrength.STRONG,
                source=["research/code_intelligence.md"]
            ),
            KnowledgeAtom(
                id="KA-002",
                type=AtomType.CONSTRAINT,
                content="Context windows degrade attention by 20-40% in middle positions",
                evidence_strength=EvidenceStrength.STRONG,
                source=["research/attention.md"]
            ),
            KnowledgeAtom(
                id="KA-003",
                type=AtomType.TOOL,
                content="Sourcegraph provides sub-second multi-repo code search",
                evidence_strength=EvidenceStrength.STRONG,
                source=["research/tools.md"]
            ),
        ]

        # Run domain mapping
        domain_mapper = DomainMapper()
        domain_atoms = domain_mapper.map_atoms_to_domains(atoms)
        ranked_domains = domain_mapper.rank_atoms_in_domains(domain_atoms)

        # Run phase assignment
        phase_assigner = PhaseAssigner()
        phase_atoms = phase_assigner.assign_atoms_to_phases(atoms)
        ranked_phases = phase_assigner.rank_atoms_in_phases(phase_atoms)

        # Verify integration
        assert len(domain_atoms) == 12  # All domains
        assert len(phase_atoms) == 8    # All phases

        # Check that atoms have both domains and phases assigned
        for atom in atoms:
            assert len(atom.domains) > 0
            assert len(atom.sdlc_phases) > 0

        # Verify cross-domain links can be identified
        cross_links = domain_mapper.identify_cross_domain_links(domain_atoms)
        assert isinstance(cross_links, dict)

        # Verify gap analysis works
        gap_report = domain_mapper.generate_gap_report(domain_atoms)
        assert len(gap_report) == 12