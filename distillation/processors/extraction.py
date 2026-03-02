"""Knowledge atom extraction processor."""

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ..models import (
    AtomType,
    EvidenceStrength,
    ExtractionConfig,
    KnowledgeAtom,
    ResearchFile,
)


@dataclass
class ExtractionPattern:
    """Pattern for extracting knowledge atoms."""

    name: str
    pattern: str
    atom_type: AtomType
    evidence_keywords: list[str]
    priority: int = 1
    enabled: bool = True

    def matches(self, text: str) -> bool:
        """Check if this pattern matches the given text."""
        return bool(re.search(self.pattern, text, re.IGNORECASE | re.MULTILINE))


class AtomExtractor:
    """Extracts knowledge atoms from research files using pattern-based rules."""

    def __init__(self, config: Optional[ExtractionConfig] = None, min_evidence_strength: str = "MODERATE"):
        """Initialize the atom extractor.

        Args:
            config: Extraction configuration. If None, uses defaults.
            min_evidence_strength: Minimum evidence strength to extract (STRONG, MODERATE, WEAK).
        """
        self.config = config or ExtractionConfig()
        self.min_evidence_strength = min_evidence_strength
        self.patterns = self._load_default_patterns()
        self._load_custom_patterns()

    def _load_default_patterns(self) -> list[ExtractionPattern]:
        """Load the default extraction patterns based on the distillation rules."""
        return [
            # TECHNIQUE patterns
            ExtractionPattern(
                name="technique_procedure",
                pattern=r"(?:use|implement|apply|perform|execute)\s+([^.!?]+?)(?:\s+to|\s+for|\s+which|\s+that)",
                atom_type=AtomType.TECHNIQUE,
                evidence_keywords=["measured", "improves", "reduces", "achieves", "demonstrates"],
                priority=10
            ),
            ExtractionPattern(
                name="technique_named_method",
                pattern=r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*):\s*([^.!?]+?)(?:\s+improves|\s+reduces|\s+achieves|\s+provides)",
                atom_type=AtomType.TECHNIQUE,
                evidence_keywords=["improves", "reduces", "achieves", "provides", "enables"],
                priority=9
            ),

            # METRIC patterns
            ExtractionPattern(
                name="metric_percentage",
                pattern=r"(\d+(?:\.\d+)?%)\s+(?:improvement|reduction|increase|decrease|precision|recall|accuracy)",
                atom_type=AtomType.METRIC,
                evidence_keywords=["measured", "benchmark", "evaluation", "compared"],
                priority=8
            ),
            ExtractionPattern(
                name="metric_quantitative",
                pattern=r"(\d+(?:\.\d+)?(?:x|\s+times?))\s+(?:faster|slower|better|worse|improvement|reduction)",
                atom_type=AtomType.METRIC,
                evidence_keywords=["benchmark", "performance", "evaluation", "measured"],
                priority=8
            ),

            # CONSTRAINT patterns
            ExtractionPattern(
                name="constraint_must_not",
                pattern=r"(?:must\s+not|cannot|never|always|required|mandatory)\s+([^.!?]+?)(?:\s+because|\s+to|\s+for)",
                atom_type=AtomType.CONSTRAINT,
                evidence_keywords=["because", "due to", "required", "mandatory", "critical"],
                priority=7
            ),
            ExtractionPattern(
                name="constraint_limit",
                pattern=r"(?:limit|maximum|minimum|threshold|boundary)\s+(?:of\s+)?([^.!?]+?)(?:\s+to|\s+for|\s+because)",
                atom_type=AtomType.CONSTRAINT,
                evidence_keywords=["critical", "failure", "degradation", "breaks"],
                priority=7
            ),

            # TOOL patterns
            ExtractionPattern(
                name="tool_capability",
                pattern=r"([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+)*):\s*([^.!?]+?)(?:\s+supports|\s+provides|\s+enables|\s+handles)",
                atom_type=AtomType.TOOL,
                evidence_keywords=["supports", "provides", "enables", "handles", "processes"],
                priority=6
            ),

            # COMBINATION patterns
            ExtractionPattern(
                name="combination_recipe",
                pattern=r"(?:combine|integrate|unify)\s+([^.!?]+?)\s+(?:with|and)\s+([^.!?]+?)(?:\s+to|\s+for|\s+improves)",
                atom_type=AtomType.COMBINATION,
                evidence_keywords=["combined", "integrated", "unified", "improves", "enhances"],
                priority=5
            ),

            # FAILURE_MODE patterns
            ExtractionPattern(
                name="failure_mode_detection",
                pattern=r"(?:failure|error|problem|issue)\s+(?:when|if|occurs)\s+([^.!?]+?)(?:\s+detect|\s+identify|\s+handle)",
                atom_type=AtomType.FAILURE_MODE,
                evidence_keywords=["detect", "identify", "handle", "prevent", "mitigate"],
                priority=4
            ),

            # ANTI_PATTERN patterns
            ExtractionPattern(
                name="anti_pattern_warning",
                pattern=r"(?:avoid|don't|never)\s+([^.!?]+?)(?:\s+because|\s+as|\s+since|\s+leads)",
                atom_type=AtomType.ANTI_PATTERN,
                evidence_keywords=["because", "leads to", "causes", "results in", "problem"],
                priority=3
            ),

            # TRADEOFF patterns
            ExtractionPattern(
                name="tradeoff_comparison",
                pattern=r"(?:use|choose)\s+([^.!?]+?)\s+(?:when|if|for)\s+([^.!?]+?)(?:\s+but|\s+however|\s+whereas)",
                atom_type=AtomType.TRADEOFF,
                evidence_keywords=["when", "for", "but", "however", "tradeoff", "vs", "versus"],
                priority=2
            ),

            # RECIPE patterns
            ExtractionPattern(
                name="recipe_steps",
                pattern=r"(?:\d+\.|•|\-)\s*([^.!?]+?)(?:\s*\d+\.|•|\-|\n\s*(?:\d+\.|•|\-))",
                atom_type=AtomType.RECIPE,
                evidence_keywords=["step", "first", "then", "next", "finally", "procedure"],
                priority=1
            ),
        ]

    def _load_custom_patterns(self) -> None:
        """Load custom patterns from configuration."""
        if self.config.custom_patterns:
            for name, pattern_str in self.config.custom_patterns.items():
                # Parse pattern string: "TYPE:pattern"
                if ":" in pattern_str:
                    type_str, pattern = pattern_str.split(":", 1)
                    try:
                        atom_type = AtomType(type_str.upper())
                        self.patterns.append(ExtractionPattern(
                            name=name,
                            pattern=pattern,
                            atom_type=atom_type,
                            evidence_keywords=[],  # Custom patterns need manual keywords
                            priority=5
                        ))
                    except ValueError:
                        continue  # Skip invalid atom types

    def extract_atoms(self, research_file: ResearchFile) -> list[KnowledgeAtom]:
        """Extract knowledge atoms from a research file.

        Args:
            research_file: The research file to process.

        Returns:
            List of extracted knowledge atoms.
        """
        atoms = []

        # Split content into sentences for processing
        sentences = self._split_into_sentences(research_file.content)

        for i, sentence in enumerate(sentences):
            # Get context window around the sentence
            context = self._get_context_window(sentences, i)

            # Try to extract atoms from this sentence
            atom = self._extract_atom_from_text(sentence, context, research_file)
            if atom:
                atoms.append(atom)

        # Deduplicate atoms across the file
        atoms = self._deduplicate_atoms(atoms)

        return atoms

    def _split_into_sentences(self, text: str) -> list[str]:
        """Split text into sentences."""
        # Simple sentence splitting - can be enhanced with NLP libraries
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        return [s.strip() for s in sentences if s.strip()]

    def _get_context_window(self, sentences: list[str], index: int) -> str:
        """Get context window around a sentence."""
        start = max(0, index - self.config.context_window)
        end = min(len(sentences), index + self.config.context_window + 1)
        return " ".join(sentences[start:end])

    def _extract_atom_from_text(self, sentence: str, context: str, research_file: ResearchFile) -> Optional[KnowledgeAtom]:
        """Extract a single knowledge atom from text."""
        if len(sentence) < self.config.min_content_length:
            return None
        if len(sentence) > self.config.max_content_length:
            return None

        # Try each pattern in priority order
        for pattern in sorted(self.patterns, key=lambda p: p.priority, reverse=True):
            if not pattern.enabled:
                continue

            if pattern.matches(sentence):
                # Assess evidence strength
                evidence_strength = self._assess_evidence_strength(sentence, context, pattern)

                # Skip if below minimum strength
                if evidence_strength.value < EvidenceStrength[self.min_evidence_strength].value:
                    continue

                # Generate unique ID
                atom_id = self._generate_atom_id(sentence, research_file.path)

                # Extract clean content
                content = self._clean_content(sentence)

                # Create atom
                atom = KnowledgeAtom(
                    id=atom_id,
                    type=pattern.atom_type,
                    content=content,
                    evidence_strength=evidence_strength,
                    source=[str(research_file.path)]
                )

                return atom

        return None

    def _assess_evidence_strength(self, sentence: str, context: str, pattern: ExtractionPattern) -> EvidenceStrength:
        """Assess the evidence strength of a potential atom."""
        text = sentence + " " + context
        text_lower = text.lower()

        # Count evidence keywords
        evidence_count = sum(1 for keyword in pattern.evidence_keywords
                           if keyword.lower() in text_lower)

        # Look for specific evidence indicators
        strong_indicators = ["measured", "benchmark", "evaluation", "study", "research", "experiment"]
        moderate_indicators = ["improves", "reduces", "achieves", "provides", "enables", "based on"]
        strong_count = sum(1 for ind in strong_indicators if ind in text_lower)
        moderate_count = sum(1 for ind in moderate_indicators if ind in text_lower)

        # Determine strength
        if strong_count > 0 or evidence_count >= 2:
            return EvidenceStrength.STRONG
        elif moderate_count > 0 or evidence_count >= 1:
            return EvidenceStrength.MODERATE
        else:
            return EvidenceStrength.WEAK

    def _generate_atom_id(self, content: str, source_path: Path) -> str:
        """Generate a unique ID for a knowledge atom."""
        # Create hash from content and source
        hash_input = f"{content}:{source_path}"
        hash_obj = hashlib.md5(hash_input.encode('utf-8'))
        hash_str = hash_obj.hexdigest()[:8].upper()
        return f"KA-{hash_str}"

    def _clean_content(self, content: str) -> str:
        """Clean and normalize atom content."""
        # Remove extra whitespace
        content = re.sub(r'\s+', ' ', content.strip())

        # Limit length
        if len(content) > 500:
            content = content[:497] + "..."

        return content

    def _deduplicate_atoms(self, atoms: list[KnowledgeAtom]) -> list[KnowledgeAtom]:
        """Deduplicate atoms based on content similarity."""
        if not atoms:
            return atoms

        # Group by content similarity
        unique_atoms = []
        seen_hashes = set()

        for atom in atoms:
            # Create content hash for deduplication
            content_hash = hashlib.md5(atom.content.encode('utf-8')).hexdigest()

            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                unique_atoms.append(atom)
            else:
                # Merge sources if duplicate
                for existing in unique_atoms:
                    if hashlib.md5(existing.content.encode('utf-8')).hexdigest() == content_hash:
                        existing.source.extend(atom.source)
                        existing.source = list(set(existing.source))  # Remove duplicates
                        break

        return unique_atoms

    def batch_extract(self, research_files: list[ResearchFile]) -> list[KnowledgeAtom]:
        """Extract atoms from multiple research files.

        Args:
            research_files: List of research files to process.

        Returns:
            Combined list of extracted knowledge atoms.
        """
        all_atoms = []

        for research_file in research_files:
            try:
                atoms = self.extract_atoms(research_file)
                all_atoms.extend(atoms)
            except Exception as e:
                # Log error but continue processing
                print(f"Error processing {research_file.path}: {e}")
                continue

        # Cross-file deduplication
        return self._deduplicate_atoms(all_atoms)
