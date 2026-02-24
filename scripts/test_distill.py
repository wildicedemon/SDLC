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


# ── Parser tests ───────────────────────────────────────────────────

SAMPLE_MARKDOWN = """\
# Research on Code Analysis

## Key Techniques

- **Tree-sitter AST parsing**: Incremental AST parsing supporting 40+ languages with error recovery, widely adopted as de facto standard for code intelligence tools.
- See also: Other parsing approaches
- **Sourcegraph symbol search**: Multi-repo symbol search with sub-second queries across million-line codebases for fast cross-repository navigation.

## Metrics and Benchmarks

| Technique | Precision | Improvement |
|-----------|-----------|-------------|
| AST-based search | 60-80% | Over text-based search |
| Interprocedural analysis | 40-60% | Over intraprocedural |

1. Parse target files with Tree-sitter to build AST representation of the source code structure.
2. Query symbol index for cross-file references using Sourcegraph or LSIF offline indexes.
3. If security review, construct full CPG via Joern unifying AST, CFG, and DFG for vulnerability detection.

## See also

- [Link to other resources](http://example.com)
- Related topics

## Methodology

Search queries used: "code analysis", "AST parsing"

## Patterns and Anti-Patterns

- **Unguarded reflection loops**: Infinite loops or hallucinated improvements that degrade system quality over time. Don't use reflection without kill-switches.
- Short item

## Confidence: LOW

- Only one bullet here
"""

SAMPLE_CSV_SIMPLE = """\
title,abstract
Tool X for Code Analysis,Tool X provides advanced static analysis with 95% accuracy on common vulnerability patterns in production codebases.
Short,Too brief
Another Research Paper Title,This paper presents a novel approach to automated code review achieving 45% reduction in review time.
"""

SAMPLE_CSV_NESTED = """\
total_results,papers
2,"[{'id': '1', 'title': 'Adaptive Routing for LLM Queries', 'abstract': 'We propose an adaptive routing mechanism that selects specialized models based on query complexity achieving 30% latency reduction.'}, {'id': '2', 'title': 'Short', 'abstract': 'No'}]"
"""


def test_parser_markdown() -> None:
    print("\n=== Parser Tests (Markdown) ===")
    from distillation.parser import parse_markdown, RawAtom

    atoms = parse_markdown(SAMPLE_MARKDOWN, "test/sample.md")
    check("returns list", isinstance(atoms, list))
    check("atoms are RawAtom", all(isinstance(a, RawAtom) for a in atoms))
    check("extracts atoms > 0", len(atoms) > 0, f"got {len(atoms)}")

    all_content = " ".join(a.content for a in atoms)
    check("Tree-sitter extracted", "Tree-sitter" in all_content)
    check("Sourcegraph extracted", "Sourcegraph" in all_content)

    check(
        "See also section discarded",
        not any("Link to other resources" in a.content for a in atoms),
    )
    check(
        "Methodology section discarded",
        not any("Search queries used" in a.content for a in atoms),
    )

    check(
        "See also bullet discarded",
        not any(a.content.startswith("See also") for a in atoms),
    )

    check(
        "low-confidence section discarded",
        not any("Only one bullet" in a.content for a in atoms),
    )

    check(
        "table rows extracted",
        any("60-80%" in a.content for a in atoms),
    )

    check(
        "numbered list items extracted",
        any("Parse target files" in a.content for a in atoms),
    )

    check("all atoms have source_path", all(a.source_path == "test/sample.md" for a in atoms))
    check("all atoms have raw_section", all(len(a.raw_section) > 0 for a in atoms))

    check(
        "short items filtered",
        not any(a.content == "Short item" for a in atoms),
    )

    print(f"  Extracted {len(atoms)} atoms from sample markdown")


def test_parser_csv_simple() -> None:
    print("\n=== Parser Tests (CSV Simple) ===")
    from distillation.parser import parse_csv, RawAtom

    atoms = parse_csv(SAMPLE_CSV_SIMPLE, "test/sample.csv")
    check("returns list", isinstance(atoms, list))
    check("csv atoms > 0", len(atoms) > 0, f"got {len(atoms)}")
    check("csv atoms are RawAtom", all(isinstance(a, RawAtom) for a in atoms))

    check(
        "Tool X extracted",
        any("Tool X" in a.content for a in atoms),
    )
    check(
        "short rows filtered",
        not any(a.content == "Short. Too brief" for a in atoms),
    )
    check(
        "Another paper extracted",
        any("automated code review" in a.content for a in atoms),
    )

    print(f"  Extracted {len(atoms)} atoms from simple CSV")


def test_parser_csv_nested() -> None:
    print("\n=== Parser Tests (CSV Nested) ===")
    from distillation.parser import parse_csv, RawAtom

    atoms = parse_csv(SAMPLE_CSV_NESTED, "test/nested.csv")
    check("nested csv atoms > 0", len(atoms) > 0, f"got {len(atoms)}")

    check(
        "Adaptive Routing extracted",
        any("Adaptive Routing" in a.content for a in atoms),
    )
    check(
        "short nested paper filtered",
        not any(a.content == "Short. No" for a in atoms),
    )

    print(f"  Extracted {len(atoms)} atoms from nested CSV")


def test_parser_real_file() -> None:
    print("\n=== Parser Tests (Real Files) ===")
    from distillation.parser import parse_file
    from distillation.scanner import scan_corpus

    corpus = scan_corpus(PROJECT_ROOT)

    md_files = corpus.get("perplexity", []) + corpus.get("overviews", [])
    if md_files:
        sample_md = md_files[0]
        atoms = parse_file(sample_md)
        check(
            f"real md file produces atoms ({sample_md.name})",
            len(atoms) > 0,
            f"got {len(atoms)} from {sample_md}",
        )
        check(
            "real md atoms have content",
            all(len(a.content) >= 40 for a in atoms),
        )
        print(f"  {sample_md.name}: {len(atoms)} atoms")
    else:
        check("real md files found", False, "no perplexity or overview files")

    csv_files = corpus.get("kimi_csv", [])
    if csv_files:
        sample_csv = csv_files[0]
        atoms = parse_file(sample_csv)
        check(
            f"real csv file produces atoms ({sample_csv.name})",
            len(atoms) > 0,
            f"got {len(atoms)} from {sample_csv}",
        )
        print(f"  {sample_csv.name}: {len(atoms)} atoms")
    else:
        check("real csv files found", False, "no csv files")


def test_parser_code_fence_stripping() -> None:
    print("\n=== Parser Tests (Code Fence Stripping) ===")
    from distillation.parser import parse_markdown

    fenced = "```markdown\n# Title\n\n## Section\n\n- **Technique Alpha**: A specific method for parsing code with 85% accuracy improvement over baseline approaches.\n```"
    atoms = parse_markdown(fenced, "test/fenced.md")
    check("code-fenced content parsed", len(atoms) > 0, f"got {len(atoms)}")
    if atoms:
        check(
            "code fence markers removed from content",
            "```" not in atoms[0].content,
        )


# ── Classifier tests ───────────────────────────────────────────────

def test_classifier_types() -> None:
    print("\n=== Classifier Tests (Type Detection) ===")
    from distillation.parser import RawAtom
    from distillation.classifier import classify
    from distillation.constants import AtomType

    cases: list[tuple[str, AtomType | None, str]] = [
        (
            "AST-based code search improves precision 60-80% over text-based grep approaches",
            AtomType.METRIC,
            "metric with percentage range",
        ),
        (
            "Tree-sitter: incremental AST parsing supporting 40+ languages with error recovery, de facto standard for code intelligence",
            AtomType.TOOL,
            "tool with capability description",
        ),
        (
            "Chain-of-Verification: generate answer then extract claims then verify each independently then produce final answer",
            AtomType.TECHNIQUE,
            "technique with procedural verbs",
        ),
        (
            "1. Parse target files with Tree-sitter to build AST\n2. Query symbol index for cross-file references\n3. Construct CFG for execution flow analysis\n4. Build DFG for data dependency tracking",
            AtomType.RECIPE,
            "numbered steps with procedural verbs",
        ),
        (
            "AST + CFG + DFG combined together improves code understanding 35-50% over single representation",
            AtomType.METRIC,
            "combination with metric gets METRIC priority",
        ),
        (
            "Context window attention degrades 20-40% for mid-context items — must place critical info at boundaries",
            AtomType.METRIC,
            "constraint-like but has metric",
        ),
        (
            "19.7% of AI-recommended packages are fabricated — verify every package against registry before inclusion to prevent slopsquatting attacks",
            AtomType.METRIC,
            "failure mode with metric gets METRIC",
        ),
        (
            "Wake-up prompts don't recover degraded context — measured failure across models, avoid this anti-pattern",
            AtomType.ANTI_PATTERN,
            "anti-pattern with don't/avoid",
        ),
        (
            "Selective Context: 50% reduction, 97% quality vs. LLMLingua: 20x compression, less than 3% loss — use SC for moderate needs, LLMLingua for aggressive compression",
            AtomType.METRIC,
            "tradeoff with metrics gets METRIC",
        ),
        (
            "Agent must never commit directly to main branch — all changes require review approval before merge",
            AtomType.CONSTRAINT,
            "constraint with must never",
        ),
        (
            "Prompt injection attacks can bypass guardrails — detect via input sanitization and respond with request rejection to handle the vulnerability",
            AtomType.FAILURE_MODE,
            "failure mode with detect/respond",
        ),
        (
            "Use AST combined with symbol index together for fast navigation instead of full CPG",
            AtomType.COMBINATION,
            "combination with together/combined",
        ),
        (
            "Selective Context vs LLMLingua: when moderate compression needed use SC, when aggressive compression needed use LLMLingua alternatively",
            AtomType.TRADEOFF,
            "tradeoff with vs and when...use",
        ),
    ]

    for content, expected_type, label in cases:
        raw = RawAtom(content=content, source_path="test/cls.md", raw_section=content)
        result = classify(raw)
        if expected_type is None:
            check(f"classify None: {label}", result is None, f"got {result}")
        else:
            check(
                f"classify {expected_type.value}: {label}",
                result is not None and result.type == expected_type,
                f"got {result.type.value if result else 'None'}",
            )


def test_classifier_discard() -> None:
    print("\n=== Classifier Tests (Discard) ===")
    from distillation.parser import RawAtom
    from distillation.classifier import classify

    discard_cases = [
        "An AST represents the syntactic structure of source code in a tree format.",
        "Use appropriate error handling in your code implementation.",
        "Follow best practices when designing your system architecture.",
        "The quick brown fox jumps over the lazy dog repeatedly today.",
    ]

    for content in discard_cases:
        raw = RawAtom(content=content, source_path="test/cls.md", raw_section=content)
        result = classify(raw)
        check(f"discard: {content[:50]}...", result is None, f"got {result.type.value if result else 'None'}")


def test_classifier_evidence_strength() -> None:
    print("\n=== Classifier Tests (Evidence Strength) ===")
    from distillation.parser import RawAtom
    from distillation.classifier import classify
    from distillation.constants import EvidenceStrength

    strong_text = "According to [12], AST-based search improves precision by 60-80% over text-based approaches"
    raw = RawAtom(content=strong_text, source_path="test/cls.md", raw_section=strong_text)
    result = classify(raw)
    check(
        "STRONG: citation + number",
        result is not None and result.evidence_strength == EvidenceStrength.STRONG,
        f"got {result.evidence_strength.value if result else 'None'}",
    )

    moderate_num = "Tree-sitter: incremental AST parsing supporting 40+ languages with error recovery capabilities"
    raw = RawAtom(content=moderate_num, source_path="test/cls.md", raw_section=moderate_num)
    result = classify(raw)
    check(
        "MODERATE: number without citation",
        result is not None and result.evidence_strength == EvidenceStrength.MODERATE,
        f"got {result.evidence_strength.value if result else 'None'}",
    )

    moderate_src = "According to a benchmark study, Tree-sitter provides the fastest incremental parsing implementation available"
    raw = RawAtom(content=moderate_src, source_path="test/cls.md", raw_section=moderate_src)
    result = classify(raw)
    check(
        "MODERATE: named source without number",
        result is not None and result.evidence_strength == EvidenceStrength.MODERATE,
        f"got {result.evidence_strength.value if result else 'None'}",
    )

    weak_text = "Agent must never commit directly to main branch — all changes require review approval before merge"
    raw = RawAtom(content=weak_text, source_path="test/cls.md", raw_section=weak_text)
    result = classify(raw)
    check(
        "WEAK: no number or source",
        result is not None and result.evidence_strength == EvidenceStrength.WEAK,
        f"got {result.evidence_strength.value if result else 'None'}",
    )


def test_classifier_output_fields() -> None:
    print("\n=== Classifier Tests (Output Fields) ===")
    from distillation.parser import RawAtom
    from distillation.classifier import classify
    from distillation.models import KnowledgeAtom

    text = "Tree-sitter: incremental AST parsing supporting 40+ languages with error recovery capabilities"
    raw = RawAtom(content=text, source_path="test/src.md", raw_section="## Section\n" + text)
    result = classify(raw)

    check("result is KnowledgeAtom", isinstance(result, KnowledgeAtom))
    if result:
        check("id is empty (assigned later)", result.id == "")
        check("content preserved", result.content == text)
        check("source_path set", result.sources == ["test/src.md"])
        check("raw_section set", len(result.raw_section) > 0)
        check("domains empty (tagger assigns later)", result.domains == [])
        check("sdlc_phases empty", result.sdlc_phases == [])
        check("products empty", result.products == [])


def test_classifier_priority() -> None:
    print("\n=== Classifier Tests (Priority: RECIPE > TECHNIQUE > COMBINATION) ===")
    from distillation.parser import RawAtom
    from distillation.classifier import classify
    from distillation.constants import AtomType

    recipe_text = (
        "1. Parse target files with Tree-sitter to build AST\n"
        "2. Extract symbol references and build call graph\n"
        "3. Construct combined CFG integrated together with DFG\n"
        "4. Verify all references resolve correctly"
    )
    raw = RawAtom(content=recipe_text, source_path="test/cls.md", raw_section=recipe_text)
    result = classify(raw)
    check(
        "RECIPE wins over TECHNIQUE+COMBINATION",
        result is not None and result.type == AtomType.RECIPE,
        f"got {result.type.value if result else 'None'}",
    )

    technique_combo = "Parse the AST and build the CFG combined together with DFG for unified code analysis"
    raw = RawAtom(content=technique_combo, source_path="test/cls.md", raw_section=technique_combo)
    result = classify(raw)
    check(
        "TECHNIQUE wins over COMBINATION",
        result is not None and result.type == AtomType.TECHNIQUE,
        f"got {result.type.value if result else 'None'}",
    )


# ── Main ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    test_scanner()
    test_parser_markdown()
    test_parser_csv_simple()
    test_parser_csv_nested()
    test_parser_real_file()
    test_parser_code_fence_stripping()
    test_classifier_types()
    test_classifier_discard()
    test_classifier_evidence_strength()
    test_classifier_output_fields()
    test_classifier_priority()

    print(f"\n{'=' * 40}")
    print(f"Results: {PASS} passed, {FAIL} failed")
    if FAIL:
        sys.exit(1)
    print("All checks passed.")
