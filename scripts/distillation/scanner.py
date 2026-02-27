from __future__ import annotations

from pathlib import Path


def scan_corpus(root: Path) -> dict[str, list[Path]]:
    root = root.resolve()

    perplexity = sorted(root.glob("docs/research/**/perplexityai_research_overview*.md"))

    overviews = sorted(
        p
        for p in root.glob("docs/research/**/overview.md")
        if "_indices" not in p.parts
    )

    indices = sorted(root.glob("docs/research/_indices/*.md"))

    kimi_docs = sorted(
        p
        for p in root.glob("Kimi-Research/docs/research/**/*.md")
        if p.suffix == ".md"
    )

    kimi_csv: list[Path] = []
    for pattern in (
        "Kimi-Research/*.csv",
        "Kimi-Research/research/*.csv",
        "Kimi-Research/docs/research/**/*.csv",
    ):
        kimi_csv.extend(root.glob(pattern))
    kimi_csv = sorted(set(kimi_csv))

    root_files = sorted(
        p
        for p in root.glob("*.md")
        if p.is_file()
    )

    return {
        "perplexity": perplexity,
        "overviews": overviews,
        "indices": indices,
        "kimi_docs": kimi_docs,
        "kimi_csv": kimi_csv,
        "root_files": root_files,
    }
