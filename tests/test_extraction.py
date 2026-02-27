"""Tests for knowledge atom extraction."""

import pytest
from pathlib import Path
from unittest.mock import Mock

from distillation.models import (
    KnowledgeAtom,
    AtomType,
    EvidenceStrength,
    ResearchFile,
    ExtractionConfig,
)
from distillation.processors.extraction import AtomExtractor, ExtractionPattern


class TestExtractionPattern:
    """Test ExtractionPattern functionality."""

    def test_pattern_matches(self):
        """Test pattern matching."""
        pattern = ExtractionPattern(
            name="test",
            pattern=r"Tree-sitter:\s*([^.!?]+)",
            atom_type=AtomType.TOOL,
            evidence_keywords=["supports", "provides"]
        )

        assert pattern.matches("Tree-sitter: incremental AST parsing, 40+ languages")
        assert not pattern.matches("Some other text without Tree-sitter")

    def test_pattern_with_flags(self):
        """Test pattern matching with regex flags."""
        pattern = ExtractionPattern(
            name="case_insensitive",
            pattern=r"tree-sitter",
            atom_type=AtomType.TOOL,
            evidence_keywords=[]
        )

        assert pattern.matches("Tree-Sitter is great")
        assert pattern.matches("TREE-SITTER works well")


class TestAtomExtractor:
    """Test AtomExtractor functionality."""

    @pytest.fixture
    def extractor(self):
        """Create a test extractor."""
        return AtomExtractor()

    @pytest.fixture
    def sample_research_file(self):
        """Create a sample research file for testing."""
        content = """
        Tree-sitter: incremental AST parsing, 40+ languages, error recovery, de facto standard.
        AST-based code search improves precision 60-80% over text-based methods.
        Context window attention degrades 20-40% for mid-context items — place critical info at boundaries.
        Combine AST with CFG and DFG for comprehensive code understanding.
        """
        return ResearchFile(
            path=Path("test/research.md"),
            content=content,
            format="md"
        )

    def test_extract_technique_atom(self, extractor, sample_research_file):
        """Test extraction of technique atoms."""
        atoms = extractor.extract_atoms(sample_research_file)

        # Should extract Tree-sitter technique
        tree_sitter_atoms = [a for a in atoms if "Tree-sitter" in a.content]
        assert len(tree_sitter_atoms) >= 1

        atom = tree_sitter_atoms[0]
        assert atom.type == AtomType.TOOL
        assert atom.evidence_strength in [EvidenceStrength.STRONG, EvidenceStrength.MODERATE]
        assert "research.md" in atom.source[0]

    def test_extract_metric_atom(self, extractor, sample_research_file):
        """Test extraction of metric atoms."""
        atoms = extractor.extract_atoms(sample_research_file)

        # Should extract precision metric
        metric_atoms = [a for a in atoms if "60-80%" in a.content]
        assert len(metric_atoms) >= 1

        atom = metric_atoms[0]
        assert atom.type == AtomType.METRIC
        assert atom.evidence_strength == EvidenceStrength.MODERATE

    def test_extract_constraint_atom(self, extractor, sample_research_file):
        """Test extraction of constraint atoms."""
        atoms = extractor.extract_atoms(sample_research_file)

        # Should extract context window constraint
        constraint_atoms = [a for a in atoms if "20-40%" in a.content]
        assert len(constraint_atoms) >= 1

        atom = constraint_atoms[0]
        assert atom.type == AtomType.CONSTRAINT
        assert "boundaries" in atom.content

    def test_extract_combination_atom(self, extractor, sample_research_file):
        """Test extraction of combination atoms."""
        atoms = extractor.extract_atoms(sample_research_file)

        # Should extract AST+CFG+DFG combination
        combo_atoms = [a for a in atoms if "CFG" in a.content and "DFG" in a.content]
        assert len(combo_atoms) >= 1

        atom = combo_atoms[0]
        assert atom.type == AtomType.COMBINATION

    def test_content_length_filtering(self, extractor):
        """Test that content length filtering works."""
        config = ExtractionConfig(min_content_length=50, max_content_length=100)
        extractor_with_config = AtomExtractor(config)

        # Create content that's too short
        short_content = ResearchFile(
            path=Path("test/short.md"),
            content="Short text.",
            format="md"
        )

        atoms = extractor_with_config.extract_atoms(short_content)
        assert len(atoms) == 0

    def test_deduplication(self, extractor):
        """Test that duplicate atoms are deduplicated."""
        content = """
        Tree-sitter: incremental AST parsing, 40+ languages.
        Tree-sitter provides incremental AST parsing for 40+ languages.
        """

        research_file = ResearchFile(
            path=Path("test/dup.md"),
            content=content,
            format="md"
        )

        atoms = extractor.extract_atoms(research_file)

        # Should have only one Tree-sitter atom despite duplicate content
        tree_sitter_atoms = [a for a in atoms if "Tree-sitter" in a.content]
        assert len(tree_sitter_atoms) <= 1

    def test_evidence_strength_assessment(self, extractor):
        """Test evidence strength assessment."""
        # Strong evidence
        strong_content = ResearchFile(
            path=Path("test/strong.md"),
            content="Measured improvement of 60% in precision when using AST-based search.",
            format="md"
        )

        strong_atoms = extractor.extract_atoms(strong_content)
        assert len(strong_atoms) >= 1
        assert strong_atoms[0].evidence_strength == EvidenceStrength.STRONG

        # Weak evidence
        weak_content = ResearchFile(
            path=Path("test/weak.md"),
            content="Might improve precision when using AST-based search.",
            format="md"
        )

        weak_atoms = extractor.extract_atoms(weak_content)
        assert len(weak_atoms) >= 1
        assert weak_atoms[0].evidence_strength == EvidenceStrength.WEAK

    def test_batch_extract(self, extractor):
        """Test batch extraction from multiple files."""
        files = [
            ResearchFile(
                path=Path("test/file1.md"),
                content="Tree-sitter: incremental AST parsing, 40+ languages.",
                format="md"
            ),
            ResearchFile(
                path=Path("test/file2.md"),
                content="AST-based search improves precision 60-80%.",
                format="md"
            )
        ]

        atoms = extractor.batch_extract(files)
        assert len(atoms) >= 2

        # Check that sources are merged correctly
        tree_sitter_atoms = [a for a in atoms if "Tree-sitter" in a.content]
        if tree_sitter_atoms:
            assert len(tree_sitter_atoms[0].source) >= 1

    def test_custom_patterns(self):
        """Test custom pattern loading."""
        config = ExtractionConfig(
            custom_patterns={
                "custom_technique": "TECHNIQUE:CustomTech:\\s*([^.!?]+)"
            }
        )

        extractor = AtomExtractor(config)

        # Should have loaded the custom pattern
        custom_patterns = [p for p in extractor.patterns if p.name == "custom_technique"]
        assert len(custom_patterns) == 1
        assert custom_patterns[0].atom_type == AtomType.TECHNIQUE

    def test_disabled_patterns(self, extractor):
        """Test that disabled patterns are not used."""
        # Disable all patterns
        for pattern in extractor.patterns:
            pattern.enabled = False

        research_file = ResearchFile(
            path=Path("test/disabled.md"),
            content="Tree-sitter: incremental AST parsing, 40+ languages.",
            format="md"
        )

        atoms = extractor.extract_atoms(research_file)
        assert len(atoms) == 0

    def test_atom_id_generation(self, extractor):
        """Test that atom IDs are generated consistently."""
        content1 = "Tree-sitter: incremental AST parsing"
        content2 = "Tree-sitter: incremental AST parsing"

        research_file = ResearchFile(
            path=Path("test/id.md"),
            content=content1,
            format="md"
        )

        atom1 = extractor._extract_atom_from_text(content1, "", research_file)
        atom2 = extractor._extract_atom_from_text(content2, "", research_file)

        # Same content should generate same ID
        if atom1 and atom2:
            assert atom1.id == atom2.id

    def test_content_cleaning(self, extractor):
        """Test content cleaning and normalization."""
        dirty_content = "  Tree-sitter:   incremental   AST     parsing,   40+   languages.  "

        research_file = ResearchFile(
            path=Path("test/clean.md"),
            content=dirty_content,
            format="md"
        )

        atoms = extractor.extract_atoms(research_file)

        if atoms:
            # Should be cleaned of extra whitespace
            assert "  " not in atoms[0].content
            assert atoms[0].content.count(" ") < dirty_content.count(" ")

    def test_context_window(self):
        """Test context window functionality."""
        config = ExtractionConfig(context_window=2)
        extractor = AtomExtractor(config)

        sentences = [
            "First sentence.",
            "Second sentence with Tree-sitter.",
            "Third sentence.",
            "Fourth sentence.",
            "Fifth sentence."
        ]

        context = extractor._get_context_window(sentences, 1)  # Second sentence
        assert "First sentence" in context
        assert "Second sentence" in context
        assert "Third sentence" in context
        assert "Fourth sentence" in context
        assert "Fifth sentence" not in context  # Beyond window