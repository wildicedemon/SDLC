from __future__ import annotations

from dataclasses import dataclass, field

from .models import DomainSpec, KnowledgeAtom, PhaseSpec, ProductSpec


@dataclass
class ValidationReport:
    total_atoms: int = 0
    atoms_with_domain: int = 0
    atoms_with_phase: int = 0
    atoms_with_product: int = 0
    orphan_atoms: list[str] = field(default_factory=list)
    missing_skills_in_modes: list[str] = field(default_factory=list)
    missing_context_strategies_in_modes: list[str] = field(default_factory=list)
    missing_skills_in_workflows: list[str] = field(default_factory=list)
    cross_ref_issues: list[str] = field(default_factory=list)
    passed: bool = True

    @property
    def summary(self) -> str:
        lines = [
            f"Total atoms: {self.total_atoms}",
            f"Atoms with >=1 domain ref: {self.atoms_with_domain}",
            f"Atoms with >=1 phase ref: {self.atoms_with_phase}",
            f"Atoms with >=1 product ref: {self.atoms_with_product}",
            f"Orphan atoms: {len(self.orphan_atoms)}",
            f"Cross-ref issues: {len(self.cross_ref_issues)}",
        ]
        return "\n".join(lines)


def _collect_all_atom_ids_in_domains(domain_specs: list[DomainSpec]) -> set[str]:
    ids: set[str] = set()
    for spec in domain_specs:
        ids.update(spec.atom_ids)
    return ids


def _collect_all_atom_ids_in_phases(phase_specs: list[PhaseSpec]) -> set[str]:
    ids: set[str] = set()
    for spec in phase_specs:
        ids.update(spec.atom_ids)
    return ids


def _collect_all_atom_ids_in_products(product_specs: list[ProductSpec]) -> set[str]:
    ids: set[str] = set()
    for spec in product_specs:
        ids.update(spec.atom_ids)
    return ids


def validate(
    atoms: list[KnowledgeAtom],
    domain_specs: list[DomainSpec],
    phase_specs: list[PhaseSpec],
    product_specs: list[ProductSpec],
) -> ValidationReport:
    report = ValidationReport()
    report.total_atoms = len(atoms)

    all_atom_ids = {a.id for a in atoms}
    domain_referenced = _collect_all_atom_ids_in_domains(domain_specs)
    phase_referenced = _collect_all_atom_ids_in_phases(phase_specs)
    product_referenced = _collect_all_atom_ids_in_products(product_specs)

    report.atoms_with_domain = len(all_atom_ids & domain_referenced)
    report.atoms_with_phase = len(all_atom_ids & phase_referenced)
    report.atoms_with_product = len(all_atom_ids & product_referenced)

    all_referenced = domain_referenced | phase_referenced | product_referenced
    report.orphan_atoms = sorted(all_atom_ids - all_referenced)

    skill_instance_names = {
        s.instance_name for s in product_specs if s.category.value == "PC2"
    }
    mode_specs = [s for s in product_specs if s.category.value == "PC1"]
    for ms in mode_specs:
        skills_in_mode = ms.yaml_spec.get("skills_available", [])
        for sk in skills_in_mode:
            if isinstance(sk, dict):
                for sk_id in sk:
                    if sk_id.startswith("KA-"):
                        continue
                    if sk_id not in skill_instance_names:
                        report.missing_skills_in_modes.append(
                            f"Mode '{ms.instance_name}' references skill '{sk_id}' not found in PC2 specs"
                        )

    cs_in_mode = ms.yaml_spec.get("context_strategy", "") if mode_specs else ""
    context_strategy_names = {
        s.instance_name for s in product_specs if s.category.value == "PC7"
    }
    for ms in mode_specs:
        cs = ms.yaml_spec.get("context_strategy", "")
        if cs and cs != "# GAP: insufficient research data to fill this field" and cs not in context_strategy_names:
            report.missing_context_strategies_in_modes.append(
                f"Mode '{ms.instance_name}' references context strategy '{cs}' not found in PC7 specs"
            )

    workflow_specs = [s for s in product_specs if s.category.value == "PC3"]
    for ws in workflow_specs:
        phases = ws.yaml_spec.get("phases", [])
        for phase in phases:
            if isinstance(phase, dict):
                for sk_id in phase.get("skills", []):
                    if sk_id.startswith("KA-"):
                        continue
                    if sk_id not in skill_instance_names:
                        report.missing_skills_in_workflows.append(
                            f"Workflow '{ws.instance_name}' references skill '{sk_id}' not found in PC2 specs"
                        )

    report.cross_ref_issues = (
        report.missing_skills_in_modes
        + report.missing_context_strategies_in_modes
        + report.missing_skills_in_workflows
    )

    if report.orphan_atoms:
        report.passed = False

    return report
