#!/usr/bin/env python3
"""CLI entrypoint for the multi-prong research distillation pipeline."""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from distillation.scanner import scan_corpus
from distillation.parser import parse_file
from distillation.classifier import classify
from distillation.dedup import deduplicate
from distillation.ranker import rank
from distillation.tagger import tag
from distillation.prong2_domains import generate_domain_specs
from distillation.prong3_phases import generate_phase_specs
from distillation.prong4_products import generate_product_specs
from distillation.validator import validate
from distillation.gap_report import generate_gap_report


def _log(msg: str, verbose: bool) -> None:
    if verbose:
        print(f"  [distill] {msg}")


def _create_output_dirs(output_dir: Path) -> None:
    for subdir in (
        "registry",
        "domains",
        "phases",
        "products/modes",
        "products/skills",
        "products/workflows",
        "products/prompts",
        "products/mcp_configurations",
        "products/rules",
        "products/context_strategies",
        "products/task_decomposition_patterns",
        "products/workspace_management",
        "products/techniques",
        "reports",
    ):
        (output_dir / subdir).mkdir(parents=True, exist_ok=True)


def _serialize_atom(atom) -> dict:
    return {
        "id": atom.id,
        "type": atom.type.value,
        "content": atom.content,
        "evidence_strength": atom.evidence_strength.value,
        "sources": atom.sources,
        "domains": atom.domains,
        "sdlc_phases": atom.sdlc_phases,
        "products": atom.products,
        "content_hash": atom.content_hash,
    }


def run_pipeline(
    corpus_root: Path,
    output_dir: Path,
    dry_run: bool = False,
    verbose: bool = False,
) -> int:
    _log(f"Corpus root: {corpus_root}", verbose)
    _log(f"Output dir:  {output_dir}", verbose)

    _log("Step 1/9: Scanning corpus...", verbose)
    corpus = scan_corpus(corpus_root)
    total_files = sum(len(v) for v in corpus.values())
    _log(f"  Found {total_files} files across {len(corpus)} categories", verbose)
    for cat, paths in corpus.items():
        _log(f"    {cat}: {len(paths)}", verbose)

    _log("Step 2/9: Parsing files...", verbose)
    all_raw = []
    all_paths = []
    for paths in corpus.values():
        all_paths.extend(paths)
    for p in all_paths:
        raw_atoms = parse_file(p)
        all_raw.extend(raw_atoms)
    _log(f"  Extracted {len(all_raw)} raw atoms", verbose)

    _log("Step 3/9: Classifying atoms...", verbose)
    classified = []
    for raw in all_raw:
        atom = classify(raw)
        if atom is not None:
            classified.append(atom)
    _log(f"  Classified {len(classified)} atoms (discarded {len(all_raw) - len(classified)})", verbose)

    _log("Step 4/9: Deduplicating...", verbose)
    deduped = deduplicate(classified)
    _log(f"  {len(deduped)} unique atoms (removed {len(classified) - len(deduped)} duplicates)", verbose)

    _log("Step 5/9: Ranking and assigning IDs...", verbose)
    ranked = rank(deduped)
    _log(f"  Ranked {len(ranked)} atoms", verbose)

    _log("Step 6/9: Tagging (domains, phases, products)...", verbose)
    tagged = tag(ranked)
    _log(f"  Tagged {len(tagged)} atoms", verbose)

    if dry_run:
        print(f"\n=== Dry Run Summary ===")
        print(f"Files scanned:    {total_files}")
        print(f"Raw atoms:        {len(all_raw)}")
        print(f"Classified:       {len(classified)}")
        print(f"After dedup:      {len(deduped)}")
        print(f"Final atoms:      {len(tagged)}")
        from collections import Counter
        type_counts = Counter(a.type.value for a in tagged)
        print(f"\nBy type:")
        for t, c in sorted(type_counts.items()):
            print(f"  {t}: {c}")
        evidence_counts = Counter(a.evidence_strength.value for a in tagged)
        print(f"\nBy evidence strength:")
        for e, c in sorted(evidence_counts.items()):
            print(f"  {e}: {c}")
        return 0

    _create_output_dirs(output_dir)

    _log("Step 7/9: Writing registry JSON...", verbose)
    registry = [_serialize_atom(a) for a in tagged]
    registry_path = output_dir / "registry" / "knowledge_atoms.json"
    registry_path.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    _log(f"  Wrote {len(registry)} atoms to {registry_path}", verbose)

    _log("Step 7a/9: Generating Prong 2 (domain specs)...", verbose)
    domain_specs = generate_domain_specs(tagged, output_dir)
    _log(f"  Generated {len(domain_specs)} domain specs", verbose)

    _log("Step 7b/9: Generating Prong 3 (phase specs)...", verbose)
    phase_specs = generate_phase_specs(tagged, output_dir)
    _log(f"  Generated {len(phase_specs)} phase specs", verbose)

    _log("Step 7c/9: Generating Prong 4 (product specs)...", verbose)
    product_specs = generate_product_specs(tagged, output_dir)
    _log(f"  Generated {len(product_specs)} product specs", verbose)

    _log("Step 8/9: Validating cross-references...", verbose)
    validation = validate(tagged, domain_specs, phase_specs, product_specs)
    val_path = output_dir / "reports" / "validation_report.md"
    val_lines = [
        "# Validation Report",
        "",
        validation.summary,
        "",
    ]
    if validation.orphan_atoms:
        val_lines.append("## Orphan Atoms")
        val_lines.append("")
        for oid in validation.orphan_atoms:
            val_lines.append(f"- `{oid}`")
        val_lines.append("")
    if validation.cross_ref_issues:
        val_lines.append("## Cross-Reference Issues")
        val_lines.append("")
        for issue in validation.cross_ref_issues:
            val_lines.append(f"- {issue}")
        val_lines.append("")
    val_path.write_text("\n".join(val_lines), encoding="utf-8")
    _log(f"  Validation: {validation.summary}", verbose)

    _log("Step 9/9: Generating gap report...", verbose)
    gap_text = generate_gap_report(tagged, domain_specs, phase_specs, product_specs)
    gap_path = output_dir / "reports" / "gap_report.md"
    gap_path.write_text(gap_text, encoding="utf-8")
    _log(f"  Gap report written to {gap_path}", verbose)

    print(f"\nPipeline complete.")
    print(f"  Atoms:    {len(tagged)}")
    print(f"  Domains:  {len(domain_specs)}")
    print(f"  Phases:   {len(phase_specs)}")
    print(f"  Products: {len(product_specs)}")
    print(f"  Output:   {output_dir}")
    if validation.orphan_atoms:
        print(f"  WARNING: {len(validation.orphan_atoms)} orphan atom(s)")

    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Multi-prong research distillation pipeline",
    )
    parser.add_argument(
        "--corpus-root",
        type=Path,
        default=SCRIPT_DIR.parent,
        help="Root directory of the research corpus (default: project root)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=SCRIPT_DIR.parent / "distillation",
        help="Output directory (default: distillation/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scan and parse only, report counts without writing output",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Log each pipeline step",
    )
    args = parser.parse_args()
    sys.exit(run_pipeline(args.corpus_root, args.output_dir, args.dry_run, args.verbose))


if __name__ == "__main__":
    main()
