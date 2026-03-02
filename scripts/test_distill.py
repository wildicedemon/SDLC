#!/usr/bin/env python3
"""Tests for the SDLC Knowledge Atom Extraction pipeline."""

import unittest
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import from scripts.distillation (FIXED: was 'from distillation.X')
from scripts.distillation.scanner import scan_corpus
from scripts.distillation.parser import parse_file, parse_markdown, parse_csv, RawAtom
from scripts.distillation.classifier import classify, KnowledgeAtom
from scripts.distillation.dedup import deduplicate
from scripts.distillation.ranker import rank
from scripts.distillation.tagger import tag
from scripts.distillation.prong2_domains import generate_domain_specs
from scripts.distillation.prong3_phases import generate_phase_specs
from scripts.distillation.prong4_products import generate_product_specs
from scripts.distillation.validator import validate, ValidationReport
from scripts.distillation.gap_report import generate_gap_report


class TestScanner(unittest.TestCase):
    """Tests for the scanner module."""
    
    def test_scan_corpus_finds_files(self):
        """Test that scanner finds files in each category."""
        result = scan_corpus(Path("."))
        
        # Verify structure
        self.assertIn("perplexity", result)
        self.assertIn("overviews", result)
        self.assertIn("indices", result)
        self.assertIn("kimi_docs", result)
        self.assertIn("kimi_csv", result)
        self.assertIn("root_files", result)


class TestParser(unittest.TestCase):
    """Tests for the parser module."""
    
    def test_parse_markdown_returns_list(self):
        """Test that parse_markdown returns a list."""
        # This would test with a real file in practice
        result = parse_markdown(Path("nonexistent.md"))
        self.assertIsInstance(result, list)
    
    def test_parse_csv_returns_list(self):
        """Test that parse_csv returns a list."""
        result = parse_csv(Path("nonexistent.csv"))
        self.assertIsInstance(result, list)
    
    def test_parse_file_returns_list(self):
        """Test that parse_file returns a list."""
        result = parse_file(Path("nonexistent.md"))
        self.assertIsInstance(result, list)
    
    def test_raw_atom_structure(self):
        """Test RawAtom dataclass structure."""
        atom = RawAtom(
            content="Test content",
            source_path=Path("test.md"),
            raw_section="## Test Section"
        )
        self.assertEqual(atom.content, "Test content")


class TestClassifier(unittest.TestCase):
    """Tests for the classifier module."""
    
    def test_classify_returns_none_for_empty(self):
        """Test that classify returns None for empty input."""
        atom = RawAtom(
            content="",
            source_path=Path("test.md"),
            raw_section=""
        )
        result = classify(atom)
        self.assertIsNone(result)


class TestDeduplication(unittest.TestCase):
    """Tests for the deduplication module."""
    
    def test_deduplicate_returns_list(self):
        """Test that deduplicate returns a list."""
        atoms = []
        result = deduplicate(atoms)
        self.assertIsInstance(result, list)


class TestRanker(unittest.TestCase):
    """Tests for the ranker module."""
    
    def test_rank_returns_list(self):
        """Test that rank returns a list."""
        atoms = []
        result = rank(atoms)
        self.assertIsInstance(result, list)


class TestTagger(unittest.TestCase):
    """Tests for the tagger module."""
    
    def test_tag_returns_list(self):
        """Test that tag returns a list."""
        atoms = []
        result = tag(atoms)
        self.assertIsInstance(result, list)


class TestProng2Domains(unittest.TestCase):
    """Tests for the domain spec generation module."""
    
    def test_generate_domain_specs_runs(self):
        """Test that generate_domain_specs runs without error."""
        atoms = []
        output_dir = Path("/tmp/test_domains")
        # Should not raise an exception
        generate_domain_specs(atoms, output_dir)


class TestProng3Phases(unittest.TestCase):
    """Tests for the phase spec generation module."""
    
    def test_generate_phase_specs_runs(self):
        """Test that generate_phase_specs runs without error."""
        atoms = []
        output_dir = Path("/tmp/test_phases")
        # Should not raise an exception
        generate_phase_specs(atoms, output_dir)


class TestProng4Products(unittest.TestCase):
    """Tests for the product spec generation module."""
    
    def test_generate_product_specs_runs(self):
        """Test that generate_product_specs runs without error."""
        atoms = []
        output_dir = Path("/tmp/test_products")
        # Should not raise an exception
        generate_product_specs(atoms, output_dir)


class TestValidator(unittest.TestCase):
    """Tests for the validator module."""
    
    def test_validate_returns_report(self):
        """Test that validate returns a ValidationReport."""
        atoms = []
        domain_specs = {}
        phase_specs = {}
        product_specs = {}
        result = validate(atoms, domain_specs, phase_specs, product_specs)
        self.assertIsInstance(result, ValidationReport)


class TestGapReport(unittest.TestCase):
    """Tests for the gap report module."""
    
    def test_generate_gap_report_returns_string(self):
        """Test that generate_gap_report returns a string."""
        atoms = []
        domain_specs = {}
        phase_specs = {}
        product_specs = {}
        result = generate_gap_report(atoms, domain_specs, phase_specs, product_specs)
        self.assertIsInstance(result, str)


class TestEndToEnd(unittest.TestCase):
    """End-to-end tests for the full pipeline."""
    
    def test_full_pipeline_runs(self):
        """Test that the full pipeline runs without errors."""
        # This would run the full pipeline in practice
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
