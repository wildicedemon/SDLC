from pathlib import Path

from corpus.ingestion.normalizer import normalize


class TestNormalizeSplitsChunks:
    def test_splits_on_h2_headings(self, tmp_path: Path) -> None:
        content = "# Title\n\nPreamble text.\n\n## Section A\n\nBody A.\n\n## Section B\n\nBody B.\n"
        canonical = str(tmp_path / "out.md")

        result = normalize(content, "test_domain", canonical)

        assert len(result.chunks) == 3
        assert all(c.strip() for c in result.chunks)

    def test_no_headings_single_chunk(self, tmp_path: Path) -> None:
        content = "# Title\n\nJust a plain document with no level-2 headings.\n"
        canonical = str(tmp_path / "out.md")

        result = normalize(content, "test_domain", canonical)

        assert len(result.chunks) == 1
        assert "plain document" in result.chunks[0]

    def test_merge_appends_to_existing(self, tmp_path: Path) -> None:
        canonical = tmp_path / "existing.md"
        canonical.write_text("# Existing\n\nOld content.\n", encoding="utf-8")

        new_content = "## New Section\n\nNew body.\n"
        result = normalize(new_content, "test_domain", str(canonical))

        assert result.merged is True
        written = canonical.read_text(encoding="utf-8")
        assert "Old content." in written
        assert "New body." in written

    def test_chunk_count_matches_heading_count_plus_preamble(self, tmp_path: Path) -> None:
        content = "Preamble.\n\n## H1\n\nA\n\n## H2\n\nB\n\n## H3\n\nC\n"
        canonical = str(tmp_path / "out.md")

        result = normalize(content, "test_domain", canonical)

        assert len(result.chunks) == 4

    def test_title_extracted_from_h1(self, tmp_path: Path) -> None:
        content = "# My Great Title\n\nBody.\n"
        canonical = str(tmp_path / "out.md")

        result = normalize(content, "test_domain", canonical)

        assert result.title == "My Great Title"

    def test_no_h1_title_empty(self, tmp_path: Path) -> None:
        content = "## Only H2\n\nBody.\n"
        canonical = str(tmp_path / "out.md")

        result = normalize(content, "test_domain", canonical)

        assert result.title == ""

    def test_new_file_not_merged(self, tmp_path: Path) -> None:
        content = "# Title\n\nBody.\n"
        canonical = str(tmp_path / "new.md")

        result = normalize(content, "test_domain", canonical)

        assert result.merged is False
        assert Path(canonical).read_text(encoding="utf-8") == content

    def test_creates_parent_directories(self, tmp_path: Path) -> None:
        canonical = str(tmp_path / "deep" / "nested" / "dir" / "file.md")
        content = "# Title\n\nBody.\n"

        normalize(content, "test_domain", canonical)

        assert Path(canonical).exists()

    def test_merge_does_not_overwrite_existing(self, tmp_path: Path) -> None:
        canonical = tmp_path / "existing.md"
        original = "# Original\n\n## Existing Section\n\nOld body.\n"
        canonical.write_text(original, encoding="utf-8")

        result = normalize("## Added\n\nNew.\n", "test_domain", str(canonical))

        written = canonical.read_text(encoding="utf-8")
        assert "Existing Section" in written
        assert "Old body." in written
        assert "Added" in written
        assert result.merged is True
