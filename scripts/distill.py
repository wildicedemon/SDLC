#!/usr/bin/env python3
"""CLI entrypoint for the SDLC Knowledge Atom Extraction pipeline."""

import argparse
import sys
from pathlib import Path

# Import from scripts.distillation (FIXED: was 'from distillation.X')
from scripts.distillation.scanner import scan_corpus
from scripts.distillation.parser import parse_file
from scripts.distillation.classifier import classify
from scripts.distillation.dedup import deduplicate
from scripts.distillation.ranker import rank
from scripts.distillation.tagger import tag
from scripts.distillation.prong2_domains import generate_domain_specs
from scripts.distillation.prong3_phases import generate_phase_specs
from scripts.distillation.prong4_products import generate_product_specs
from scripts.distillation.validator import validate
from scripts.distillation.gap_report import generate_gap_report


def main():
    """Main entrypoint for the CLI."""
    parser = argparse.ArgumentParser(
        description="SDLC Knowledge Atom Extraction Pipeline"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scan and parse only, report counts"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Log each step"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("distillation/"),
        help="Output directory (default: distillation/)"
    )
    
    args = parser.parse_args()
    
    # Pipeline sequence:
    # scan → parse → classify → dedup → rank → tag → write registry → prong2 → prong3 → prong4 → validate → gap report
    
    if args.verbose:
        print("Starting SDLC Knowledge Atom Extraction Pipeline...")
    
    # Step 1: Scan corpus
    if args.verbose:
        print("Scanning corpus...")
    corpus_files = scan_corpus(Path("."))
    
    if args.dry_run:
        print(f"Found {sum(len(v) for v in corpus_files.values())} files")
        return 0
    
    # TODO: Implement full pipeline
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
