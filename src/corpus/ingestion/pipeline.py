from __future__ import annotations

import json
import logging
import re
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository
from corpus.ingestion.classifier import classify
from corpus.ingestion.enumerator import enumerate_changes
from corpus.ingestion.normalizer import normalize
from corpus.ingestion.path_mapper import record_mapping

logger = logging.getLogger(__name__)


@dataclass
class IngestResult:
    run_id: str = ""
    artifacts_ingested: int = 0
    chunks_created: int = 0
    unclassified_files: list[str] = field(default_factory=list)
    failed: bool = False


def run_ingest(
    repo: CorpusRepository,
    repo_path: str,
    source_branch: str,
    base_branch: str = "main",
    corpus_root: str | None = None,
) -> IngestResult:
    run_id = f"cr_{uuid.uuid4().hex[:12]}"
    now = datetime.now(timezone.utc).isoformat()

    repo.create_run(
        run_id=run_id,
        source_branch=source_branch,
        started_at=now,
        status="running",
    )

    changes = enumerate_changes(repo_path, source_branch, base_branch)

    if corpus_root is None:
        corpus_root = repo_path

    unclassified: list[str] = []
    artifacts_ingested = 0
    chunks_created = 0

    for change in changes:
        if change.change_type == "deleted":
            continue

        classification = classify(change.path)

        if not classification.is_classified:
            unclassified.append(change.path)
            continue

        content_str = ""
        if change.content is not None:
            content_str = change.content.decode("utf-8", errors="replace")

        domain = classification.domain_tags[0] if classification.domain_tags else "unknown"
        canonical_path = str(Path(corpus_root) / change.path)
        normalized = normalize(content_str, domain, canonical_path)

        if change.path != canonical_path:
            record_mapping(repo, change.path, canonical_path, run_id)

        artifact_id = f"ra_{uuid.uuid4().hex[:12]}"
        repo.create_artifact(
            artifact_id=artifact_id,
            title=normalized.title or Path(change.path).stem,
            content=content_str,
            domain_tags=json.dumps(classification.domain_tags),
            capability_tags=json.dumps(classification.capability_tags),
            source_branch=source_branch,
            source_path=change.path,
            captured_at=now,
            run_id=run_id,
            status="active",
        )
        artifacts_ingested += 1

        for idx, chunk_content in enumerate(normalized.chunks):
            chunk_id = f"ac_{uuid.uuid4().hex[:12]}"
            repo.create_chunk(
                chunk_id=chunk_id,
                artifact_id=artifact_id,
                chunk_index=idx,
                content=chunk_content,
            )
            chunks_created += 1

    # Unclassified files are skipped (not a hard failure).
    # The caller can inspect unclassified_files for reporting.

    run = repo.get_run(run_id)
    if run is not None:
        run.artifacts_ingested = artifacts_ingested  # type: ignore[assignment]
        repo.session.flush()

    return IngestResult(
        run_id=run_id,
        artifacts_ingested=artifacts_ingested,
        chunks_created=chunks_created,
        unclassified_files=unclassified,
    )


# ---------------------------------------------------------------------------
# Single-file ingestion (no git required)
# ---------------------------------------------------------------------------

_PARAGRAPH_SPLIT = re.compile(r"\n\s*\n")
_CHUNK_MAX = 2000


def _chunk_plain_text(content: str) -> list[str]:
    """Split plain text into chunks by paragraph or by size (~2000 chars)."""
    paragraphs = _PARAGRAPH_SPLIT.split(content)
    chunks: list[str] = []
    buf = ""
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if buf and len(buf) + len(para) + 2 > _CHUNK_MAX:
            chunks.append(buf)
            buf = para
        else:
            buf = f"{buf}\n\n{para}" if buf else para
    if buf:
        chunks.append(buf)
    return chunks if chunks else [content]


def ingest_file(
    file_path: Path,
    content: str,
    title: str,
    metadata: dict,
    session: Session,
    run_id: str,
    corpus_root: Path | None = None,
) -> None:
    """Ingest a single file into the corpus without requiring git.

    Classifies the content, normalizes it, chunks it, and stores
    artifacts and chunks in the database.

    Parameters
    ----------
    file_path:
        Path to the source file.
    content:
        Pre-parsed text content.
    title:
        Pre-extracted title.
    metadata:
        Arbitrary metadata from the parser.
    session:
        Active SQLAlchemy session.
    run_id:
        Consolidation run ID to associate the artifact with.
    corpus_root:
        Optional root directory for canonical path computation.
    """
    repo = CorpusRepository(session)
    file_path = Path(file_path)
    str_path = str(file_path)
    now = datetime.now(timezone.utc).isoformat()

    # 1. Classify
    classification = classify(str_path)
    domain = classification.domain_tags[0] if classification.domain_tags else "unknown"
    if not classification.is_classified:
        logger.info("File %s not classified by path — using domain='unknown'", str_path)

    # 2. Determine chunks
    is_markdown = file_path.suffix.lower() in {".md", ".markdown"}
    if is_markdown:
        canonical_path = str(Path(corpus_root) / file_path.name) if corpus_root else str_path
        normalized = normalize(content, domain, canonical_path)
        chunks = normalized.chunks
        title = normalized.title or title
    else:
        chunks = _chunk_plain_text(content)

    if not chunks:
        chunks = [content]

    # 3. Create artifact
    artifact_id = f"ra_{uuid.uuid4().hex[:12]}"
    repo.create_artifact(
        artifact_id=artifact_id,
        title=title or file_path.stem,
        content=content,
        domain_tags=json.dumps(classification.domain_tags),
        capability_tags=json.dumps(classification.capability_tags),
        source_branch="watch",
        source_path=str_path,
        captured_at=now,
        run_id=run_id,
        status="active",
    )
    logger.info("Created artifact %s for %s", artifact_id, str_path)

    # 4. Create chunks
    for idx, chunk_content in enumerate(chunks):
        chunk_id = f"ac_{uuid.uuid4().hex[:12]}"
        repo.create_chunk(
            chunk_id=chunk_id,
            artifact_id=artifact_id,
            chunk_index=idx,
            content=chunk_content,
        )
    logger.info("Created %d chunks for artifact %s", len(chunks), artifact_id)

    # 5. Record path mapping
    canonical = str(Path(corpus_root) / file_path.name) if corpus_root else str_path
    if str_path != canonical:
        record_mapping(repo, str_path, canonical, run_id)
