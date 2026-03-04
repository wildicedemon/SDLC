#!/usr/bin/env python3
"""Apply actions based on relevance-audit results.

Companion to ``scripts/audit_corpus_relevance.py``.  Reads the audit
JSON produced by that script and takes one of four actions on items
flagged as irrelevant to autonomous AI agents:

* **report** -- print a summary table (default, no mutations).
* **soft-delete** -- mark items as irrelevant in the database.
* **hard-delete** -- remove items from SQLite, ChromaDB, and the graph.
* **export** -- dump flagged items to a backup JSON file.

Usage examples::

    # Preview what would be acted on
    python scripts/apply_relevance_audit.py --action report

    # Soft-delete with higher confidence bar
    python scripts/apply_relevance_audit.py --action soft-delete --confidence-threshold 0.85

    # Export first, then hard-delete
    python scripts/apply_relevance_audit.py --action export
    python scripts/apply_relevance_audit.py --action hard-delete --confirm-delete

    # Dry-run hard-delete to see what would happen
    python scripts/apply_relevance_audit.py --action hard-delete --confirm-delete --dry-run
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Ensure the project root is on sys.path so ``corpus.*`` imports resolve
# when running the script directly from the repo root.
# ---------------------------------------------------------------------------
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT / "src"))

from corpus.config import CorpusSettings, get_settings
from corpus.db.engine import create_db_engine, get_session
from corpus.db.models import ArtifactChunk, DecisionCard, ResearchArtifact

logger = logging.getLogger("apply_relevance_audit")

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

_ITEM_TYPE_ARTIFACT = "artifact"
_ITEM_TYPE_DECISION = "decision"


class FlaggedItem:
    """A single audit result that was flagged as irrelevant."""

    def __init__(
        self,
        item_type: str,
        item_id: str,
        title: str,
        confidence: float,
        reason: str,
        raw: dict[str, Any],
    ) -> None:
        self.item_type = item_type
        self.item_id = item_id
        self.title = title
        self.confidence = confidence
        self.reason = reason
        self.raw = raw

    def __repr__(self) -> str:
        return f"FlaggedItem({self.item_type}, {self.item_id!r}, conf={self.confidence:.2f})"


# ---------------------------------------------------------------------------
# Audit-file loader & filter
# ---------------------------------------------------------------------------


def load_audit(path: Path) -> dict[str, Any]:
    """Read and parse the relevance-audit JSON file.

    Args:
        path: Filesystem path to ``relevance_audit.json``.

    Returns:
        The parsed JSON as a dictionary.

    Raises:
        SystemExit: If the file is missing or unparseable.
    """
    if not path.exists():
        logger.error("Audit file not found: %s", path)
        sys.exit(1)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        logger.error("Failed to parse audit file: %s", exc)
        sys.exit(1)


def filter_flagged(
    audit: dict[str, Any],
    confidence_threshold: float,
) -> list[FlaggedItem]:
    """Return items where ``relevant is False`` and confidence >= threshold.

    Both ``artifact_results`` and ``decision_card_results`` arrays are
    scanned.  Items that had an ``error`` during auditing are skipped.
    """
    flagged: list[FlaggedItem] = []

    for entry in audit.get("artifact_results", []):
        if entry.get("error"):
            continue
        if entry.get("relevant") is False and entry.get("confidence", 0) >= confidence_threshold:
            flagged.append(
                FlaggedItem(
                    item_type=_ITEM_TYPE_ARTIFACT,
                    item_id=entry["artifact_id"],
                    title=entry.get("title", "<untitled>"),
                    confidence=entry["confidence"],
                    reason=entry.get("reason", ""),
                    raw=entry,
                )
            )

    for entry in audit.get("decision_card_results", []):
        if entry.get("error"):
            continue
        if entry.get("relevant") is False and entry.get("confidence", 0) >= confidence_threshold:
            flagged.append(
                FlaggedItem(
                    item_type=_ITEM_TYPE_DECISION,
                    item_id=entry["decision_id"],
                    title=entry.get("question", entry.get("title", "<untitled>")),
                    confidence=entry["confidence"],
                    reason=entry.get("reason", ""),
                    raw=entry,
                )
            )

    return flagged


# ---------------------------------------------------------------------------
# Action: report
# ---------------------------------------------------------------------------


def action_report(flagged: list[FlaggedItem]) -> None:
    """Print a human-readable table of flagged items."""
    if not flagged:
        print("\n[OK] No items flagged as irrelevant at the given confidence threshold.\n")
        return

    artifacts = [f for f in flagged if f.item_type == _ITEM_TYPE_ARTIFACT]
    decisions = [f for f in flagged if f.item_type == _ITEM_TYPE_DECISION]

    print(f"\n{'=' * 90}")
    print(f"  RELEVANCE AUDIT -- FLAGGED ITEMS REPORT")
    print(f"  Artifacts: {len(artifacts)}   Decision cards: {len(decisions)}   Total: {len(flagged)}")
    print(f"{'=' * 90}\n")

    header = f"{'Type':<10} {'ID':<40} {'Conf':>5}  {'Title / Reason'}"
    print(header)
    print("-" * len(header) + "-" * 40)

    for item in flagged:
        short_title = (item.title[:50] + "...") if len(item.title) > 50 else item.title
        short_reason = (item.reason[:60] + "...") if len(item.reason) > 60 else item.reason
        print(f"{item.item_type:<10} {item.item_id:<40} {item.confidence:>5.2f}  {short_title}")
        print(f"{'':>57} -> {short_reason}")

    print()


# ---------------------------------------------------------------------------
# Action: export
# ---------------------------------------------------------------------------


def action_export(flagged: list[FlaggedItem], output_path: Path) -> int:
    """Export flagged items to a backup JSON file.

    Args:
        flagged: List of items to export.
        output_path: Where to write the JSON backup.

    Returns:
        Number of items exported.
    """
    if not flagged:
        logger.info("Nothing to export -- no items flagged.")
        return 0

    payload: dict[str, Any] = {
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "total_items": len(flagged),
        "artifacts": [f.raw for f in flagged if f.item_type == _ITEM_TYPE_ARTIFACT],
        "decision_cards": [f.raw for f in flagged if f.item_type == _ITEM_TYPE_DECISION],
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    logger.info("Exported %d flagged items -> %s", len(flagged), output_path)
    return len(flagged)


# ---------------------------------------------------------------------------
# Action: soft-delete
# ---------------------------------------------------------------------------


def action_soft_delete(
    flagged: list[FlaggedItem],
    settings: CorpusSettings,
    db_url: str,
    *,
    dry_run: bool = False,
) -> dict[str, int]:
    """Mark flagged items as irrelevant in the database.

    For :class:`ResearchArtifact` records, ``|irrelevant`` is appended
    to ``domain_tags`` (the ``status`` CHECK constraint forbids custom
    values like ``retired_irrelevant``).

    For :class:`DecisionCard` records, ``status`` is set to ``archived``
    (closest permitted value) and ``revisit_triggers`` is prefixed with
    ``[IRRELEVANT]`` as a human-readable marker.

    Args:
        flagged: Items to act on.
        settings: Corpus pipeline settings.
        db_url: SQLAlchemy database URL.
        dry_run: If ``True``, log planned actions without committing.

    Returns:
        Counts dict with keys ``modified``, ``skipped``, ``errors``.
    """
    counts = {"modified": 0, "skipped": 0, "errors": 0}
    engine = create_db_engine(db_url)

    with get_session(engine) as session:
        for item in flagged:
            try:
                if item.item_type == _ITEM_TYPE_ARTIFACT:
                    artifact = session.get(ResearchArtifact, item.item_id)
                    if artifact is None:
                        logger.warning("Artifact %s not found in DB -- skipping.", item.item_id)
                        counts["skipped"] += 1
                        continue

                    current_tags = str(artifact.domain_tags) if artifact.domain_tags else ""
                    if "|irrelevant" not in current_tags:
                        if dry_run:
                            logger.info(
                                "[DRY-RUN] Would tag artifact %s (%s) as irrelevant.",
                                item.item_id,
                                item.title,
                            )
                        else:
                            artifact.domain_tags = current_tags + "|irrelevant"  # type: ignore[assignment]
                            logger.info("Tagged artifact %s as irrelevant.", item.item_id)
                        counts["modified"] += 1
                    else:
                        logger.info("Artifact %s already tagged -- skipping.", item.item_id)
                        counts["skipped"] += 1

                elif item.item_type == _ITEM_TYPE_DECISION:
                    card = session.get(DecisionCard, item.item_id)
                    if card is None:
                        logger.warning("Decision card %s not found in DB -- skipping.", item.item_id)
                        counts["skipped"] += 1
                        continue

                    if dry_run:
                        logger.info(
                            "[DRY-RUN] Would archive decision card %s (%s) as irrelevant.",
                            item.item_id,
                            item.title,
                        )
                    else:
                        card.status = "archived"  # type: ignore[assignment]
                        existing_triggers = str(card.revisit_triggers) if card.revisit_triggers else ""
                        if "[IRRELEVANT]" not in existing_triggers:
                            card.revisit_triggers = (  # type: ignore[assignment]
                                "[IRRELEVANT] " + existing_triggers
                            )
                        logger.info("Archived decision card %s as irrelevant.", item.item_id)
                    counts["modified"] += 1

            except Exception:
                logger.exception("Error soft-deleting %s %s", item.item_type, item.item_id)
                counts["errors"] += 1

        if dry_run:
            logger.info("[DRY-RUN] Rolling back -- no changes persisted.")
            session.rollback()
            # Re-raise out of the context manager to prevent commit.
            # get_session commits on clean exit, so we need to avoid that.
            # Since we already rolled back, we can just let it proceed --
            # the commit on an already-rolled-back session is a no-op
            # in SQLAlchemy (it starts a new empty transaction).

    return counts


# ---------------------------------------------------------------------------
# Action: hard-delete
# ---------------------------------------------------------------------------


def _backup_graph(graph_path: Path) -> Path:
    """Create a timestamped backup of the graph JSON file.

    Returns:
        Path to the newly created backup file.
    """
    if not graph_path.exists():
        logger.warning("Graph file %s does not exist -- nothing to back up.", graph_path)
        return graph_path

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = graph_path.with_suffix(f".backup-{ts}.json")
    shutil.copy2(str(graph_path), str(backup))
    logger.info("Graph backup created -> %s", backup)
    return backup


def _delete_from_chromadb(chunk_ids: list[str], settings: CorpusSettings) -> int:
    """Remove chunk embeddings from ChromaDB.

    Args:
        chunk_ids: Chunk IDs to delete.
        settings: Corpus settings (provides ``chroma_dir``).

    Returns:
        Number of chunks successfully targeted for deletion.
    """
    if not chunk_ids:
        return 0

    try:
        import chromadb
    except ImportError:
        logger.error("chromadb is not installed -- cannot delete vectors.")
        return 0

    client = chromadb.PersistentClient(path=settings.chroma_dir)
    try:
        collection = client.get_collection("corpus_chunks")
    except Exception:
        logger.warning("ChromaDB collection 'corpus_chunks' not found -- skipping vector deletion.")
        return 0

    # ChromaDB delete accepts a list of IDs
    batch_size = 5000
    deleted = 0
    for i in range(0, len(chunk_ids), batch_size):
        batch = chunk_ids[i : i + batch_size]
        try:
            collection.delete(ids=batch)
            deleted += len(batch)
        except Exception:
            logger.exception("Error deleting chunk batch from ChromaDB (offset %d).", i)

    logger.info("Deleted %d chunk embeddings from ChromaDB.", deleted)
    return deleted


def _delete_from_graph(node_ids: list[str], settings: CorpusSettings) -> int:
    """Remove nodes (and their edges) from the NetworkX graph JSON.

    Args:
        node_ids: Graph node IDs to remove.
        settings: Corpus settings (provides ``graph_path``).

    Returns:
        Number of nodes actually removed.
    """
    if not node_ids:
        return 0

    graph_path = Path(settings.graph_path)
    if not graph_path.exists():
        logger.warning("Graph file %s not found -- skipping graph deletion.", graph_path)
        return 0

    try:
        import networkx as nx
    except ImportError:
        logger.error("networkx is not installed -- cannot modify graph.")
        return 0

    data = json.loads(graph_path.read_text(encoding="utf-8"))
    G = nx.node_link_graph(data)

    removed = 0
    for nid in node_ids:
        if G.has_node(nid):
            G.remove_node(nid)  # also removes incident edges
            removed += 1

    # Write back
    updated = nx.node_link_data(G)
    graph_path.write_text(json.dumps(updated, indent=2), encoding="utf-8")
    logger.info("Removed %d nodes from graph -> %s", removed, graph_path)
    return removed


def action_hard_delete(
    flagged: list[FlaggedItem],
    settings: CorpusSettings,
    db_url: str,
    *,
    dry_run: bool = False,
) -> dict[str, int]:
    """Remove flagged items from SQLite, ChromaDB, and the graph.

    Deletion order per artifact:
      1. Collect chunk IDs for ChromaDB removal.
      2. Delete ``ArtifactChunk`` rows from SQLite.
      3. Delete ``ResearchArtifact`` row from SQLite.
      4. Remove node from graph.

    For decision cards:
      1. Delete ``DecisionCard`` row from SQLite.
      2. Remove node from graph.

    The graph JSON is backed up before any modifications.

    Args:
        flagged: Items to delete.
        settings: Corpus pipeline settings.
        db_url: SQLAlchemy database URL.
        dry_run: If ``True``, log what would happen without persisting.

    Returns:
        Counts dict with keys ``deleted``, ``chunks_removed``,
        ``vectors_removed``, ``graph_nodes_removed``, ``skipped``,
        ``errors``.
    """
    counts: dict[str, int] = {
        "deleted": 0,
        "chunks_removed": 0,
        "vectors_removed": 0,
        "graph_nodes_removed": 0,
        "skipped": 0,
        "errors": 0,
    }

    # Back up graph before any changes
    graph_path = Path(settings.graph_path)
    if not dry_run:
        _backup_graph(graph_path)

    # ---- Phase 1: Collect chunk IDs & graph node IDs ----
    engine = create_db_engine(db_url)
    all_chunk_ids: list[str] = []
    graph_node_ids: list[str] = []

    with get_session(engine) as session:
        for item in flagged:
            try:
                if item.item_type == _ITEM_TYPE_ARTIFACT:
                    artifact = session.get(ResearchArtifact, item.item_id)
                    if artifact is None:
                        logger.warning("Artifact %s not found -- skipping.", item.item_id)
                        counts["skipped"] += 1
                        continue

                    # Gather chunk IDs for vector store cleanup
                    chunks = (
                        session.query(ArtifactChunk)
                        .filter(ArtifactChunk.artifact_id == item.item_id)
                        .all()
                    )
                    chunk_ids = [str(c.chunk_id) for c in chunks]
                    all_chunk_ids.extend(chunk_ids)

                    if dry_run:
                        logger.info(
                            "[DRY-RUN] Would delete artifact %s (%s) with %d chunks.",
                            item.item_id,
                            item.title,
                            len(chunk_ids),
                        )
                    else:
                        # Delete chunks first (FK dependency)
                        for chunk in chunks:
                            session.delete(chunk)
                        counts["chunks_removed"] += len(chunks)

                        # Delete the artifact
                        session.delete(artifact)
                        logger.info(
                            "Deleted artifact %s (%d chunks) from SQLite.",
                            item.item_id,
                            len(chunks),
                        )

                    graph_node_ids.append(item.item_id)
                    counts["deleted"] += 1

                elif item.item_type == _ITEM_TYPE_DECISION:
                    card = session.get(DecisionCard, item.item_id)
                    if card is None:
                        logger.warning("Decision card %s not found -- skipping.", item.item_id)
                        counts["skipped"] += 1
                        continue

                    if dry_run:
                        logger.info(
                            "[DRY-RUN] Would delete decision card %s (%s).",
                            item.item_id,
                            item.title,
                        )
                    else:
                        # Delete related capability mappings first
                        from corpus.db.models import CapabilityMapping

                        session.query(CapabilityMapping).filter(
                            CapabilityMapping.decision_id == item.item_id
                        ).delete()

                        # Delete related drift events
                        from corpus.db.models import DriftEvent

                        session.query(DriftEvent).filter(
                            DriftEvent.decision_id == item.item_id
                        ).delete()

                        # Delete related telemetry outcomes
                        from corpus.db.models import TelemetryOutcome

                        session.query(TelemetryOutcome).filter(
                            TelemetryOutcome.decision_id == item.item_id
                        ).delete()

                        session.delete(card)
                        logger.info("Deleted decision card %s from SQLite.", item.item_id)

                    graph_node_ids.append(item.item_id)
                    counts["deleted"] += 1

            except Exception:
                logger.exception("Error deleting %s %s from SQLite.", item.item_type, item.item_id)
                counts["errors"] += 1

        if dry_run:
            logger.info("[DRY-RUN] Rolling back SQLite transaction.")
            session.rollback()

    # ---- Phase 2: ChromaDB vector deletion (outside DB transaction) ----
    if dry_run:
        logger.info("[DRY-RUN] Would remove %d chunk embeddings from ChromaDB.", len(all_chunk_ids))
    else:
        counts["vectors_removed"] = _delete_from_chromadb(all_chunk_ids, settings)

    # ---- Phase 3: Graph node removal ----
    if dry_run:
        logger.info("[DRY-RUN] Would remove %d nodes from graph.", len(graph_node_ids))
    else:
        counts["graph_nodes_removed"] = _delete_from_graph(graph_node_ids, settings)

    return counts


# ---------------------------------------------------------------------------
# Summary printer
# ---------------------------------------------------------------------------


def print_summary(action: str, counts: dict[str, int]) -> None:
    """Print a concise summary of the action taken."""
    print(f"\n{'=' * 60}")
    print(f"  ACTION SUMMARY -- {action.upper()}")
    print(f"{'=' * 60}")
    for key, val in counts.items():
        label = key.replace("_", " ").capitalize()
        print(f"  {label:<30} {val:>6}")
    print(f"{'=' * 60}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser."""
    p = argparse.ArgumentParser(
        description="Apply actions based on relevance-audit results.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument(
        "--audit-file",
        type=Path,
        default=Path("data/relevance_audit.json"),
        help="Path to the relevance audit JSON (default: data/relevance_audit.json).",
    )
    p.add_argument(
        "--action",
        choices=["report", "soft-delete", "hard-delete", "export"],
        default="report",
        help="Action to perform on flagged items (default: report).",
    )
    p.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.7,
        help="Only act on items with confidence >= this value (default: 0.7).",
    )
    p.add_argument(
        "--db-url",
        type=str,
        default=None,
        help="SQLAlchemy DB URL (default: from corpus settings).",
    )
    p.add_argument(
        "--confirm-delete",
        action="store_true",
        default=False,
        help="Required safety flag for --action hard-delete.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Show what would happen without making changes.",
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose (DEBUG-level) logging.",
    )
    return p


def main(argv: list[str] | None = None) -> None:
    """Entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)

    # --- Logging setup ---
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # --- Safety gate for hard-delete ---
    if args.action == "hard-delete" and not args.confirm_delete:
        logger.error(
            "hard-delete requires --confirm-delete flag. "
            "This is a destructive operation that cannot be undone."
        )
        sys.exit(1)

    # --- Load and filter audit ---
    logger.info("Loading audit file: %s", args.audit_file)
    audit = load_audit(args.audit_file)

    metadata = audit.get("audit_metadata", {})
    logger.info(
        "Audit metadata -- model: %s, artifacts audited: %s, decisions audited: %s",
        metadata.get("model", "?"),
        metadata.get("total_artifacts_audited", "?"),
        metadata.get("total_decisions_audited", "?"),
    )

    flagged = filter_flagged(audit, args.confidence_threshold)
    logger.info(
        "Found %d flagged items (confidence >= %.2f).",
        len(flagged),
        args.confidence_threshold,
    )

    if not flagged and args.action != "report":
        logger.info("No items to process -- exiting.")
        return

    # --- Resolve settings ---
    settings = get_settings()
    db_url = args.db_url or settings.db_url

    # --- Dispatch action ---
    if args.action == "report":
        action_report(flagged)
        return

    if args.action == "export":
        export_path = Path("data/irrelevant_items_export.json")
        n = action_export(flagged, export_path)
        print_summary("export", {"exported": n})
        return

    if args.action == "soft-delete":
        if args.dry_run:
            logger.info("*** DRY-RUN MODE -- no changes will be persisted. ***")
        counts = action_soft_delete(flagged, settings, db_url, dry_run=args.dry_run)
        print_summary("soft-delete", counts)
        return

    if args.action == "hard-delete":
        if args.dry_run:
            logger.info("*** DRY-RUN MODE -- no changes will be persisted. ***")
        counts = action_hard_delete(flagged, settings, db_url, dry_run=args.dry_run)
        print_summary("hard-delete", counts)
        return


if __name__ == "__main__":
    main()
