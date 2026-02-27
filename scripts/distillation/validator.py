from typing import List, Dict, Any, Set, Tuple


class Validator:
    def __init__(
        self,
        atoms: List[Dict[str, Any]],
        domains: List[Dict[str, Any]],
        phases: List[Dict[str, Any]],
        products: List[Dict[str, Any]],
    ):
        self.atoms = atoms
        self.domains = domains
        self.phases = phases
        self.products = products

        self.atom_ids: Set[str] = {
            str(atom.get("id")) for atom in self.atoms if atom.get("id")
        }

    def _get_referenced_atoms(self) -> Tuple[Set[str], Set[str], Set[str]]:
        domain_refs = set()
        for d in self.domains:
            domain_refs.update(d.get("knowledge_atoms", []))
            for kt in d.get("key_techniques", []):
                domain_refs.add(kt.get("atom_id"))
            for kc in d.get("key_constraints", []):
                domain_refs.add(kc.get("atom_id"))
            for kt in d.get("key_tools", []):
                domain_refs.add(kt.get("atom_id"))
            for cr in d.get("combination_recipes", []):
                domain_refs.add(cr.get("atom_id"))
            for fm in d.get("failure_modes", []):
                domain_refs.add(fm.get("atom_id"))
            for cdl in d.get("cross_domain_links", []):
                domain_refs.add(cdl.get("atom_id"))

        phase_refs = set()
        for p in self.phases:
            phase_refs.update(p.get("knowledge_atoms", []))
            for ttu in p.get("techniques_to_use", []):
                phase_refs.update(ttu.get("atom_ids", []))
            phase_refs.update(p.get("constraints_in_effect", []))
            phase_refs.update(p.get("tools_needed", []))
            phase_refs.update(p.get("failure_modes_to_watch_for", []))

        product_refs = set()
        for p in self.products:
            product_refs.update(p.get("knowledge_atoms_consumed", []))

        return domain_refs, phase_refs, product_refs

    def check_orphaned_atoms(self) -> List[Dict[str, Any]]:
        """Find atoms extracted but not consumed by any product."""
        _, _, product_refs = self._get_referenced_atoms()
        orphaned = []
        for atom in self.atoms:
            atom_id = atom.get("id")
            if atom_id and atom_id not in product_refs:
                orphaned.append(atom)
        return orphaned

    def check_missing_references(self) -> List[str]:
        """Find atoms referenced in products/domains/phases but don't exist."""
        domain_refs, phase_refs, product_refs = self._get_referenced_atoms()
        all_refs = domain_refs | phase_refs | product_refs

        # Remove None if it exists
        all_refs_clean = {str(ref) for ref in all_refs if ref is not None}

        missing = [ref for ref in all_refs_clean if ref not in self.atom_ids]
        return missing

    def check_unhandled_failure_modes(self) -> List[str]:
        """Find FAILURE_MODE atoms that are not consumed by any product (or specifically handled)."""
        failure_modes = {
            str(atom.get("id"))
            for atom in self.atoms
            if atom.get("type") == "FAILURE_MODE" and atom.get("id")
        }
        _, _, product_refs = self._get_referenced_atoms()

        unhandled = [fm for fm in failure_modes if fm not in product_refs]
        return unhandled

    def generate_gap_report(self) -> str:
        """Generate the final Gap Report based on evidence strength and missing links."""
        domain_refs, phase_refs, product_refs = self._get_referenced_atoms()

        strong_atoms = [a for a in self.atoms if a.get("evidence_strength") == "STRONG"]
        adequate_atoms = [
            a for a in self.atoms if a.get("evidence_strength") == "MODERATE"
        ]
        weak_atoms = [a for a in self.atoms if a.get("evidence_strength") == "WEAK"]

        orphaned = self.check_orphaned_atoms()
        missing_refs = self.check_missing_references()
        unhandled_fms = self.check_unhandled_failure_modes()

        report_lines = []
        report_lines.append("STRONG BACKING (≥5 atoms with STRONG evidence):")
        report_lines.append(f"- Total Strong Atoms: {len(strong_atoms)}")

        report_lines.append("\nADEQUATE BACKING (2-4 atoms, mixed evidence):")
        report_lines.append(f"- Total Adequate Atoms: {len(adequate_atoms)}")

        report_lines.append("\nWEAK/NO BACKING (<2 atoms or WEAK only):")
        report_lines.append(f"- Total Weak Atoms: {len(weak_atoms)}")

        report_lines.append("\nORPHAN RESEARCH (atoms with no product home):")
        for atom in orphaned:
            report_lines.append(f"- {atom.get('id')}: {atom.get('content')}")
        if not orphaned:
            report_lines.append("- None")

        report_lines.append("\nMISSING CROSS-REFERENCES (referenced but do not exist):")
        for ref in missing_refs:
            report_lines.append(f"- {ref}")
        if not missing_refs:
            report_lines.append("- None")

        report_lines.append(
            "\nUNHANDLED FAILURE MODES (FAILURE_MODE atoms not consumed by any product):"
        )
        for fm in unhandled_fms:
            report_lines.append(f"- {fm}")
        if not unhandled_fms:
            report_lines.append("- None")

        return "\n".join(report_lines)
