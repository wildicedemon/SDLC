from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from .constants import DOMAIN_NAMES, PRODUCT_NAMES, EvidenceStrength, ProductCategory
from .models import KnowledgeAtom, ProductSpec
from .yaml_templates import BUILDERS

PRODUCT_DIR_MAP: dict[str, str] = {
    "PC1": "modes",
    "PC2": "skills",
    "PC3": "workflows",
    "PC4": "prompts",
    "PC5": "mcp_configurations",
    "PC6": "rules",
    "PC7": "context_strategies",
    "PC8": "task_decomposition_patterns",
    "PC9": "workspace_management",
    "PC10": "techniques",
}


def _slugify(text: str) -> str:
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    return slug.strip("_")[:60]


def _compute_confidence(atoms: list[KnowledgeAtom]) -> str:
    strong = sum(1 for a in atoms if a.evidence_strength == EvidenceStrength.STRONG)
    total = len(atoms)
    if strong >= 3 and total >= 5:
        return "HIGH"
    if total >= 2:
        return "MEDIUM"
    return "LOW"


def _cluster_by_domain(atoms: list[KnowledgeAtom]) -> dict[str, list[KnowledgeAtom]]:
    clusters: dict[str, list[KnowledgeAtom]] = defaultdict(list)
    for atom in atoms:
        primary_domain = atom.domains[0] if atom.domains else "D1"
        clusters[primary_domain].append(atom)
    return dict(clusters)


def _instance_name(category: str, domain_key: str) -> str:
    cat_name = PRODUCT_NAMES.get(category, category)
    domain_name = DOMAIN_NAMES.get(domain_key, domain_key)
    return f"{_slugify(cat_name)}_{_slugify(domain_name)}"


def _write_yaml(spec: dict, path: Path) -> None:
    try:
        import yaml
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(spec, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    except ImportError:
        import json
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(spec, f, indent=2, ensure_ascii=False)


def generate_product_specs(
    atoms: list[KnowledgeAtom], output_dir: Path
) -> list[ProductSpec]:
    product_atoms: dict[str, list[KnowledgeAtom]] = defaultdict(list)
    for atom in atoms:
        for pc in atom.products:
            product_atoms[pc].append(atom)

    all_specs: list[ProductSpec] = []

    for pc_key in sorted(ProductCategory.__members__):
        pc_val = ProductCategory[pc_key].value
        builder = BUILDERS.get(pc_val)
        if not builder:
            continue

        cat_atoms = product_atoms.get(pc_val, [])
        if not cat_atoms:
            continue

        subdir = PRODUCT_DIR_MAP.get(pc_val, _slugify(PRODUCT_NAMES.get(pc_val, pc_val)))
        out_path = output_dir / "products" / subdir

        clusters = _cluster_by_domain(cat_atoms)

        for domain_key, cluster_atoms in clusters.items():
            name = _instance_name(pc_val, domain_key)
            yaml_spec, gaps = builder(name, cluster_atoms)
            confidence = _compute_confidence(cluster_atoms)

            spec = ProductSpec(
                category=ProductCategory[pc_key],
                instance_name=name,
                atom_ids=[a.id for a in cluster_atoms],
                yaml_spec=yaml_spec,
                confidence=confidence,
                gaps=gaps,
            )
            all_specs.append(spec)

            file_path = out_path / f"{name}.yaml"
            _write_yaml(yaml_spec, file_path)

    return all_specs
