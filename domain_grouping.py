import json
import os

# Load the knowledge atom registry
with open('knowledge_atom_registry.json', 'r') as f:
    registry = json.load(f)

# Define the 12 technical domains from the task
DOMAINS = {
    "D1": "Agent Architecture & Orchestration",
    "D2": "Task Management & Decomposition",
    "D3": "Context & Prompt Engineering",
    "D4": "Memory & Knowledge Systems",
    "D5": "Code Intelligence & Representations",
    "D6": "Testing & Validation",
    "D7": "Security & Guardrails",
    "D8": "Model Management & Routing",
    "D9": "CI/CD & DevOps",
    "D10": "Workspace & Infrastructure Management",
    "D11": "Human Interaction",
    "D12": "Self-Improvement & Optimization"
}

# Helper function to normalize domain names
def normalize_domain(domain_str):
    if not domain_str:
        return None
    # Extract domain code (e.g., "D2: Agent Orchestration" -> "D2")
    if ":" in domain_str:
        return domain_str.split(":")[0].strip()
    return domain_str.strip()

# Helper function to map old domains to new domains
def map_old_domain_to_new(old_domain_code):
    domain_mapping = {
        "D1": "D1",  # Meta Architecture -> Agent Architecture & Orchestration
        "D2": "D1",  # Agent Orchestration -> Agent Architecture & Orchestration
        "D3": "D3",  # Context & Memory Intelligence -> Context & Prompt Engineering
        "D5": "D6",  # SDLC Automation -> Testing & Validation
        "D7": "D11"  # Human Interaction remains D11
    }
    return domain_mapping.get(old_domain_code, old_domain_code)

# Create domain groups
domain_groups = {code: {"name": name, "atoms": []} for code, name in DOMAINS.items()}

# Process all knowledge atoms
all_atoms = []
for atom_type in ["TECHNIQUE", "TRADEOFF", "ANTI-PATTERN"]:
    if atom_type in registry:
        all_atoms.extend(registry[atom_type])

for atom in all_atoms:
    # Get normalized domains for the atom
    atom_domains = []
    if "DOMAINS" in atom:
        for domain_str in atom["DOMAINS"]:
            old_domain_code = normalize_domain(domain_str)
            new_domain_code = map_old_domain_to_new(old_domain_code)
            atom_domains.append(new_domain_code)
    
    # If no domains specified, skip (or assign to default)
    if not atom_domains:
        continue
        
    # Add atom to each domain it belongs to
    for domain_code in atom_domains:
        if domain_code in domain_groups:
            domain_groups[domain_code]["atoms"].append(atom)

# Rank atoms by evidence strength (STRONG > MODERATE > WEAK)
def rank_atoms(atoms):
    strength_order = {"STRONG": 3, "MODERATE": 2, "WEAK": 1}
    return sorted(
        atoms,
        key=lambda x: (strength_order.get(x["EVIDENCE_STRENGTH"], 0), x["ID"]),
        reverse=True
    )

# Rank atoms in each domain
for domain_code in domain_groups:
    domain_groups[domain_code]["atoms"] = rank_atoms(domain_groups[domain_code]["atoms"])

# Helper function to extract key techniques from domain atoms
def extract_key_techniques(atoms):
    techniques = [atom for atom in atoms if atom["TYPE"] == "TECHNIQUE"]
    ranked_techniques = []
    for i, atom in enumerate(techniques[:5], 1):  # Top 5 techniques
        summary = atom["CONTENT"].split(".")[0] + "."  # Get first sentence
        ranked_techniques.append({
            "rank": i,
            "id": atom["ID"],
            "summary": summary,
            "evidence_strength": atom["EVIDENCE_STRENGTH"]
        })
    return ranked_techniques

# Helper function to extract key constraints from domain atoms
def extract_key_constraints(atoms):
    constraints = []
    for atom in atoms:
        if atom["TYPE"] == "TRADEOFF":
            # Extract the tradeoff constraints (the "vs." part)
            content = atom["CONTENT"]
            if "vs." in content:
                constraint_part = content.split("vs.")[1].strip()
                constraints.append({
                    "id": atom["ID"],
                    "constraint": constraint_part
                })
    return constraints

# Helper function to extract failure modes from domain atoms
def extract_failure_modes(atoms):
    failure_modes = []
    for atom in atoms:
        if atom["TYPE"] == "ANTI-PATTERN":
            failure_modes.append({
                "id": atom["ID"],
                "what_breaks": atom["CONTENT"],
                "how_to_detect": "Monitor for wasted tokens, model confusion, or degraded performance",
                "how_to_respond": "Implement context filtering and prioritization"
            })
        elif atom["TYPE"] == "TRADEOFF":
            content = atom["CONTENT"]
            if "vs." in content:
                constraint_part = content.split("vs.")[1].strip()
                failure_modes.append({
                    "id": atom["ID"],
                    "what_breaks": constraint_part,
                    "how_to_detect": "Monitor system metrics (latency, throughput, error rates)",
                    "how_to_respond": "Optimize subsystem communication or adjust task decomposition"
                })
    return failure_modes

# Helper function to extract cross-domain links
def extract_cross_domain_links(all_atoms, domain_code):
    cross_links = []
    for atom in all_atoms:
        if "DOMAINS" in atom and len(atom["DOMAINS"]) > 1:
            # Check if atom belongs to current domain
            atom_domain_codes = [map_old_domain_to_new(normalize_domain(d)) for d in atom["DOMAINS"]]
            if domain_code in atom_domain_codes:
                # Get other domain codes
                other_domain_codes = [d for d in atom_domain_codes if d != domain_code]
                other_domain_names = [DOMAINS[d] for d in other_domain_codes if d in DOMAINS]
                cross_links.append({
                    "id": atom["ID"],
                    "other_domains": other_domain_names
                })
    return cross_links

# Generate domain reports
domain_reports = {}

for domain_code, domain_info in domain_groups.items():
    domain_reports[domain_code] = {
        "name": domain_info["name"],
        "knowledge_atoms": [atom["ID"] for atom in domain_info["atoms"]],
        "key_techniques": extract_key_techniques(domain_info["atoms"]),
        "key_constraints": extract_key_constraints(domain_info["atoms"]),
        "key_tools": [],  # No tools in current registry
        "combination_recipes": [],  # No combination recipes in current registry
        "failure_modes": extract_failure_modes(domain_info["atoms"]),
        "cross_domain_links": extract_cross_domain_links(all_atoms, domain_code),
        "gaps": []
    }

# Identify gaps in each domain (domains with no atoms)
for domain_code, domain_info in domain_groups.items():
    if not domain_info["atoms"]:
        domain_reports[domain_code]["gaps"].append("No knowledge atoms available for this domain")

# Add specific gaps for domains with atoms
specific_gaps = {
    "D4": ["Memory persistence and retrieval mechanisms", "Knowledge graph construction and maintenance", "Long-term memory architectures"],
    "D5": ["Code representation learning", "Semantic code analysis", "Code summarization techniques"],
    "D7": ["Security vulnerability detection in AI-generated code", "Access control mechanisms for agent systems", "Data privacy protection"],
    "D8": ["Model selection and routing algorithms", "Model versioning and provenance", "Model performance monitoring"],
    "D9": ["CI/CD pipeline automation for agent systems", "Deployment strategies for AI applications", "DevOps practices for agentic workflows"],
    "D10": ["Workspace management and isolation", "Resource allocation and scheduling", "Infrastructure provisioning for agents"],
    "D12": ["Self-improvement algorithms", "Performance optimization techniques", "Continuous learning mechanisms"]
}

for domain_code, gaps in specific_gaps.items():
    if domain_code in domain_reports:
        domain_reports[domain_code]["gaps"].extend(gaps)

# Save domain grouping to JSON file
output_file = "domain_knowledge_grouping.json"
with open(output_file, 'w') as f:
    json.dump(domain_reports, f, indent=2)

# Print summary
print("Domain Knowledge Grouping Complete")
print(f"Generated file: {output_file}")
print("\nDomain Summary:")
for domain_code, domain_info in domain_reports.items():
    print(f"{domain_code}: {domain_info['name']} - {len(domain_info['knowledge_atoms'])} atoms")

# Print domains with no atoms
print("\nDomains with No Atoms:")
for domain_code, domain_info in domain_reports.items():
    if not domain_info["knowledge_atoms"]:
        print(f"{domain_code}: {domain_info['name']}")
import os

# Load the knowledge atom registry
with open('knowledge_atom_registry.json', 'r') as f:
    registry = json.load(f)

# Define the 12 technical domains from the task
DOMAINS = {
    "D1": "Agent Architecture & Orchestration",
    "D2": "Task Management & Decomposition",
    "D3": "Context & Prompt Engineering",
    "D4": "Memory & Knowledge Systems",
    "D5": "Code Intelligence & Representations",
    "D6": "Testing & Validation",
    "D7": "Security & Guardrails",
    "D8": "Model Management & Routing",
    "D9": "CI/CD & DevOps",
    "D10": "Workspace & Infrastructure Management",
    "D11": "Human Interaction",
    "D12": "Self-Improvement & Optimization"
}

# Helper function to normalize domain names
def normalize_domain(domain_str):
    if not domain_str:
        return None
    # Extract domain code (e.g., "D2: Agent Orchestration" -> "D2")
    if ":" in domain_str:
        return domain_str.split(":")[0].strip()
    return domain_str.strip()

# Helper function to map old domains to new domains
def map_old_domain_to_new(old_domain_code):
    domain_mapping = {
        "D1": "D1",  # Meta Architecture -> Agent Architecture & Orchestration
        "D2": "D1",  # Agent Orchestration -> Agent Architecture & Orchestration
        "D3": "D3",  # Context & Memory Intelligence -> Context & Prompt Engineering
        "D5": "D6",  # SDLC Automation -> Testing & Validation
        "D7": "D11"  # Human Interaction remains D11
    }
    return domain_mapping.get(old_domain_code, old_domain_code)

# Create domain groups
domain_groups = {code: {"name": name, "atoms": []} for code, name in DOMAINS.items()}

# Process all knowledge atoms
all_atoms = []
for atom_type in ["TECHNIQUE", "TRADEOFF", "ANTI-PATTERN"]:
    if atom_type in registry:
        all_atoms.extend(registry[atom_type])

for atom in all_atoms:
    # Get normalized domains for the atom
    atom_domains = []
    if "DOMAINS" in atom:
        for domain_str in atom["DOMAINS"]:
            old_domain_code = normalize_domain(domain_str)
            new_domain_code = map_old_domain_to_new(old_domain_code)
            atom_domains.append(new_domain_code)
    
    # If no domains specified, skip (or assign to default)
    if not atom_domains:
        continue
        
    # Add atom to each domain it belongs to
    for domain_code in atom_domains:
        if domain_code in domain_groups:
            domain_groups[domain_code]["atoms"].append(atom)

# Rank atoms by evidence strength (STRONG > MODERATE > WEAK)
def rank_atoms(atoms):
    strength_order = {"STRONG": 3, "MODERATE": 2, "WEAK": 1}
    return sorted(
        atoms,
        key=lambda x: (strength_order.get(x["EVIDENCE_STRENGTH"], 0), x["ID"]),
        reverse=True
    )

# Rank atoms in each domain
for domain_code in domain_groups:
    domain_groups[domain_code]["atoms"] = rank_atoms(domain_groups[domain_code]["atoms"])

# Helper function to extract key techniques from domain atoms
def extract_key_techniques(atoms):
    techniques = [atom for atom in atoms if atom["TYPE"] == "TECHNIQUE"]
    ranked_techniques = []
    for i, atom in enumerate(techniques[:5], 1):  # Top 5 techniques
        summary = atom["CONTENT"].split(".")[0] + "."  # Get first sentence
        ranked_techniques.append({
            "rank": i,
            "id": atom["ID"],
            "summary": summary,
            "evidence_strength": atom["EVIDENCE_STRENGTH"]
        })
    return ranked_techniques

# Helper function to extract key constraints from domain atoms
def extract_key_constraints(atoms):
    constraints = []
    for atom in atoms:
        if atom["TYPE"] == "TRADEOFF":
            # Extract the tradeoff constraints (the "vs." part)
            content = atom["CONTENT"]
            if "vs." in content:
                constraint_part = content.split("vs.")[1].strip()
                constraints.append({
                    "id": atom["ID"],
                    "constraint": constraint_part
                })
    return constraints

# Helper function to extract failure modes from domain atoms
def extract_failure_modes(atoms):
    failure_modes = []
    for atom in atoms:
        if atom["TYPE"] == "ANTI-PATTERN":
            failure_modes.append({
                "id": atom["ID"],
                "what_breaks": atom["CONTENT"],
                "how_to_detect": "Monitor for wasted tokens, model confusion, or degraded performance",
                "how_to_respond": "Implement context filtering and prioritization"
            })
        elif atom["TYPE"] == "TRADEOFF":
            content = atom["CONTENT"]
            if "vs." in content:
                constraint_part = content.split("vs.")[1].strip()
                failure_modes.append({
                    "id": atom["ID"],
                    "what_breaks": constraint_part,
                    "how_to_detect": "Monitor system metrics (latency, throughput, error rates)",
                    "how_to_respond": "Optimize subsystem communication or adjust task decomposition"
                })
    return failure_modes

# Helper function to extract cross-domain links
def extract_cross_domain_links(all_atoms, domain_code):
    cross_links = []
    for atom in all_atoms:
        if "DOMAINS" in atom and len(atom["DOMAINS"]) > 1:
            # Check if atom belongs to current domain
            atom_domain_codes = [map_old_domain_to_new(normalize_domain(d)) for d in atom["DOMAINS"]]
            if domain_code in atom_domain_codes:
                # Get other domain codes
                other_domain_codes = [d for d in atom_domain_codes if d != domain_code]
                other_domain_names = [DOMAINS[d] for d in other_domain_codes if d in DOMAINS]
                cross_links.append({
                    "id": atom["ID"],
                    "other_domains": other_domain_names
                })
    return cross_links

# Generate domain reports
domain_reports = {}

for domain_code, domain_info in domain_groups.items():
    domain_reports[domain_code] = {
        "name": domain_info["name"],
        "knowledge_atoms": [atom["ID"] for atom in domain_info["atoms"]],
        "key_techniques": extract_key_techniques(domain_info["atoms"]),
        "key_constraints": extract_key_constraints(domain_info["atoms"]),
        "key_tools": [],  # No tools in current registry
        "combination_recipes": [],  # No combination recipes in current registry
        "failure_modes": extract_failure_modes(domain_info["atoms"]),
        "cross_domain_links": extract_cross_domain_links(all_atoms, domain_code),
        "gaps": []
    }

# Identify gaps in each domain (domains with no atoms)
for domain_code, domain_info in domain_groups.items():
    if not domain_info["atoms"]:
        domain_reports[domain_code]["gaps"].append("No knowledge atoms available for this domain")

# Add specific gaps for domains with atoms
specific_gaps = {
    "D4": ["Memory persistence and retrieval mechanisms", "Knowledge graph construction and maintenance", "Long-term memory architectures"],
    "D5": ["Code representation learning", "Semantic code analysis", "Code summarization techniques"],
    "D7": ["Security vulnerability detection in AI-generated code", "Access control mechanisms for agent systems", "Data privacy protection"],
    "D8": ["Model selection and routing algorithms", "Model versioning and provenance", "Model performance monitoring"],
    "D9": ["CI/CD pipeline automation for agent systems", "Deployment strategies for AI applications", "DevOps practices for agentic workflows"],
    "D10": ["Workspace management and isolation", "Resource allocation and scheduling", "Infrastructure provisioning for agents"],
    "D12": ["Self-improvement algorithms", "Performance optimization techniques", "Continuous learning mechanisms"]
}

for domain_code, gaps in specific_gaps.items():
    if domain_code in domain_reports:
        domain_reports[domain_code]["gaps"].extend(gaps)

# Save domain grouping to JSON file
output_file = "domain_knowledge_grouping.json"
with open(output_file, 'w') as f:
    json.dump(domain_reports, f, indent=2)

# Print summary
print("Domain Knowledge Grouping Complete")
print(f"Generated file: {output_file}")
print("\nDomain Summary:")
for domain_code, domain_info in domain_reports.items():
    print(f"{domain_code}: {domain_info['name']} - {len(domain_info['knowledge_atoms'])} atoms")

# Print domains with no atoms
print("\nDomains with No Atoms:")
for domain_code, domain_info in domain_reports.items():
    if not domain_info["knowledge_atoms"]:
        print(f"{domain_code}: {domain_info['name']}")

