"""Tests for :mod:`corpus.ingestion.parsers`."""

from __future__ import annotations

import pytest
from pathlib import Path

from corpus.ingestion.parsers import ParsedDocument, parse_file


class TestParseMarkdown:
    """parse_file() with Markdown input."""

    def test_extracts_title_from_heading(self, tmp_path: Path) -> None:
        md = tmp_path / "sample.md"
        md.write_text("# My Document\n\nSome body text.\n", encoding="utf-8")

        doc = parse_file(md)

        assert doc.title == "My Document"
        assert "Some body text." in doc.content
        assert doc.source_format == "markdown"

    def test_fallback_title_to_stem(self, tmp_path: Path) -> None:
        md = tmp_path / "no_heading.md"
        md.write_text("Just plain text, no heading.\n", encoding="utf-8")

        doc = parse_file(md)

        assert doc.title == "no_heading"

    def test_metadata_contains_source(self, tmp_path: Path) -> None:
        md = tmp_path / "meta.md"
        md.write_text("# Title\n", encoding="utf-8")

        doc = parse_file(md)

        assert "source" in doc.metadata


class TestParsePlainText:
    """parse_file() with plain-text files."""

    def test_txt_extension(self, tmp_path: Path) -> None:
        txt = tmp_path / "readme.txt"
        txt.write_text("Hello world\n", encoding="utf-8")

        doc = parse_file(txt)

        assert doc.source_format == "text"
        assert doc.title == "readme"
        assert "Hello world" in doc.content

    def test_csv_extension(self, tmp_path: Path) -> None:
        csv = tmp_path / "data.csv"
        csv.write_text("a,b,c\n1,2,3\n", encoding="utf-8")

        doc = parse_file(csv)

        assert doc.source_format == "text"
        assert "a,b,c" in doc.content

    def test_log_extension(self, tmp_path: Path) -> None:
        log = tmp_path / "app.log"
        log.write_text("2024-01-01 INFO started\n", encoding="utf-8")

        doc = parse_file(log)

        assert doc.source_format == "text"


class TestParseHtml:
    """parse_file() with HTML input."""

    def test_strips_tags_and_extracts_title(self, tmp_path: Path) -> None:
        html = tmp_path / "page.html"
        html.write_text(
            "<html><head><title>Page Title</title></head>"
            "<body><h1>Heading</h1><p>Body text.</p></body></html>",
            encoding="utf-8",
        )

        doc = parse_file(html)

        assert doc.source_format == "html"
        assert doc.title == "Page Title"
        assert "Body text." in doc.content
        # Tags should be stripped
        assert "<p>" not in doc.content

    def test_h1_fallback_when_no_title_tag(self, tmp_path: Path) -> None:
        html = tmp_path / "simple.htm"
        html.write_text(
            "<html><body><h1>Fallback Title</h1><p>Content</p></body></html>",
            encoding="utf-8",
        )

        doc = parse_file(html)

        assert doc.title == "Fallback Title"


class TestParseUnknownExtension:
    """parse_file() with an unrecognised extension."""

    def test_unknown_ext_falls_back_to_text(self, tmp_path: Path) -> None:
        weird = tmp_path / "data.xyz"
        weird.write_text("some content\n", encoding="utf-8")

        doc = parse_file(weird)

        # Should still succeed as text
        assert doc.content == "some content\n"
        assert doc.source_format == "text"


class TestParseMissingFile:
    """parse_file() with a non-existent path."""

    def test_raises_file_not_found(self, tmp_path: Path) -> None:
        missing = tmp_path / "does_not_exist.md"

        with pytest.raises(FileNotFoundError):
            parse_file(missing)
