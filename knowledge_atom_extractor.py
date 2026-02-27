#!/usr/bin/env python3
# Knowledge Atom Extractor for Autonomous AI Coding Research
# Transforms raw research into cleaned, ranked, deduplicated knowledge atoms

import os
import re
import json
from typing import List, Dict, Any, Union
import datetime

# Knowledge Atom Types
ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
]

# Evidence Strength Levels
EVIDENCE_STRENGTH = ["STRONG", "MODERATE", "WEAK"]

# Technical Domains (D1-D12) - from taxonomy
DOMAINS = [
    "D1: Meta Architecture", "D2: Agent Orchestration", "D3: Context & Memory Intelligence",
    "D4: Code Intelligence", "D5: SDLC Automation", "D6: Data Infrastructure",
    "D7: Human Interaction", "D8: Model Management", "D9: Research Discipline",
    "D10: Scaling Enterprise", "D11: Advanced Runtime", "D12: Self-Improvement"
]

# SDLC Phases (P1-P8)
SDLC_PHASES = [
    "P1: Requirements", "P2: Design", "P3: Implementation", "P4: Testing",
    "P5: Deployment", "P6: Operation", "P7: Maintenance", "P8: Retirement"
]

# Product Categories (PC1-PC10) - AI coding tools/products
PRODUCT_CATEGORIES = [
    "PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks",
    "PC3: Code Analysis Tools", "PC4: Testing Automation",
    "PC5: CI/CD Systems", "PC6: Context Management",
    "PC7: Knowledge Bases", "PC8: DevOps Platforms",
    "PC9: Security Tools", "PC10: Observability Platforms"
]

class KnowledgeAtom:
    """Class to represent a knowledge atom with all required properties"""
    def __init__(self, atom_id: str, atom_type: str, content: str, 
                 evidence_strength: str, sources: List[str], 
                 domains: List[str], sdlc_phases: List[str], 
                 products: List[str]):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.content = content
        self.evidence_strength = evidence_strength
        self.sources = sources
        self.domains = domains
        self.sdlc_phases = sdlc_phases
        self.products = products
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            "ID": self.atom_id,
            "TYPE": self.atom_type,
            "CONTENT": self.content,
            "EVIDENCE_STRENGTH": self.evidence_strength,
            "SOURCE": self.sources,
            "DOMAINS": self.domains,
            "SDLC_PHASES": self.sdlc_phases,
            "PRODUCTS": self.products
        }
    
    def __hash__(self):
        """Hash based on content and type for deduplication"""
        return hash((self.atom_type, self.content.strip().lower()))
    
    def __eq__(self, other):
        """Equality check for deduplication"""
        if not isinstance(other, KnowledgeAtom):
            return False
        return (self.atom_type == other.atom_type and 
                self.content.strip().lower() == other.content.strip().lower())

class ResearchFileProcessor:
    """Process research files and extract knowledge atoms"""
    
    def __init__(self, root_dir: str = "docs/research"):
        self.root_dir = root_dir
        self.known_atoms: List[KnowledgeAtom] = []
        self.atom_counter: int = 1
        self.evidence_patterns = self._build_evidence_patterns()
        self.domain_patterns = self._build_domain_patterns()
        self.sdlc_patterns = self._build_sdlc_patterns()
        self.product_patterns = self._build_product_patterns()
    
    def _build_evidence_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to detect evidence strength"""
        return {
            "STRONG": [
                re.compile(r"Confidence: HIGH", re.IGNORECASE),
                re.compile(r"Empirically validated", re.IGNORECASE),
                re.compile(r"Based on .* research", re.IGNORECASE),
                re.compile(r"\[[^]]*\]:.*(arxiv|ieee|acm|springer)", re.IGNORECASE),
                re.compile(r"\d+% improvement", re.IGNORECASE),
                re.compile(r"r\s*=\s*\d+\.\d+", re.IGNORECASE),
                re.compile(r"Hard limit|invariant|must", re.IGNORECASE)
            ],
            "MODERATE": [
                re.compile(r"Confidence: MEDIUM", re.IGNORECASE),
                re.compile(r"Emerging pattern", re.IGNORECASE),
                re.compile(r"Practitioner experience", re.IGNORECASE),
                re.compile(r"May improve|could reduce", re.IGNORECASE),
                re.compile(r"Plausible|suggested", re.IGNORECASE)
            ],
            "WEAK": [
                re.compile(r"Confidence: LOW", re.IGNORECASE),
                re.compile(r"Should consider|may want to", re.IGNORECASE),
                re.compile(r"Recommendation|suggestion", re.IGNORECASE),
                re.compile(r"Possibly|potentially", re.IGNORECASE)
            ]
        }
    
    def _build_domain_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to technical domains"""
        return {
            "D1: Meta Architecture": [r"system design.*philosophy", r"governance.*compliance", r"security.*architecture", r"economic.*optimization"],
            "D2: Agent Orchestration": [r"agent.*orchestration", r"multi-agent.*system", r"agent.*coordination", r"task.*decomposition", r"distributed.*orchestration"],
            "D3: Context & Memory Intelligence": [r"context.*management", r"memory.*system", r"knowledge.*representation", r"retrieval.*augmented", r"reasoning.*architecture"],
            "D4: Code Intelligence": [r"code.*exploration", r"refactoring.*optimization", r"specification.*design", r"code.*analysis", r"program.*understanding"],
            "D5: SDLC Automation": [r"cicd.*devops", r"testing.*architecture", r"observability.*feedback", r"build.*system", r"deployment.*automation"],
            "D6: Data Infrastructure": [r"database.*engineering", r"infrastructure.*engineering", r"cloud.*computing", r"data.*pipeline", r"storage.*system"],
            "D7: Human Interaction": [r"human.*loop", r"human.*interaction", r"user.*interface", r"collaboration.*tool", r"feedback.*system"],
            "D8: Model Management": [r"model.*management", r"model.*capability", r"fine.*tuning", r"model.*selection", r"model.*evaluation"],
            "D9: Research Discipline": [r"research.*methodology", r"benchmarking.*framework", r"evaluation.*metric", r"research.*design", r"experiment.*protocol"],
            "D10: Scaling Enterprise": [r"large.*codebase", r"enterprise.*scaling", r"ecosystem.*intelligence", r"team.*collaboration", r"organizational.*scale"],
            "D11: Advanced Runtime": [r"autonomous.*runtime", r"runtime.*system", r"execution.*engine", r"process.*management", r"resource.*allocation"],
            "D12: Self-Improvement": [r"self.*improvement", r"system.*optimization", r"continuous.*learning", r"adaptive.*system", r"performance.*tuning"]
        }
    
    def _build_sdlc_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to SDLC phases"""
        return {
            "P1: Requirements": [r"requirement.*gathering", r"specification.*analysis", r"user.*story", r"business.*need"],
            "P2: Design": [r"architectural.*design", r"system.*design", r"component.*design", r"interface.*design"],
            "P3: Implementation": [r"code.*generation", r"implementation.*phase", r"coding.*standard", r"development.*process"],
            "P4: Testing": [r"test.*generation", r"test.*automation", r"quality.*assurance", r"defect.*detection"],
            "P5: Deployment": [r"deployment.*process", r"release.*management", r"environment.*provisioning", r"configuration.*management"],
            "P6: Operation": [r"production.*run", r"monitoring.*system", r"incident.*response", r"performance.*management"],
            "P7: Maintenance": [r"code.*maintenance", r"refactoring.*process", r"bug.*fixing", r"system.*evolution"],
            "P8: Retirement": [r"system.*retirement", r"decommissioning.*process", r"legacy.*system", r"end.*of.*life"]
        }
    
    def _build_product_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to product categories"""
        return {
            "PC1: AI Coding Assistants": [r"coding.*assistant", r"code.*completion", r"AI.*programmer", r"developer.*assistant"],
            "PC2: Agent Orchestration Frameworks": [r"agent.*framework", r"orchestration.*platform", r"workflow.*management", r"task.*orchestrator"],
            "PC3: Code Analysis Tools": [r"code.*analysis", r"static.*analysis", r"dynamic.*analysis", r"code.*quality"],
            "PC4: Testing Automation": [r"test.*automation", r"test.*generation", r"testing.*framework", r"quality.*gate"],
            "PC5: CI/CD Systems": [r"CI/CD.*system", r"build.*automation", r"continuous.*integration", r"continuous.*delivery"],
            "PC6: Context Management": [r"context.*manager", r"memory.*system", r"knowledge.*base", r"information.*retrieval"],
            "PC7: Knowledge Bases": [r"knowledge.*base", r"documentation.*system", r"information.*repository", r"knowledge.*management"],
            "PC8: DevOps Platforms": [r"DevOps.*platform", r"cloud.*platform", r"infrastructure.*platform", r"tool.*chain"],
            "PC9: Security Tools": [r"security.*tool", r"vulnerability.*detection", r"compliance.*checker", r"security.*scanner"],
            "PC10: Observability Platforms": [r"observability.*platform", r"monitoring.*tool", r"log.*management", r"trace.*analysis"]
        }
    
    def _calculate_evidence_strength(self, content: str) -> str:
        """Determine evidence strength based on content patterns"""
        for strength, patterns in self.evidence_patterns.items():
            for pattern in patterns:
                if pattern.search(content):
                    return strength
        return "WEAK"  # default
    
    def _map_to_domains(self, content: str, file_path: str) -> List[str]:
        """Map content to technical domains using patterns and file location"""
        matched_domains = []
        
        domain_mapping = {
            "01_meta_architecture": "D1: Meta Architecture",
            "02_agent_orchestration": "D2: Agent Orchestration",
            "03_context_memory_intelligence": "D3: Context & Memory Intelligence",
            "04_code_intelligence": "D4: Code Intelligence",
            "05_sdlc_automation": "D5: SDLC Automation",
            "06_data_infrastructure": "D6: Data Infrastructure",
            "07_human_interaction": "D7: Human Interaction",
            "08_model_management": "D8: Model Management",
            "09_research_discipline": "D9: Research Discipline",
            "10_scaling_enterprise": "D10: Scaling Enterprise",
            "11_advanced_runtime": "D11: Advanced Runtime",
            "12_self_improvement": "D12: Self-Improvement"
        }
        
        for dir_name, domain in domain_mapping.items():
            if dir_name in file_path:
                matched_domains.append(domain)
        
        for domain, patterns in self.domain_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE) and domain not in matched_domains:
                    matched_domains.append(domain)
        
        return matched_domains if matched_domains else ["D9: Research Discipline"]
    
    def _map_to_sdlc_phases(self, content: str) -> List[str]:
        """Map content to SDLC phases using patterns"""
        matched_phases = []
        for phase, patterns in self.sdlc_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    matched_phases.append(phase)
        return matched_phases
    
    def _map_to_products(self, content: str) -> List[str]:
        """Map content to product categories using patterns"""
        matched_products = []
        for product, patterns in self.product_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    matched_products.append(product)
        return matched_products
    
    def _determine_atom_type(self, content: str) -> str:
        """Determine knowledge atom type based on content patterns"""
        patterns = {
            "TECHNIQUE": [
                r"Pattern: .*", r"Method: .*", r"Approach: .*",
                r"Strategy: .*", r"Technique: .*", r"Algorithm: .*",
                r"Protocol: .*", r"Architecture: .*", r"Framework: .*"
            ],
            "METRIC": [
                r"Score: .*", r"Metric: .*", r"Measurement: .*",
                r"\d+% .*", r"r\s*=\s*\d+\.\d+", r"F-score|precision|recall",
                r"Performance.*metric", r"Quality.*metric"
            ],
            "CONSTRAINT": [
                r"Constraint: .*", r"Hard limit: .*", r"Must.*",
                r"Cannot.*", r"Limit.*", r"Restriction.*"
            ],
            "TOOL": [
                r"Tool: .*", r"Platform: .*", r"Framework: .*",
                r"Library: .*", r"System: .*", r"Service: .*",
                r"LangGraph|CrewAI|AutoGen|MetaGPT|ChatDev"
            ],
            "COMBINATION": [
                r"Combine.*and.*", r"Integrate.*with.*", r"Work together.*",
                r"Synergy.*", r"Hybrid.*approach", r"Multi.*combination"
            ],
            "FAILURE MODE": [
                r"Failure mode: .*", r"Failure.*", r"Error.*",
                r"Bug.*", r"Problem.*", r"Issue.*", r"Risk.*"
            ],
            "ANTI-PATTERN": [
                r"Anti-pattern: .*", r"Bad practice: .*",
                r"Should avoid: .*", r"Not recommended: .*"
            ],
            "TRADEOFF": [
                r"Tradeoff: .*", r"Trade-off: .*", r"Balance.*",
                r"Advantage.*disadvantage", r"Pros.*cons", r"Benefit.*cost"
            ],
            "RECIPE": [
                r"Step \d+: .*", r"Procedure: .*", r"Process: .*",
                r"Sequence: .*", r"How to.*", r"Steps to.*"
            ]
        }
        
        for atom_type, pattern_list in patterns.items():
            for pattern in pattern_list:
                if re.search(pattern, content, re.IGNORECASE):
                    return atom_type
        
        return "TECHNIQUE"  # default
    
    def _should_keep(self, content: str) -> bool:
        """Determine if content should be kept as a knowledge atom"""
        discard_patterns = [
            r"Definition: .*", r"Definition of .*",
            r"Introduction to .*", r"Overview of .*",
            r"This paper.*", r"This study.*",
            r"Background.*", r"Related work.*",
            r"Future work.*", r"Conclusion.*",
            r"Abstract.*", r"Summary.*",
            r"References.*", r"Citations.*",
            r"Literature review.*", r"Survey of .*"
        ]
        
        for pattern in discard_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return False
        
        keep_patterns = [
            r"\d+%.*", r"r\s*=\s*\d+\.\d+", r"[A-Z][a-zA-Z]+ v\d+\.\d+",
            r"https?://[^\s]+", r"[A-Z]{2,}\d+", r"Step \d+:"
        ]
        
        return any(re.search(pattern, content) for pattern in keep_patterns)
    
    def _extract_pattern_sections(self, content: str) -> List[str]:
        """Extract sections that match pattern definitions"""
        sections = []
        
        pattern_matches = re.finditer(r"### Pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in pattern_matches:
            sections.append(match.group(0).strip())
        
        tradeoff_matches = re.finditer(r"### Tradeoff: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in tradeoff_matches:
            sections.append(match.group(0).strip())
        
        antipattern_matches = re.finditer(r"### Anti-pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in antipattern_matches:
            sections.append(match.group(0).strip())
        
        technique_matches = re.finditer(r"### [^\n]+Algorithm[^\\n]*(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in technique_matches:
            sections.append(match.group(0).strip())
        
        return sections
    
    def process_file(self, file_path: str) -> List[KnowledgeAtom]:
        """Process a single research file and extract knowledge atoms"""
        atoms = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return []
        
        sections = self._extract_pattern_sections(content)
        
        if not sections:
            paragraphs = re.split(r'\n\s*\n', content)
            sections = [p.strip() for p in paragraphs if len(p.strip()) > 50]
        
        for section in sections:
            if not self._should_keep(section):
                continue
                
            atom_type = self._determine_atom_type(section)
            evidence_strength = self._calculate_evidence_strength(section)
            domains = self._map_to_domains(section, file_path)
            sdlc_phases = self._map_to_sdlc_phases(section)
            products = self._map_to_products(section)
            
            atom = KnowledgeAtom(
                atom_id=f"KA-{self.atom_counter:03d}",
                atom_type=atom_type,
                content=section.strip(),
                evidence_strength=evidence_strength,
                sources=[file_path],
                domains=domains,
                sdlc_phases=sdlc_phases,
                products=products
            )
            
            self.atom_counter += 1
            atoms.append(atom)
        
        return atoms
    
    def process_directory(self, directory: str) -> List[KnowledgeAtom]:
        """Process all research files in a directory recursively"""
        atoms = []
        
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.md') and not file_name.startswith('_'):
                    file_path = os.path.join(root, file_name)
                    print(f"Processing file: {file_path}")
                    file_atoms = self.process_file(file_path)
                    atoms.extend(file_atoms)
        
        return atoms
    
    def deduplicate_atoms(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Deduplicate knowledge atoms"""
        unique_atoms = []
        seen = set()
        
        for atom in atoms:
            atom_hash = hash(atom)
            if atom_hash not in seen:
                seen.add(atom_hash)
                unique_atoms.append(atom)
            else:
                index = unique_atoms.index(atom)
                for source in atom.sources:
                    if source not in unique_atoms[index].sources:
                        unique_atoms[index].sources.append(source)
        
        return unique_atoms
    
    def rank_atoms(self, atoms: List[KnowledgeAtom]) -> Dict[str, List[KnowledgeAtom]]:
        """Rank atoms by type with evidence strength > specificity > uniqueness"""
        ranked = {atom_type: [] for atom_type in ATOM_TYPES}
        
        for atom in atoms:
            ranked[atom.atom_type].append(atom)
        
        for atom_type in ranked:
            ranked[atom_type].sort(
                key=lambda x: (
                    -EVIDENCE_STRENGTH.index(x.evidence_strength),
                    -sum(1 for c in x.content if c.isdigit()),
                    -len(x.content.split()),
                    x.atom_id
                )
            )
        
        return ranked
    
    def process_all(self) -> Dict[str, List[KnowledgeAtom]]:
        """Process all research files and generate ranked, deduplicated atoms"""
        all_atoms = []
        
        all_atoms.extend(self.process_directory(self.root_dir))
        
        additional_files = [
            "Perplexity_Thread.md",
            "Prompt_thread.md",
            "Research.md",
            "start_prompt.md"
        ]
        
        for file_name in additional_files:
            if os.path.exists(file_name):
                print(f"Processing additional file: {file_name}")
                file_atoms = self.process_file(file_name)
                all_atoms.extend(file_atoms)
        
        zenflow_dir = ".zenflow/tasks/new-task-97b2/reports"
        if os.path.exists(zenflow_dir):
            all_atoms.extend(self.process_directory(zenflow_dir))
        
        unique_atoms = self.deduplicate_atoms(all_atoms)
        
        ranked_atoms = self.rank_atoms(unique_atoms)
        
        return ranked_atoms

def main():
    print("Starting knowledge atom extraction...")
    
    processor = ResearchFileProcessor(root_dir="docs/research")
    ranked_atoms = processor.process_all()
    
    output_data = {}
    for atom_type, atoms in ranked_atoms.items():
        if atoms:
            output_data[atom_type] = [atom.to_dict() for atom in atoms]
    
    output_path = "knowledge_atom_registry.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nExtraction complete!")
    print(f"Generated knowledge atom registry at: {output_path}")
    
    total_atoms = sum(len(atoms) for atoms in ranked_atoms.values())
    print(f"\nSummary:")
    print(f"Total knowledge atoms extracted: {total_atoms}")
    for atom_type in ATOM_TYPES:
        count = len(ranked_atoms[atom_type])
        if count > 0:
            print(f"  {atom_type}: {count} atoms")

if __name__ == "__main__":
    main()
# Knowledge Atom Extractor for Autonomous AI Coding Research
# Transforms raw research into cleaned, ranked, deduplicated knowledge atoms

import os
import re
import json
from typing import List, Dict, Any, Union
import datetime

# Knowledge Atom Types
ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
]

# Evidence Strength Levels
EVIDENCE_STRENGTH = ["STRONG", "MODERATE", "WEAK"]

# Technical Domains (D1-D12) - from taxonomy
DOMAINS = [
    "D1: Meta Architecture", "D2: Agent Orchestration", "D3: Context & Memory Intelligence",
    "D4: Code Intelligence", "D5: SDLC Automation", "D6: Data Infrastructure",
    "D7: Human Interaction", "D8: Model Management", "D9: Research Discipline",
    "D10: Scaling Enterprise", "D11: Advanced Runtime", "D12: Self-Improvement"
]

# SDLC Phases (P1-P8)
SDLC_PHASES = [
    "P1: Requirements", "P2: Design", "P3: Implementation", "P4: Testing",
    "P5: Deployment", "P6: Operation", "P7: Maintenance", "P8: Retirement"
]

# Product Categories (PC1-PC10) - AI coding tools/products
PRODUCT_CATEGORIES = [
    "PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks",
    "PC3: Code Analysis Tools", "PC4: Testing Automation",
    "PC5: CI/CD Systems", "PC6: Context Management",
    "PC7: Knowledge Bases", "PC8: DevOps Platforms",
    "PC9: Security Tools", "PC10: Observability Platforms"
]

class KnowledgeAtom:
    """Class to represent a knowledge atom with all required properties"""
    def __init__(self, atom_id: str, atom_type: str, content: str, 
                 evidence_strength: str, sources: List[str], 
                 domains: List[str], sdlc_phases: List[str], 
                 products: List[str]):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.content = content
        self.evidence_strength = evidence_strength
        self.sources = sources
        self.domains = domains
        self.sdlc_phases = sdlc_phases
        self.products = products
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            "ID": self.atom_id,
            "TYPE": self.atom_type,
            "CONTENT": self.content,
            "EVIDENCE_STRENGTH": self.evidence_strength,
            "SOURCE": self.sources,
            "DOMAINS": self.domains,
            "SDLC_PHASES": self.sdlc_phases,
            "PRODUCTS": self.products
        }
    
    def __hash__(self):
        """Hash based on content and type for deduplication"""
        return hash((self.atom_type, self.content.strip().lower()))
    
    def __eq__(self, other):
        """Equality check for deduplication"""
        if not isinstance(other, KnowledgeAtom):
            return False
        return (self.atom_type == other.atom_type and 
                self.content.strip().lower() == other.content.strip().lower())

class ResearchFileProcessor:
    """Process research files and extract knowledge atoms"""
    
    def __init__(self, root_dir: str = "docs/research"):
        self.root_dir = root_dir
        self.known_atoms: List[KnowledgeAtom] = []
        self.atom_counter: int = 1
        self.evidence_patterns = self._build_evidence_patterns()
        self.domain_patterns = self._build_domain_patterns()
        self.sdlc_patterns = self._build_sdlc_patterns()
        self.product_patterns = self._build_product_patterns()
    
    def _build_evidence_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to detect evidence strength"""
        return {
            "STRONG": [
                re.compile(r"Confidence: HIGH", re.IGNORECASE),
                re.compile(r"Empirically validated", re.IGNORECASE),
                re.compile(r"Based on .* research", re.IGNORECASE),
                re.compile(r"\[[^]]*\]:.*(arxiv|ieee|acm|springer)", re.IGNORECASE),
                re.compile(r"\d+% improvement", re.IGNORECASE),
                re.compile(r"r\s*=\s*\d+\.\d+", re.IGNORECASE),
                re.compile(r"Hard limit|invariant|must", re.IGNORECASE)
            ],
            "MODERATE": [
                re.compile(r"Confidence: MEDIUM", re.IGNORECASE),
                re.compile(r"Emerging pattern", re.IGNORECASE),
                re.compile(r"Practitioner experience", re.IGNORECASE),
                re.compile(r"May improve|could reduce", re.IGNORECASE),
                re.compile(r"Plausible|suggested", re.IGNORECASE)
            ],
            "WEAK": [
                re.compile(r"Confidence: LOW", re.IGNORECASE),
                re.compile(r"Should consider|may want to", re.IGNORECASE),
                re.compile(r"Recommendation|suggestion", re.IGNORECASE),
                re.compile(r"Possibly|potentially", re.IGNORECASE)
            ]
        }
    
    def _build_domain_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to technical domains"""
        return {
            "D1: Meta Architecture": [r"system design.*philosophy", r"governance.*compliance", r"security.*architecture", r"economic.*optimization"],
            "D2: Agent Orchestration": [r"agent.*orchestration", r"multi-agent.*system", r"agent.*coordination", r"task.*decomposition", r"distributed.*orchestration"],
            "D3: Context & Memory Intelligence": [r"context.*management", r"memory.*system", r"knowledge.*representation", r"retrieval.*augmented", r"reasoning.*architecture"],
            "D4: Code Intelligence": [r"code.*exploration", r"refactoring.*optimization", r"specification.*design", r"code.*analysis", r"program.*understanding"],
            "D5: SDLC Automation": [r"cicd.*devops", r"testing.*architecture", r"observability.*feedback", r"build.*system", r"deployment.*automation"],
            "D6: Data Infrastructure": [r"database.*engineering", r"infrastructure.*engineering", r"cloud.*computing", r"data.*pipeline", r"storage.*system"],
            "D7: Human Interaction": [r"human.*loop", r"human.*interaction", r"user.*interface", r"collaboration.*tool", r"feedback.*system"],
            "D8: Model Management": [r"model.*management", r"model.*capability", r"fine.*tuning", r"model.*selection", r"model.*evaluation"],
            "D9: Research Discipline": [r"research.*methodology", r"benchmarking.*framework", r"evaluation.*metric", r"research.*design", r"experiment.*protocol"],
            "D10: Scaling Enterprise": [r"large.*codebase", r"enterprise.*scaling", r"ecosystem.*intelligence", r"team.*collaboration", r"organizational.*scale"],
            "D11: Advanced Runtime": [r"autonomous.*runtime", r"runtime.*system", r"execution.*engine", r"process.*management", r"resource.*allocation"],
            "D12: Self-Improvement": [r"self.*improvement", r"system.*optimization", r"continuous.*learning", r"adaptive.*system", r"performance.*tuning"]
        }
    
    def _build_sdlc_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to SDLC phases"""
        return {
            "P1: Requirements": [r"requirement.*gathering", r"specification.*analysis", r"user.*story", r"business.*need"],
            "P2: Design": [r"architectural.*design", r"system.*design", r"component.*design", r"interface.*design"],
            "P3: Implementation": [r"code.*generation", r"implementation.*phase", r"coding.*standard", r"development.*process"],
            "P4: Testing": [r"test.*generation", r"test.*automation", r"quality.*assurance", r"defect.*detection"],
            "P5: Deployment": [r"deployment.*process", r"release.*management", r"environment.*provisioning", r"configuration.*management"],
            "P6: Operation": [r"production.*run", r"monitoring.*system", r"incident.*response", r"performance.*management"],
            "P7: Maintenance": [r"code.*maintenance", r"refactoring.*process", r"bug.*fixing", r"system.*evolution"],
            "P8: Retirement": [r"system.*retirement", r"decommissioning.*process", r"legacy.*system", r"end.*of.*life"]
        }
    
    def _build_product_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to product categories"""
        return {
            "PC1: AI Coding Assistants": [r"coding.*assistant", r"code.*completion", r"AI.*programmer", r"developer.*assistant"],
            "PC2: Agent Orchestration Frameworks": [r"agent.*framework", r"orchestration.*platform", r"workflow.*management", r"task.*orchestrator"],
            "PC3: Code Analysis Tools": [r"code.*analysis", r"static.*analysis", r"dynamic.*analysis", r"code.*quality"],
            "PC4: Testing Automation": [r"test.*automation", r"test.*generation", r"testing.*framework", r"quality.*gate"],
            "PC5: CI/CD Systems": [r"CI/CD.*system", r"build.*automation", r"continuous.*integration", r"continuous.*delivery"],
            "PC6: Context Management": [r"context.*manager", r"memory.*system", r"knowledge.*base", r"information.*retrieval"],
            "PC7: Knowledge Bases": [r"knowledge.*base", r"documentation.*system", r"information.*repository", r"knowledge.*management"],
            "PC8: DevOps Platforms": [r"DevOps.*platform", r"cloud.*platform", r"infrastructure.*platform", r"tool.*chain"],
            "PC9: Security Tools": [r"security.*tool", r"vulnerability.*detection", r"compliance.*checker", r"security.*scanner"],
            "PC10: Observability Platforms": [r"observability.*platform", r"monitoring.*tool", r"log.*management", r"trace.*analysis"]
        }
    
    def _calculate_evidence_strength(self, content: str) -> str:
        """Determine evidence strength based on content patterns"""
        for strength, patterns in self.evidence_patterns.items():
            for pattern in patterns:
                if pattern.search(content):
                    return strength
        return "WEAK"  # default
    
    def _map_to_domains(self, content: str, file_path: str) -> List[str]:
        """Map content to technical domains using patterns and file location"""
        matched_domains = []
        
        domain_mapping = {
            "01_meta_architecture": "D1: Meta Architecture",
            "02_agent_orchestration": "D2: Agent Orchestration",
            "03_context_memory_intelligence": "D3: Context & Memory Intelligence",
            "04_code_intelligence": "D4: Code Intelligence",
            "05_sdlc_automation": "D5: SDLC Automation",
            "06_data_infrastructure": "D6: Data Infrastructure",
            "07_human_interaction": "D7: Human Interaction",
            "08_model_management": "D8: Model Management",
            "09_research_discipline": "D9: Research Discipline",
            "10_scaling_enterprise": "D10: Scaling Enterprise",
            "11_advanced_runtime": "D11: Advanced Runtime",
            "12_self_improvement": "D12: Self-Improvement"
        }
        
        for dir_name, domain in domain_mapping.items():
            if dir_name in file_path:
                matched_domains.append(domain)
        
        for domain, patterns in self.domain_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE) and domain not in matched_domains:
                    matched_domains.append(domain)
        
        return matched_domains if matched_domains else ["D9: Research Discipline"]
    
    def _map_to_sdlc_phases(self, content: str) -> List[str]:
        """Map content to SDLC phases using patterns"""
        matched_phases = []
        for phase, patterns in self.sdlc_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    matched_phases.append(phase)
        return matched_phases
    
    def _map_to_products(self, content: str) -> List[str]:
        """Map content to product categories using patterns"""
        matched_products = []
        for product, patterns in self.product_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    matched_products.append(product)
        return matched_products
    
    def _determine_atom_type(self, content: str) -> str:
        """Determine knowledge atom type based on content patterns"""
        patterns = {
            "TECHNIQUE": [
                r"Pattern: .*", r"Method: .*", r"Approach: .*",
                r"Strategy: .*", r"Technique: .*", r"Algorithm: .*",
                r"Protocol: .*", r"Architecture: .*", r"Framework: .*"
            ],
            "METRIC": [
                r"Score: .*", r"Metric: .*", r"Measurement: .*",
                r"\d+% .*", r"r\s*=\s*\d+\.\d+", r"F-score|precision|recall",
                r"Performance.*metric", r"Quality.*metric"
            ],
            "CONSTRAINT": [
                r"Constraint: .*", r"Hard limit: .*", r"Must.*",
                r"Cannot.*", r"Limit.*", r"Restriction.*"
            ],
            "TOOL": [
                r"Tool: .*", r"Platform: .*", r"Framework: .*",
                r"Library: .*", r"System: .*", r"Service: .*",
                r"LangGraph|CrewAI|AutoGen|MetaGPT|ChatDev"
            ],
            "COMBINATION": [
                r"Combine.*and.*", r"Integrate.*with.*", r"Work together.*",
                r"Synergy.*", r"Hybrid.*approach", r"Multi.*combination"
            ],
            "FAILURE MODE": [
                r"Failure mode: .*", r"Failure.*", r"Error.*",
                r"Bug.*", r"Problem.*", r"Issue.*", r"Risk.*"
            ],
            "ANTI-PATTERN": [
                r"Anti-pattern: .*", r"Bad practice: .*",
                r"Should avoid: .*", r"Not recommended: .*"
            ],
            "TRADEOFF": [
                r"Tradeoff: .*", r"Trade-off: .*", r"Balance.*",
                r"Advantage.*disadvantage", r"Pros.*cons", r"Benefit.*cost"
            ],
            "RECIPE": [
                r"Step \d+: .*", r"Procedure: .*", r"Process: .*",
                r"Sequence: .*", r"How to.*", r"Steps to.*"
            ]
        }
        
        for atom_type, pattern_list in patterns.items():
            for pattern in pattern_list:
                if re.search(pattern, content, re.IGNORECASE):
                    return atom_type
        
        return "TECHNIQUE"  # default
    
    def _should_keep(self, content: str) -> bool:
        """Determine if content should be kept as a knowledge atom"""
        discard_patterns = [
            r"Definition: .*", r"Definition of .*",
            r"Introduction to .*", r"Overview of .*",
            r"This paper.*", r"This study.*",
            r"Background.*", r"Related work.*",
            r"Future work.*", r"Conclusion.*",
            r"Abstract.*", r"Summary.*",
            r"References.*", r"Citations.*",
            r"Literature review.*", r"Survey of .*"
        ]
        
        for pattern in discard_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return False
        
        keep_patterns = [
            r"\d+%.*", r"r\s*=\s*\d+\.\d+", r"[A-Z][a-zA-Z]+ v\d+\.\d+",
            r"https?://[^\s]+", r"[A-Z]{2,}\d+", r"Step \d+:"
        ]
        
        return any(re.search(pattern, content) for pattern in keep_patterns)
    
    def _extract_pattern_sections(self, content: str) -> List[str]:
        """Extract sections that match pattern definitions"""
        sections = []
        
        pattern_matches = re.finditer(r"### Pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in pattern_matches:
            sections.append(match.group(0).strip())
        
        tradeoff_matches = re.finditer(r"### Tradeoff: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in tradeoff_matches:
            sections.append(match.group(0).strip())
        
        antipattern_matches = re.finditer(r"### Anti-pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in antipattern_matches:
            sections.append(match.group(0).strip())
        
        technique_matches = re.finditer(r"### [^\n]+Algorithm[^\\n]*(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in technique_matches:
            sections.append(match.group(0).strip())
        
        return sections
    
    def process_file(self, file_path: str) -> List[KnowledgeAtom]:
        """Process a single research file and extract knowledge atoms"""
        atoms = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return []
        
        sections = self._extract_pattern_sections(content)
        
        if not sections:
            paragraphs = re.split(r'\n\s*\n', content)
            sections = [p.strip() for p in paragraphs if len(p.strip()) > 50]
        
        for section in sections:
            if not self._should_keep(section):
                continue
                
            atom_type = self._determine_atom_type(section)
            evidence_strength = self._calculate_evidence_strength(section)
            domains = self._map_to_domains(section, file_path)
            sdlc_phases = self._map_to_sdlc_phases(section)
            products = self._map_to_products(section)
            
            atom = KnowledgeAtom(
                atom_id=f"KA-{self.atom_counter:03d}",
                atom_type=atom_type,
                content=section.strip(),
                evidence_strength=evidence_strength,
                sources=[file_path],
                domains=domains,
                sdlc_phases=sdlc_phases,
                products=products
            )
            
            self.atom_counter += 1
            atoms.append(atom)
        
        return atoms
    
    def process_directory(self, directory: str) -> List[KnowledgeAtom]:
        """Process all research files in a directory recursively"""
        atoms = []
        
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.md') and not file_name.startswith('_'):
                    file_path = os.path.join(root, file_name)
                    print(f"Processing file: {file_path}")
                    file_atoms = self.process_file(file_path)
                    atoms.extend(file_atoms)
        
        return atoms
    
    def deduplicate_atoms(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Deduplicate knowledge atoms"""
        unique_atoms = []
        seen = set()
        
        for atom in atoms:
            atom_hash = hash(atom)
            if atom_hash not in seen:
                seen.add(atom_hash)
                unique_atoms.append(atom)
            else:
                index = unique_atoms.index(atom)
                for source in atom.sources:
                    if source not in unique_atoms[index].sources:
                        unique_atoms[index].sources.append(source)
        
        return unique_atoms
    
    def rank_atoms(self, atoms: List[KnowledgeAtom]) -> Dict[str, List[KnowledgeAtom]]:
        """Rank atoms by type with evidence strength > specificity > uniqueness"""
        ranked = {atom_type: [] for atom_type in ATOM_TYPES}
        
        for atom in atoms:
            ranked[atom.atom_type].append(atom)
        
        for atom_type in ranked:
            ranked[atom_type].sort(
                key=lambda x: (
                    -EVIDENCE_STRENGTH.index(x.evidence_strength),
                    -sum(1 for c in x.content if c.isdigit()),
                    -len(x.content.split()),
                    x.atom_id
                )
            )
        
        return ranked
    
    def process_all(self) -> Dict[str, List[KnowledgeAtom]]:
        """Process all research files and generate ranked, deduplicated atoms"""
        all_atoms = []
        
        all_atoms.extend(self.process_directory(self.root_dir))
        
        additional_files = [
            "Perplexity_Thread.md",
            "Prompt_thread.md",
            "Research.md",
            "start_prompt.md"
        ]
        
        for file_name in additional_files:
            if os.path.exists(file_name):
                print(f"Processing additional file: {file_name}")
                file_atoms = self.process_file(file_name)
                all_atoms.extend(file_atoms)
        
        zenflow_dir = ".zenflow/tasks/new-task-97b2/reports"
        if os.path.exists(zenflow_dir):
            all_atoms.extend(self.process_directory(zenflow_dir))
        
        unique_atoms = self.deduplicate_atoms(all_atoms)
        
        ranked_atoms = self.rank_atoms(unique_atoms)
        
        return ranked_atoms

def main():
    print("Starting knowledge atom extraction...")
    
    processor = ResearchFileProcessor(root_dir="docs/research")
    ranked_atoms = processor.process_all()
    
    output_data = {}
    for atom_type, atoms in ranked_atoms.items():
        if atoms:
            output_data[atom_type] = [atom.to_dict() for atom in atoms]
    
    output_path = "knowledge_atom_registry.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nExtraction complete!")
    print(f"Generated knowledge atom registry at: {output_path}")
    
    total_atoms = sum(len(atoms) for atoms in ranked_atoms.values())
    print(f"\nSummary:")
    print(f"Total knowledge atoms extracted: {total_atoms}")
    for atom_type in ATOM_TYPES:
        count = len(ranked_atoms[atom_type])
        if count > 0:
            print(f"  {atom_type}: {count} atoms")

if __name__ == "__main__":
    main()
    ranked_atoms = processor.process_all()
    
    # Generate JSON output
    output_data = {}
    for atom_type, atoms in ranked_atoms.items():
        if atoms:
            output_data[atom_type] = [atom.to_dict() for atom in atoms]
    
    # Write to file
    output_path = "knowledge_atom_registry.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nExtraction complete!")
    print(f"Generated knowledge atom registry at: {output_path}")
    
    # Print summary
    total_atoms = sum(len(atoms) for atoms in ranked_atoms.values())
    print(f"\nSummary:")
    print(f"Total knowledge atoms extracted: {total_atoms}")
    for atom_type in ATOM_TYPES:
        count = len(ranked_atoms[atom_type])
        if count > 0:
            print(f"  {atom_type}: {count} atoms")

if __name__ == "__main__":
    main()"""
Knowledge Atom Extractor for Autonomous AI Coding Research
Transforms raw research into cleaned, ranked, deduplicated knowledge atoms
"""

import os
import re
import json
import yaml
from typing import List, Dict, Any, Union
import datetime

# Knowledge Atom Types
ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
]

# Evidence Strength Levels
EVIDENCE_STRENGTH = ["STRONG", "MODERATE", "WEAK"]

# Technical Domains (D1-D12) - from taxonomy
DOMAINS = [
    "D1: Meta Architecture", "D2: Agent Orchestration", "D3: Context & Memory Intelligence",
    "D4: Code Intelligence", "D5: SDLC Automation", "D6: Data Infrastructure",
    "D7: Human Interaction", "D8: Model Management", "D9: Research Discipline",
    "D10: Scaling Enterprise", "D11: Advanced Runtime", "D12: Self-Improvement"
]

# SDLC Phases (P1-P8)
SDLC_PHASES = [
    "P1: Requirements", "P2: Design", "P3: Implementation", "P4: Testing",
    "P5: Deployment", "P6: Operation", "P7: Maintenance", "P8: Retirement"
]

# Product Categories (PC1-PC10) - AI coding tools/products
PRODUCT_CATEGORIES = [
    "PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks",
    "PC3: Code Analysis Tools", "PC4: Testing Automation",
    "PC5: CI/CD Systems", "PC6: Context Management",
    "PC7: Knowledge Bases", "PC8: DevOps Platforms",
    "PC9: Security Tools", "PC10: Observability Platforms"
]

class KnowledgeAtom:
    """Class to represent a knowledge atom with all required properties"""
    def __init__(self, atom_id: str, atom_type: str, content: str, 
                 evidence_strength: str, sources: List[str], 
                 domains: List[str], sdlc_phases: List[str], 
                 products: List[str]):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.content = content
        self.evidence_strength = evidence_strength
        self.sources = sources
        self.domains = domains
        self.sdlc_phases = sdlc_phases
        self.products = products
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            "ID": self.atom_id,
            "TYPE": self.atom_type,
            "CONTENT": self.content,
            "EVIDENCE_STRENGTH": self.evidence_strength,
            "SOURCE": self.sources,
            "DOMAINS": self.domains,
            "SDLC_PHASES": self.sdlc_phases,
            "PRODUCTS": self.products
        }
    
    def __hash__(self):
        """Hash based on content and type for deduplication"""
        return hash((self.atom_type, self.content.strip().lower()))
    
    def __eq__(self, other):
        """Equality check for deduplication"""
        if not isinstance(other, KnowledgeAtom):
            return False
        return (self.atom_type == other.atom_type and 
                self.content.strip().lower() == other.content.strip().lower())

class ResearchFileProcessor:
    """Process research files and extract knowledge atoms"""
    
    def __init__(self, root_dir: str = "docs/research"):
        self.root_dir = root_dir
        self.known_atoms: List[KnowledgeAtom] = []
        self.atom_counter: int = 1
        self.evidence_patterns = self._build_evidence_patterns()
        self.domain_patterns = self._build_domain_patterns()
        self.sdlc_patterns = self._build_sdlc_patterns()
        self.product_patterns = self._build_product_patterns()
    
    def _build_evidence_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to detect evidence strength"""
        return {
            "STRONG": [
                re.compile(r"Confidence: HIGH", re.IGNORECASE),
                re.compile(r"Empirically validated", re.IGNORECASE),
                re.compile(r"Based on .* research", re.IGNORECASE),
                re.compile(r"\[[^]]*\]:.*(arxiv|ieee|acm|springer)", re.IGNORECASE),
                re.compile(r"\d+% improvement", re.IGNORECASE),
                re.compile(r"r\s*=\s*\d+\.\d+", re.IGNORECASE),
                re.compile(r"Hard limit|invariant|must", re.IGNORECASE)
            ],
            "MODERATE": [
                re.compile(r"Confidence: MEDIUM", re.IGNORECASE),
                re.compile(r"Emerging pattern", re.IGNORECASE),
                re.compile(r"Practitioner experience", re.IGNORECASE),
                re.compile(r"May improve|could reduce", re.IGNORECASE),
                re.compile(r"Plausible|suggested", re.IGNORECASE)
            ],
            "WEAK": [
                re.compile(r"Confidence: LOW", re.IGNORECASE),
                re.compile(r"Should consider|may want to", re.IGNORECASE),
                re.compile(r"Recommendation|suggestion", re.IGNORECASE),
                re.compile(r"Possibly|potentially", re.IGNORECASE)
            ]
        }
    
    def _build_domain_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to technical domains"""
        return {
            "D1: Meta Architecture": [r"system design.*philosophy", r"governance.*compliance", r"security.*architecture", r"economic.*optimization"],
            "D2: Agent Orchestration": [r"agent.*orchestration", r"multi-agent.*system", r"agent.*coordination", r"task.*decomposition", r"distributed.*orchestration"],
            "D3: Context & Memory Intelligence": [r"context.*management", r"memory.*system", r"knowledge.*representation", r"retrieval.*augmented", r"reasoning.*architecture"],
            "D4: Code Intelligence": [r"code.*exploration", r"refactoring.*optimization", r"specification.*design", r"code.*analysis", r"program.*understanding"],
            "D5: SDLC Automation": [r"cicd.*devops", r"testing.*architecture", r"observability.*feedback", r"build.*system", r"deployment.*automation"],
            "D6: Data Infrastructure": [r"database.*engineering", r"infrastructure.*engineering", r"cloud.*computing", r"data.*pipeline", r"storage.*system"],
            "D7: Human Interaction": [r"human.*loop", r"human.*interaction", r"user.*interface", r"collaboration.*tool", r"feedback.*system"],
            "D8: Model Management": [r"model.*management", r"model.*capability", r"fine.*tuning", r"model.*selection", r"model.*evaluation"],
            "D9: Research Discipline": [r"research.*methodology", r"benchmarking.*framework", r"evaluation.*metric", r"research.*design", r"experiment.*protocol"],
            "D10: Scaling Enterprise": [r"large.*codebase", r"enterprise.*scaling", r"ecosystem.*intelligence", r"team.*collaboration", r"organizational.*scale"],
            "D11: Advanced Runtime": [r"autonomous.*runtime", r"runtime.*system", r"execution.*engine", r"process.*management", r"resource.*allocation"],
            "D12: Self-Improvement": [r"self.*improvement", r"system.*optimization", r"continuous.*learning", r"adaptive.*system", r"performance.*tuning"]
        }
    
    def _build_sdlc_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to SDLC phases"""
        return {
            "P1: Requirements": [r"requirement.*gathering", r"specification.*analysis", r"user.*story", r"business.*need"],
            "P2: Design": [r"architectural.*design", r"system.*design", r"component.*design", r"interface.*design"],
            "P3: Implementation": [r"code.*generation", r"implementation.*phase", r"coding.*standard", r"development.*process"],
            "P4: Testing": [r"test.*generation", r"test.*automation", r"quality.*assurance", r"defect.*detection"],
            "P5: Deployment": [r"deployment.*process", r"release.*management", r"environment.*provisioning", r"configuration.*management"],
            "P6: Operation": [r"production.*run", r"monitoring.*system", r"incident.*response", r"performance.*management"],
            "P7: Maintenance": [r"code.*maintenance", r"refactoring.*process", r"bug.*fixing", r"system.*evolution"],
            "P8: Retirement": [r"system.*retirement", r"decommissioning.*process", r"legacy.*system", r"end.*of.*life"]
        }
    
    def _build_product_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Build patterns to map content to product categories"""
        return {
            "PC1: AI Coding Assistants": [r"coding.*assistant", r"code.*completion", r"AI.*programmer", r"developer.*assistant"],
            "PC2: Agent Orchestration Frameworks": [r"agent.*framework", r"orchestration.*platform", r"workflow.*management", r"task.*orchestrator"],
            "PC3: Code Analysis Tools": [r"code.*analysis", r"static.*analysis", r"dynamic.*analysis", r"code.*quality"],
            "PC4: Testing Automation": [r"test.*automation", r"test.*generation", r"testing.*framework", r"quality.*gate"],
            "PC5: CI/CD Systems": [r"CI/CD.*system", r"build.*automation", r"continuous.*integration", r"continuous.*delivery"],
            "PC6: Context Management": [r"context.*manager", r"memory.*system", r"knowledge.*base", r"information.*retrieval"],
            "PC7: Knowledge Bases": [r"knowledge.*base", r"documentation.*system", r"information.*repository", r"knowledge.*management"],
            "PC8: DevOps Platforms": [r"DevOps.*platform", r"cloud.*platform", r"infrastructure.*platform", r"tool.*chain"],
            "PC9: Security Tools": [r"security.*tool", r"vulnerability.*detection", r"compliance.*checker", r"security.*scanner"],
            "PC10: Observability Platforms": [r"observability.*platform", r"monitoring.*tool", r"log.*management", r"trace.*analysis"]
        }
    
    def _calculate_evidence_strength(self, content: str) -> str:
        """Determine evidence strength based on content patterns"""
        for strength, patterns in self.evidence_patterns.items():
            for pattern in patterns:
                if pattern.search(content):
                    return strength
        return "WEAK"  # default
    
    def _map_to_domains(self, content: str, file_path: str) -> List[str]:
        """Map content to technical domains using patterns and file location"""
        matched_domains = []
        
        # First, use file location to infer domain
        domain_mapping = {
            "01_meta_architecture": "D1: Meta Architecture",
            "02_agent_orchestration": "D2: Agent Orchestration",
            "03_context_memory_intelligence": "D3: Context & Memory Intelligence",
            "04_code_intelligence": "D4: Code Intelligence",
            "05_sdlc_automation": "D5: SDLC Automation",
            "06_data_infrastructure": "D6: Data Infrastructure",
            "07_human_interaction": "D7: Human Interaction",
            "08_model_management": "D8: Model Management",
            "09_research_discipline": "D9: Research Discipline",
            "10_scaling_enterprise": "D10: Scaling Enterprise",
            "11_advanced_runtime": "D11: Advanced Runtime",
            "12_self_improvement": "D12: Self-Improvement"
        }
        
        for dir_name, domain in domain_mapping.items():
            if dir_name in file_path:
                matched_domains.append(domain)
        
        # Then, use content patterns to find additional domains
        for domain, patterns in self.domain_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE) and domain not in matched_domains:
                    matched_domains.append(domain)
        
        return matched_domains if matched_domains else ["D9: Research Discipline"]
    
    def _map_to_sdlc_phases(self, content: str) -> List[str]:
        """Map content to SDLC phases using patterns"""
        matched_phases = []
        for phase, patterns in self.sdlc_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    matched_phases.append(phase)
        return matched_phases
    
    def _map_to_products(self, content: str) -> List[str]:
        """Map content to product categories using patterns"""
        matched_products = []
        for product, patterns in self.product_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    matched_products.append(product)
        return matched_products
    
    def _determine_atom_type(self, content: str) -> str:
        """Determine knowledge atom type based on content patterns"""
        patterns = {
            "TECHNIQUE": [
                r"Pattern: .*", r"Method: .*", r"Approach: .*",
                r"Strategy: .*", r"Technique: .*", r"Algorithm: .*",
                r"Protocol: .*", r"Architecture: .*", r"Framework: .*"
            ],
            "METRIC": [
                r"Score: .*", r"Metric: .*", r"Measurement: .*",
                r"\d+% .*", r"r\s*=\s*\d+\.\d+", r"F-score|precision|recall",
                r"Performance.*metric", r"Quality.*metric"
            ],
            "CONSTRAINT": [
                r"Constraint: .*", r"Hard limit: .*", r"Must.*",
                r"Cannot.*", r"Limit.*", r"Restriction.*"
            ],
            "TOOL": [
                r"Tool: .*", r"Platform: .*", r"Framework: .*",
                r"Library: .*", r"System: .*", r"Service: .*",
                r"LangGraph|CrewAI|AutoGen|MetaGPT|ChatDev"
            ],
            "COMBINATION": [
                r"Combine.*and.*", r"Integrate.*with.*", r"Work together.*",
                r"Synergy.*", r"Hybrid.*approach", r"Multi.*combination"
            ],
            "FAILURE MODE": [
                r"Failure mode: .*", r"Failure.*", r"Error.*",
                r"Bug.*", r"Problem.*", r"Issue.*", r"Risk.*"
            ],
            "ANTI-PATTERN": [
                r"Anti-pattern: .*", r"Bad practice: .*",
                r"Should avoid: .*", r"Not recommended: .*"
            ],
            "TRADEOFF": [
                r"Tradeoff: .*", r"Trade-off: .*", r"Balance.*",
                r"Advantage.*disadvantage", r"Pros.*cons", r"Benefit.*cost"
            ],
            "RECIPE": [
                r"Step \d+: .*", r"Procedure: .*", r"Process: .*",
                r"Sequence: .*", r"How to.*", r"Steps to.*"
            ]
        }
        
        for atom_type, pattern_list in patterns.items():
            for pattern in pattern_list:
                if re.search(pattern, content, re.IGNORECASE):
                    return atom_type
        
        return "TECHNIQUE"  # default
    
    def _should_keep(self, content: str) -> bool:
        """Determine if content should be kept as a knowledge atom"""
        discard_patterns = [
            r"Definition: .*", r"Definition of .*",
            r"Introduction to .*", r"Overview of .*",
            r"This paper.*", r"This study.*",
            r"Background.*", r"Related work.*",
            r"Future work.*", r"Conclusion.*",
            r"Abstract.*", r"Summary.*",
            r"References.*", r"Citations.*",
            r"Literature review.*", r"Survey of .*"
        ]
        
        for pattern in discard_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return False
        
        # Keep if contains specific information
        keep_patterns = [
            r"\d+%.*", r"r\s*=\s*\d+\.\d+", r"[A-Z][a-zA-Z]+ v\d+\.\d+",
            r"https?://[^\s]+", r"[A-Z]{2,}\d+", r"Step \d+:"
        ]
        
        return any(re.search(pattern, content) for pattern in keep_patterns)
    
    def _extract_pattern_sections(self, content: str) -> List[str]:
        """Extract sections that match pattern definitions"""
        sections = []
        
        # Pattern sections start with "Pattern:" or similar headers
        pattern_matches = re.finditer(r"### Pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in pattern_matches:
            sections.append(match.group(0).strip())
        
        # Tradeoff sections
        tradeoff_matches = re.finditer(r"### Tradeoff: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in tradeoff_matches:
            sections.append(match.group(0).strip())
        
        # Anti-pattern sections
        antipattern_matches = re.finditer(r"### Anti-pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in antipattern_matches:
            sections.append(match.group(0).strip())
        
        # Technique/algorithm sections
        technique_matches = re.finditer(r"### [^\n]+Algorithm[^\n]*(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
        for match in technique_matches:
            sections.append(match.group(0).strip())
        
        return sections
    
    def process_file(self, file_path: str) -> List[KnowledgeAtom]:
        """Process a single research file and extract knowledge atoms"""
        atoms = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return []
        
        # Extract sections that might contain knowledge atoms
        sections = self._extract_pattern_sections(content)
        
        if not sections:
            # Fallback: extract paragraphs containing pattern keywords
            paragraphs = re.split(r'\n\s*\n', content)
            sections = [p.strip() for p in paragraphs if len(p.strip()) > 50]
        
        for section in sections:
            if not self._should_keep(section):
                continue
                
            atom_type = self._determine_atom_type(section)
            evidence_strength = self._calculate_evidence_strength(section)
            domains = self._map_to_domains(section, file_path)
            sdlc_phases = self._map_to_sdlc_phases(section)
            products = self._map_to_products(section)
            
            # Create atom
            atom = KnowledgeAtom(
                atom_id=f"KA-{self.atom_counter:03d}",
                atom_type=atom_type,
                content=section.strip(),
                evidence_strength=evidence_strength,
                sources=[file_path],
                domains=domains,
                sdlc_phases=sdlc_phases,
                products=products
            )
            
            self.atom_counter += 1
            atoms.append(atom)
        
        return atoms
    
    def process_directory(self, directory: str) -> List[KnowledgeAtom]:
        """Process all research files in a directory recursively"""
        atoms = []
        
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                if file_name.endswith('.md') and not file_name.startswith('_'):
                    file_path = os.path.join(root, file_name)
                    print(f"Processing file: {file_path}")
                    file_atoms = self.process_file(file_path)
                    atoms.extend(file_atoms)
        
        return atoms
    
    def deduplicate_atoms(self, atoms: List[KnowledgeAtom]) -> List[KnowledgeAtom]:
        """Deduplicate knowledge atoms"""
        unique_atoms = []
        seen = set()
        
        for atom in atoms:
            atom_hash = hash(atom)
            if atom_hash not in seen:
                seen.add(atom_hash)
                unique_atoms.append(atom)
            else:
                # Merge sources if duplicate
                index = unique_atoms.index(atom)
                for source in atom.sources:
                    if source not in unique_atoms[index].sources:
                        unique_atoms[index].sources.append(source)
        
        return unique_atoms
    
    def rank_atoms(self, atoms: List[KnowledgeAtom]) -> Dict[str, List[KnowledgeAtom]]:
        """Rank atoms by type with evidence strength > specificity > uniqueness"""
        ranked = {atom_type: [] for atom_type in ATOM_TYPES}
        
        for atom in atoms:
            ranked[atom.atom_type].append(atom)
        
        # Rank within each type
        for atom_type in ranked:
            # First by evidence strength (STRONG > MODERATE > WEAK)
            # Then by specificity (more numbers, citations, details)
            # Then by uniqueness (longer content with more details)
            ranked[atom_type].sort(
                key=lambda x: (
                    -EVIDENCE_STRENGTH.index(x.evidence_strength),
                    -sum(1 for c in x.content if c.isdigit()),
                    -len(x.content.split()),
                    x.atom_id
                )
            )
        
        return ranked
    
    def process_all(self) -> Dict[str, List[KnowledgeAtom]]:
        """Process all research files and generate ranked, deduplicated atoms"""
        all_atoms = []
        
        # Process main research directory
        all_atoms.extend(self.process_directory(self.root_dir))
        
        # Process additional files
        additional_files = [
            "Perplexity_Thread.md",
            "Prompt_thread.md",
            "Research.md",
            "start_prompt.md"
        ]
        
        for file_name in additional_files:
            if os.path.exists(file_name):
                print(f"Processing additional file: {file_name}")
                file_atoms = self.process_file(file_name)
                all_atoms.extend(file_atoms)
        
        # Process Zenflow reports
        zenflow_dir = ".zenflow/tasks/new-task-97b2/reports"
        if os.path.exists(zenflow_dir):
            all_atoms.extend(self.process_directory(zenflow_dir))
        
        # Deduplicate
        unique_atoms = self.deduplicate_atoms(all_atoms)
        
        # Rank
        ranked_atoms = self.rank_atoms(unique_atoms)
        
        return ranked_atoms

def main():
    """Main function to run the extraction process"""
    print("Starting knowledge atom extraction...")
    
    processor = ResearchFileProcessor(root_dir="docs/research")
    ranked_atoms = processor.process_all()
    
    # Generate JSON output
    output_data = {}
    for atom_type, atoms in ranked_atoms.items():
        if atoms:
            output_data[atom_type] = [atom.to_dict() for atom in atoms]
    
    # Write to file
    output_path = "knowledge_atom_registry.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nExtraction complete!")
    print(f"Generated knowledge atom registry at: {output_path}")
    
    # Print summary
    total_atoms = sum(len(atoms) for atoms in ranked_atoms.values())
    print(f"\nSummary:")
    print(f"Total knowledge atoms extracted: {total_atoms}")
    for atom_type in ATOM_TYPES:
        count = len(ranked_atoms[atom_type])
        if count > 0:
            print(f"  {atom_type}: {count} atoms")

if __name__ == "__main__":
    main()
