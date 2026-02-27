"""
Test suite for knowledge atom extraction system.
Tests all components of the extraction system for correctness and reliability.
"""

import unittest
import tempfile
import os
import json
from pathlib import Path
from knowledge_atom_extractor.main import KnowledgeAtom, AtomExtractor, DeduplicationEngine, RankingSystem, RegistryManager


class TestKnowledgeAtom(unittest.TestCase):
    """Test cases for KnowledgeAtom data model."""
    
    def test_atom_creation(self):
        """Test basic atom creation."""
        atom = KnowledgeAtom(
            id="atom_001",
            content="Test content",
            type="pattern",
            category="test_category",
            evidence_strength=0.8,
            specificity=0.9,
            confidence="HIGH",
            sources=[{
                "file": "test.md",
                "lines": [1, 2],
                "relevance": 0.95
            }]
        )
        
        self.assertEqual(atom.id, "atom_001")
        self.assertEqual(atom.content, "Test content")
        self.assertEqual(atom.type, "pattern")
        self.assertEqual(atom.category, "test_category")
        self.assertEqual(atom.evidence_strength, 0.8)
        self.assertEqual(atom.specificity, 0.9)
        self.assertEqual(atom.confidence, "HIGH")
        self.assertEqual(len(atom.sources), 1)
        self.assertEqual(atom.sources[0]["file"], "test.md")
        self.assertEqual(atom.sources[0]["lines"], [1, 2])
        self.assertEqual(atom.sources[0]["relevance"], 0.95)
        self.assertTrue(atom.validation["schema_compliant"])
        self.assertFalse(atom.validation["duplicate_check"])
        self.assertFalse(atom.validation["ranking_applied"])


class TestAtomExtractor(unittest.TestCase):
    """Test cases for AtomExtractor class."""
    
    def setUp(self):
        """Set up test environment."""
        self.extractor = AtomExtractor()
        
        # Create temporary test files
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.test_dir.name, "test_pattern.md")
        
        # Create test content with patterns
        test_content = """# Test Research File

## Pattern: Test Pattern

**Description**: This is a test pattern for validation.

**When to Use**: When testing pattern extraction.

**Tradeoffs**:
- +++ Works correctly
- --- May have edge cases

**Confidence**: HIGH - This is a test pattern.

**Source**: Test file

**Evidence**: Validated through unit tests.

### Anti-Pattern: Test Anti-Pattern

**Description**: This is a test anti-pattern.

**Failure Mode**: May fail in certain conditions.

**Mitigation**: Use proper error handling.

#### Test Principle (Test Category)

**Description**: Test principle description.

**Evidence**: Validated through testing.

**Guideline**: Test guideline

**Context**: Testing context

**Implementation**: Test implementation
"""
        
        with open(self.test_file_path, 'w', encoding='utf-8') as f:
            f.write(test_content)
    
    def tearDown(self):
        """Clean up test environment."""
        self.test_dir.cleanup()
    
    def test_extract_design_pattern(self):
        """Test design pattern extraction."""
        atoms = self.extractor.extract_from_file(self.test_file_path)
        
        # Should find at least one pattern
        patterns = [a for a in atoms if a.type == "pattern"]
        self.assertGreaterEqual(len(patterns), 1)
        
        pattern = patterns[0]
        self.assertEqual(pattern.type, "pattern")
        self.assertIn("Test Pattern", pattern.content)
        self.assertIn("When testing pattern extraction", pattern.content)
        self.assertIn("Works correctly", pattern.content)
        self.assertIn("May have edge cases", pattern.content)
        self.assertEqual(pattern.confidence, "HIGH")
        self.assertEqual(pattern.category, "test")  # From test_ prefix
        self.assertGreaterEqual(len(pattern.sources), 1)
    
    def test_extract_anti_pattern(self):
        """Test anti-pattern extraction."""
        atoms = self.extractor.extract_from_file(self.test_file_path)
        
        # Should find at least one anti-pattern
        anti_patterns = [a for a in atoms if a.type == "anti-pattern"]
        self.assertGreaterEqual(len(anti_patterns), 1)
        
        anti_pattern = anti_patterns[0]
        self.assertEqual(anti_pattern.type, "anti-pattern")
        self.assertIn("Test Anti-Pattern", anti_pattern.content)
        self.assertIn("May fail in certain conditions", anti_pattern.content)
        self.assertIn("Use proper error handling", anti_pattern.content)
        self.assertEqual(anti_pattern.confidence, "MEDIUM")  # Default for anti-patterns
        self.assertEqual(anti_pattern.category, "test")
        self.assertGreaterEqual(len(anti_pattern.sources), 1)
    
    def test_extract_principle(self):
        """Test principle extraction."""
        atoms = self.extractor.extract_from_file(self.test_file_path)
        
        # Should find at least one principle
        principles = [a for a in atoms if a.type == "principle"]
        self.assertGreaterEqual(len(principles), 1)
        
        principle = principles[0]
        self.assertEqual(principle.type, "principle")
        self.assertIn("Test Principle", principle.content)
        self.assertIn("Test principle description", principle.content)
        self.assertIn("Validated through testing", principle.content)
        self.assertEqual(principle.confidence, "HIGH")
        self.assertEqual(principle.category, "test")
        self.assertGreaterEqual(len(principle.sources), 1)
    
    def test_extract_guideline(self):
        """Test guideline extraction."""
        atoms = self.extractor.extract_from_file(self.test_file_path)
        
        # Should find at least one guideline (treated as principle)
        guidelines = [a for a in atoms if a.type == "principle" and "Guideline" in a.content]
        self.assertGreaterEqual(len(guidelines), 1)
        
        guideline = guidelines[0]
        self.assertEqual(guideline.type, "principle")
        self.assertIn("Test guideline", guideline.content)
        self.assertIn("Testing context", guideline.content)
        self.assertIn("Test implementation", guideline.content)
        self.assertEqual(guideline.confidence, "MEDIUM")  # Default for guidelines
        self.assertEqual(guideline.category, "test")
        self.assertGreaterEqual(len(guideline.sources), 1)
    
    def test_category_extraction(self):
        """Test category extraction from file path."""
        # Test with different file path formats
        test_cases = [
            ("docs/research/01_meta_architecture/test.md", "meta_architecture"),
            ("docs/research/02_agent_orchestration/subdir/test.md", "agent_orchestration"),
            ("docs/research/03_context_memory_intelligence/test.md", "context_memory_intelligence"),
            ("docs/research/unknown_category/test.md", "unknown_category"),
            ("test.md", "uncategorized")
        ]
        
        for file_path, expected_category in test_cases:
            category = self.extractor._extract_category(file_path)
            self.assertEqual(category, expected_category, f"Failed for {file_path}")


class TestDeduplicationEngine(unittest.TestCase):
    """Test cases for DeduplicationEngine."""
    
    def setUp(self):
        self.deduplicator = DeduplicationEngine()
        
        # Create test atoms
        self.atom1 = KnowledgeAtom(
            id="atom_001",
            content="This is a test pattern about design patterns",
            type="pattern",
            category="test",
            evidence_strength=0.8,
            specificity=0.9,
            confidence="HIGH",
            sources=[{"file": "test1.md", "lines": [1], "relevance": 0.9}]
        )
        
        self.atom2 = KnowledgeAtom(
            id="atom_002",
            content="This is a test pattern about design patterns",
            type="pattern",
            category="test",
            evidence_strength=0.85,
            specificity=0.85,
            confidence="HIGH",
            sources=[{"file": "test2.md", "lines": [1], "relevance": 0.95}]
        )
        
        self.atom3 = KnowledgeAtom(
            id="atom_003",
            content="This is a completely different pattern",
            type="pattern",
            category="test",
            evidence_strength=0.6,
            specificity=0.7,
            confidence="MEDIUM",
            sources=[{"file": "test3.md", "lines": [1], "relevance": 0.8}]
        )
    
    def test_similarity_calculation(self):
        """Test similarity calculation."""
        # Identical content should have high similarity
        similarity = self.deduplicator.calculate_similarity(self.atom1, self.atom2)
        self.assertGreaterEqual(similarity, 0.8)
        
        # Different content should have low similarity
        similarity = self.deduplicator.calculate_similarity(self.atom1, self.atom3)
        self.assertLessEqual(similarity, 0.3)
    
    def test_deduplication(self):
        """Test deduplication process."""
        atoms = [self.atom1, self.atom2, self.atom3]
        
        unique_atoms = self.deduplicator.deduplicate(atoms)
        
        # Should have 2 unique atoms (atom1 and atom2 are duplicates)
        self.assertEqual(len(unique_atoms), 2)
        
        # Check that unique atoms contain the different content
        contents = [a.content for a in unique_atoms]
        self.assertIn(self.atom1.content, contents)
        self.assertIn(self.atom3.content, contents)


class TestRankingSystem(unittest.TestCase):
    """Test cases for RankingSystem."""
    
    def setUp(self):
        self.ranker = RankingSystem()
        
        # Create test atoms with different confidence levels
        self.atom_high = KnowledgeAtom(
            id="atom_001",
            content="High confidence pattern",
            type="pattern",
            category="test",
            evidence_strength=0.9,
            specificity=0.95,
            confidence="HIGH",
            sources=[{"file": "test.md", "lines": [1], "relevance": 0.9}]
        )
        
        self.atom_medium = KnowledgeAtom(
            id="atom_002",
            content="Medium confidence pattern",
            type="pattern",
            category="test",
            evidence_strength=0.7,
            specificity=0.8,
            confidence="MEDIUM",
            sources=[{"file": "test.md", "lines": [1], "relevance": 0.8}]
        )
        
        self.atom_low = KnowledgeAtom(
            id="atom_003",
            content="Low confidence pattern",
            type="pattern",
            category="test",
            evidence_strength=0.5,
            specificity=0.6,
            confidence="LOW",
            sources=[{"file": "test.md", "lines": [1], "relevance": 0.7}]
        )
    
    def test_score_calculation(self):
        """Test score calculation."""
        # High confidence atom should have high score
        high_score = self.ranker.calculate_score(self.atom_high)
        self.assertGreaterEqual(high_score, 0.85)
        
        # Medium confidence atom should have medium score
        medium_score = self.ranker.calculate_score(self.atom_medium)
        self.assertGreaterEqual(medium_score, 0.65)
        self.assertLessEqual(medium_score, 0.85)
        
        # Low confidence atom should have low score
        low_score = self.ranker.calculate_score(self.atom_low)
        self.assertLessEqual(low_score, 0.65)
    
    def test_ranking(self):
        """Test ranking process."""
        atoms = [self.atom_low, self.atom_high, self.atom_medium]
        
        ranked_atoms = self.ranker.rank_atoms(atoms)
        
        # Should be sorted by score (descending)
        scores = [a.evidence_strength for a in ranked_atoms]
        self.assertEqual(scores, sorted(scores, reverse=True))
        
        # Check categories
        for atom in ranked_atoms:
            if atom.evidence_strength > 0.85:
                self.assertEqual(atom.relationships.get("category"), "foundational")
            elif atom.evidence_strength > 0.70:
                self.assertEqual(atom.relationships.get("category"), "critical")
            elif atom.evidence_strength > 0.50:
                self.assertEqual(atom.relationships.get("category"), "useful")
            else:
                self.assertEqual(atom.relationships.get("category"), "exploratory")


class TestRegistryManager(unittest.TestCase):
    """Test cases for RegistryManager."""
    
    def setUp(self):
        self.registry = RegistryManager()
        
        # Create test atoms
        self.test_atoms = [
            KnowledgeAtom(
                id="atom_001",
                content="Test atom 1",
                type="pattern",
                category="test",
                evidence_strength=0.8,
                specificity=0.9,
                confidence="HIGH",
                sources=[{"file": "test.md", "lines": [1], "relevance": 0.9}]
            ),
            KnowledgeAtom(
                id="atom_002",
                content="Test atom 2",
                type="pattern",
                category="test",
                evidence_strength=0.7,
                specificity=0.8,
                confidence="MEDIUM",
                sources=[{"file": "test.md", "lines": [2], "relevance": 0.8}]
            )
        ]
    
    def test_save_and_load(self):
        """Test saving and loading atoms."""
        # Save atoms
        self.registry.save_atoms(self.test_atoms)
        
        # Load atoms
        loaded_atoms = self.registry.load_atoms()
        
        # Should have same number of atoms
        self.assertEqual(len(loaded_atoms), len(self.test_atoms))
        
        # Check that atoms match
        for original, loaded in zip(self.test_atoms, loaded_atoms):
            self.assertEqual(original.id, loaded.id)
            self.assertEqual(original.content, loaded.content)
            self.assertEqual(original.type, loaded.type)
            self.assertEqual(original.category, loaded.category)
            self.assertEqual(original.evidence_strength, loaded.evidence_strength)
            self.assertEqual(original.specificity, loaded.specificity)
            self.assertEqual(original.confidence, loaded.confidence)
            self.assertEqual(len(original.sources), len(loaded.sources))
            self.assertEqual(original.sources[0]["file"], loaded.sources[0]["file"])


def suite():
    """Create test suite."""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestKnowledgeAtom))
    test_suite.addTest(unittest.makeSuite(TestAtomExtractor))
    test_suite.addTest(unittest.makeSuite(TestDeduplicationEngine))
    test_suite.addTest(unittest.makeSuite(TestRankingSystem))
    test_suite.addTest(unittest.makeSuite(TestRegistryManager))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())Test suite for knowledge atom extraction system.
Tests all components of the extraction system for correctness and reliability.
"""

import unittest
import tempfile
import os
import json
from pathlib import Path
from knowledge_atom_extractor.main import KnowledgeAtom, AtomExtractor, DeduplicationEngine, RankingSystem, RegistryManager


class TestKnowledgeAtom(unittest.TestCase):
    """Test cases for KnowledgeAtom data model."""
    
    def test_atom_creation(self):
        """Test basic atom creation."""
        atom = KnowledgeAtom(
            id="atom_001",
            content="Test content",
            type="pattern",
            category="test_category",
            evidence_strength=0.8,
            specificity=0.9,
            confidence="HIGH",
            sources=[{
                "file": "test.md",
                "lines": [1, 2],
                "relevance": 0.95
            }]
        )
        
        self.assertEqual(atom.id, "atom_001")
        self.assertEqual(atom.content, "Test content")
        self.assertEqual(atom.type, "pattern")
        self.assertEqual(atom.category, "test_category")
        self.assertEqual(atom.evidence_strength, 0.8)
        self.assertEqual(atom.specificity, 0.9)
        self.assertEqual(atom.confidence, "HIGH")
        self.assertEqual(len(atom.sources), 1)
        self.assertEqual(atom.sources[0]["file"], "test.md")
        self.assertEqual(atom.sources[0]["lines"], [1, 2])
        self.assertEqual(atom.sources[0]["relevance"], 0.95)
        self.assertTrue(atom.validation["schema_compliant"])
        self.assertFalse(atom.validation["duplicate_check"])
        self.assertFalse(atom.validation["ranking_applied"])


class TestAtomExtractor(unittest.TestCase):
    """Test cases for AtomExtractor class."""
    
    def setUp(self):
        """Set up test environment."""
        self.extractor = AtomExtractor()
        
        # Create temporary test files
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.test_dir.name, "test_pattern.md")
        
        # Create test content with patterns
        test_content = """# Test Research File

## Pattern: Test Pattern

**Description**: This is a test pattern for validation.

**When to Use**: When testing pattern extraction.

**Tradeoffs**:
- +++ Works correctly
- --- May have edge cases

**Confidence**: HIGH - This is a test pattern.

**Source**: Test file

**Evidence**: Validated through unit tests.

### Anti-Pattern: Test Anti-Pattern

**Description**: This is a test anti-pattern.

**Failure Mode**: May fail in certain conditions.

**Mitigation**: Use proper error handling.

#### Test Principle (Test Category)

**Description**: Test principle description.

**Evidence**: Validated through testing.

**Guideline**: Test guideline

**Context**: Testing context

**Implementation**: Test implementation
"""
        
        with open(self.test_file_path, 'w', encoding='utf-8') as f:
            f.write(test_content)
    
    def tearDown(self):
        """Clean up test environment."""
        self.test_dir.cleanup()
    
    def test_extract_design_pattern(self):
        """Test design pattern extraction."""
        atoms = self.extractor.extract_from_file(self.test_file_path)
        
        # Should find at least one pattern
        patterns = [a for a in atoms if a.type == "pattern"]
        self.assertGreaterEqual(len(patterns), 1)
        
        pattern = patterns[0]
        self.assertEqual(pattern.type, "pattern")
        self.assertIn("Test Pattern", pattern.content)
        self.assertIn("When testing pattern extraction", pattern.content)
        self.assertIn("Works correctly", pattern.content)
        self.assertIn("May have edge cases", pattern.content)
        self.assertEqual(pattern.confidence, "HIGH")
        self.assertEqual(pattern.category, "test")  # From test_ prefix
        self.assertGreaterEqual(len(pattern.sources), 1)
    
    def test_extract_anti_pattern(self):
        """Test anti-pattern extraction."""
        atoms = self.extractor.extract_from_file(self.test_file_path)
        
        # Should find at least one anti-pattern
        anti_patterns = [a for a in atoms if a.type == "anti-pattern"]
        self.assertGreaterEqual(len(anti_patterns), 1)
        
        anti_pattern = anti_patterns[0]
        self.assertEqual(anti_pattern.type, "anti-pattern")
        self.assertIn("Test Anti-Pattern", anti_pattern.content)
        self.assertIn("May fail in certain conditions", anti_pattern.content)
        self.assertIn("Use proper error handling", anti_pattern.content)
        self.assertEqual(anti_pattern.confidence, "MEDIUM")  # Default for anti-patterns
        self.assertEqual(anti_pattern.category, "test")
        self.assertGreaterEqual(len(anti_pattern.sources), 1)
    
    def test_extract_principle(self):
        """Test principle extraction."""
        atoms = self.extractor.extract_from_file(self.test_file_path)
        
        # Should find at least one principle
        principles = [a for a in atoms if a.type == "principle"]
        self.assertGreaterEqual(len(principles), 1)
        
        principle = principles[0]
        self.assertEqual(principle.type, "principle")
        self.assertIn("Test Principle", principle.content)
        self.assertIn("Test principle description", principle.content)
        self.assertIn("Validated through testing", principle.content)
        self.assertEqual(principle.confidence, "HIGH")
        self.assertEqual(principle.category, "test")
        self.assertGreaterEqual(len(principle.sources), 1)
    
    def test_extract_guideline(self):
        """Test guideline extraction."""
        atoms = self.extractor.extract_from_file(self.test_file_path)
        
        # Should find at least one guideline (treated as principle)
        guidelines = [a for a in atoms if a.type == "principle" and "Guideline" in a.content]
        self.assertGreaterEqual(len(guidelines), 1)
        
        guideline = guidelines[0]
        self.assertEqual(guideline.type, "principle")
        self.assertIn("Test guideline", guideline.content)
        self.assertIn("Testing context", guideline.content)
        self.assertIn("Test implementation", guideline.content)
        self.assertEqual(guideline.confidence, "MEDIUM")  # Default for guidelines
        self.assertEqual(guideline.category, "test")
        self.assertGreaterEqual(len(guideline.sources), 1)
    
    def test_category_extraction(self):
        """Test category extraction from file path."""
        # Test with different file path formats
        test_cases = [
            ("docs/research/01_meta_architecture/test.md", "meta_architecture"),
            ("docs/research/02_agent_orchestration/subdir/test.md", "agent_orchestration"),
            ("docs/research/03_context_memory_intelligence/test.md", "context_memory_intelligence"),
            ("docs/research/unknown_category/test.md", "unknown_category"),
            ("test.md", "uncategorized")
        ]
        
        for file_path, expected_category in test_cases:
            category = self.extractor._extract_category(file_path)
            self.assertEqual(category, expected_category, f"Failed for {file_path}")


class TestDeduplicationEngine(unittest.TestCase):
    """Test cases for DeduplicationEngine."""
    
    def setUp(self):
        self.deduplicator = DeduplicationEngine()
        
        # Create test atoms
        self.atom1 = KnowledgeAtom(
            id="atom_001",
            content="This is a test pattern about design patterns",
            type="pattern",
            category="test",
            evidence_strength=0.8,
            specificity=0.9,
            confidence="HIGH",
            sources=[{"file": "test1.md", "lines": [1], "relevance": 0.9}]
        )
        
        self.atom2 = KnowledgeAtom(
            id="atom_002",
            content="This is a test pattern about design patterns",
            type="pattern",
            category="test",
            evidence_strength=0.85,
            specificity=0.85,
            confidence="HIGH",
            sources=[{"file": "test2.md", "lines": [1], "relevance": 0.95}]
        )
        
        self.atom3 = KnowledgeAtom(
            id="atom_003",
            content="This is a completely different pattern",
            type="pattern",
            category="test",
            evidence_strength=0.6,
            specificity=0.7,
            confidence="MEDIUM",
            sources=[{"file": "test3.md", "lines": [1], "relevance": 0.8}]
        )
    
    def test_similarity_calculation(self):
        """Test similarity calculation."""
        # Identical content should have high similarity
        similarity = self.deduplicator.calculate_similarity(self.atom1, self.atom2)
        self.assertGreaterEqual(similarity, 0.8)
        
        # Different content should have low similarity
        similarity = self.deduplicator.calculate_similarity(self.atom1, self.atom3)
        self.assertLessEqual(similarity, 0.3)
    
    def test_deduplication(self):
        """Test deduplication process."""
        atoms = [self.atom1, self.atom2, self.atom3]
        
        unique_atoms = self.deduplicator.deduplicate(atoms)
        
        # Should have 2 unique atoms (atom1 and atom2 are duplicates)
        self.assertEqual(len(unique_atoms), 2)
        
        # Check that unique atoms contain the different content
        contents = [a.content for a in unique_atoms]
        self.assertIn(self.atom1.content, contents)
        self.assertIn(self.atom3.content, contents)


class TestRankingSystem(unittest.TestCase):
    """Test cases for RankingSystem."""
    
    def setUp(self):
        self.ranker = RankingSystem()
        
        # Create test atoms with different confidence levels
        self.atom_high = KnowledgeAtom(
            id="atom_001",
            content="High confidence pattern",
            type="pattern",
            category="test",
            evidence_strength=0.9,
            specificity=0.95,
            confidence="HIGH",
            sources=[{"file": "test.md", "lines": [1], "relevance": 0.9}]
        )
        
        self.atom_medium = KnowledgeAtom(
            id="atom_002",
            content="Medium confidence pattern",
            type="pattern",
            category="test",
            evidence_strength=0.7,
            specificity=0.8,
            confidence="MEDIUM",
            sources=[{"file": "test.md", "lines": [1], "relevance": 0.8}]
        )
        
        self.atom_low = KnowledgeAtom(
            id="atom_003",
            content="Low confidence pattern",
            type="pattern",
            category="test",
            evidence_strength=0.5,
            specificity=0.6,
            confidence="LOW",
            sources=[{"file": "test.md", "lines": [1], "relevance": 0.7}]
        )
    
    def test_score_calculation(self):
        """Test score calculation."""
        # High confidence atom should have high score
        high_score = self.ranker.calculate_score(self.atom_high)
        self.assertGreaterEqual(high_score, 0.85)
        
        # Medium confidence atom should have medium score
        medium_score = self.ranker.calculate_score(self.atom_medium)
        self.assertGreaterEqual(medium_score, 0.65)
        self.assertLessEqual(medium_score, 0.85)
        
        # Low confidence atom should have low score
        low_score = self.ranker.calculate_score(self.atom_low)
        self.assertLessEqual(low_score, 0.65)
    
    def test_ranking(self):
        """Test ranking process."""
        atoms = [self.atom_low, self.atom_high, self.atom_medium]
        
        ranked_atoms = self.ranker.rank_atoms(atoms)
        
        # Should be sorted by score (descending)
        scores = [a.evidence_strength for a in ranked_atoms]
        self.assertEqual(scores, sorted(scores, reverse=True))
        
        # Check categories
        for atom in ranked_atoms:
            if atom.evidence_strength > 0.85:
                self.assertEqual(atom.relationships.get("category"), "foundational")
            elif atom.evidence_strength > 0.70:
                self.assertEqual(atom.relationships.get("category"), "critical")
            elif atom.evidence_strength > 0.50:
                self.assertEqual(atom.relationships.get("category"), "useful")
            else:
                self.assertEqual(atom.relationships.get("category"), "exploratory")


class TestRegistryManager(unittest.TestCase):
    """Test cases for RegistryManager."""
    
    def setUp(self):
        self.registry = RegistryManager()
        
        # Create test atoms
        self.test_atoms = [
            KnowledgeAtom(
                id="atom_001",
                content="Test atom 1",
                type="pattern",
                category="test",
                evidence_strength=0.8,
                specificity=0.9,
                confidence="HIGH",
                sources=[{"file": "test.md", "lines": [1], "relevance": 0.9}]
            ),
            KnowledgeAtom(
                id="atom_002",
                content="Test atom 2",
                type="pattern",
                category="test",
                evidence_strength=0.7,
                specificity=0.8,
                confidence="MEDIUM",
                sources=[{"file": "test.md", "lines": [2], "relevance": 0.8}]
            )
        ]
    
    def test_save_and_load(self):
        """Test saving and loading atoms."""
        # Save atoms
        self.registry.save_atoms(self.test_atoms)
        
        # Load atoms
        loaded_atoms = self.registry.load_atoms()
        
        # Should have same number of atoms
        self.assertEqual(len(loaded_atoms), len(self.test_atoms))
        
        # Check that atoms match
        for original, loaded in zip(self.test_atoms, loaded_atoms):
            self.assertEqual(original.id, loaded.id)
            self.assertEqual(original.content, loaded.content)
            self.assertEqual(original.type, loaded.type)
            self.assertEqual(original.category, loaded.category)
            self.assertEqual(original.evidence_strength, loaded.evidence_strength)
            self.assertEqual(original.specificity, loaded.specificity)
            self.assertEqual(original.confidence, loaded.confidence)
            self.assertEqual(len(original.sources), len(loaded.sources))
            self.assertEqual(original.sources[0]["file"], loaded.sources[0]["file"])


def suite():
    """Create test suite."""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestKnowledgeAtom))
    test_suite.addTest(unittest.makeSuite(TestAtomExtractor))
    test_suite.addTest(unittest.makeSuite(TestDeduplicationEngine))
    test_suite.addTest(unittest.makeSuite(TestRankingSystem))
    test_suite.addTest(unittest.makeSuite(TestRegistryManager))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
