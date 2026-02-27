"""Integration tests for research file ingestion."""

import pytest
import tempfile
import json
import csv
from pathlib import Path
from typing import Dict, Any

from distillation.processors.ingestion import ResearchIngestor
from distillation.models.research import ResearchFile


class TestResearchIngestor:
    """Test the ResearchIngestor class."""

    @pytest.fixture
    def ingestor(self):
        """Create a ResearchIngestor instance."""
        return ResearchIngestor()

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    def test_ingest_markdown_file(self, ingestor, temp_dir):
        """Test ingesting a Markdown file."""
        md_content = """# Test Research Paper

## Abstract

This is a test abstract for our research on AI agents.

## Introduction

Authors: John Doe, Jane Smith
Date: 2024-01-15

This paper explores autonomous coding systems.

## Methods

We used various techniques including:
- Tree-sitter for AST parsing
- Vector databases for retrieval

## Results

Our findings show that AST-based search improves precision by 60-80%.

## References

[1] Smith et al. (2023). Code Understanding Techniques.
[2] Johnson (2024). AI Agent Architectures.
"""

        md_file = temp_dir / "test_paper.md"
        md_file.write_text(md_content)

        result = ingestor.ingest_file(md_file)

        assert isinstance(result, ResearchFile)
        assert result.path == md_file
        assert result.format == "md"
        assert "Test Research Paper" in result.content
        assert result.metadata["title"] == "Test Research Paper"
        assert "John Doe" in result.metadata.get("authors", [])
        assert result.metadata.get("date") == "2024-01-15"
        assert len(result.metadata.get("citations", [])) > 0
        assert result.checksum is not None

    def test_ingest_html_file(self, ingestor, temp_dir):
        """Test ingesting an HTML file."""
        html_content = """<!DOCTYPE html>
<html>
<head>
    <title>AI Research Paper</title>
</head>
<body>
    <h1>AI Research Paper</h1>
    <p>Authors: Alice Johnson, Bob Wilson</p>
    <p>Date: 2024-02-20</p>

    <h2>Abstract</h2>
    <p>This paper discusses machine learning applications.</p>

    <h2>Methods</h2>
    <p>We implemented several algorithms including neural networks.</p>

    <script>console.log("This should be removed");</script>
</body>
</html>"""

        html_file = temp_dir / "test_paper.html"
        html_file.write_text(html_content)

        result = ingestor.ingest_file(html_file)

        assert isinstance(result, ResearchFile)
        assert result.format == "html"
        assert "AI Research Paper" in result.content
        assert "Alice Johnson" in result.metadata.get("authors", [])
        assert result.metadata.get("date") == "2024-02-20"
        # Script content should be removed
        assert "console.log" not in result.content

    def test_ingest_json_file(self, ingestor, temp_dir):
        """Test ingesting a JSON file."""
        json_data = {
            "title": "JSON Research Data",
            "authors": ["Dr. Data", "Prof. Structure"],
            "date": "2024-03-10",
            "abstract": "This is JSON research data about data structures.",
            "sections": {
                "introduction": "We explore JSON parsing techniques.",
                "results": "Found that structured parsing improves accuracy by 75%."
            },
            "citations": ["Parser2023", "Data2024"]
        }

        json_file = temp_dir / "test_data.json"
        json_file.write_text(json.dumps(json_data, indent=2))

        result = ingestor.ingest_file(json_file)

        assert isinstance(result, ResearchFile)
        assert result.format == "json"
        assert "JSON Research Data" in result.content
        assert "Dr. Data" in result.metadata.get("authors", [])
        assert result.metadata.get("date") == "2024-03-10"
        assert "Parser2023" in result.metadata.get("citations", [])

    def test_ingest_csv_file(self, ingestor, temp_dir):
        """Test ingesting a CSV file."""
        csv_content = """title,authors,date,abstract
"CSV Research Data","Dr. CSV, Prof. Table","2024-04-05","Research on tabular data formats"
"Another Paper","Researcher X","2024-04-06","More findings on data processing"
"""

        csv_file = temp_dir / "test_data.csv"
        csv_file.write_text(csv_content)

        result = ingestor.ingest_file(csv_file)

        assert isinstance(result, ResearchFile)
        assert result.format == "csv"
        assert "CSV Research Data" in result.content
        assert "Headers: title, authors, date, abstract" in result.content
        assert "Dr. CSV" in result.content

    def test_ingest_yaml_file(self, ingestor, temp_dir):
        """Test ingesting a YAML file."""
        yaml_content = """title: "YAML Research Data"
authors:
  - "Dr. YAML"
  - "Prof. Schema"
date: "2024-05-15"
abstract: "Research on configuration formats"
sections:
  intro: "We explore YAML parsing"
  results: "YAML provides clean configuration"
citations:
  - "YAML2023"
  - "Config2024"
"""

        yaml_file = temp_dir / "test_data.yaml"
        yaml_file.write_text(yaml_content)

        result = ingestor.ingest_file(yaml_file)

        assert isinstance(result, ResearchFile)
        assert result.format == "yaml"
        assert "YAML Research Data" in result.content
        assert "Dr. YAML" in result.metadata.get("authors", [])
        assert result.metadata.get("date") == "2024-05-15"

    def test_ingest_text_file(self, ingestor, temp_dir):
        """Test ingesting a plain text file."""
        text_content = """Plain Text Research

Authors: Text Author, Simple Writer
Date: 2024-06-01

This is plain text research content.

Abstract: Plain text parsing techniques.

Results: Simple text works well for basic content.
"""

        txt_file = temp_dir / "test_paper.txt"
        txt_file.write_text(text_content)

        result = ingestor.ingest_file(txt_file)

        assert isinstance(result, ResearchFile)
        assert result.format == "txt"
        assert "Plain Text Research" in result.content
        assert "Text Author" in result.metadata.get("authors", [])

    def test_content_chunking(self, ingestor, temp_dir):
        """Test content chunking for large files."""
        # Create content larger than MAX_CHUNK_SIZE (50,000 chars)
        large_content = "This is a test sentence. " * 2500  # ~50KB+ of content

        txt_file = temp_dir / "large_file.txt"
        txt_file.write_text(large_content)

        result = ingestor.ingest_file(txt_file)

        assert isinstance(result, ResearchFile)
        # Should have chunks metadata for large content
        assert "chunks" in result.metadata
        chunks = result.metadata["chunks"]
        assert len(chunks) > 1  # Should be split into multiple chunks

        # Verify chunk structure
        for chunk in chunks:
            assert "content" in chunk
            assert "start_line" in chunk
            assert "end_line" in chunk
            assert "metadata" in chunk

    def test_file_not_found(self, ingestor):
        """Test handling of non-existent files."""
        with pytest.raises(FileNotFoundError):
            ingestor.ingest_file("nonexistent_file.md")

    def test_unsupported_format(self, ingestor, temp_dir):
        """Test handling of unsupported file formats."""
        unsupported_file = temp_dir / "test.xyz"
        unsupported_file.write_text("unsupported content")

        with pytest.raises(ValueError, match="Unsupported file format"):
            ingestor.ingest_file(unsupported_file)

    def test_checksum_calculation(self, ingestor, temp_dir):
        """Test that checksums are calculated correctly."""
        content = "Test content for checksum"
        txt_file = temp_dir / "checksum_test.txt"
        txt_file.write_text(content)

        result1 = ingestor.ingest_file(txt_file)
        result2 = ingestor.ingest_file(txt_file)

        # Same content should produce same checksum
        assert result1.checksum == result2.checksum

        # Different content should produce different checksum
        txt_file.write_text(content + " modified")
        result3 = ingestor.ingest_file(txt_file)
        assert result1.checksum != result3.checksum

    def test_metadata_extraction_comprehensive(self, ingestor, temp_dir):
        """Test comprehensive metadata extraction."""
        comprehensive_content = """# Comprehensive Research Paper

Authors: Dr. Alice Smith, Prof. Bob Johnson, Researcher Charlie Brown
Date: 2024-07-15
Published: 2024-07-20

## Abstract

This comprehensive paper covers multiple aspects of AI research including autonomous agents, context management, and code intelligence.

## Introduction

We explore various techniques for building better AI systems.

## Methods

Our approach combines multiple methodologies:
- Tree-sitter for AST parsing (improves precision 60-80%)
- Vector databases for retrieval-augmented generation
- Confidence-based model routing

## Results

Key findings:
- AST-based search: 75% precision improvement
- Context compression: 20x reduction with <3% quality loss
- Multi-agent orchestration: 40% efficiency gain

## References

[1] Smith et al. (2023). AST-based Code Understanding.
[2] Johnson (2024). Context Management Techniques.
[3] Brown & Davis (2024). Multi-Agent Systems.
"""

        md_file = temp_dir / "comprehensive.md"
        md_file.write_text(comprehensive_content)

        result = ingestor.ingest_file(md_file)

        # Verify all metadata fields
        assert result.metadata["title"] == "Comprehensive Research Paper"
        assert len(result.metadata["authors"]) == 3
        assert "Dr. Alice Smith" in result.metadata["authors"]
        assert result.metadata["date"] == "2024-07-15"
        assert len(result.metadata["citations"]) >= 3
        assert result.metadata["word_count"] > 50
        assert result.metadata["line_count"] > 10

    def test_csv_delimiter_detection(self, ingestor):
        """Test CSV delimiter detection."""
        # Test comma delimiter
        assert ingestor._detect_csv_delimiter("a,b,c,d") == ","

        # Test tab delimiter
        assert ingestor._detect_csv_delimiter("a\tb\tc\td") == "\t"

        # Test semicolon delimiter
        assert ingestor._detect_csv_delimiter("a;b;c;d") == ";"

        # Test pipe delimiter
        assert ingestor._detect_csv_delimiter("a|b|c|d") == "|"