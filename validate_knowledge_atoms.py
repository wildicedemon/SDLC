import json
import sys

def validate_knowledge_atoms():
    # Load all JSON files
    with open('knowledge_atom_registry.json', 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    with open('domain_knowledge_grouping.json', 'r', encoding='utf-8') as f:
        domain_grouping = json.load(f)
    
    with open('sdlc_phase_knowledge_mapping.json', 'r', encoding='utf-8') as f:
        phase_mapping = json.load(f)
    
    with open('product_specs.json', 'r', encoding='utf-8') as f:
        product_specs = json.load(f)
    
    # Collect all knowledge atoms from registry
    all_atoms = set()
    for atom_type in registry:
        for atom in registry[atom_type]:
            all_atoms.add(atom['ID'])
    
    print(f"Total atoms in registry: {len(all_atoms)}")
    
    # Collect atoms from domain grouping
    domain_atoms = set()
    for domain in domain_grouping:
        for atom in domain_grouping[domain]['knowledge_atoms']:
            domain_atoms.add(atom)
    
    print(f"Total atoms in domain grouping: {len(domain_atoms)}")
    
    # Collect atoms from phase mapping
    phase_atoms = set()
    for phase in phase_mapping['PHASES']:
        for atom in phase['KNOWLEDGE_ATOMS']:
            phase_atoms.add(atom)
    
    print(f"Total atoms in phase mapping: {len(phase_atoms)}")
    
    # Collect atoms from product specs
    product_atoms = set()
    for product in product_specs['products']:
        for atom in product['knowledge_atoms']:
            product_atoms.add(atom)
    
    print(f"Total atoms in product specs: {len(product_atoms)}")
    
    # Check 1: Every atom referenced by at least one domain, phase, and product
    print("\n=== Check 1: Atoms referenced by domain, phase, and product ===")
    missing_domain = all_atoms - domain_atoms
    missing_phase = all_atoms - phase_atoms
    missing_product = all_atoms - product_atoms
    
    if missing_domain:
        print(f"Atoms missing from domains: {sorted(list(missing_domain))}")
    else:
        print("All atoms referenced by at least one domain")
    
    if missing_phase:
        print(f"Atoms missing from phases: {sorted(list(missing_phase))}")
    else:
        print("All atoms referenced by at least one phase")
    
    if missing_product:
        print(f"Atoms missing from products: {sorted(list(missing_product))}")
    else:
        print("All atoms referenced by at least one product")
    
    # Check 2: Skills referenced by Modes exist as Skill specs
    print("\n=== Check 2: Skills referenced by Modes ===")
    # Note: Mode specs don't explicitly reference skills in the provided files
    
    # Check 3: Skills referenced by Workflows exist as Skill specs
    print("\n=== Check 3: Skills referenced by Workflows ===")
    # Note: Workflow specs don't explicitly reference skills in the provided files
    
    # Check 4: Context strategies referenced by Modes exist as Context Strategy specs
    print("\n=== Check 4: Context strategies referenced by Modes ===")
    # Note: Mode specs don't explicitly reference context strategies in the provided files
    
    # Check 5: Rules are consistently applied across products that reference them
    print("\n=== Check 5: Consistent rule application ===")
    # Collect all rule atoms
    rule_atoms = set()
    for product in product_specs['products']:
        if product['category'] == 'PC6: RULES (Constraints & Guardrails)':
            for atom in product['knowledge_atoms']:
                rule_atoms.add(atom)
    
    # Check if all products that reference rules reference existing rule atoms
    for product in product_specs['products']:
        if 'constraints' in product['spec']:
            for constraint in product['spec']['constraints']:
                if constraint not in rule_atoms:
                    print(f"Product {product['instance']} references non-rule atom as constraint: {constraint}")
        if 'failure_modes' in product['spec']:
            for failure_mode in product['spec']['failure_modes']:
                if failure_mode['id'] not in rule_atoms:
                    print(f"Product {product['instance']} references non-rule atom as failure mode: {failure_mode['id']}")
    
    # Check 6: MCP configurations match the tools enabled in Mode specs
    print("\n=== Check 6: MCP configurations vs Mode tools ===")
    # Collect all MCP tool names
    mcp_tools = set()
    for product in product_specs['products']:
        if product['category'] == 'PC5: MCP CONFIGURATIONS (Tool Access Patterns)':
            if 'tools' in product['spec']:
                for tool in product['spec']['tools']:
                    mcp_tools.add(tool)
    
    # Check Mode tools against MCP tools
    for product in product_specs['products']:
        if product['category'] == 'PC1: MODES (Agent Operational Personas)':
            if 'tools' in product['spec']:
                for tool in product['spec']['tools']:
                    if tool.startswith('mcp--') and tool not in mcp_tools:
                        print(f"Mode {product['instance']} references undefined MCP tool: {tool}")
    
    # Check 7: Techniques cover the failure modes documented in Rules
    print("\n=== Check 7: Techniques covering failure modes ===")
    # Note: Need to analyze technique content vs rule failure modes (manual check)
    
    # Check 8: No orphan atoms (extracted but never consumed by any product)
    print("\n=== Check 8: Orphan atoms ===")
    orphan_atoms = all_atoms - product_atoms
    if orphan_atoms:
        print(f"Orphan atoms (not consumed by any product): {sorted(list(orphan_atoms))}")
    else:
        print("No orphan atoms")
    
    # Check for duplicate atoms in domain grouping
    print("\n=== Check: Duplicate atoms in domain grouping ===")
    all_domain_atoms = []
    for domain in domain_grouping:
        for atom in domain_grouping[domain]['knowledge_atoms']:
            all_domain_atoms.append(atom)
    
    duplicates = []
    seen = set()
    for atom in all_domain_atoms:
        if atom in seen:
            duplicates.append(atom)
        else:
            seen.add(atom)
    
    if duplicates:
        print(f"Duplicate atoms in domain grouping: {sorted(list(set(duplicates)))}")
    else:
        print("No duplicate atoms in domain grouping")
    
    # Check for atoms in domain/phase/product that don't exist in registry
    print("\n=== Check: Atoms in domain/phase/product not in registry ===")
    invalid_domain = domain_atoms - all_atoms
    invalid_phase = phase_atoms - all_atoms
    invalid_product = product_atoms - all_atoms
    
    if invalid_domain:
        print(f"Invalid atoms in domain grouping: {sorted(list(invalid_domain))}")
    if invalid_phase:
        print(f"Invalid atoms in phase mapping: {sorted(list(invalid_phase))}")
    if invalid_product:
        print(f"Invalid atoms in product specs: {sorted(list(invalid_product))}")

if __name__ == "__main__":
    validate_knowledge_atoms()
import sys

def validate_knowledge_atoms():
    # Load all JSON files
    with open('knowledge_atom_registry.json', 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    with open('domain_knowledge_grouping.json', 'r', encoding='utf-8') as f:
        domain_grouping = json.load(f)
    
    with open('sdlc_phase_knowledge_mapping.json', 'r', encoding='utf-8') as f:
        phase_mapping = json.load(f)
    
    with open('product_specs.json', 'r', encoding='utf-8') as f:
        product_specs = json.load(f)
    
    # Collect all knowledge atoms from registry
    all_atoms = set()
    for atom_type in registry:
        for atom in registry[atom_type]:
            all_atoms.add(atom['ID'])
    
    print(f"Total atoms in registry: {len(all_atoms)}")
    
    # Collect atoms from domain grouping
    domain_atoms = set()
    for domain in domain_grouping:
        for atom in domain_grouping[domain]['knowledge_atoms']:
            domain_atoms.add(atom)
    
    print(f"Total atoms in domain grouping: {len(domain_atoms)}")
    
    # Collect atoms from phase mapping
    phase_atoms = set()
    for phase in phase_mapping['PHASES']:
        for atom in phase['KNOWLEDGE_ATOMS']:
            phase_atoms.add(atom)
    
    print(f"Total atoms in phase mapping: {len(phase_atoms)}")
    
    # Collect atoms from product specs
    product_atoms = set()
    for product in product_specs['products']:
        for atom in product['knowledge_atoms']:
            product_atoms.add(atom)
    
    print(f"Total atoms in product specs: {len(product_atoms)}")
    
    # Check 1: Every atom referenced by at least one domain, phase, and product
    print("\n=== Check 1: Atoms referenced by domain, phase, and product ===")
    missing_domain = all_atoms - domain_atoms
    missing_phase = all_atoms - phase_atoms
    missing_product = all_atoms - product_atoms
    
    if missing_domain:
        print(f"Atoms missing from domains: {sorted(list(missing_domain))}")
    else:
        print("All atoms referenced by at least one domain")
    
    if missing_phase:
        print(f"Atoms missing from phases: {sorted(list(missing_phase))}")
    else:
        print("All atoms referenced by at least one phase")
    
    if missing_product:
        print(f"Atoms missing from products: {sorted(list(missing_product))}")
    else:
        print("All atoms referenced by at least one product")
    
    # Check 2: Skills referenced by Modes exist as Skill specs
    print("\n=== Check 2: Skills referenced by Modes ===")
    # Note: Mode specs don't explicitly reference skills in the provided files
    
    # Check 3: Skills referenced by Workflows exist as Skill specs
    print("\n=== Check 3: Skills referenced by Workflows ===")
    # Note: Workflow specs don't explicitly reference skills in the provided files
    
    # Check 4: Context strategies referenced by Modes exist as Context Strategy specs
    print("\n=== Check 4: Context strategies referenced by Modes ===")
    # Note: Mode specs don't explicitly reference context strategies in the provided files
    
    # Check 5: Rules are consistently applied across products that reference them
    print("\n=== Check 5: Consistent rule application ===")
    # Collect all rule atoms
    rule_atoms = set()
    for product in product_specs['products']:
        if product['category'] == 'PC6: RULES (Constraints & Guardrails)':
            for atom in product['knowledge_atoms']:
                rule_atoms.add(atom)
    
    # Check if all products that reference rules reference existing rule atoms
    for product in product_specs['products']:
        if 'constraints' in product['spec']:
            for constraint in product['spec']['constraints']:
                if constraint not in rule_atoms:
                    print(f"Product {product['instance']} references non-rule atom as constraint: {constraint}")
        if 'failure_modes' in product['spec']:
            for failure_mode in product['spec']['failure_modes']:
                if failure_mode['id'] not in rule_atoms:
                    print(f"Product {product['instance']} references non-rule atom as failure mode: {failure_mode['id']}")
    
    # Check 6: MCP configurations match the tools enabled in Mode specs
    print("\n=== Check 6: MCP configurations vs Mode tools ===")
    # Collect all MCP tool names
    mcp_tools = set()
    for product in product_specs['products']:
        if product['category'] == 'PC5: MCP CONFIGURATIONS (Tool Access Patterns)':
            if 'tools' in product['spec']:
                for tool in product['spec']['tools']:
                    mcp_tools.add(tool)
    
    # Check Mode tools against MCP tools
    for product in product_specs['products']:
        if product['category'] == 'PC1: MODES (Agent Operational Personas)':
            if 'tools' in product['spec']:
                for tool in product['spec']['tools']:
                    if tool.startswith('mcp--') and tool not in mcp_tools:
                        print(f"Mode {product['instance']} references undefined MCP tool: {tool}")
    
    # Check 7: Techniques cover the failure modes documented in Rules
    print("\n=== Check 7: Techniques covering failure modes ===")
    # Note: Need to analyze technique content vs rule failure modes (manual check)
    
    # Check 8: No orphan atoms (extracted but never consumed by any product)
    print("\n=== Check 8: Orphan atoms ===")
    orphan_atoms = all_atoms - product_atoms
    if orphan_atoms:
        print(f"Orphan atoms (not consumed by any product): {sorted(list(orphan_atoms))}")
    else:
        print("No orphan atoms")
    
    # Check for duplicate atoms in domain grouping
    print("\n=== Check: Duplicate atoms in domain grouping ===")
    all_domain_atoms = []
    for domain in domain_grouping:
        for atom in domain_grouping[domain]['knowledge_atoms']:
            all_domain_atoms.append(atom)
    
    duplicates = []
    seen = set()
    for atom in all_domain_atoms:
        if atom in seen:
            duplicates.append(atom)
        else:
            seen.add(atom)
    
    if duplicates:
        print(f"Duplicate atoms in domain grouping: {sorted(list(set(duplicates)))}")
    else:
        print("No duplicate atoms in domain grouping")
    
    # Check for atoms in domain/phase/product that don't exist in registry
    print("\n=== Check: Atoms in domain/phase/product not in registry ===")
    invalid_domain = domain_atoms - all_atoms
    invalid_phase = phase_atoms - all_atoms
    invalid_product = product_atoms - all_atoms
    
    if invalid_domain:
        print(f"Invalid atoms in domain grouping: {sorted(list(invalid_domain))}")
    if invalid_phase:
        print(f"Invalid atoms in phase mapping: {sorted(list(invalid_phase))}")
    if invalid_product:
        print(f"Invalid atoms in product specs: {sorted(list(invalid_product))}")

if __name__ == "__main__":
    validate_knowledge_atoms()

def validate_knowledge_atoms():
    # Load all JSON files
    with open('knowledge_atom_registry.json', 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    with open('domain_knowledge_grouping.json', 'r', encoding='utf-8') as f:
        domain_grouping = json.load(f)
    
    with open('sdlc_phase_knowledge_mapping.json', 'r', encoding='utf-8') as f:
        phase_mapping = json.load(f)
    
    with open('product_specs.json', 'r', encoding='utf-8') as f:
        product_specs = json.load(f)
    
    # Collect all knowledge atoms from registry
    all_atoms = set()
    for atom_type in registry:
        for atom in registry[atom_type]:
            all_atoms.add(atom['ID'])
    
    print(f"Total atoms in registry: {len(all_atoms)}")
    
    # Collect atoms from domain grouping
    domain_atoms = set()
    for domain in domain_grouping:
        for atom in domain_grouping[domain]['knowledge_atoms']:
            domain_atoms.add(atom)
    
    print(f"Total atoms in domain grouping: {len(domain_atoms)}")
    
    # Collect atoms from phase mapping
    phase_atoms = set()
    for phase in phase_mapping['PHASES']:
        for atom in phase['KNOWLEDGE_ATOMS']:
            phase_atoms.add(atom)
    
    print(f"Total atoms in phase mapping: {len(phase_atoms)}")
    
    # Collect atoms from product specs
    product_atoms = set()
    for product in product_specs['products']:
        for atom in product['knowledge_atoms']:
            product_atoms.add(atom)
    
    print(f"Total atoms in product specs: {len(product_atoms)}")
    
    # Check 1: Every atom referenced by at least one domain, phase, and product
    print("\n=== Check 1: Atoms referenced by domain, phase, and product ===")
    missing_domain = all_atoms - domain_atoms
    missing_phase = all_atoms - phase_atoms
    missing_product = all_atoms - product_atoms
    
    if missing_domain:
        print(f"Atoms missing from domains: {sorted(list(missing_domain))}")
    else:
        print("All atoms referenced by at least one domain")
    
    if missing_phase:
        print(f"Atoms missing from phases: {sorted(list(missing_phase))}")
    else:
        print("All atoms referenced by at least one phase")
    
    if missing_product:
        print(f"Atoms missing from products: {sorted(list(missing_product))}")
    else:
        print("All atoms referenced by at least one product")
    
    # Check 2: Skills referenced by Modes exist as Skill specs
    print("\n=== Check 2: Skills referenced by Modes ===")
    # Note: Mode specs don't explicitly reference skills in the provided files
    
    # Check 3: Skills referenced by Workflows exist as Skill specs
    print("\n=== Check 3: Skills referenced by Workflows ===")
    # Note: Workflow specs don't explicitly reference skills in the provided files
    
    # Check 4: Context strategies referenced by Modes exist as Context Strategy specs
    print("\n=== Check 4: Context strategies referenced by Modes ===")
    # Note: Mode specs don't explicitly reference context strategies in the provided files
    
    # Check 5: Rules are consistently applied across products that reference them
    print("\n=== Check 5: Consistent rule application ===")
    # Collect all rule atoms
    rule_atoms = set()
    for product in product_specs['products']:
        if product['category'] == 'PC6: RULES (Constraints & Guardrails)':
            for atom in product['knowledge_atoms']:
                rule_atoms.add(atom)
    
    # Check if all products that reference rules reference existing rule atoms
    for product in product_specs['products']:
        if 'constraints' in product['spec']:
            for constraint in product['spec']['constraints']:
                if constraint not in rule_atoms:
                    print(f"Product {product['instance']} references non-rule atom as constraint: {constraint}")
        if 'failure_modes' in product['spec']:
            for failure_mode in product['spec']['failure_modes']:
                if failure_mode['id'] not in rule_atoms:
                    print(f"Product {product['instance']} references non-rule atom as failure mode: {failure_mode['id']}")
    
    # Check 6: MCP configurations match the tools enabled in Mode specs
    print("\n=== Check 6: MCP configurations vs Mode tools ===")
    # Collect all MCP tool names
    mcp_tools = set()
    for product in product_specs['products']:
        if product['category'] == 'PC5: MCP CONFIGURATIONS (Tool Access Patterns)':
            if 'tools' in product['spec']:
                for tool in product['spec']['tools']:
                    mcp_tools.add(tool)
    
    # Check Mode tools against MCP tools
    for product in product_specs['products']:
        if product['category'] == 'PC1: MODES (Agent Operational Personas)':
            if 'tools' in product['spec']:
                for tool in product['spec']['tools']:
                    if tool.startswith('mcp--') and tool not in mcp_tools:
                        print(f"Mode {product['instance']} references undefined MCP tool: {tool}")
    
    # Check 7: Techniques cover the failure modes documented in Rules
    print("\n=== Check 7: Techniques covering failure modes ===")
    # Note: Need to analyze technique content vs rule failure modes (manual check)
    
    # Check 8: No orphan atoms (extracted but never consumed by any product)
    print("\n=== Check 8: Orphan atoms ===")
    orphan_atoms = all_atoms - product_atoms
    if orphan_atoms:
        print(f"Orphan atoms (not consumed by any product): {sorted(list(orphan_atoms))}")
    else:
        print("No orphan atoms")
    
    # Check for duplicate atoms in domain grouping
    print("\n=== Check: Duplicate atoms in domain grouping ===")
    all_domain_atoms = []
    for domain in domain_grouping:
        for atom in domain_grouping[domain]['knowledge_atoms']:
            all_domain_atoms.append(atom)
    
    duplicates = []
    seen = set()
    for atom in all_domain_atoms:
        if atom in seen:
            duplicates.append(atom)
        else:
            seen.add(atom)
    
    if duplicates:
        print(f"Duplicate atoms in domain grouping: {sorted(list(set(duplicates)))}")
    else:
        print("No duplicate atoms in domain grouping")
    
    # Check for atoms in domain/phase/product that don't exist in registry
    print("\n=== Check: Atoms in domain/phase/product not in registry ===")
    invalid_domain = domain_atoms - all_atoms
    invalid_phase = phase_atoms - all_atoms
    invalid_product = product_atoms - all_atoms
    
    if invalid_domain:
        print(f"Invalid atoms in domain grouping: {sorted(list(invalid_domain))}")
    if invalid_phase:
        print(f"Invalid atoms in phase mapping: {sorted(list(invalid_phase))}")
    if invalid_product:
        print(f"Invalid atoms in product specs: {sorted(list(invalid_product))}")

if __name__ == "__main__":
    validate_knowledge_atoms()
