import os
import re
import json

# Knowledge Atom Types
ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
]

# Evidence Strength Levels
EVIDENCE_STRENGTH = ["STRONG", "MODERATE", "WEAK"]

def extract_knowledge_atoms():
    all_atoms = []
    atom_counter = 1
    processed_files = 0
    
    print("Starting knowledge atom extraction...")
    
    # Process main research directory
    research_dir = "docs/research"
    for root, dirs, files in os.walk(research_dir):
        for file_name in files:
            if file_name.endswith('.md') and not file_name.startswith('_'):
                file_path = os.path.join(root, file_name)
                processed_files += 1
                print(f"Processing file {processed_files}: {file_path}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    sections = extract_sections(content)
                    
                    for section in sections:
                        if should_keep(section):
                            atom = create_atom(atom_counter, section, file_path)
                            all_atoms.append(atom)
                            atom_counter += 1
                            
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    # Process additional files
    additional_files = ["Perplexity_Thread.md", "Prompt_thread.md", "Research.md", "start_prompt.md"]
    for file_name in additional_files:
        if os.path.exists(file_name):
            processed_files += 1
            print(f"Processing file {processed_files}: {file_name}")
            
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                sections = extract_sections(content)
                
                for section in sections:
                    if should_keep(section):
                        atom = create_atom(atom_counter, section, file_name)
                        all_atoms.append(atom)
                        atom_counter += 1
                        
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
    
    # Process Zenflow reports
    zenflow_dir = ".zenflow/tasks/new-task-97b2/reports"
    if os.path.exists(zenflow_dir):
        for root, dirs, files in os.walk(zenflow_dir):
            for file_name in files:
                if file_name.endswith('.md'):
                    file_path = os.path.join(root, file_name)
                    processed_files += 1
                    print(f"Processing file {processed_files}: {file_path}")
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        sections = extract_sections(content)
                        
                        for section in sections:
                            if should_keep(section):
                                atom = create_atom(atom_counter, section, file_path)
                                all_atoms.append(atom)
                                atom_counter += 1
                                
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
    
    unique_atoms = deduplicate_atoms(all_atoms)
    ranked_atoms = rank_atoms(unique_atoms)
    
    output_path = "knowledge_atom_registry.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ranked_atoms, f, indent=2, ensure_ascii=False)
    
    print(f"\nExtraction complete!")
    print(f"Generated knowledge atom registry at: {output_path}")
    
    total_atoms = sum(len(atoms) for atoms in ranked_atoms.values())
    print(f"\nSummary:")
    print(f"Total knowledge atoms extracted: {total_atoms}")
    for atom_type in ATOM_TYPES:
        count = len(ranked_atoms.get(atom_type, []))
        if count > 0:
            print(f"  {atom_type}: {count} atoms")

def extract_sections(content):
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
    
    technique_matches = re.finditer(r"### [^\n]+Algorithm[^\n]*(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
    for match in technique_matches:
        sections.append(match.group(0).strip())
    
    if not sections:
        paragraphs = re.split(r'\n\s*\n', content)
        sections = [p.strip() for p in paragraphs if len(p.strip()) > 50]
    
    return sections

def should_keep(content):
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

def determine_atom_type(content):
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
    
    return "TECHNIQUE"

def calculate_evidence_strength(content):
    evidence_patterns = {
        "STRONG": [
            r"Confidence: HIGH", r"Empirically validated",
            r"Based on .* research", r"\[[^]]*\]:.*(arxiv|ieee|acm|springer)",
            r"\d+% improvement", r"r\s*=\s*\d+\.\d+", r"Hard limit|invariant|must"
        ],
        "MODERATE": [
            r"Confidence: MEDIUM", r"Emerging pattern",
            r"Practitioner experience", r"May improve|could reduce",
            r"Plausible|suggested"
        ],
        "WEAK": [
            r"Confidence: LOW", r"Should consider|may want to",
            r"Recommendation|suggestion", r"Possibly|potentially"
        ]
    }
    
    for strength, patterns in evidence_patterns.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return strength
    return "WEAK"

def map_to_domains(content, file_path):
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
    
    domain_patterns = {
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
    
    for domain, patterns in domain_patterns.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE) and domain not in matched_domains:
                matched_domains.append(domain)
    
    return matched_domains if matched_domains else ["D9: Research Discipline"]

def map_to_sdlc_phases(content):
    matched_phases = []
    phase_patterns = {
        "P1: Requirements": [r"requirement.*gathering", r"specification.*analysis", r"user.*story", r"business.*need"],
        "P2: Design": [r"architectural.*design", r"system.*design", r"component.*design", r"interface.*design"],
        "P3: Implementation": [r"code.*generation", r"implementation.*phase", r"coding.*standard", r"development.*process"],
        "P4: Testing": [r"test.*generation", r"test.*automation", r"quality.*assurance", r"defect.*detection"],
        "P5: Deployment": [r"deployment.*process", r"release.*management", r"environment.*provisioning", r"configuration.*management"],
        "P6: Operation": [r"production.*run", r"monitoring.*system", r"incident.*response", r"performance.*management"],
        "P7: Maintenance": [r"code.*maintenance", r"refactoring.*process", r"bug.*fixing", r"system.*evolution"],
        "P8: Retirement": [r"system.*retirement", r"decommissioning.*process", r"legacy.*system", r"end.*of.*life"]
    }
    
    for phase, patterns in phase_patterns.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                matched_phases.append(phase)
    return matched_phases

def map_to_products(content):
    matched_products = []
    product_patterns = {
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
    
    for product, patterns in product_patterns.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                matched_products.append(product)
    return matched_products

def create_atom(atom_id, content, file_path):
    return {
        "ID": f"KA-{atom_id:03d}",
        "TYPE": determine_atom_type(content),
        "CONTENT": content,
        "EVIDENCE_STRENGTH": calculate_evidence_strength(content),
        "SOURCE": [file_path],
        "DOMAINS": map_to_domains(content, file_path),
        "SDLC_PHASES": map_to_sdlc_phases(content),
        "PRODUCTS": map_to_products(content)
    }

def deduplicate_atoms(atoms):
    unique_atoms = []
    seen = set()
    
    for atom in atoms:
        key = (atom["TYPE"], atom["CONTENT"].strip().lower())
        if key not in seen:
            seen.add(key)
            unique_atoms.append(atom)
        else:
            index = None
            for i, existing_atom in enumerate(unique_atoms):
                if (existing_atom["TYPE"], existing_atom["CONTENT"].strip().lower()) == key:
                    index = i
                    break
            if index is not None:
                for source in atom["SOURCE"]:
                    if source not in unique_atoms[index]["SOURCE"]:
                        unique_atoms[index]["SOURCE"].append(source)
    
    return unique_atoms

def rank_atoms(atoms):
    ranked = {atom_type: [] for atom_type in ATOM_TYPES}
    
    for atom in atoms:
        ranked[atom["TYPE"]].append(atom)
    
    for atom_type in ranked:
        ranked[atom_type].sort(
            key=lambda x: (
                -EVIDENCE_STRENGTH.index(x["EVIDENCE_STRENGTH"]),
                -sum(1 for c in x["CONTENT"] if c.isdigit()),
                -len(x["CONTENT"].split()),
                x["ID"]
            )
        )
    
    return {k: v for k, v in ranked.items() if v}

if __name__ == "__main__":
    extract_knowledge_atoms()import re
import json

# Knowledge Atom Types
ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
]

# Evidence Strength Levels
EVIDENCE_STRENGTH = ["STRONG", "MODERATE", "WEAK"]

def extract_knowledge_atoms():
    all_atoms = []
    atom_counter = 1
    processed_files = 0
    
    print("Starting knowledge atom extraction...")
    
    # Process main research directory
    research_dir = "docs/research"
    for root, dirs, files in os.walk(research_dir):
        for file_name in files:
            if file_name.endswith('.md') and not file_name.startswith('_'):
                file_path = os.path.join(root, file_name)
                processed_files += 1
                print(f"Processing file {processed_files}: {file_path}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    sections = extract_sections(content)
                    
                    for section in sections:
                        if should_keep(section):
                            atom = create_atom(atom_counter, section, file_path)
                            all_atoms.append(atom)
                            atom_counter += 1
                            
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    # Process additional files
    additional_files = ["Perplexity_Thread.md", "Prompt_thread.md", "Research.md", "start_prompt.md"]
    for file_name in additional_files:
        if os.path.exists(file_name):
            processed_files += 1
            print(f"Processing file {processed_files}: {file_name}")
            
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                sections = extract_sections(content)
                
                for section in sections:
                    if should_keep(section):
                        atom = create_atom(atom_counter, section, file_name)
                        all_atoms.append(atom)
                        atom_counter += 1
                        
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
    
    # Process Zenflow reports
    zenflow_dir = ".zenflow/tasks/new-task-97b2/reports"
    if os.path.exists(zenflow_dir):
        for root, dirs, files in os.walk(zenflow_dir):
            for file_name in files:
                if file_name.endswith('.md'):
                    file_path = os.path.join(root, file_name)
                    processed_files += 1
                    print(f"Processing file {processed_files}: {file_path}")
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        sections = extract_sections(content)
                        
                        for section in sections:
                            if should_keep(section):
                                atom = create_atom(atom_counter, section, file_path)
                                all_atoms.append(atom)
                                atom_counter += 1
                                
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
    
    unique_atoms = deduplicate_atoms(all_atoms)
    ranked_atoms = rank_atoms(unique_atoms)
    
    output_path = "knowledge_atom_registry.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(ranked_atoms, f, indent=2, ensure_ascii=False)
    
    print(f"\nExtraction complete!")
    print(f"Generated knowledge atom registry at: {output_path}")
    
    total_atoms = sum(len(atoms) for atoms in ranked_atoms.values())
    print(f"\nSummary:")
    print(f"Total knowledge atoms extracted: {total_atoms}")
    for atom_type in ATOM_TYPES:
        count = len(ranked_atoms.get(atom_type, []))
        if count > 0:
            print(f"  {atom_type}: {count} atoms")

def extract_sections(content):
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
    
    technique_matches = re.finditer(r"### [^\n]+Algorithm[^\n]*(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
    for match in technique_matches:
        sections.append(match.group(0).strip())
    
    if not sections:
        paragraphs = re.split(r'\n\s*\n', content)
        sections = [p.strip() for p in paragraphs if len(p.strip()) > 50]
    
    return sections

def should_keep(content):
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

def determine_atom_type(content):
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
    
    return "TECHNIQUE"

def calculate_evidence_strength(content):
    evidence_patterns = {
        "STRONG": [
            r"Confidence: HIGH", r"Empirically validated",
            r"Based on .* research", r"\[[^]]*\]:.*(arxiv|ieee|acm|springer)",
            r"\d+% improvement", r"r\s*=\s*\d+\.\d+", r"Hard limit|invariant|must"
        ],
        "MODERATE": [
            r"Confidence: MEDIUM", r"Emerging pattern",
            r"Practitioner experience", r"May improve|could reduce",
            r"Plausible|suggested"
        ],
        "WEAK": [
            r"Confidence: LOW", r"Should consider|may want to",
            r"Recommendation|suggestion", r"Possibly|potentially"
        ]
    }
    
    for strength, patterns in evidence_patterns.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return strength
    return "WEAK"

def map_to_domains(content, file_path):
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
    
    domain_patterns = {
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
    
    for domain, patterns in domain_patterns.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE) and domain not in matched_domains:
                matched_domains.append(domain)
    
    return matched_domains if matched_domains else ["D9: Research Discipline"]

def map_to_sdlc_phases(content):
    matched_phases = []
    phase_patterns = {
        "P1: Requirements": [r"requirement.*gathering", r"specification.*analysis", r"user.*story", r"business.*need"],
        "P2: Design": [r"architectural.*design", r"system.*design", r"component.*design", r"interface.*design"],
        "P3: Implementation": [r"code.*generation", r"implementation.*phase", r"coding.*standard", r"development.*process"],
        "P4: Testing": [r"test.*generation", r"test.*automation", r"quality.*assurance", r"defect.*detection"],
        "P5: Deployment": [r"deployment.*process", r"release.*management", r"environment.*provisioning", r"configuration.*management"],
        "P6: Operation": [r"production.*run", r"monitoring.*system", r"incident.*response", r"performance.*management"],
        "P7: Maintenance": [r"code.*maintenance", r"refactoring.*process", r"bug.*fixing", r"system.*evolution"],
        "P8: Retirement": [r"system.*retirement", r"decommissioning.*process", r"legacy.*system", r"end.*of.*life"]
    }
    
    for phase, patterns in phase_patterns.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                matched_phases.append(phase)
    return matched_phases

def map_to_products(content):
    matched_products = []
    product_patterns = {
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
    
    for product, patterns in product_patterns.items():
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                matched_products.append(product)
    return matched_products

def create_atom(atom_id, content, file_path):
    return {
        "ID": f"KA-{atom_id:03d}",
        "TYPE": determine_atom_type(content),
        "CONTENT": content,
        "EVIDENCE_STRENGTH": calculate_evidence_strength(content),
        "SOURCE": [file_path],
        "DOMAINS": map_to_domains(content, file_path),
        "SDLC_PHASES": map_to_sdlc_phases(content),
        "PRODUCTS": map_to_products(content)
    }

def deduplicate_atoms(atoms):
    unique_atoms = []
    seen = set()
    
    for atom in atoms:
        key = (atom["TYPE"], atom["CONTENT"].strip().lower())
        if key not in seen:
            seen.add(key)
            unique_atoms.append(atom)
        else:
            index = None
            for i, existing_atom in enumerate(unique_atoms):
                if (existing_atom["TYPE"], existing_atom["CONTENT"].strip().lower()) == key:
                    index = i
                    break
            if index is not None:
                for source in atom["SOURCE"]:
                    if source not in unique_atoms[index]["SOURCE"]:
                        unique_atoms[index]["SOURCE"].append(source)
    
    return unique_atoms

def rank_atoms(atoms):
    ranked = {atom_type: [] for atom_type in ATOM_TYPES}
    
    for atom in atoms:
        ranked[atom["TYPE"]].append(atom)
    
    for atom_type in ranked:
        ranked[atom_type].sort(
            key=lambda x: (
                -EVIDENCE_STRENGTH.index(x["EVIDENCE_STRENGTH"]),
                -sum(1 for c in x["CONTENT"] if c.isdigit()),
                -len(x["CONTENT"].split()),
                x["ID"]
            )
        )
    
    return {k: v for k, v in ranked.items() if v}

if __name__ == "__main__":
    extract_knowledge_atoms()
