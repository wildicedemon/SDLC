import os
import re
import json

# Knowledge Atom Types
ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
]

def main():
    print("Starting knowledge atom extraction...")
    all_atoms = []
    atom_counter = 1
    
    # Process main research files
    files_to_process = [
        "docs/research/02_agent_orchestration/agent_system_design/patterns.md",
        "docs/research/03_context_memory_intelligence/context_management/patterns.md",
        "docs/research/05_sdlc_automation/testing_architecture/patterns.md"
    ]
    
    for file_path in files_to_process:
        if os.path.exists(file_path):
            print(f"Processing file: {file_path}")
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
    
    print(f"Extracted {len(all_atoms)} atoms")
    
    # Save to JSON
    with open("knowledge_atom_registry.json", 'w', encoding='utf-8') as f:
        json.dump(all_atoms, f, indent=2, ensure_ascii=False)
    
    print("Registry saved to knowledge_atom_registry.json")

def extract_sections(content):
    sections = []
    pattern_matches = re.finditer(r"### Pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
    for match in pattern_matches:
        sections.append(match.group(0).strip())
    return sections

def should_keep(content):
    discard_patterns = [r"Definition:", r"Introduction", r"Overview"]
    for pattern in discard_patterns:
        if pattern in content:
            return False
    return True

def create_atom(atom_id, content, file_path):
    return {
        "ID": f"KA-{atom_id:03d}",
        "TYPE": determine_type(content),
        "CONTENT": content,
        "EVIDENCE_STRENGTH": "STRONG",
        "SOURCE": [file_path],
        "DOMAINS": get_domains(file_path),
        "SDLC_PHASES": get_sdlc_phases(),
        "PRODUCTS": get_products()
    }

def determine_type(content):
    if "Pattern:" in content:
        return "TECHNIQUE"
    elif "Tradeoff:" in content:
        return "TRADEOFF"
    elif "Anti-pattern:" in content:
        return "ANTI-PATTERN"
    else:
        return "TECHNIQUE"

def get_domains(file_path):
    if "agent" in file_path:
        return ["D2: Agent Orchestration"]
    elif "context" in file_path:
        return ["D3: Context & Memory Intelligence"]
    elif "testing" in file_path:
        return ["D5: SDLC Automation"]
    return ["D9: Research Discipline"]

def get_sdlc_phases():
    return ["P1: Requirements", "P2: Design", "P3: Implementation"]

def get_products():
    return ["PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks"]

if __name__ == "__main__":
    main()import re
import json

# Knowledge Atom Types
ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
]

def main():
    print("Starting knowledge atom extraction...")
    all_atoms = []
    atom_counter = 1
    
    # Process main research files
    files_to_process = [
        "docs/research/02_agent_orchestration/agent_system_design/patterns.md",
        "docs/research/03_context_memory_intelligence/context_management/patterns.md",
        "docs/research/05_sdlc_automation/testing_architecture/patterns.md"
    ]
    
    for file_path in files_to_process:
        if os.path.exists(file_path):
            print(f"Processing file: {file_path}")
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
    
    print(f"Extracted {len(all_atoms)} atoms")
    
    # Save to JSON
    with open("knowledge_atom_registry.json", 'w', encoding='utf-8') as f:
        json.dump(all_atoms, f, indent=2, ensure_ascii=False)
    
    print("Registry saved to knowledge_atom_registry.json")

def extract_sections(content):
    sections = []
    pattern_matches = re.finditer(r"### Pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)", content)
    for match in pattern_matches:
        sections.append(match.group(0).strip())
    return sections

def should_keep(content):
    discard_patterns = [r"Definition:", r"Introduction", r"Overview"]
    for pattern in discard_patterns:
        if pattern in content:
            return False
    return True

def create_atom(atom_id, content, file_path):
    return {
        "ID": f"KA-{atom_id:03d}",
        "TYPE": determine_type(content),
        "CONTENT": content,
        "EVIDENCE_STRENGTH": "STRONG",
        "SOURCE": [file_path],
        "DOMAINS": get_domains(file_path),
        "SDLC_PHASES": get_sdlc_phases(),
        "PRODUCTS": get_products()
    }

def determine_type(content):
    if "Pattern:" in content:
        return "TECHNIQUE"
    elif "Tradeoff:" in content:
        return "TRADEOFF"
    elif "Anti-pattern:" in content:
        return "ANTI-PATTERN"
    else:
        return "TECHNIQUE"

def get_domains(file_path):
    if "agent" in file_path:
        return ["D2: Agent Orchestration"]
    elif "context" in file_path:
        return ["D3: Context & Memory Intelligence"]
    elif "testing" in file_path:
        return ["D5: SDLC Automation"]
    return ["D9: Research Discipline"]

def get_sdlc_phases():
    return ["P1: Requirements", "P2: Design", "P3: Implementation"]

def get_products():
    return ["PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks"]

if __name__ == "__main__":
    main()
