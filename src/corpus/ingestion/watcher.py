"""Drop-folder watcher for automatic corpus ingestion.

Uses ``watchdog`` to monitor a directory for new/modified files and
auto-ingests them via :func:`corpus.ingestion.pipeline.ingest_file`.
"""

from __future__ import annotations

import logging
import shutil
import threading
import time
from pathlib import Path

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

logger = logging.getLogger(__name__)

# Extensions the watcher will process
_SUPPORTED_EXTS = {
    ".md", ".markdown",
    ".html", ".htm",
    ".pdf",
    ".txt", ".text", ".log", ".csv",
}


class CorpusEventHandler(FileSystemEventHandler):
    """Respond to *created* and *modified* events with a 2-second debounce.

    After the debounce window elapses without further events for the same
    file, the file is parsed and ingested into the corpus database.
    Processed files are moved to ``{watch_dir}/processed/``.
    """

    def __init__(self, watch_dir: Path) -> None:
        super().__init__()
        self.watch_dir = Path(watch_dir)
        self.processed_dir = self.watch_dir / "processed"
        self._timers: dict[str, threading.Timer] = {}
        self._lock = threading.Lock()

    # ------------------------------------------------------------------
    # watchdog callbacks
    # ------------------------------------------------------------------

    def on_created(self, event: FileSystemEvent) -> None:
        """Handle file-created events."""
        if not event.is_directory:
            self._schedule(event.src_path)

    def on_modified(self, event: FileSystemEvent) -> None:
        """Handle file-modified events."""
        if not event.is_directory:
            self._schedule(event.src_path)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _schedule(self, src_path: str) -> None:
        """(Re-)schedule processing with a 2-second debounce."""
        path = Path(src_path)

        # Ignore files anywhere under a ``processed/`` directory
        if "processed" in path.parts:
            return

        if path.suffix.lower() not in _SUPPORTED_EXTS:
            logger.debug("Ignoring unsupported extension: %s", path)
            return

        with self._lock:
            key = str(path)
            existing = self._timers.get(key)
            if existing is not None:
                existing.cancel()
            timer = threading.Timer(2.0, self._process_file, args=(path,))
            timer.daemon = True
            self._timers[key] = timer
            timer.start()
            logger.debug("Debounce (re)started for %s", path)

    def _process_file(self, path: Path) -> None:
        """Parse, ingest, and move a file after the debounce window."""
        from corpus.config import get_settings
        from corpus.db.engine import create_db_engine, get_session
        from corpus.db.repository import CorpusRepository
        from corpus.ingestion.parsers import parse_file
        from corpus.ingestion.pipeline import ingest_file

        logger.info("Processing file: %s", path)

        if not path.exists():
            logger.warning("File disappeared before processing: %s", path)
            return

        try:
            parsed = parse_file(path)
        except Exception:
            logger.exception("Failed to parse %s", path)
            return

        try:
            settings = get_settings()
            engine = create_db_engine(settings.db_url)

            with get_session(engine) as session:
                repo = CorpusRepository(session)

                # Create or re-use a consolidation run for watched files
                import uuid
                from datetime import datetime, timezone

                run_id = f"cr_watch_{uuid.uuid4().hex[:8]}"
                now = datetime.now(timezone.utc).isoformat()
                repo.create_run(
                    run_id=run_id,
                    source_branch="watch",
                    started_at=now,
                    status="running",
                )

                ingest_file(
                    file_path=path,
                    content=parsed.content,
                    title=parsed.title,
                    metadata=parsed.metadata,
                    session=session,
                    run_id=run_id,
                    corpus_root=self.watch_dir,
                )

                repo.update_run_status(run_id, "completed")

            # Move to processed/
            self.processed_dir.mkdir(parents=True, exist_ok=True)
            dest = self.processed_dir / path.name
            # Avoid overwriting — add suffix if needed
            counter = 1
            while dest.exists():
                dest = self.processed_dir / f"{path.stem}_{counter}{path.suffix}"
                counter += 1
            shutil.move(str(path), str(dest))
            logger.info("Moved processed file to %s", dest)

        except Exception:
            logger.exception("Failed to ingest %s", path)

        finally:
            with self._lock:
                self._timers.pop(str(path), None)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def watch(watch_dir: Path, poll_interval: float = 2.0) -> None:
    """Watch *watch_dir* for new files and auto-ingest them.

    Creates *watch_dir* and ``watch_dir/processed/`` if they don't exist,
    initialises the database, processes any backlog, then enters an
    observation loop until interrupted with ``Ctrl+C``.

    Parameters
    ----------
    watch_dir:
        Directory to monitor.
    poll_interval:
        Seconds between filesystem polls.
    """
    watch_dir = Path(watch_dir)
    processed_dir = watch_dir / "processed"
    watch_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)

    # Initialise the database
    from corpus.config import get_settings
    from corpus.db.engine import create_db_engine
    from corpus.db.migrations.runner import migrate_forward

    settings = get_settings()
    engine = create_db_engine(settings.db_url)
    settings.ensure_data_dirs()
    migrate_forward(engine)

    handler = CorpusEventHandler(watch_dir)

    # Process any backlog (existing files, recursively)
    logger.info("Checking for backlog in %s …", watch_dir)
    for ext in _SUPPORTED_EXTS:
        for existing_file in sorted(watch_dir.rglob(f"*{ext}")):
            if "processed" not in existing_file.parts:
                logger.info("Backlog file found: %s", existing_file)
                handler._process_file(existing_file)

    observer = Observer()
    observer.schedule(handler, str(watch_dir), recursive=True)
    observer.start()
    logger.info("Watching %s (poll every %.1fs) — press Ctrl+C to stop", watch_dir, poll_interval)

    try:
        while True:
            time.sleep(poll_interval)
    except KeyboardInterrupt:
        logger.info("Stopping watcher…")
        observer.stop()

    observer.join()
    logger.info("Watcher stopped.")
