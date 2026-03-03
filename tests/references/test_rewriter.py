from pathlib import Path

from corpus.references.rewrite_mapper import RewriteEntry
from corpus.references.rewriter import rewrite_references


class TestRewriter:
    def test_rewrites_link(self, tmp_path: Path) -> None:
        research = tmp_path / "docs" / "research"
        research.mkdir(parents=True)
        md = research / "test.md"
        md.write_text("See [guide](old/path.md) for details.", encoding="utf-8")

        rmap = [RewriteEntry(old_path="old/path.md", new_path="new/path.md")]
        count = rewrite_references(rmap, str(tmp_path))

        assert count == 1
        assert "[guide](new/path.md)" in md.read_text(encoding="utf-8")

    def test_no_matching_links_unchanged(self, tmp_path: Path) -> None:
        research = tmp_path / "docs" / "research"
        research.mkdir(parents=True)
        md = research / "test.md"
        original = "See [guide](other/path.md) for details."
        md.write_text(original, encoding="utf-8")

        rmap = [RewriteEntry(old_path="old/path.md", new_path="new/path.md")]
        count = rewrite_references(rmap, str(tmp_path))

        assert count == 0
        assert md.read_text(encoding="utf-8") == original

    def test_multiple_links_in_same_file(self, tmp_path: Path) -> None:
        research = tmp_path / "docs" / "research"
        research.mkdir(parents=True)
        md = research / "test.md"
        md.write_text(
            "See [a](old/path.md) and [b](old/path.md).",
            encoding="utf-8",
        )

        rmap = [RewriteEntry(old_path="old/path.md", new_path="new/path.md")]
        count = rewrite_references(rmap, str(tmp_path))

        assert count == 2
        content = md.read_text(encoding="utf-8")
        assert content.count("new/path.md") == 2
