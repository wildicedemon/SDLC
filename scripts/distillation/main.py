import os
import sys
import yaml  # type: ignore

# Add project root to sys.path if needed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from scripts.distillation.llm_client import LLMClient  # noqa: E402
from scripts.distillation.parser import Parser  # noqa: E402


def read_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def write_yaml(filepath: str, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)


def extract_yaml_from_response(text: str) -> str:
    """Extract YAML content from LLM response if wrapped in markdown code blocks."""
    import re

    match = re.search(r"```yaml\n(.*?)\n```", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1)

    # Also check if wrapped in json or just raw
    match = re.search(r"```json\n(.*?)\n```", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1)

    match = re.search(r"```\n(.*?)\n```", text, re.DOTALL)
    if match:
        return match.group(1)

    return text


def get_mock_response(prong: int) -> str:
    if prong == 1:
        return """
ID: KA-001
TYPE: TOOL
CONTENT: Tree-sitter is a parser generator tool and an incremental parsing library.
EVIDENCE_STRENGTH: STRONG
SOURCE: dummy_research.md
DOMAINS: D5
SDLC_PHASES: P1, P3, P5
PRODUCTS: PC2
"""
    elif prong == 2:
        return """
```yaml
domains:
  - domain: D5
    knowledge_atoms: ["KA-001"]
    key_techniques: []
    key_constraints: []
    key_tools:
      - atom_id: "KA-001"
        tool: "Tree-sitter"
        evaluated_capability: "incremental parsing"
    combination_recipes: []
    failure_modes: []
    cross_domain_links: []
    gaps: []
phases:
  - phase: P1
    knowledge_atoms: ["KA-001"]
    techniques_to_use: []
    constraints_in_effect: []
    tools_needed: ["KA-001"]
    failure_modes_to_watch_for: []
    transitions: []
```
"""
    elif prong == 4:
        return """
```yaml
products:
  - product: PC2
    instance: "Skill: Code Traversal"
    knowledge_atoms_consumed: ["KA-001"]
    draft_spec:
      skill: "code_traversal"
      purpose: "Navigate and understand code structure"
      technique_stack:
        primary: "Tree-sitter AST parsing (KA-001)"
    confidence: HIGH
    gaps: []
```
"""
    return ""


def main(research_file: str):
    print(f"Reading research from {research_file}...")
    system_prompt = read_file("scripts/prompts/distillation_prompt.txt")
    research_content = read_file(research_file)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY not set. Running in DRY RUN mode with mock data.")
        client = None
    else:
        client = LLMClient()

    # --- PRONG 1 ---
    print("Executing Prong 1: Refine (Bottom-Up)...")
    p1_user_prompt = f"Extract Knowledge Atoms from the following research according to PRONG 1 instructions. Return only the extracted Knowledge Atoms.\n\nResearch:\n{research_content}"

    p1_response = (
        client.generate(system_prompt, p1_user_prompt)
        if client
        else get_mock_response(1)
    )
    atoms = Parser.parse_knowledge_atoms(p1_response)

    if not atoms:
        print("Warning: No atoms extracted in Prong 1. Saving raw response.")
        with open("output/distilled/prong1_raw.md", "w") as f:
            f.write(p1_response)
        return

    atoms_dict = [atom.model_dump(mode="json") for atom in atoms]
    write_yaml("output/distilled/atoms.yaml", atoms_dict)
    print(f"-> Extracted {len(atoms)} atoms and saved to output/distilled/atoms.yaml")

    atoms_yaml_str = yaml.dump(atoms_dict, default_flow_style=False)

    # --- PRONG 2 & 3 ---
    print("Executing Prong 2 & 3: Domain & Phase Split...")
    p23_user_prompt = (
        f"Given the following Knowledge Atoms:\n\n{atoms_yaml_str}\n\n"
        "Execute PRONG 2 (Domain Split) and PRONG 3 (SDLC Phase Split).\n"
        "IMPORTANT: You MUST format your entire response as a single valid YAML document with two top-level keys: 'domains' and 'phases'. "
        "Do NOT use the text-based templates from the prompt; instead, adapt them to a proper YAML structure."
    )

    p23_response = (
        client.generate(system_prompt, p23_user_prompt)
        if client
        else get_mock_response(2)
    )
    p23_yaml_str = extract_yaml_from_response(p23_response)

    try:
        p23_data = yaml.safe_load(p23_yaml_str)
        if isinstance(p23_data, dict):
            if "domains" in p23_data:
                write_yaml("output/distilled/domains.yaml", p23_data["domains"])
                print("-> Saved domains to output/distilled/domains.yaml")
            if "phases" in p23_data:
                write_yaml("output/distilled/phases.yaml", p23_data["phases"])
                print("-> Saved phases to output/distilled/phases.yaml")
        else:
            print(
                "Warning: Prongs 2 & 3 output is not a dictionary. Saving as raw YAML."
            )
            write_yaml("output/distilled/domains_phases_raw.yaml", p23_data)
    except yaml.YAMLError as e:
        print(f"Error parsing Prongs 2 & 3 YAML: {e}")
        with open("output/distilled/prongs23_raw.txt", "w") as f:
            f.write(p23_response)

    # --- PRONG 4 ---
    print("Executing Prong 4: Product Mapping...")
    p4_user_prompt = (
        f"Given the following Knowledge Atoms:\n\n{atoms_yaml_str}\n\n"
        "Execute PRONG 4 (Product Mapping). Assemble the appropriate specs (e.g., Skills, Modes, Workflows).\n"
        "IMPORTANT: You MUST format your entire response as a single valid YAML document containing a top-level key 'products', which is a list of the assembled product specs."
    )

    p4_response = (
        client.generate(system_prompt, p4_user_prompt)
        if client
        else get_mock_response(4)
    )
    p4_yaml_str = extract_yaml_from_response(p4_response)

    try:
        p4_data = yaml.safe_load(p4_yaml_str)
        if isinstance(p4_data, dict) and "products" in p4_data:
            write_yaml("output/distilled/products.yaml", p4_data["products"])
            print("-> Saved products to output/distilled/products.yaml")
        else:
            print("Warning: Prong 4 output structure unexpected. Saving as raw YAML.")
            write_yaml("output/distilled/products_raw.yaml", p4_data)
    except yaml.YAMLError as e:
        print(f"Error parsing Prong 4 YAML: {e}")
        with open("output/distilled/prong4_raw.txt", "w") as f:
            f.write(p4_response)

    # --- PRONG 5: Validation ---
    print("Executing Validation Engine...")
    from scripts.distillation.validator import Validator

    # Load the written files to validate
    try:
        with open("output/distilled/atoms.yaml", "r") as f:
            v_atoms = yaml.safe_load(f) or []
        with open("output/distilled/domains.yaml", "r") as f:
            v_domains = yaml.safe_load(f) or []
        with open("output/distilled/phases.yaml", "r") as f:
            v_phases = yaml.safe_load(f) or []
        with open("output/distilled/products.yaml", "r") as f:
            v_products = yaml.safe_load(f) or []

        validator = Validator(v_atoms, v_domains, v_phases, v_products)
        gap_report = validator.generate_gap_report()

        with open("output/distilled/gap_report.txt", "w", encoding="utf-8") as f:
            f.write(gap_report)
        print("-> Saved Gap Report to output/distilled/gap_report.txt")

    except Exception as e:
        print(f"Validation failed: {e}")

    print("Pipeline execution completed.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        research_file = sys.argv[1]
    else:
        research_file = "dummy_research.md"

    main(research_file)
