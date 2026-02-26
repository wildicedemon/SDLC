from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from corpus.db.repository import CorpusRepository
from corpus.ingestion.classifier import classify
from corpus.ingestion.enumerator import ChangedFile, enumerate_changes
from corpus.ingestion.normalizer import normalize
from corpus.ingestion.path_mapper import record_mapping


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

    if unclassified:
        repo.update_run_status(run_id, "failed")
        return IngestResult(
            run_id=run_id,
            artifacts_ingested=artifacts_ingested,
            chunks_created=chunks_created,
            unclassified_files=unclassified,
            failed=True,
        )

    run = repo.get_run(run_id)
    if run is not None:
        run.artifacts_ingested = artifacts_ingested  # type: ignore[assignment]
        repo.session.flush()

    return IngestResult(
        run_id=run_id,
        artifacts_ingested=artifacts_ingested,
        chunks_created=chunks_created,
    )
