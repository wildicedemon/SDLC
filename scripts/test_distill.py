#!/usr/bin/env python3
"""Verification script for the distillation pipeline."""

from __future__ import annotations

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        msg = f"  FAIL  {name}"
        if detail:
            msg += f" -- {detail}"
        print(msg)


# ── Scanner tests ──────────────────────────────────────────────────

def test_scanner() -> None:
    print("\n=== Scanner Tests ===")
    from distillation.scanner import scan_corpus

    result = scan_corpus(PROJECT_ROOT)

    check("returns dict", isinstance(result, dict))

    expected_keys = {"perplexity", "overviews", "indices", "kimi_docs", "kimi_csv", "root_files"}
    check("has expected keys", set(result.keys()) == expected_keys, f"got {set(result.keys())}")

    check("perplexity > 0", len(result["perplexity"]) > 0, f"found {len(result['perplexity'])}")
    check("overviews > 0", len(result["overviews"]) > 0, f"found {len(result['overviews'])}")
    check("indices > 0", len(result["indices"]) > 0, f"found {len(result['indices'])}")
    check("kimi_docs > 0", len(result["kimi_docs"]) > 0, f"found {len(result['kimi_docs'])}")
    check("kimi_csv > 0", len(result["kimi_csv"]) > 0, f"found {len(result['kimi_csv'])}")
    check("root_files > 0", len(result["root_files"]) > 0, f"found {len(result['root_files'])}")

    check(
        "perplexity files match pattern",
        all("perplexityai_research_overview" in p.name for p in result["perplexity"]),
    )
    check(
        "overview files named overview.md",
        all(p.name == "overview.md" for p in result["overviews"]),
    )
    check(
        "indices under _indices/",
        all("_indices" in str(p) for p in result["indices"]),
    )
    check(
        "kimi_docs are .md files",
        all(p.suffix == ".md" for p in result["kimi_docs"]),
    )
    check(
        "kimi_csv are .csv files",
        all(p.suffix == ".csv" for p in result["kimi_csv"]),
    )
    check(
        "root_files are .md in project root",
        all(p.parent == PROJECT_ROOT and p.suffix == ".md" for p in result["root_files"]),
    )

    all_paths = []
    for paths in result.values():
        all_paths.extend(paths)
    check("all paths exist", all(p.exists() for p in all_paths))

    check("no duplicates within kimi_csv", len(result["kimi_csv"]) == len(set(result["kimi_csv"])))

    total = sum(len(v) for v in result.values())
    print(f"\n  Total files discovered: {total}")
    for key, paths in result.items():
        print(f"    {key}: {len(paths)}")


# ── Main ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    test_scanner()

    print(f"\n{'=' * 40}")
    print(f"Results: {PASS} passed, {FAIL} failed")
    if FAIL:
        sys.exit(1)
    print("All checks passed.")
