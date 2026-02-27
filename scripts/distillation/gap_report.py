from __future__ import annotations

from collections import defaultdict

from .constants import DOMAIN_NAMES, PHASE_NAMES, PRODUCT_NAMES, EvidenceStrength
from .models import DomainSpec, KnowledgeAtom, PhaseSpec, ProductSpec


def _evidence_counts(atom_ids: list[str], atoms_by_id: dict[str, KnowledgeAtom]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for aid in atom_ids:
        a = atoms_by_id.get(aid)
        if a:
            counts[a.evidence_strength.value] += 1
    return dict(counts)


def _backing_label(atom_ids: list[str], atoms_by_id: dict[str, KnowledgeAtom]) -> str:
    counts = _evidence_counts(atom_ids, atoms_by_id)
    strong = counts.get("STRONG", 0)
    total = sum(counts.values())
    if strong >= 5:
        return "STRONG"
    if total >= 2:
        return "ADEQUATE"
    return "WEAK"


def generate_gap_report(
    atoms: list[KnowledgeAtom],
    domain_specs: list[DomainSpec],
    phase_specs: list[PhaseSpec],
    product_specs: list[ProductSpec],
) -> str:
    atoms_by_id: dict[str, KnowledgeAtom] = {a.id: a for a in atoms}
    all_atom_ids = set(atoms_by_id.keys())

    strong_items: list[str] = []
    adequate_items: list[str] = []
    weak_items: list[str] = []

    for ds in domain_specs:
        label = _backing_label(ds.atom_ids, atoms_by_id)
        counts = _evidence_counts(ds.atom_ids, atoms_by_id)
        entry = f"Domain {ds.domain.value} ({ds.name}): {len(ds.atom_ids)} atoms, evidence={counts}"
        if ds.gaps:
            entry += f", gaps: {'; '.join(ds.gaps)}"
        if label == "STRONG":
            strong_items.append(entry)
        elif label == "ADEQUATE":
            adequate_items.append(entry)
        else:
            weak_items.append(entry)

    for ps in phase_specs:
        label = _backing_label(ps.atom_ids, atoms_by_id)
        counts = _evidence_counts(ps.atom_ids, atoms_by_id)
        entry = f"Phase {ps.phase.value} ({ps.name}): {len(ps.atom_ids)} atoms, evidence={counts}"
        if label == "STRONG":
            strong_items.append(entry)
        elif label == "ADEQUATE":
            adequate_items.append(entry)
        else:
            weak_items.append(entry)

    for prs in product_specs:
        label = _backing_label(prs.atom_ids, atoms_by_id)
        entry = f"Product {prs.category.value} '{prs.instance_name}': {len(prs.atom_ids)} atoms, confidence={prs.confidence}"
        if prs.gaps:
            entry += f", gaps: {len(prs.gaps)} fields"
        if label == "STRONG":
            strong_items.append(entry)
        elif label == "ADEQUATE":
            adequate_items.append(entry)
        else:
            weak_items.append(entry)

    domain_referenced: set[str] = set()
    for ds in domain_specs:
        domain_referenced.update(ds.atom_ids)
    phase_referenced: set[str] = set()
    for ps in phase_specs:
        phase_referenced.update(ps.atom_ids)
    product_referenced: set[str] = set()
    for prs in product_specs:
        product_referenced.update(prs.atom_ids)
    all_referenced = domain_referenced | phase_referenced | product_referenced
    orphans = sorted(all_atom_ids - all_referenced)

    contradictions: list[str] = []
    by_type: dict[str, list[KnowledgeAtom]] = defaultdict(list)
    for a in atoms:
        by_type[a.type.value].append(a)
    for type_key, group in by_type.items():
        if type_key in ("TRADEOFF", "ANTI_PATTERN") and len(group) >= 2:
            contradictions.append(
                f"{type_key}: {len(group)} atoms — review for potential contradictions"
            )

    lines: list[str] = []
    lines.append("# Gap Report")
    lines.append("")

    lines.append("## STRONG BACKING (>=5 atoms with STRONG evidence)")
    lines.append("")
    if strong_items:
        for item in strong_items:
            lines.append(f"- {item}")
    else:
        lines.append("- *(none)*")
    lines.append("")

    lines.append("## ADEQUATE BACKING (2-4 atoms, mixed evidence)")
    lines.append("")
    if adequate_items:
        for item in adequate_items:
            lines.append(f"- {item}")
    else:
        lines.append("- *(none)*")
    lines.append("")

    lines.append("## WEAK/NO BACKING (<2 atoms or WEAK only)")
    lines.append("")
    if weak_items:
        for item in weak_items:
            lines.append(f"- {item}")
    else:
        lines.append("- *(none)*")
    lines.append("")

    lines.append("## ORPHAN RESEARCH (atoms with no product home)")
    lines.append("")
    if orphans:
        for oid in orphans:
            a = atoms_by_id.get(oid)
            summary = a.content[:100] if a else "unknown"
            lines.append(f"- `{oid}`: {summary}")
    else:
        lines.append("- *(none)*")
    lines.append("")

    lines.append("## CONTRADICTIONS (atoms that may disagree)")
    lines.append("")
    if contradictions:
        for c in contradictions:
            lines.append(f"- {c}")
    else:
        lines.append("- *(none)*")
    lines.append("")

    return "\n".join(lines)
