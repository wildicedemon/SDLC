"""Research file ingestion and processing engine."""

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional, Union

import markdown
import yaml
from bs4 import BeautifulSoup

from ..models.research import ResearchFile


@dataclass
class ContentChunk:
    """Represents a chunk of content with metadata."""

    content: str
    start_line: int
    end_line: int
    metadata: dict[str, Any]


class ResearchIngestor:
    """Engine for ingesting and processing research files in multiple formats."""

    # Maximum content size before chunking (in characters)
    MAX_CHUNK_SIZE = 50_000
    CHUNK_OVERLAP = 1_000

    def __init__(self) -> None:
        """Initialize the ingestor with format parsers."""
        self.format_parsers = {
            'md': self._parse_markdown,
            'markdown': self._parse_markdown,
            'html': self._parse_html,
            'htm': self._parse_html,
            'json': self._parse_json,
            'csv': self._parse_csv,
            'txt': self._parse_text,
            'yaml': self._parse_yaml,
            'yml': self._parse_yaml,
        }

    def ingest_file(self, file_path: Union[str, Path]) -> ResearchFile:
        """Ingest a research file and return a processed ResearchFile object.

        Args:
            file_path: Path to the research file

        Returns:
            Processed ResearchFile with content and metadata

        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file format is unsupported
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"Research file not found: {file_path}")

        # Determine format from extension
        format_type = self._detect_format(file_path)

        if format_type not in self.format_parsers:
            raise ValueError(f"Unsupported file format: {format_type}")

        # Read raw content
        raw_content = self._read_file_content(file_path)

        # Parse content based on format
        parsed_content = self.format_parsers[format_type](raw_content, file_path)

        # Extract metadata
        metadata = self._extract_metadata(parsed_content, file_path)

        # Calculate checksum for change detection
        checksum = self._calculate_checksum(raw_content)

        # Handle large content with chunking if needed
        if len(parsed_content) > self.MAX_CHUNK_SIZE:
            chunks = self._chunk_content(parsed_content)
            metadata['chunks'] = [chunk.__dict__ for chunk in chunks]

        return ResearchFile(
            path=file_path,
            content=parsed_content,
            format=format_type,
            metadata=metadata,
            checksum=checksum
        )

    def _detect_format(self, file_path: Path) -> str:
        """Detect file format from extension."""
        extension = file_path.suffix.lower().lstrip('.')
        if not extension:
            # Try to detect from filename patterns
            if 'markdown' in file_path.name.lower():
                return 'markdown'
            return 'txt'
        return extension

    def _read_file_content(self, file_path: Path) -> str:
        """Read file content with encoding detection."""
        try:
            # Try UTF-8 first
            with open(file_path, encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Fall back to latin-1 for files with unknown encoding
            with open(file_path, encoding='latin-1') as f:
                return f.read()

    def _parse_markdown(self, content: str, file_path: Path) -> str:
        """Parse Markdown content to HTML, then extract text."""
        # Convert markdown to HTML
        html_content = markdown.markdown(content, extensions=['extra', 'codehilite'])

        # Extract text from HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove code blocks and pre tags to preserve formatting
        for tag in soup.find_all(['code', 'pre']):
            tag.string = f"\n```\n{tag.get_text()}\n```\n"

        return soup.get_text()

    def _parse_html(self, content: str, file_path: Path) -> str:
        """Parse HTML content and extract clean text."""
        soup = BeautifulSoup(content, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Extract text
        text = soup.get_text()

        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        return ' '.join(chunk for chunk in chunks if chunk)

    def _parse_json(self, content: str, file_path: Path) -> str:
        """Parse JSON content and convert to readable text."""
        try:
            data = json.loads(content)
            # Store structured data for metadata extraction
            if not hasattr(self, '_temp_structured_data'):
                self._temp_structured_data = {}
            self._temp_structured_data[file_path] = data
            return self._json_to_text(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {file_path}: {e}") from e

    def _parse_csv(self, content: str, file_path: Path) -> str:
        """Parse CSV content and convert to readable text."""
        import csv
        import io

        lines = content.splitlines()
        if not lines:
            return ""

        # Try to detect delimiter
        sample = lines[0] if len(lines) > 0 else ""
        delimiter = self._detect_csv_delimiter(sample)

        try:
            reader = csv.DictReader(io.StringIO(content), delimiter=delimiter)
            rows = list(reader)

            if not rows:
                return content  # Return raw content if parsing fails

            # Store structured data for metadata extraction
            if not hasattr(self, '_temp_structured_data'):
                self._temp_structured_data = {}
            self._temp_structured_data[file_path] = rows

            # Convert to readable text format
            headers = list(rows[0].keys())
            text_parts = [f"Headers: {', '.join(headers)}"]

            for i, row in enumerate(rows[:10]):  # Limit to first 10 rows for readability
                values = [str(row.get(h, '')) for h in headers]
                text_parts.append(f"Row {i+1}: {', '.join(values)}")

            if len(rows) > 10:
                text_parts.append(f"... and {len(rows) - 10} more rows")

            return '\n'.join(text_parts)

        except Exception:
            # Fall back to raw content if CSV parsing fails
            return content

    def _parse_text(self, content: str, file_path: Path) -> str:
        """Parse plain text content."""
        return content.strip()

    def _parse_yaml(self, content: str, file_path: Path) -> str:
        """Parse YAML content and convert to readable text."""
        try:
            data = yaml.safe_load(content)
            # Store structured data for metadata extraction
            if not hasattr(self, '_temp_structured_data'):
                self._temp_structured_data = {}
            self._temp_structured_data[file_path] = data
            return self._json_to_text(data)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in {file_path}: {e}") from e

    def _json_to_text(self, data: Any, prefix: str = "") -> str:
        """Convert JSON/YAML data structure to readable text."""
        if isinstance(data, dict):
            parts = []
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    parts.append(f"{prefix}{key}:")
                    parts.append(self._json_to_text(value, prefix + "  "))
                else:
                    parts.append(f"{prefix}{key}: {value}")
            return '\n'.join(parts)
        elif isinstance(data, list):
            parts = []
            for i, item in enumerate(data):
                if isinstance(item, (dict, list)):
                    parts.append(f"{prefix}[{i}]:")
                    parts.append(self._json_to_text(item, prefix + "  "))
                else:
                    parts.append(f"{prefix}[{i}]: {item}")
            return '\n'.join(parts)
        else:
            return str(data)

    def _detect_csv_delimiter(self, sample: str) -> str:
        """Detect CSV delimiter from a sample line."""
        delimiters = [',', '\t', ';', '|']
        counts = {}

        for delimiter in delimiters:
            counts[delimiter] = sample.count(delimiter)

        # Return delimiter with highest count, default to comma
        return max(counts.items(), key=lambda x: x[1])[0] if counts else ','

    def _extract_metadata(self, content: str, file_path: Path) -> dict[str, Any]:
        """Extract metadata from content and file path."""
        metadata = {
            'filename': file_path.name,
            'file_size': len(content),
            'word_count': len(content.split()),
            'line_count': len(content.splitlines()),
        }

        # Check for structured data first (JSON/YAML/CSV)
        structured_data = getattr(self, '_temp_structured_data', {}).get(file_path)
        if structured_data:
            # Extract from structured data
            metadata.update(self._extract_metadata_from_structured(structured_data))
            # Clean up temp data
            if hasattr(self, '_temp_structured_data'):
                del self._temp_structured_data[file_path]
        else:
            # Extract from text content
            # Extract title from first line or heading
            title = self._extract_title(content)
            if title:
                metadata['title'] = title

            # Extract author information
            authors = self._extract_authors(content)
            if authors:
                metadata['authors'] = authors

            # Extract date information
            date = self._extract_date(content)
            if date:
                metadata['date'] = date

            # Extract citations/references
            citations = self._extract_citations(content)
            if citations:
                metadata['citations'] = citations

            # Extract abstract/summary if present
            abstract = self._extract_abstract(content)
            if abstract:
                metadata['abstract'] = abstract

        return metadata

    def _extract_metadata_from_structured(self, data: Any) -> dict[str, Any]:
        """Extract metadata from structured data (JSON/YAML/CSV)."""
        metadata = {}

        if isinstance(data, dict):
            # JSON/YAML object
            # Look for common metadata fields
            if 'title' in data:
                metadata['title'] = str(data['title'])
            if 'authors' in data:
                authors = data['authors']
                if isinstance(authors, list):
                    metadata['authors'] = [str(a) for a in authors]
                elif isinstance(authors, str):
                    metadata['authors'] = [a.strip() for a in authors.split(',')]
            if 'date' in data:
                metadata['date'] = str(data['date'])
            if 'abstract' in data:
                metadata['abstract'] = str(data['abstract'])
            if 'citations' in data:
                citations = data['citations']
                if isinstance(citations, list):
                    metadata['citations'] = [str(c) for c in citations]
                elif isinstance(citations, str):
                    metadata['citations'] = [c.strip() for c in citations.split(',')]

        elif isinstance(data, list) and data:
            # CSV rows - extract from first row or look for common patterns
            first_row = data[0]
            if isinstance(first_row, dict):
                # Try to find title in various columns
                for col in ['title', 'Title', 'TITLE']:
                    if col in first_row and first_row[col]:
                        metadata['title'] = str(first_row[col])
                        break

                # Try to find authors
                for col in ['authors', 'Authors', 'AUTHORS', 'author', 'Author', 'AUTHOR']:
                    if col in first_row and first_row[col]:
                        authors_text = str(first_row[col])
                        metadata['authors'] = [a.strip() for a in authors_text.split(',')]
                        break

                # Try to find date
                for col in ['date', 'Date', 'DATE', 'published', 'Published', 'PUBLISHED']:
                    if col in first_row and first_row[col]:
                        metadata['date'] = str(first_row[col])
                        break

        return metadata

    def _extract_title(self, content: str) -> Optional[str]:
        """Extract title from content."""
        lines = content.splitlines()

        # Look for markdown headers first
        for line in lines[:10]:  # Check first 10 lines
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
            elif line.startswith('## '):
                return line[3:].strip()

        # Look for title-like patterns
        for line in lines[:5]:
            line = line.strip()
            if len(line) > 10 and len(line) < 100 and not line.endswith('.'):
                # Likely a title if it's a substantial line without ending punctuation
                return line

        return None

    def _extract_authors(self, content: str) -> Optional[list[str]]:
        """Extract author information from content."""
        # Look for common author patterns
        author_patterns = [
            r'Authors?:?\s*([^\n]+)',
            r'By:?\s*([^\n]+)',
            r'Author:?\s*([^\n]+)',
            r'@author:?\s*([^\n]+)',
        ]

        for pattern in author_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                authors_text = match.group(1).strip()
                # Split by common separators
                authors = re.split(r'[,&;]', authors_text)
                return [author.strip() for author in authors if author.strip()]

        return None

    def _extract_date(self, content: str) -> Optional[str]:
        """Extract date information from content."""
        # Look for date patterns - be more specific
        date_patterns = [
            r'Date:?\s*(\d{4}-\d{2}-\d{2})',  # Date: 2024-01-15
            r'Published:?\s*(\d{4}-\d{2}-\d{2})',  # Published: 2024-01-15
            r'Date:?\s*(\d{2}/\d{2}/\d{4})',  # Date: 01/15/2024
            r'Published:?\s*(\d{2}/\d{2}/\d{4})',  # Published: 01/15/2024
            r'Date:?\s*(\d{2}-\d{2}-\d{4})',  # Date: 01-15-2024
            r'Published:?\s*(\d{2}-\d{2}-\d{4})',  # Published: 01-15-2024
            r'(\d{4}-\d{2}-\d{2})',  # Just ISO date on its own line
        ]

        for pattern in date_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                date_str = match.group(1).strip()
                # Validate it's a reasonable date
                if self._is_valid_date(date_str):
                    return date_str

        return None

    def _is_valid_date(self, date_str: str) -> bool:
        """Check if a date string looks valid."""
        # Basic validation for common formats
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):  # YYYY-MM-DD
            year, month, day = map(int, date_str.split('-'))
            return 1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31
        elif re.match(r'^\d{2}/\d{2}/\d{4}$', date_str):  # MM/DD/YYYY
            month, day, year = map(int, date_str.replace('/', '-').split('-'))
            return 1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31
        elif re.match(r'^\d{2}-\d{2}-\d{4}$', date_str):  # MM-DD-YYYY
            month, day, year = map(int, date_str.split('-'))
            return 1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31
        return False

    def _extract_citations(self, content: str) -> Optional[list[str]]:
        """Extract citations and references."""
        citations = []

        # Look for citation patterns - be more specific
        citation_patterns = [
            r'\[(\d+)\]',  # [1], [2], etc. - numbered references
            r'\[([A-Za-z][^]]*(?:et al\.?|&\s*[A-Za-z][^]]*|\d{4})[^]]*)\]',  # [Smith et al. 2023], [Johnson 2024]
            r'\(([A-Za-z][^)]*(?:et al\.?|&\s*[A-Za-z][^)]*|\d{4})[^)]*)\)',  # (Smith et al., 2023)
        ]

        for pattern in citation_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            citations.extend(matches)

        # Remove duplicates and filter
        citations = list(set(citations))
        # Filter out likely non-citation matches (too short, but allow numbered citations)
        citations = [c for c in citations if len(c) > 2 or c.isdigit()]

        return citations if citations else None

    def _extract_abstract(self, content: str) -> Optional[str]:
        """Extract abstract or summary."""
        # Look for abstract section
        abstract_patterns = [
            r'Abstract:?\s*([^\n]+(?:\n(?!\n)[^\n]*)*)',
            r'Summary:?\s*([^\n]+(?:\n(?!\n)[^\n]*)*)',
            r'Overview:?\s*([^\n]+(?:\n(?!\n)[^\n]*)*)',
        ]

        for pattern in abstract_patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
            if match:
                abstract = match.group(1).strip()
                # Limit to reasonable length
                if len(abstract) < 1000:
                    return abstract

        return None

    def _calculate_checksum(self, content: str) -> str:
        """Calculate SHA256 checksum of content."""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def _chunk_content(self, content: str) -> list[ContentChunk]:
        """Chunk large content into manageable pieces."""
        if len(content) <= self.MAX_CHUNK_SIZE:
            return []

        chunks = []
        start_pos = 0

        while start_pos < len(content):
            # Calculate end position for this chunk
            end_pos = min(start_pos + self.MAX_CHUNK_SIZE, len(content))

            # Try to break at a reasonable boundary (sentence, paragraph, etc.)
            if end_pos < len(content):
                # Look for sentence endings within the last 500 characters
                search_start = max(start_pos, end_pos - 500)
                sentence_end = content.rfind('. ', search_start, end_pos)
                if sentence_end > start_pos:
                    end_pos = sentence_end + 1
                else:
                    # Look for paragraph breaks
                    para_end = content.rfind('\n\n', search_start, end_pos)
                    if para_end > start_pos:
                        end_pos = para_end + 2
                    else:
                        # Look for line breaks
                        line_end = content.rfind('\n', search_start, end_pos)
                        if line_end > start_pos:
                            end_pos = line_end + 1

            # Extract chunk content
            chunk_content = content[start_pos:end_pos]

            # Calculate line numbers (approximate)
            lines_before = content[:start_pos].count('\n')
            lines_in_chunk = chunk_content.count('\n')
            start_line = lines_before
            end_line = lines_before + lines_in_chunk

            chunks.append(ContentChunk(
                content=chunk_content,
                start_line=start_line,
                end_line=end_line,
                metadata={'chunk_size': len(chunk_content)}
            ))

            # Move start position with overlap, but ensure progress
            next_start = end_pos - self.CHUNK_OVERLAP
            if next_start <= start_pos:
                # No progress made, force advance
                start_pos = end_pos
            else:
                start_pos = next_start

            if start_pos >= len(content):
                break

        return chunks

