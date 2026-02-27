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


# ── Dedup tests ────────────────────────────────────────────────────

def test_dedup_exact_duplicates() -> None:
    print("\n=== Dedup Tests (Exact Duplicates) ===")
    from distillation.dedup import deduplicate
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    a1 = KnowledgeAtom(
        id="", type=AtomType.METRIC,
        content="AST-based code search improves precision 60-80% over text-based",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["file_a.md"],
    )
    a2 = KnowledgeAtom(
        id="", type=AtomType.METRIC,
        content="AST-based code search improves precision 60-80% over text-based",
        evidence_strength=EvidenceStrength.STRONG,
        sources=["file_b.md"],
    )
    result = deduplicate([a1, a2])
    check("exact dup merged to 1", len(result) == 1, f"got {len(result)}")
    check("kept STRONG version", result[0].evidence_strength == EvidenceStrength.STRONG)
    check("merged sources", set(result[0].sources) == {"file_a.md", "file_b.md"})


def test_dedup_whitespace_normalization() -> None:
    print("\n=== Dedup Tests (Whitespace Normalization) ===")
    from distillation.dedup import deduplicate
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    a1 = KnowledgeAtom(
        id="", type=AtomType.TOOL,
        content="Tree-sitter:  incremental AST   parsing",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["f1.md"],
    )
    a2 = KnowledgeAtom(
        id="", type=AtomType.TOOL,
        content="Tree-sitter: incremental AST parsing",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["f2.md"],
    )
    result = deduplicate([a1, a2])
    check("whitespace-different dup merged", len(result) == 1, f"got {len(result)}")


def test_dedup_citation_normalization() -> None:
    print("\n=== Dedup Tests (Citation Normalization) ===")
    from distillation.dedup import deduplicate
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    a1 = KnowledgeAtom(
        id="", type=AtomType.METRIC,
        content="According to [12], precision improves 60-80%",
        evidence_strength=EvidenceStrength.STRONG,
        sources=["f1.md"],
    )
    a2 = KnowledgeAtom(
        id="", type=AtomType.METRIC,
        content="According to , precision improves 60-80%",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["f2.md"],
    )
    result = deduplicate([a1, a2])
    check("citation-stripped dup merged", len(result) == 1, f"got {len(result)}")
    check("kept STRONG with citation", result[0].evidence_strength == EvidenceStrength.STRONG)


def test_dedup_distinct_preserved() -> None:
    print("\n=== Dedup Tests (Distinct Atoms Preserved) ===")
    from distillation.dedup import deduplicate
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    a1 = KnowledgeAtom(
        id="", type=AtomType.TOOL,
        content="Tree-sitter: incremental AST parsing 40+ languages",
        evidence_strength=EvidenceStrength.STRONG,
        sources=["f1.md"],
    )
    a2 = KnowledgeAtom(
        id="", type=AtomType.TOOL,
        content="Sourcegraph: multi-repo symbol search with sub-second queries",
        evidence_strength=EvidenceStrength.STRONG,
        sources=["f2.md"],
    )
    result = deduplicate([a1, a2])
    check("distinct atoms kept", len(result) == 2, f"got {len(result)}")


def test_dedup_content_hash_set() -> None:
    print("\n=== Dedup Tests (Content Hash) ===")
    from distillation.dedup import deduplicate
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    a1 = KnowledgeAtom(
        id="", type=AtomType.METRIC,
        content="Precision improves 60-80%",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["f1.md"],
    )
    result = deduplicate([a1])
    check("content_hash populated", len(result[0].content_hash) == 64, f"got len={len(result[0].content_hash)}")


# ── Ranker tests ───────────────────────────────────────────────────

def test_ranker_evidence_ordering() -> None:
    print("\n=== Ranker Tests (Evidence Ordering) ===")
    from distillation.ranker import rank
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atoms = [
        KnowledgeAtom(id="", type=AtomType.METRIC, content="Weak metric assertion", evidence_strength=EvidenceStrength.WEAK, sources=["f.md"]),
        KnowledgeAtom(id="", type=AtomType.METRIC, content="Strong metric with 80% improvement [12]", evidence_strength=EvidenceStrength.STRONG, sources=["f.md"]),
        KnowledgeAtom(id="", type=AtomType.METRIC, content="Moderate metric with 50% gain", evidence_strength=EvidenceStrength.MODERATE, sources=["f.md"]),
    ]
    result = rank(atoms)
    metrics = [a for a in result if a.type == AtomType.METRIC]
    check(
        "STRONG first",
        metrics[0].evidence_strength == EvidenceStrength.STRONG,
        f"got {metrics[0].evidence_strength.value}",
    )
    check(
        "MODERATE second",
        metrics[1].evidence_strength == EvidenceStrength.MODERATE,
        f"got {metrics[1].evidence_strength.value}",
    )
    check(
        "WEAK last",
        metrics[2].evidence_strength == EvidenceStrength.WEAK,
        f"got {metrics[2].evidence_strength.value}",
    )


def test_ranker_assigns_ids() -> None:
    print("\n=== Ranker Tests (ID Assignment) ===")
    from distillation.ranker import rank
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atoms = [
        KnowledgeAtom(id="", type=AtomType.TECHNIQUE, content="Parse AST and build graph", evidence_strength=EvidenceStrength.MODERATE, sources=["f.md"]),
        KnowledgeAtom(id="", type=AtomType.METRIC, content="60-80% improvement", evidence_strength=EvidenceStrength.STRONG, sources=["f.md"]),
        KnowledgeAtom(id="", type=AtomType.TOOL, content="Tree-sitter supports 40+ languages", evidence_strength=EvidenceStrength.STRONG, sources=["f.md"]),
    ]
    result = rank(atoms)
    check("all have KA- IDs", all(a.id.startswith("KA-") for a in result))
    ids = [a.id for a in result]
    check("IDs are unique", len(ids) == len(set(ids)), f"ids={ids}")
    check("IDs are sequential format", all(a.id[3:].isdigit() for a in result))


def test_ranker_groups_by_type() -> None:
    print("\n=== Ranker Tests (Grouped by Type) ===")
    from distillation.ranker import rank
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atoms = [
        KnowledgeAtom(id="", type=AtomType.TOOL, content="Sourcegraph multi-repo search", evidence_strength=EvidenceStrength.STRONG, sources=["f.md"]),
        KnowledgeAtom(id="", type=AtomType.TECHNIQUE, content="Parse and build AST with verification step", evidence_strength=EvidenceStrength.MODERATE, sources=["f.md"]),
        KnowledgeAtom(id="", type=AtomType.TOOL, content="Tree-sitter AST parsing 40+ languages", evidence_strength=EvidenceStrength.MODERATE, sources=["f.md"]),
        KnowledgeAtom(id="", type=AtomType.TECHNIQUE, content="Extract and verify claims independently", evidence_strength=EvidenceStrength.STRONG, sources=["f.md"]),
    ]
    result = rank(atoms)
    types = [a.type for a in result]
    first_technique = types.index(AtomType.TECHNIQUE)
    last_technique = len(types) - 1 - types[::-1].index(AtomType.TECHNIQUE)
    first_tool = types.index(AtomType.TOOL)
    last_tool = len(types) - 1 - types[::-1].index(AtomType.TOOL)
    check(
        "techniques contiguous",
        last_technique - first_technique == 1,
        f"technique indices {first_technique}-{last_technique}",
    )
    check(
        "tools contiguous",
        last_tool - first_tool == 1,
        f"tool indices {first_tool}-{last_tool}",
    )


def test_ranker_specificity_tiebreak() -> None:
    print("\n=== Ranker Tests (Specificity Tiebreak) ===")
    from distillation.ranker import rank
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    vague = KnowledgeAtom(
        id="", type=AtomType.TECHNIQUE,
        content="Parse the code and analyze it for issues",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["f.md"],
    )
    specific = KnowledgeAtom(
        id="", type=AtomType.TECHNIQUE,
        content="Parse target files with Tree-sitter to build AST then extract symbol references step 1 and verify step 2",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["f.md"],
    )
    result = rank([vague, specific])
    techniques = [a for a in result if a.type == AtomType.TECHNIQUE]
    check(
        "more specific ranked first",
        "Tree-sitter" in techniques[0].content,
        f"first content: {techniques[0].content[:40]}",
    )


# ── Tagger tests ───────────────────────────────────────────────────

def test_tagger_domain_assignment() -> None:
    print("\n=== Tagger Tests (Domain Assignment) ===")
    from distillation.tagger import tag
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atom = KnowledgeAtom(
        id="KA-001", type=AtomType.TOOL,
        content="Tree-sitter: incremental AST parsing supporting 40+ languages with error recovery, de facto standard for code intelligence",
        evidence_strength=EvidenceStrength.STRONG,
        sources=["f.md"],
    )
    result = tag([atom])
    check("domain tagged", len(result[0].domains) > 0, f"got {result[0].domains}")
    check("D5 assigned (code intelligence)", "D5" in result[0].domains, f"got {result[0].domains}")


def test_tagger_phase_assignment() -> None:
    print("\n=== Tagger Tests (Phase Assignment) ===")
    from distillation.tagger import tag
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atom = KnowledgeAtom(
        id="KA-002", type=AtomType.METRIC,
        content="Mutation testing detects 70% of quality gate failures in test generation validation pipelines",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["f.md"],
    )
    result = tag([atom])
    check("phase tagged", len(result[0].sdlc_phases) > 0, f"got {result[0].sdlc_phases}")
    check("P4 assigned (testing)", "P4" in result[0].sdlc_phases, f"got {result[0].sdlc_phases}")


def test_tagger_product_assignment() -> None:
    print("\n=== Tagger Tests (Product Assignment) ===")
    from distillation.tagger import tag
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atom = KnowledgeAtom(
        id="KA-003", type=AtomType.CONSTRAINT,
        content="Agent must never commit directly to main branch — all changes require review approval as a hard constraint and guardrail rule",
        evidence_strength=EvidenceStrength.WEAK,
        sources=["f.md"],
    )
    result = tag([atom])
    check("product tagged", len(result[0].products) > 0, f"got {result[0].products}")
    check("PC6 assigned (rules)", "PC6" in result[0].products, f"got {result[0].products}")


def test_tagger_multi_domain() -> None:
    print("\n=== Tagger Tests (Multi-Domain) ===")
    from distillation.tagger import tag
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atom = KnowledgeAtom(
        id="KA-004", type=AtomType.TOOL,
        content="Code Property Graphs via Joern unify AST CFG DFG for vulnerability detection and taint tracking of security issues",
        evidence_strength=EvidenceStrength.MODERATE,
        sources=["f.md"],
    )
    result = tag([atom])
    check("multiple domains", len(result[0].domains) >= 2, f"got {result[0].domains}")
    check("D5 present (code intelligence)", "D5" in result[0].domains, f"got {result[0].domains}")
    check("D7 present (security)", "D7" in result[0].domains, f"got {result[0].domains}")


def test_tagger_fallback_assignment() -> None:
    print("\n=== Tagger Tests (Fallback Assignment) ===")
    from distillation.tagger import tag
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atom = KnowledgeAtom(
        id="KA-005", type=AtomType.TECHNIQUE,
        content="Apply a novel specialized approach for improved system outcomes",
        evidence_strength=EvidenceStrength.WEAK,
        sources=["f.md"],
    )
    result = tag([atom])
    check("domain fallback >=1", len(result[0].domains) >= 1, f"got {result[0].domains}")
    check("phase fallback >=1", len(result[0].sdlc_phases) >= 1, f"got {result[0].sdlc_phases}")
    check("product fallback >=1", len(result[0].products) >= 1, f"got {result[0].products}")


def test_tagger_all_atoms_tagged() -> None:
    print("\n=== Tagger Tests (All Atoms Get Tags) ===")
    from distillation.tagger import tag
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atoms = [
        KnowledgeAtom(id="KA-010", type=AtomType.METRIC, content="LLMLingua achieves 20x compression with less than 3% quality loss", evidence_strength=EvidenceStrength.MODERATE, sources=["f.md"]),
        KnowledgeAtom(id="KA-011", type=AtomType.RECIPE, content="1. Parse AST 2. Build call graph 3. Overlay DFG 4. Construct CPG", evidence_strength=EvidenceStrength.MODERATE, sources=["f.md"]),
        KnowledgeAtom(id="KA-012", type=AtomType.FAILURE_MODE, content="19.7% of AI-recommended packages are fabricated hallucinations", evidence_strength=EvidenceStrength.STRONG, sources=["f.md"]),
    ]
    result = tag(atoms)
    for a in result:
        check(f"{a.id} has domains", len(a.domains) >= 1, f"got {a.domains}")
        check(f"{a.id} has phases", len(a.sdlc_phases) >= 1, f"got {a.sdlc_phases}")
        check(f"{a.id} has products", len(a.products) >= 1, f"got {a.products}")


def test_tagger_raw_section_fallback() -> None:
    print("\n=== Tagger Tests (Raw Section Fallback) ===")
    from distillation.tagger import tag
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    atom = KnowledgeAtom(
        id="KA-006", type=AtomType.TECHNIQUE,
        content="A generic method for processing data efficiently",
        evidence_strength=EvidenceStrength.WEAK,
        sources=["f.md"],
        raw_section="## Agent Architecture & Orchestration\nMulti-agent delegation handoff patterns for hierarchical orchestration",
    )
    result = tag([atom])
    check("raw_section fallback domain D1", "D1" in result[0].domains, f"got {result[0].domains}")


# ── Prong 2 (Domain Grouping) tests ───────────────────────────────

def _make_tagged_atoms() -> list:
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    return [
        KnowledgeAtom(
            id="KA-001", type=AtomType.TOOL,
            content="Tree-sitter: incremental AST parsing supporting 40+ languages with error recovery",
            evidence_strength=EvidenceStrength.STRONG,
            sources=["file_a.md"],
            domains=["D5"], sdlc_phases=["P1", "P3"], products=["PC2"],
        ),
        KnowledgeAtom(
            id="KA-002", type=AtomType.METRIC,
            content="AST-based code search improves precision 60-80% over text-based approaches",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_a.md"],
            domains=["D5"], sdlc_phases=["P1"], products=["PC2"],
        ),
        KnowledgeAtom(
            id="KA-003", type=AtomType.COMBINATION,
            content="AST + CFG + DFG combined improves code understanding 35-50% over single representation",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_a.md"],
            domains=["D5", "D7"], sdlc_phases=["P1", "P5"], products=["PC2"],
        ),
        KnowledgeAtom(
            id="KA-004", type=AtomType.CONSTRAINT,
            content="Agent must never commit directly to main branch — all changes require review approval",
            evidence_strength=EvidenceStrength.WEAK,
            sources=["file_b.md"],
            domains=["D2", "D10"], sdlc_phases=["P3"], products=["PC6"],
        ),
        KnowledgeAtom(
            id="KA-005", type=AtomType.FAILURE_MODE,
            content="19.7% of AI-recommended packages are fabricated — verify against registry before inclusion",
            evidence_strength=EvidenceStrength.STRONG,
            sources=["file_c.md"],
            domains=["D7"], sdlc_phases=["P3"], products=["PC6"],
        ),
        KnowledgeAtom(
            id="KA-006", type=AtomType.TECHNIQUE,
            content="Parse target files with Tree-sitter to build AST then extract symbol references",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_a.md"],
            domains=["D5"], sdlc_phases=["P1", "P5"], products=["PC2"],
        ),
        KnowledgeAtom(
            id="KA-007", type=AtomType.TRADEOFF,
            content="Selective Context vs LLMLingua: use SC for moderate compression, LLMLingua for aggressive",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_d.md"],
            domains=["D3"], sdlc_phases=["P3"], products=["PC7"],
        ),
        KnowledgeAtom(
            id="KA-008", type=AtomType.ANTI_PATTERN,
            content="Wake-up prompts don't recover degraded context — measured failure across models",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_d.md"],
            domains=["D3"], sdlc_phases=["P3"], products=["PC6", "PC10"],
        ),
    ]


def test_prong2_generates_12_files() -> None:
    print("\n=== Prong 2 Tests (12 Domain Files Generated) ===")
    import shutil
    import tempfile
    from distillation.prong2_domains import generate_domain_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_domain_specs(atoms, tmp)
        domains_dir = tmp / "domains"
        check("domains dir created", domains_dir.is_dir())

        md_files = sorted(domains_dir.glob("*.md"))
        check("12 domain files generated", len(md_files) == 12, f"got {len(md_files)}")

        check("12 DomainSpec objects returned", len(specs) == 12, f"got {len(specs)}")

        expected_prefixes = [
            "D01_", "D02_", "D03_", "D04_", "D05_", "D06_",
            "D07_", "D08_", "D09_", "D10_", "D11_", "D12_",
        ]
        actual_names = [f.name for f in md_files]
        for prefix in expected_prefixes:
            check(
                f"file with prefix {prefix} exists",
                any(n.startswith(prefix) for n in actual_names),
                f"files: {actual_names}",
            )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong2_atom_id_references() -> None:
    print("\n=== Prong 2 Tests (Valid Atom ID References) ===")
    import re as _re
    import shutil
    import tempfile
    from distillation.prong2_domains import generate_domain_specs

    atoms = _make_tagged_atoms()
    valid_ids = {a.id for a in atoms}
    tmp = Path(tempfile.mkdtemp())
    try:
        generate_domain_specs(atoms, tmp)
        domains_dir = tmp / "domains"
        ka_pattern = _re.compile(r"`(KA-\d+)`")
        for md_file in domains_dir.glob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            referenced_ids = set(ka_pattern.findall(content))
            invalid = referenced_ids - valid_ids
            check(
                f"{md_file.name}: all atom IDs valid",
                len(invalid) == 0,
                f"invalid IDs: {invalid}",
            )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong2_domain_content() -> None:
    print("\n=== Prong 2 Tests (Domain Content Sections) ===")
    import shutil
    import tempfile
    from distillation.prong2_domains import generate_domain_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_domain_specs(atoms, tmp)
        domains_dir = tmp / "domains"

        d5_file = domains_dir / "D05_code_intelligence.md"
        check("D5 file exists", d5_file.exists())
        d5_content = d5_file.read_text(encoding="utf-8")
        check("D5 has KNOWLEDGE ATOMS section", "KNOWLEDGE ATOMS" in d5_content)
        check("D5 has KEY TECHNIQUES section", "KEY TECHNIQUES" in d5_content)
        check("D5 has KEY TOOLS section", "KEY TOOLS" in d5_content)
        check("D5 has COMBINATION RECIPES section", "COMBINATION RECIPES" in d5_content)
        check("D5 has CROSS-DOMAIN LINKS section", "CROSS-DOMAIN LINKS" in d5_content)
        check("D5 has GAPS section", "GAPS" in d5_content)
        check("D5 references KA-001", "KA-001" in d5_content)
        check("D5 references KA-006", "KA-006" in d5_content)

        d5_spec = next(s for s in specs if s.domain.value == "D5")
        check("D5 spec has atoms", len(d5_spec.atom_ids) >= 3, f"got {len(d5_spec.atom_ids)}")
        check("D5 spec has tools", len(d5_spec.key_tools) >= 1)
        check("D5 spec has techniques", len(d5_spec.key_techniques) >= 1)
        check("D5 spec has combination_recipes", len(d5_spec.combination_recipes) >= 1)

        d7_spec = next(s for s in specs if s.domain.value == "D7")
        check("D7 spec has failure_modes", len(d7_spec.failure_modes) >= 1)

        cross_links = d5_spec.cross_domain_links
        check(
            "D5 cross-domain link for KA-003",
            "KA-003" in cross_links and "D7" in cross_links["KA-003"],
            f"got {cross_links}",
        )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong2_empty_domain_gaps() -> None:
    print("\n=== Prong 2 Tests (Empty Domain Gap Reporting) ===")
    import shutil
    import tempfile
    from distillation.prong2_domains import generate_domain_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_domain_specs(atoms, tmp)
        d4_spec = next(s for s in specs if s.domain.value == "D4")
        check("empty domain D4 has gaps", len(d4_spec.gaps) > 0, f"got {d4_spec.gaps}")
        check("empty domain D4 has 0 atoms", len(d4_spec.atom_ids) == 0)

        d4_file = (tmp / "domains" / "D04_memory_knowledge_systems.md")
        check("D4 file exists even with no atoms", d4_file.exists())
        d4_content = d4_file.read_text(encoding="utf-8")
        check("D4 has thin coverage gap", "Thin coverage" in d4_content or "No " in d4_content)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong2_evidence_ranking() -> None:
    print("\n=== Prong 2 Tests (Evidence Strength Ranking) ===")
    import shutil
    import tempfile
    from distillation.prong2_domains import generate_domain_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_domain_specs(atoms, tmp)
        d5_spec = next(s for s in specs if s.domain.value == "D5")
        if len(d5_spec.atom_ids) >= 2:
            from distillation.constants import EvidenceStrength
            atoms_by_id = {a.id: a for a in atoms}
            first = atoms_by_id.get(d5_spec.atom_ids[0])
            check(
                "STRONG evidence atom ranked first in D5",
                first is not None and first.evidence_strength == EvidenceStrength.STRONG,
                f"first atom {d5_spec.atom_ids[0]} has {first.evidence_strength.value if first else 'N/A'}",
            )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ── Prong 3 (SDLC Phase Mapping) tests ─────────────────────────────

def _make_phase_test_atoms() -> list:
    from distillation.models import KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength

    return _make_tagged_atoms() + [
        KnowledgeAtom(
            id="KA-009", type=AtomType.TOOL,
            content="Sourcegraph: multi-repo symbol search with sub-second queries across million-line codebases",
            evidence_strength=EvidenceStrength.STRONG,
            sources=["file_e.md"],
            domains=["D5"], sdlc_phases=["P1", "P5"], products=["PC2"],
        ),
        KnowledgeAtom(
            id="KA-010", type=AtomType.TECHNIQUE,
            content="Canary deployment: route 5% traffic to new version, monitor error rates, gradually increase",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_f.md"],
            domains=["D9"], sdlc_phases=["P7"], products=["PC3"],
        ),
        KnowledgeAtom(
            id="KA-011", type=AtomType.RECIPE,
            content="1. Parse AST via Tree-sitter 2. Build call graph 3. Overlay DFG 4. For security: full CPG",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_a.md"],
            domains=["D5"], sdlc_phases=["P1", "P5"], products=["PC2"],
        ),
        KnowledgeAtom(
            id="KA-012", type=AtomType.TECHNIQUE,
            content="Root cause analysis: collect stack traces, build execution timeline, isolate variable state changes",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_g.md"],
            domains=["D5"], sdlc_phases=["P6"], products=["PC10"],
        ),
        KnowledgeAtom(
            id="KA-013", type=AtomType.FAILURE_MODE,
            content="Self-healing pipeline loops can exhaust resources — cap retry count and escalate after threshold",
            evidence_strength=EvidenceStrength.MODERATE,
            sources=["file_h.md"],
            domains=["D9"], sdlc_phases=["P8"], products=["PC6"],
        ),
    ]


def test_prong3_generates_8_files() -> None:
    print("\n=== Prong 3 Tests (8 Phase Files Generated) ===")
    import shutil
    import tempfile
    from distillation.prong3_phases import generate_phase_specs

    atoms = _make_phase_test_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_phase_specs(atoms, tmp)
        phases_dir = tmp / "phases"
        check("phases dir created", phases_dir.is_dir())

        md_files = sorted(phases_dir.glob("*.md"))
        check("8 phase files generated", len(md_files) == 8, f"got {len(md_files)}")
        check("8 PhaseSpec objects returned", len(specs) == 8, f"got {len(specs)}")

        expected_files = [
            "P1_discovery_onboarding.md",
            "P2_planning_design.md",
            "P3_implementation.md",
            "P4_testing_verification.md",
            "P5_code_review.md",
            "P6_debugging_error_recovery.md",
            "P7_deployment_release.md",
            "P8_maintenance_monitoring.md",
        ]
        actual_names = [f.name for f in md_files]
        for fname in expected_files:
            check(f"{fname} exists", fname in actual_names, f"files: {actual_names}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong3_atom_id_references() -> None:
    print("\n=== Prong 3 Tests (Valid Atom ID References) ===")
    import re as _re
    import shutil
    import tempfile
    from distillation.prong3_phases import generate_phase_specs

    atoms = _make_phase_test_atoms()
    valid_ids = {a.id for a in atoms}
    tmp = Path(tempfile.mkdtemp())
    try:
        generate_phase_specs(atoms, tmp)
        phases_dir = tmp / "phases"
        ka_pattern = _re.compile(r"KA-\d+")
        for md_file in sorted(phases_dir.glob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            referenced_ids = set(ka_pattern.findall(content))
            invalid = referenced_ids - valid_ids
            check(
                f"{md_file.name}: all atom IDs valid",
                len(invalid) == 0,
                f"invalid IDs: {invalid}",
            )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong3_content_structure() -> None:
    print("\n=== Prong 3 Tests (Content Structure) ===")
    import shutil
    import tempfile
    from distillation.prong3_phases import generate_phase_specs

    atoms = _make_phase_test_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        generate_phase_specs(atoms, tmp)
        phases_dir = tmp / "phases"

        p1 = (phases_dir / "P1_discovery_onboarding.md").read_text(encoding="utf-8")
        check("P1 has title", "# P1: Discovery & Onboarding" in p1)
        check("P1 has WHAT THE AGENT section", "WHAT THE AGENT IS DOING" in p1)
        check("P1 has Knowledge Atoms section", "## Knowledge Atoms" in p1)
        check("P1 has Techniques section", "## Techniques to Use" in p1)
        check("P1 has Constraints section", "## Constraints in Effect" in p1)
        check("P1 has Tools section", "## Tools Needed" in p1)
        check("P1 has Failure Modes section", "## Failure Modes to Watch For" in p1)
        check("P1 has Transitions section", "## Transitions" in p1)
        check("P1 references KA-001 (Tree-sitter)", "KA-001" in p1)
        check("P1 references KA-009 (Sourcegraph)", "KA-009" in p1)

        p7 = (phases_dir / "P7_deployment_release.md").read_text(encoding="utf-8")
        check("P7 references KA-010 (canary)", "KA-010" in p7)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong3_spec_fields() -> None:
    print("\n=== Prong 3 Tests (PhaseSpec Fields) ===")
    import shutil
    import tempfile
    from distillation.prong3_phases import generate_phase_specs
    from distillation.constants import SDLCPhase

    atoms = _make_phase_test_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_phase_specs(atoms, tmp)
        phases_by_key = {s.phase.value: s for s in specs}

        p3 = phases_by_key["P3"]
        check("P3 has atoms", len(p3.atom_ids) > 0, f"got {len(p3.atom_ids)}")
        check("P3 has constraints", len(p3.constraints) > 0, f"got {p3.constraints}")
        check("P3 KA-004 in constraints", "KA-004" in p3.constraints)
        check("P3 has failure_modes", len(p3.failure_modes) > 0, f"got {p3.failure_modes}")
        check("P3 KA-005 in failure_modes", "KA-005" in p3.failure_modes)
        check("P3 has tools", len(p3.tools) > 0, f"got {p3.tools}")
        check("P3 KA-001 in tools", "KA-001" in p3.tools)
        check("P3 has transitions", len(p3.transitions) > 0)

        p6 = phases_by_key["P6"]
        check("P6 has atoms", len(p6.atom_ids) > 0, f"got {len(p6.atom_ids)}")

        all_phases = {SDLCPhase.P1, SDLCPhase.P2, SDLCPhase.P3, SDLCPhase.P4,
                      SDLCPhase.P5, SDLCPhase.P6, SDLCPhase.P7, SDLCPhase.P8}
        check("all 8 phases present", set(s.phase for s in specs) == all_phases)
        for s in specs:
            check(f"{s.phase.value} has name", len(s.name) > 0)
            check(f"{s.phase.value} has description", len(s.description) > 0)
            check(f"{s.phase.value} has transitions", len(s.transitions) > 0)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong3_empty_phase_handling() -> None:
    print("\n=== Prong 3 Tests (Empty Phase Handling) ===")
    import shutil
    import tempfile
    from distillation.prong3_phases import generate_phase_specs

    atoms = _make_phase_test_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_phase_specs(atoms, tmp)
        phases_by_key = {s.phase.value: s for s in specs}

        p4 = phases_by_key["P4"]
        check("P4 file generated even with few atoms", (tmp / "phases" / "P4_testing_verification.md").exists())

        p2 = phases_by_key["P2"]
        check("P2 file generated even with 0 atoms", (tmp / "phases" / "P2_planning_design.md").exists())
        check("P2 still has transitions", len(p2.transitions) > 0)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ── Prong 4 (Product Spec Assembly) tests ──────────────────────────

def test_prong4_generates_yaml_files() -> None:
    print("\n=== Prong 4 Tests (YAML Files Generated) ===")
    import shutil
    import tempfile
    from distillation.prong4_products import generate_product_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_product_specs(atoms, tmp)
        products_dir = tmp / "products"
        check("products dir created", products_dir.is_dir())

        yaml_files = list(products_dir.rglob("*.yaml"))
        check("at least 1 yaml file generated", len(yaml_files) >= 1, f"got {len(yaml_files)}")

        check("at least 1 ProductSpec returned", len(specs) >= 1, f"got {len(specs)}")

        for spec in specs:
            check(
                f"{spec.instance_name}: has atom_ids",
                len(spec.atom_ids) >= 1,
                f"got {len(spec.atom_ids)}",
            )
            check(
                f"{spec.instance_name}: has yaml_spec",
                isinstance(spec.yaml_spec, dict) and len(spec.yaml_spec) > 0,
            )
            check(
                f"{spec.instance_name}: confidence is valid",
                spec.confidence in ("HIGH", "MEDIUM", "LOW"),
                f"got {spec.confidence}",
            )

        print(f"  Generated {len(yaml_files)} YAML files across {len(specs)} product specs")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong4_valid_yaml_syntax() -> None:
    print("\n=== Prong 4 Tests (Valid YAML Syntax) ===")
    import shutil
    import tempfile
    from distillation.prong4_products import generate_product_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        generate_product_specs(atoms, tmp)
        products_dir = tmp / "products"
        yaml_files = list(products_dir.rglob("*.yaml"))

        try:
            import yaml
            for yf in yaml_files:
                content = yf.read_text(encoding="utf-8")
                parsed = yaml.safe_load(content)
                check(
                    f"{yf.name}: valid YAML",
                    parsed is not None and isinstance(parsed, dict),
                    f"got {type(parsed)}",
                )
        except ImportError:
            import json
            for yf in yaml_files:
                content = yf.read_text(encoding="utf-8")
                parsed = json.loads(content)
                check(
                    f"{yf.name}: valid JSON fallback",
                    parsed is not None and isinstance(parsed, dict),
                    f"got {type(parsed)}",
                )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong4_template_structure() -> None:
    print("\n=== Prong 4 Tests (Template Structure Conformance) ===")
    import shutil
    import tempfile
    from distillation.prong4_products import generate_product_specs, PRODUCT_DIR_MAP

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_product_specs(atoms, tmp)

        template_keys = {
            "PC1": ["mode", "role_definition", "tools", "skills_available"],
            "PC2": ["skill", "purpose", "technique_stack", "procedure"],
            "PC3": ["workflow", "trigger", "phases", "rollback_plan"],
            "PC4": ["prompt", "target", "structure", "guardrails"],
            "PC5": ["configuration", "servers", "security_constraints"],
            "PC6": ["rule", "constraint", "rationale", "enforcement"],
            "PC7": ["strategy", "window_partition", "compression_pipeline"],
            "PC8": ["pattern", "decomposition", "dependency_rules"],
            "PC9": ["workspace", "branch_strategy", "conflict_resolution"],
            "PC10": ["technique", "situation", "recognition", "response"],
        }

        for spec in specs:
            pc_val = spec.category.value
            expected = template_keys.get(pc_val, [])
            for key in expected:
                check(
                    f"{spec.instance_name}: has '{key}' key",
                    key in spec.yaml_spec,
                    f"keys: {list(spec.yaml_spec.keys())}",
                )

        products_dir = tmp / "products"
        for pc_val, dirname in PRODUCT_DIR_MAP.items():
            cat_specs = [s for s in specs if s.category.value == pc_val]
            if cat_specs:
                subdir = products_dir / dirname
                check(
                    f"{dirname}/ dir exists",
                    subdir.is_dir(),
                    f"missing {subdir}",
                )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong4_confidence_levels() -> None:
    print("\n=== Prong 4 Tests (Confidence Computation) ===")
    import shutil
    import tempfile
    from distillation.prong4_products import generate_product_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_product_specs(atoms, tmp)
        confidences = {s.confidence for s in specs}
        check(
            "at least one confidence level assigned",
            len(confidences) >= 1,
            f"got {confidences}",
        )
        for spec in specs:
            check(
                f"{spec.instance_name}: confidence valid",
                spec.confidence in ("HIGH", "MEDIUM", "LOW"),
            )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong4_gaps_tracked() -> None:
    print("\n=== Prong 4 Tests (Gaps Tracked) ===")
    import shutil
    import tempfile
    from distillation.prong4_products import generate_product_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_product_specs(atoms, tmp)
        check(
            "gaps are list type for all specs",
            all(isinstance(s.gaps, list) for s in specs),
        )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_prong4_atom_id_coverage() -> None:
    print("\n=== Prong 4 Tests (Atom ID Coverage) ===")
    import shutil
    import tempfile
    from distillation.prong4_products import generate_product_specs

    atoms = _make_tagged_atoms()
    valid_ids = {a.id for a in atoms}
    tmp = Path(tempfile.mkdtemp())
    try:
        specs = generate_product_specs(atoms, tmp)
        all_referenced = set()
        for spec in specs:
            all_referenced.update(spec.atom_ids)
        invalid = all_referenced - valid_ids
        check(
            "all referenced atom IDs are valid",
            len(invalid) == 0,
            f"invalid: {invalid}",
        )
        check(
            "at least some atoms consumed",
            len(all_referenced) >= 1,
            f"got {len(all_referenced)}",
        )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ── Validator tests ─────────────────────────────────────────────────

def test_validator_basic() -> None:
    print("\n=== Validator Tests (Basic) ===")
    import shutil
    import tempfile
    from distillation.validator import validate, ValidationReport
    from distillation.prong2_domains import generate_domain_specs
    from distillation.prong3_phases import generate_phase_specs
    from distillation.prong4_products import generate_product_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        domain_specs = generate_domain_specs(atoms, tmp)
        phase_specs = generate_phase_specs(atoms, tmp)
        product_specs = generate_product_specs(atoms, tmp)
        report = validate(atoms, domain_specs, phase_specs, product_specs)

        check("returns ValidationReport", isinstance(report, ValidationReport))
        check("total_atoms correct", report.total_atoms == len(atoms), f"got {report.total_atoms}")
        check("atoms_with_domain > 0", report.atoms_with_domain > 0, f"got {report.atoms_with_domain}")
        check("atoms_with_phase > 0", report.atoms_with_phase > 0, f"got {report.atoms_with_phase}")
        check("atoms_with_product > 0", report.atoms_with_product > 0, f"got {report.atoms_with_product}")
        check("summary is string", isinstance(report.summary, str))
        check("summary non-empty", len(report.summary) > 0)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_validator_orphans() -> None:
    print("\n=== Validator Tests (Orphan Detection) ===")
    from distillation.validator import validate
    from distillation.models import DomainSpec, PhaseSpec, ProductSpec, KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength, Domain, SDLCPhase, ProductCategory

    atoms = [
        KnowledgeAtom(
            id="KA-001", type=AtomType.TOOL,
            content="Tree-sitter AST parsing",
            evidence_strength=EvidenceStrength.STRONG,
            sources=["f.md"], domains=["D5"], sdlc_phases=["P1"], products=["PC2"],
        ),
        KnowledgeAtom(
            id="KA-099", type=AtomType.METRIC,
            content="Orphan atom with no references anywhere",
            evidence_strength=EvidenceStrength.WEAK,
            sources=["f.md"], domains=["D1"], sdlc_phases=["P1"], products=["PC1"],
        ),
    ]
    domain_specs = [
        DomainSpec(domain=Domain.D5, name="Code Intelligence", atom_ids=["KA-001"]),
    ]
    phase_specs = [
        PhaseSpec(phase=SDLCPhase.P1, name="Discovery", atom_ids=["KA-001"]),
    ]
    product_specs = [
        ProductSpec(category=ProductCategory.PC2, instance_name="test_skill", atom_ids=["KA-001"]),
    ]
    report = validate(atoms, domain_specs, phase_specs, product_specs)
    check("orphan KA-099 detected", "KA-099" in report.orphan_atoms, f"got {report.orphan_atoms}")
    check("KA-001 not orphan", "KA-001" not in report.orphan_atoms)


def test_validator_cross_refs() -> None:
    print("\n=== Validator Tests (Cross-Reference Issues) ===")
    from distillation.validator import validate
    from distillation.models import DomainSpec, PhaseSpec, ProductSpec, KnowledgeAtom
    from distillation.constants import AtomType, EvidenceStrength, Domain, SDLCPhase, ProductCategory

    atoms = _make_tagged_atoms()
    domain_specs = [DomainSpec(domain=Domain.D5, name="Code Intelligence", atom_ids=[a.id for a in atoms])]
    phase_specs = [PhaseSpec(phase=SDLCPhase.P1, name="Discovery", atom_ids=[a.id for a in atoms])]
    product_specs = [
        ProductSpec(
            category=ProductCategory.PC1,
            instance_name="test_mode",
            atom_ids=[a.id for a in atoms],
            yaml_spec={
                "skills_available": [{"nonexistent_skill": "test"}],
                "context_strategy": "nonexistent_strategy",
            },
        ),
    ]
    report = validate(atoms, domain_specs, phase_specs, product_specs)
    check("cross_ref_issues is list", isinstance(report.cross_ref_issues, list))


# ── Gap Report tests ───────────────────────────────────────────────

def test_gap_report_sections() -> None:
    print("\n=== Gap Report Tests (Section Structure) ===")
    import shutil
    import tempfile
    from distillation.gap_report import generate_gap_report
    from distillation.prong2_domains import generate_domain_specs
    from distillation.prong3_phases import generate_phase_specs
    from distillation.prong4_products import generate_product_specs

    atoms = _make_tagged_atoms()
    tmp = Path(tempfile.mkdtemp())
    try:
        domain_specs = generate_domain_specs(atoms, tmp)
        phase_specs = generate_phase_specs(atoms, tmp)
        product_specs = generate_product_specs(atoms, tmp)
        report_text = generate_gap_report(atoms, domain_specs, phase_specs, product_specs)

        check("report is string", isinstance(report_text, str))
        check("report non-empty", len(report_text) > 0)
        check("has STRONG BACKING section", "STRONG BACKING" in report_text)
        check("has ADEQUATE BACKING section", "ADEQUATE BACKING" in report_text)
        check("has WEAK/NO BACKING section", "WEAK/NO BACKING" in report_text)
        check("has ORPHAN RESEARCH section", "ORPHAN RESEARCH" in report_text)
        check("has CONTRADICTIONS section", "CONTRADICTIONS" in report_text)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_gap_report_orphans() -> None:
    print("\n=== Gap Report Tests (Orphan Listing) ===")
    from distillation.gap_report import generate_gap_report
    from distillation.models import DomainSpec, KnowledgeAtom, PhaseSpec, ProductSpec
    from distillation.constants import AtomType, EvidenceStrength, Domain, SDLCPhase, ProductCategory

    atoms = [
        KnowledgeAtom(
            id="KA-001", type=AtomType.TOOL,
            content="Referenced atom",
            evidence_strength=EvidenceStrength.STRONG,
            sources=["f.md"], domains=["D5"], sdlc_phases=["P1"], products=["PC2"],
        ),
        KnowledgeAtom(
            id="KA-099", type=AtomType.METRIC,
            content="Orphan with no refs in any spec",
            evidence_strength=EvidenceStrength.WEAK,
            sources=["f.md"], domains=["D1"], sdlc_phases=["P1"], products=["PC1"],
        ),
    ]
    domain_specs = [DomainSpec(domain=Domain.D5, name="D5", atom_ids=["KA-001"])]
    phase_specs = [PhaseSpec(phase=SDLCPhase.P1, name="P1", atom_ids=["KA-001"])]
    product_specs = [ProductSpec(category=ProductCategory.PC2, instance_name="s", atom_ids=["KA-001"])]

    report_text = generate_gap_report(atoms, domain_specs, phase_specs, product_specs)
    check("orphan KA-099 in gap report", "KA-099" in report_text)
    check("KA-001 not in orphan section", "KA-001" not in report_text.split("ORPHAN RESEARCH")[1].split("##")[0] if "ORPHAN RESEARCH" in report_text else False)


# ── End-to-End tests ───────────────────────────────────────────────

def test_e2e_dry_run() -> None:
    print("\n=== E2E Tests (Dry Run) ===")
    import subprocess
    result = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "distill.py"), "--dry-run"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        cwd=str(PROJECT_ROOT),
    )
    check("dry-run exit code 0", result.returncode == 0, f"exit={result.returncode}, stderr={result.stderr[:200]}")
    check("dry-run shows summary", "Dry Run Summary" in result.stdout, f"stdout[:200]={result.stdout[:200]}")
    check("dry-run shows file count", "Files scanned" in result.stdout)
    check("dry-run shows atom count", "Final atoms" in result.stdout)


def test_e2e_full_pipeline() -> None:
    print("\n=== E2E Tests (Full Pipeline) ===")
    import shutil
    import subprocess
    import tempfile

    tmp = Path(tempfile.mkdtemp())
    try:
        result = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "distill.py"), "--output-dir", str(tmp), "--verbose"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            cwd=str(PROJECT_ROOT),
        )
        check("full pipeline exit code 0", result.returncode == 0, f"exit={result.returncode}, stderr={result.stderr[:300]}")

        registry = tmp / "registry" / "knowledge_atoms.json"
        check("registry JSON exists", registry.exists())
        if registry.exists():
            import json
            data = json.loads(registry.read_text(encoding="utf-8"))
            check("registry is non-empty list", isinstance(data, list) and len(data) > 0, f"got {type(data)} len={len(data) if isinstance(data, list) else 'N/A'}")

        domains_dir = tmp / "domains"
        check("domains dir exists", domains_dir.is_dir())
        domain_files = list(domains_dir.glob("*.md")) if domains_dir.is_dir() else []
        check("12 domain files", len(domain_files) == 12, f"got {len(domain_files)}")

        phases_dir = tmp / "phases"
        check("phases dir exists", phases_dir.is_dir())
        phase_files = list(phases_dir.glob("*.md")) if phases_dir.is_dir() else []
        check("8 phase files", len(phase_files) == 8, f"got {len(phase_files)}")

        products_dir = tmp / "products"
        check("products dir exists", products_dir.is_dir())
        yaml_files = list(products_dir.rglob("*.yaml")) if products_dir.is_dir() else []
        check("at least 1 product yaml", len(yaml_files) >= 1, f"got {len(yaml_files)}")

        reports_dir = tmp / "reports"
        check("reports dir exists", reports_dir.is_dir())
        val_report = reports_dir / "validation_report.md"
        check("validation_report.md exists", val_report.exists())
        if val_report.exists():
            check("validation report non-empty", val_report.stat().st_size > 0)
        gap_report = reports_dir / "gap_report.md"
        check("gap_report.md exists", gap_report.exists())
        if gap_report.exists():
            check("gap report non-empty", gap_report.stat().st_size > 0)

        for f in domain_files + phase_files:
            check(f"{f.name} non-empty", f.stat().st_size > 0)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


SCRIPT_DIR = Path(__file__).resolve().parent


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
    test_dedup_exact_duplicates()
    test_dedup_whitespace_normalization()
    test_dedup_citation_normalization()
    test_dedup_distinct_preserved()
    test_dedup_content_hash_set()
    test_ranker_evidence_ordering()
    test_ranker_assigns_ids()
    test_ranker_groups_by_type()
    test_ranker_specificity_tiebreak()
    test_tagger_domain_assignment()
    test_tagger_phase_assignment()
    test_tagger_product_assignment()
    test_tagger_multi_domain()
    test_tagger_fallback_assignment()
    test_tagger_all_atoms_tagged()
    test_tagger_raw_section_fallback()
    test_prong2_generates_12_files()
    test_prong2_atom_id_references()
    test_prong2_domain_content()
    test_prong2_empty_domain_gaps()
    test_prong2_evidence_ranking()
    test_prong3_generates_8_files()
    test_prong3_atom_id_references()
    test_prong3_content_structure()
    test_prong3_spec_fields()
    test_prong3_empty_phase_handling()
    test_prong4_generates_yaml_files()
    test_prong4_valid_yaml_syntax()
    test_prong4_template_structure()
    test_prong4_confidence_levels()
    test_prong4_gaps_tracked()
    test_prong4_atom_id_coverage()
    test_validator_basic()
    test_validator_orphans()
    test_validator_cross_refs()
    test_gap_report_sections()
    test_gap_report_orphans()
    test_e2e_dry_run()
    test_e2e_full_pipeline()

    print(f"\n{'=' * 40}")
    print(f"Results: {PASS} passed, {FAIL} failed")
    if FAIL:
        sys.exit(1)
    print("All checks passed.")
