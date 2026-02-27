"""
Knowledge Atom Extraction System for Multi-Prong Research Distillation

Processes research files in docs/research/ directory and extracts structured knowledge atoms
according to the defined schema and extraction rules.
"""

import json
import re
import os
import glob
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
from collections import defaultdict
import hashlib
import math
from concurrent.futures import ThreadPoolExecutor


@dataclass
class KnowledgeAtom:
    """Data model for a knowledge atom."""
    id: str
    content: str
    type: str  # pattern, anti-pattern, principle, finding
    category: str
    evidence_strength: float  # 0.0-1.0
    specificity: float  # 0.0-1.0
    tags: List[str] = None
    confidence: str  # HIGH, MEDIUM, LOW
    sources: List[Dict[str, Any]] = None
    timestamp: str = None
    relationships: Dict[str, List[str]] = None
    validation: Dict[str, Any] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.sources is None:
            self.sources = []
        if self.relationships is None:
            self.relationships = {"upstream": [], "downstream": []}
        if self.validation is None:
            self.validation = {
                "schema_compliant": True,
                "duplicate_check": False,
                "ranking_applied": False
            }
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat() + "Z"


class AtomExtractor:
    """Main class for extracting knowledge atoms from research files."""

    def __init__(self, research_dir: str = "docs/research"):
        self.research_dir = research_dir
        self.extracted_atoms: List[KnowledgeAtom] = []
        self.file_index = {}
        self.pattern_cache = {}
        
        # Regex patterns for extraction
        self.patterns = {
            "design_pattern": re.compile(
                r'^###\s+(Pattern|Name):\s+(.+)$\n^\*\*Description\*\*:\s+(.+)$\n^\*\*When\s+to\s+Use\*\*:\s+(.+)$\n^\*\*Tradeoffs\*\*:\n\s*-\s+\+\+\+\s+(.+)$\n\s*-\s+-\--\s+(.+)$',
                re.MULTILINE
            ),
            "anti_pattern": re.compile(
                r'^###\s+(Anti-Pattern|Name):\s+(.+)$\n^\*\*Description\*\*:\s+(.+)$\n^\*\*Failure\s+Mode\*\*:\s+(.+)$\n^\*\*Mitigation\*\*:\s+(.+)$',
                re.MULTILINE
            ),
            "research_finding": re.compile(
                r'^\*\*Confidence\*\*:\s+(HIGH|MEDIUM|LOW)\s+-\s+(.+)$\n^\*\*Source\*\*:\s+(.+)$\n^\*\*Evidence\*\*:\s+(.+)$',
                re.MULTILINE
            ),
            "principle": re.compile(
                r'^####\s+([A-Z\s]+)\s+Principle\s+\((.+)\)$\n^\*\*Description\*\*:\s+(.+)$\n^\*\*Evidence\*\*:\s+(.+)$',
                re.MULTILINE
            ),
            "guideline": re.compile(
                r'^\*\*Guideline\*\*:\s+(.+)$\n^\*\*Context\*\*:\s+(.+)$\n^\*\*Implementation\*\*:\s+(.+)$',
                re.MULTILINE
            )
        }

    def extract_from_file(self, file_path: str) -> List[KnowledgeAtom]:
        """Extract knowledge atoms from a single research file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            atoms = []
            
            # Extract category from file path
            category = self._extract_category(file_path)
            
            # Extract design patterns
            atoms.extend(self._extract_design_patterns(content, file_path, category))
            
            # Extract anti-patterns
            atoms.extend(self._extract_anti_patterns(content, file_path, category))
            
            # Extract research findings
            atoms.extend(self._extract_research_findings(content, file_path, category))
            
            # Extract principles
            atoms.extend(self._extract_principles(content, file_path, category))
            
            # Extract guidelines
            atoms.extend(self._extract_guidelines(content, file_path, category))
            
            return atoms
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return []

    def _extract_category(self, file_path: str) -> str:
        """Extract category from file path."""
        path = Path(file_path)
        parts = path.parts
        
        # Find the first numeric directory (01_, 02_, etc.)
        for part in parts:
            if part.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_')):
                return part[3:]  # Remove the numeric prefix
        
        return "uncategorized"

    def _extract_design_patterns(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract design patterns from content."""
        atoms = []
        matches = self.patterns["design_pattern"].finditer(content)
        
        for match in matches:
            try:
                name = match.group(2).strip()
                description = match.group(3).strip()
                when_to_use = match.group(4).strip()
                tradeoffs_pro = match.group(5).strip()
                tradeoffs_con = match.group(6).strip()
                
                content_str = f"**Pattern**: {name}\n\n**Description**: {description}\n\n**When to Use**: {when_to_use}\n\n**Tradeoffs**:\n- +++ {tradeoffs_pro}\n- --- {tradeoffs_con}"
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(name, "pattern"),
                    content=content_str,
                    type="pattern",
                    category=category,
                    evidence_strength=0.85,
                    specificity=0.9,
                    tags=["pattern", "design", "architecture"],
                    confidence="HIGH",
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.95
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting design pattern: {e}")
                continue
        
        return atoms

    def _extract_anti_patterns(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract anti-patterns from content."""
        atoms = []
        matches = self.patterns["anti_pattern"].finditer(content)
        
        for match in matches:
            try:
                name = match.group(2).strip()
                description = match.group(3).strip()
                failure_mode = match.group(4).strip()
                mitigation = match.group(5).strip()
                
                content_str = f"**Anti-Pattern**: {name}\n\n**Description**: {description}\n\n**Failure Mode**: {failure_mode}\n\n**Mitigation**: {mitigation}"
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(name, "anti-pattern"),
                    content=content_str,
                    type="anti-pattern",
                    category=category,
                    evidence_strength=0.75,
                    specificity=0.85,
                    tags=["anti-pattern", "failure-mode", "mitigation"],
                    confidence="MEDIUM",
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.9
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting anti-pattern: {e}")
                continue
        
        return atoms

    def _extract_research_findings(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract research findings from content."""
        atoms = []
        matches = self.patterns["research_finding"].finditer(content)
        
        for match in matches:
            try:
                confidence = match.group(1).strip()
                finding = match.group(2).strip()
                source = match.group(3).strip()
                evidence = match.group(4).strip()
                
                content_str = f"**Confidence**: {confidence} - {finding}\n\n**Source**: {source}\n\n**Evidence**: {evidence}"
                
                # Calculate evidence strength based on confidence
                evidence_strength = {
                    "HIGH": 0.9,
                    "MEDIUM": 0.7,
                    "LOW": 0.4
                }.get(confidence, 0.5)
                
                specificity = 0.8 if evidence_strength > 0.7 else 0.6
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(finding, "finding"),
                    content=content_str,
                    type="finding",
                    category=category,
                    evidence_strength=evidence_strength,
                    specificity=specificity,
                    tags=["research", "finding", "evidence"],
                    confidence=confidence,
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.85
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting research finding: {e}")
                continue
        
        return atoms

    def _extract_principles(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract principles from content."""
        atoms = []
        matches = self.patterns["principle"].finditer(content)
        
        for match in matches:
            try:
                name = match.group(1).strip()
                description = match.group(3).strip()
                evidence = match.group(4).strip()
                
                content_str = f"**Principle**: {name}\n\n**Description**: {description}\n\n**Evidence**: {evidence}"
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(name, "principle"),
                    content=content_str,
                    type="principle",
                    category=category,
                    evidence_strength=0.8,
                    specificity=0.85,
                    tags=["principle", "foundation", "concept"],
                    confidence="HIGH",
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.9
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting principle: {e}")
                continue
        
        return atoms

    def _extract_guidelines(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract guidelines from content."""
        atoms = []
        matches = self.patterns["guideline"].finditer(content)
        
        for match in matches:
            try:
                guideline = match.group(1).strip()
                context = match.group(2).strip()
                implementation = match.group(3).strip()
                
                content_str = f"**Guideline**: {guideline}\n\n**Context**: {context}\n\n**Implementation**: {implementation}"
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(guideline, "guideline"),
                    content=content_str,
                    type="principle",  # Treat guidelines as principles
                    category=category,
                    evidence_strength=0.7,
                    specificity=0.75,
                    tags=["guideline", "recommendation", "implementation"],
                    confidence="MEDIUM",
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.8
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting guideline: {e}")
                continue
        
        return atoms

    def _generate_atom_id(self, content: str, atom_type: str) -> str:
        """Generate unique ID for atom."""
        hash_input = f"{atom_type}_{content}"
        hash_digest = hashlib.md5(hash_input.encode('utf-8')).hexdigest()[:8]
        return f"atom_{hash_digest}"

    def _get_match_lines(self, content: str, match) -> List[int]:
        """Get line numbers for match."""
        start = match.start()
        end = match.end()
        
        # Find line numbers
        lines = content[:start].count('\n') + 1
        end_lines = content[:end].count('\n') + 1
        
        return list(range(lines, end_lines + 1))

    def process_all_files(self) -> List[KnowledgeAtom]:
        """Process all research files and extract atoms."""
        research_files = glob.glob(os.path.join(self.research_dir, '**', '*.md'), recursive=True)
        
        print(f"Found {len(research_files)} research files to process")
        
        # Process files in parallel for better performance
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(self.extract_from_file, research_files))
        
        # Flatten the list of lists
        all_atoms = [atom for sublist in results for atom in sublist]
        
        print(f"Extracted {len(all_atoms)} knowledge atoms")
        return all_atoms


class DeduplicationEngine:
    """Handles deduplication of knowledge atoms."""

    def __init__(self):
        self.similarity_threshold = 0.85

    def calculate_similarity(self, atom1: KnowledgeAtom, atom2: KnowledgeAtom) -> float:
        """Calculate similarity between two atoms."""
        # Simple content similarity based on shared words
        content1 = atom1.content.lower()
        content2 = atom2.content.lower()
        
        words1 = set(content1.split())
        words2 = set(content2.split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)

    def deduplicate(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Remove duplicate atoms."""
        unique_atoms = []
        seen_hashes = set()
        
        for atom in atoms:
            # Create a hash of the content for quick comparison
            content_hash = hashlib.md5(atom.content.encode('utf-8')).hexdigest()
            
            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                unique_atoms.append(atom)
        
        print(f"After deduplication: {len(unique_atoms)} atoms")
        return unique_atoms


class RankingSystem:
    """Handles ranking of knowledge atoms."""

    def __init__(self):
        self.foundational_threshold = 0.85
        self.critical_threshold = 0.70
        self.useful_threshold = 0.50

    def calculate_score(self, atom: KnowledgeAtom) -> float:
        """Calculate ranking score for an atom."""
        evidence_weight = 0.6
        specificity_weight = 0.3
        confidence_weight = 0.1
        
        evidence_score = atom.evidence_strength
        specificity_score = atom.specificity
        
        confidence_score = {
            'HIGH': 1.0,
            'MEDIUM': 0.7,
            'LOW': 0.3
        }.get(atom.confidence, 0.5)
        
        return (
            evidence_weight * evidence_score +
            specificity_weight * specificity_score +
            confidence_weight * confidence_score
        )

    def rank_atoms(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Rank atoms and assign categories."""
        # Calculate scores for all atoms
        for atom in atoms:
            atom.validation["ranking_applied"] = True
            atom.evidence_strength = self.calculate_score(atom)
        
        # Sort by score (descending)
        atoms.sort(key=lambda a: a.evidence_strength, reverse=True)
        
        # Assign categories
        for atom in atoms:
            score = atom.evidence_strength
            if score > self.foundational_threshold:
                atom.relationships["category"] = "foundational"
            elif score > self.critical_threshold:
                atom.relationships["category"] = "critical"
            elif score > self.useful_threshold:
                atom.relationships["category"] = "useful"
            else:
                atom.relationships["category"] = "exploratory"
        
        return atoms


class RegistryManager:
    """Manages the knowledge atom registry in JSONL format."""

    def __init__(self, output_file: str = "knowledge_atoms.jsonl"):
        self.output_file = output_file

    def save_atoms(self, atoms: List[KnowledgeAtom]):
        """Save atoms to JSONL file."""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            for atom in atoms:
                # Convert dataclass to dict and then to JSON
                atom_dict = asdict(atom)
                f.write(json.dumps(atom_dict) + '\n')
        
        print(f"Saved {len(atoms)} atoms to {self.output_file}")

    def load_atoms(self) -> List[KnowledgeAtom]:
        """Load atoms from JSONL file."""
        atoms = []
        
        if not os.path.exists(self.output_file):
            return atoms
        
        with open(self.output_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    atom_dict = json.loads(line)
                    atom = KnowledgeAtom(**atom_dict)
                    atoms.append(atom)
                except Exception as e:
                    print(f"Error loading atom: {e}")
                    continue
        
        return atoms


def main():
    """Main execution function."""
    print("Starting Knowledge Atom Extraction System...")
    
    # Initialize components
    extractor = AtomExtractor()
    deduplicator = DeduplicationEngine()
    ranker = RankingSystem()
    registry = RegistryManager()
    
    # Step 1: Extract atoms from all research files
    print("Step 1: Extracting knowledge atoms...")
    atoms = extractor.process_all_files()
    
    # Step 2: Deduplicate atoms
    print("Step 2: Deduplicating atoms...")
    atoms = deduplicator.deduplicate(atoms)
    
    # Step 3: Rank and categorize atoms
    print("Step 3: Ranking and categorizing atoms...")
    atoms = ranker.rank_atoms(atoms)
    
    # Step 4: Save to registry
    print("Step 4: Saving to knowledge atom registry...")
    registry.save_atoms(atoms)
    
    print("\nExtraction complete!")
    print(f"Total atoms processed: {len(atoms)}")
    print(f"Foundational atoms: {sum(1 for a in atoms if a.relationships.get('category') == 'foundational')}")
    print(f"Critical atoms: {sum(1 for a in atoms if a.relationships.get('category') == 'critical')}")
    print(f"Useful atoms: {sum(1 for a in atoms if a.relationships.get('category') == 'useful')}")
    print(f"Exploratory atoms: {sum(1 for a in atoms if a.relationships.get('category') == 'exploratory')}")


if __name__ == "__main__":
    main()Knowledge Atom Extraction System for Multi-Prong Research Distillation

Processes research files in docs/research/ directory and extracts structured knowledge atoms
according to the defined schema and extraction rules.
"""

import json
import re
import os
import glob
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
from collections import defaultdict
import hashlib
import math
from concurrent.futures import ThreadPoolExecutor


@dataclass
class KnowledgeAtom:
    """Data model for a knowledge atom."""
    id: str
    content: str
    type: str  # pattern, anti-pattern, principle, finding
    category: str
    evidence_strength: float  # 0.0-1.0
    specificity: float  # 0.0-1.0
    tags: List[str] = None
    confidence: str  # HIGH, MEDIUM, LOW
    sources: List[Dict[str, Any]] = None
    timestamp: str = None
    relationships: Dict[str, List[str]] = None
    validation: Dict[str, Any] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.sources is None:
            self.sources = []
        if self.relationships is None:
            self.relationships = {"upstream": [], "downstream": []}
        if self.validation is None:
            self.validation = {
                "schema_compliant": True,
                "duplicate_check": False,
                "ranking_applied": False
            }
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat() + "Z"


class AtomExtractor:
    """Main class for extracting knowledge atoms from research files."""

    def __init__(self, research_dir: str = "docs/research"):
        self.research_dir = research_dir
        self.extracted_atoms: List[KnowledgeAtom] = []
        self.file_index = {}
        self.pattern_cache = {}
        
        # Regex patterns for extraction
        self.patterns = {
            "design_pattern": re.compile(
                r'^###\s+(Pattern|Name):\s+(.+)$\n^\*\*Description\*\*:\s+(.+)$\n^\*\*When\s+to\s+Use\*\*:\s+(.+)$\n^\*\*Tradeoffs\*\*:\n\s*-\s+\+\+\+\s+(.+)$\n\s*-\s+-\--\s+(.+)$',
                re.MULTILINE
            ),
            "anti_pattern": re.compile(
                r'^###\s+(Anti-Pattern|Name):\s+(.+)$\n^\*\*Description\*\*:\s+(.+)$\n^\*\*Failure\s+Mode\*\*:\s+(.+)$\n^\*\*Mitigation\*\*:\s+(.+)$',
                re.MULTILINE
            ),
            "research_finding": re.compile(
                r'^\*\*Confidence\*\*:\s+(HIGH|MEDIUM|LOW)\s+-\s+(.+)$\n^\*\*Source\*\*:\s+(.+)$\n^\*\*Evidence\*\*:\s+(.+)$',
                re.MULTILINE
            ),
            "principle": re.compile(
                r'^####\s+([A-Z\s]+)\s+Principle\s+\((.+)\)$\n^\*\*Description\*\*:\s+(.+)$\n^\*\*Evidence\*\*:\s+(.+)$',
                re.MULTILINE
            ),
            "guideline": re.compile(
                r'^\*\*Guideline\*\*:\s+(.+)$\n^\*\*Context\*\*:\s+(.+)$\n^\*\*Implementation\*\*:\s+(.+)$',
                re.MULTILINE
            )
        }

    def extract_from_file(self, file_path: str) -> List[KnowledgeAtom]:
        """Extract knowledge atoms from a single research file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            atoms = []
            
            # Extract category from file path
            category = self._extract_category(file_path)
            
            # Extract design patterns
            atoms.extend(self._extract_design_patterns(content, file_path, category))
            
            # Extract anti-patterns
            atoms.extend(self._extract_anti_patterns(content, file_path, category))
            
            # Extract research findings
            atoms.extend(self._extract_research_findings(content, file_path, category))
            
            # Extract principles
            atoms.extend(self._extract_principles(content, file_path, category))
            
            # Extract guidelines
            atoms.extend(self._extract_guidelines(content, file_path, category))
            
            return atoms
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return []

    def _extract_category(self, file_path: str) -> str:
        """Extract category from file path."""
        path = Path(file_path)
        parts = path.parts
        
        # Find the first numeric directory (01_, 02_, etc.)
        for part in parts:
            if part.startswith(('01_', '02_', '03_', '04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_', '12_')):
                return part[3:]  # Remove the numeric prefix
        
        return "uncategorized"

    def _extract_design_patterns(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract design patterns from content."""
        atoms = []
        matches = self.patterns["design_pattern"].finditer(content)
        
        for match in matches:
            try:
                name = match.group(2).strip()
                description = match.group(3).strip()
                when_to_use = match.group(4).strip()
                tradeoffs_pro = match.group(5).strip()
                tradeoffs_con = match.group(6).strip()
                
                content_str = f"**Pattern**: {name}\n\n**Description**: {description}\n\n**When to Use**: {when_to_use}\n\n**Tradeoffs**:\n- +++ {tradeoffs_pro}\n- --- {tradeoffs_con}"
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(name, "pattern"),
                    content=content_str,
                    type="pattern",
                    category=category,
                    evidence_strength=0.85,
                    specificity=0.9,
                    tags=["pattern", "design", "architecture"],
                    confidence="HIGH",
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.95
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting design pattern: {e}")
                continue
        
        return atoms

    def _extract_anti_patterns(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract anti-patterns from content."""
        atoms = []
        matches = self.patterns["anti_pattern"].finditer(content)
        
        for match in matches:
            try:
                name = match.group(2).strip()
                description = match.group(3).strip()
                failure_mode = match.group(4).strip()
                mitigation = match.group(5).strip()
                
                content_str = f"**Anti-Pattern**: {name}\n\n**Description**: {description}\n\n**Failure Mode**: {failure_mode}\n\n**Mitigation**: {mitigation}"
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(name, "anti-pattern"),
                    content=content_str,
                    type="anti-pattern",
                    category=category,
                    evidence_strength=0.75,
                    specificity=0.85,
                    tags=["anti-pattern", "failure-mode", "mitigation"],
                    confidence="MEDIUM",
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.9
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting anti-pattern: {e}")
                continue
        
        return atoms

    def _extract_research_findings(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract research findings from content."""
        atoms = []
        matches = self.patterns["research_finding"].finditer(content)
        
        for match in matches:
            try:
                confidence = match.group(1).strip()
                finding = match.group(2).strip()
                source = match.group(3).strip()
                evidence = match.group(4).strip()
                
                content_str = f"**Confidence**: {confidence} - {finding}\n\n**Source**: {source}\n\n**Evidence**: {evidence}"
                
                # Calculate evidence strength based on confidence
                evidence_strength = {
                    "HIGH": 0.9,
                    "MEDIUM": 0.7,
                    "LOW": 0.4
                }.get(confidence, 0.5)
                
                specificity = 0.8 if evidence_strength > 0.7 else 0.6
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(finding, "finding"),
                    content=content_str,
                    type="finding",
                    category=category,
                    evidence_strength=evidence_strength,
                    specificity=specificity,
                    tags=["research", "finding", "evidence"],
                    confidence=confidence,
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.85
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting research finding: {e}")
                continue
        
        return atoms

    def _extract_principles(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract principles from content."""
        atoms = []
        matches = self.patterns["principle"].finditer(content)
        
        for match in matches:
            try:
                name = match.group(1).strip()
                description = match.group(3).strip()
                evidence = match.group(4).strip()
                
                content_str = f"**Principle**: {name}\n\n**Description**: {description}\n\n**Evidence**: {evidence}"
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(name, "principle"),
                    content=content_str,
                    type="principle",
                    category=category,
                    evidence_strength=0.8,
                    specificity=0.85,
                    tags=["principle", "foundation", "concept"],
                    confidence="HIGH",
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.9
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting principle: {e}")
                continue
        
        return atoms

    def _extract_guidelines(self, content: str, file_path: str, category: str) -> List[KnowledgeAtom]:
        """Extract guidelines from content."""
        atoms = []
        matches = self.patterns["guideline"].finditer(content)
        
        for match in matches:
            try:
                guideline = match.group(1).strip()
                context = match.group(2).strip()
                implementation = match.group(3).strip()
                
                content_str = f"**Guideline**: {guideline}\n\n**Context**: {context}\n\n**Implementation**: {implementation}"
                
                atom = KnowledgeAtom(
                    id=self._generate_atom_id(guideline, "guideline"),
                    content=content_str,
                    type="principle",  # Treat guidelines as principles
                    category=category,
                    evidence_strength=0.7,
                    specificity=0.75,
                    tags=["guideline", "recommendation", "implementation"],
                    confidence="MEDIUM",
                    sources=[{
                        "file": file_path,
                        "lines": self._get_match_lines(content, match),
                        "relevance": 0.8
                    }]
                )
                atoms.append(atom)
                
            except Exception as e:
                print(f"Error extracting guideline: {e}")
                continue
        
        return atoms

    def _generate_atom_id(self, content: str, atom_type: str) -> str:
        """Generate unique ID for atom."""
        hash_input = f"{atom_type}_{content}"
        hash_digest = hashlib.md5(hash_input.encode('utf-8')).hexdigest()[:8]
        return f"atom_{hash_digest}"

    def _get_match_lines(self, content: str, match) -> List[int]:
        """Get line numbers for match."""
        start = match.start()
        end = match.end()
        
        # Find line numbers
        lines = content[:start].count('\n') + 1
        end_lines = content[:end].count('\n') + 1
        
        return list(range(lines, end_lines + 1))

    def process_all_files(self) -> List[KnowledgeAtom]:
        """Process all research files and extract atoms."""
        research_files = glob.glob(os.path.join(self.research_dir, '**', '*.md'), recursive=True)
        
        print(f"Found {len(research_files)} research files to process")
        
        # Process files in parallel for better performance
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(self.extract_from_file, research_files))
        
        # Flatten the list of lists
        all_atoms = [atom for sublist in results for atom in sublist]
        
        print(f"Extracted {len(all_atoms)} knowledge atoms")
        return all_atoms


class DeduplicationEngine:
    """Handles deduplication of knowledge atoms."""

    def __init__(self):
        self.similarity_threshold = 0.85

    def calculate_similarity(self, atom1: KnowledgeAtom, atom2: KnowledgeAtom) -> float:
        """Calculate similarity between two atoms."""
        # Simple content similarity based on shared words
        content1 = atom1.content.lower()
        content2 = atom2.content.lower()
        
        words1 = set(content1.split())
        words2 = set(content2.split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)

    def deduplicate(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Remove duplicate atoms."""
        unique_atoms = []
        seen_hashes = set()
        
        for atom in atoms:
            # Create a hash of the content for quick comparison
            content_hash = hashlib.md5(atom.content.encode('utf-8')).hexdigest()
            
            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                unique_atoms.append(atom)
        
        print(f"After deduplication: {len(unique_atoms)} atoms")
        return unique_atoms


class RankingSystem:
    """Handles ranking of knowledge atoms."""

    def __init__(self):
        self.foundational_threshold = 0.85
        self.critical_threshold = 0.70
        self.useful_threshold = 0.50

    def calculate_score(self, atom: KnowledgeAtom) -> float:
        """Calculate ranking score for an atom."""
        evidence_weight = 0.6
        specificity_weight = 0.3
        confidence_weight = 0.1
        
        evidence_score = atom.evidence_strength
        specificity_score = atom.specificity
        
        confidence_score = {
            'HIGH': 1.0,
            'MEDIUM': 0.7,
            'LOW': 0.3
        }.get(atom.confidence, 0.5)
        
        return (
            evidence_weight * evidence_score +
            specificity_weight * specificity_score +
            confidence_weight * confidence_score
        )

    def rank_atoms(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Rank atoms and assign categories."""
        # Calculate scores for all atoms
        for atom in atoms:
            atom.validation["ranking_applied"] = True
            atom.evidence_strength = self.calculate_score(atom)
        
        # Sort by score (descending)
        atoms.sort(key=lambda a: a.evidence_strength, reverse=True)
        
        # Assign categories
        for atom in atoms:
            score = atom.evidence_strength
            if score > self.foundational_threshold:
                atom.relationships["category"] = "foundational"
            elif score > self.critical_threshold:
                atom.relationships["category"] = "critical"
            elif score > self.useful_threshold:
                atom.relationships["category"] = "useful"
            else:
                atom.relationships["category"] = "exploratory"
        
        return atoms


class RegistryManager:
    """Manages the knowledge atom registry in JSONL format."""

    def __init__(self, output_file: str = "knowledge_atoms.jsonl"):
        self.output_file = output_file

    def save_atoms(self, atoms: List[KnowledgeAtom]):
        """Save atoms to JSONL file."""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            for atom in atoms:
                # Convert dataclass to dict and then to JSON
                atom_dict = asdict(atom)
                f.write(json.dumps(atom_dict) + '\n')
        
        print(f"Saved {len(atoms)} atoms to {self.output_file}")

    def load_atoms(self) -> List[KnowledgeAtom]:
        """Load atoms from JSONL file."""
        atoms = []
        
        if not os.path.exists(self.output_file):
            return atoms
        
        with open(self.output_file, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    atom_dict = json.loads(line)
                    atom = KnowledgeAtom(**atom_dict)
                    atoms.append(atom)
                except Exception as e:
                    print(f"Error loading atom: {e}")
                    continue
        
        return atoms


def main():
    """Main execution function."""
    print("Starting Knowledge Atom Extraction System...")
    
    # Initialize components
    extractor = AtomExtractor()
    deduplicator = DeduplicationEngine()
    ranker = RankingSystem()
    registry = RegistryManager()
    
    # Step 1: Extract atoms from all research files
    print("Step 1: Extracting knowledge atoms...")
    atoms = extractor.process_all_files()
    
    # Step 2: Deduplicate atoms
    print("Step 2: Deduplicating atoms...")
    atoms = deduplicator.deduplicate(atoms)
    
    # Step 3: Rank and categorize atoms
    print("Step 3: Ranking and categorizing atoms...")
    atoms = ranker.rank_atoms(atoms)
    
    # Step 4: Save to registry
    print("Step 4: Saving to knowledge atom registry...")
    registry.save_atoms(atoms)
    
    print("\nExtraction complete!")
    print(f"Total atoms processed: {len(atoms)}")
    print(f"Foundational atoms: {sum(1 for a in atoms if a.relationships.get('category') == 'foundational')}")
    print(f"Critical atoms: {sum(1 for a in atoms if a.relationships.get('category') == 'critical')}")
    print(f"Useful atoms: {sum(1 for a in atoms if a.relationships.get('category') == 'useful')}")
    print(f"Exploratory atoms: {sum(1 for a in atoms if a.relationships.get('category') == 'exploratory')}")


if __name__ == "__main__":
    main()
