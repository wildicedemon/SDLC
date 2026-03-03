"""Tests for :mod:`corpus.ingestion.watcher`."""

from __future__ import annotations

import threading
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from corpus.ingestion.watcher import CorpusEventHandler, _SUPPORTED_EXTS


class TestCorpusEventHandlerDebounce:
    """Verify the 2-second debounce logic."""

    def test_debounce_reschedules_timer(self, tmp_path: Path) -> None:
        """Multiple rapid events for the same file should only keep one timer."""
        handler = CorpusEventHandler(tmp_path)

        # Patch _process_file to prevent actual DB work
        handler._process_file = MagicMock()  # type: ignore[assignment]

        test_file = tmp_path / "test.md"
        test_file.write_text("# Hello", encoding="utf-8")

        # Simulate three rapid events
        event = MagicMock()
        event.is_directory = False
        event.src_path = str(test_file)

        handler.on_created(event)
        handler.on_modified(event)
        handler.on_modified(event)

        # Only one timer should be active for this file
        assert str(test_file) in handler._timers
        # Cancel all timers to avoid side-effects
        for timer in handler._timers.values():
            timer.cancel()

    def test_ignores_files_in_processed_dir(self, tmp_path: Path) -> None:
        """Events for files inside processed/ should be skipped."""
        handler = CorpusEventHandler(tmp_path)
        handler._process_file = MagicMock()  # type: ignore[assignment]

        processed = tmp_path / "processed"
        processed.mkdir()
        pfile = processed / "old.md"
        pfile.write_text("done", encoding="utf-8")

        event = MagicMock()
        event.is_directory = False
        event.src_path = str(pfile)

        handler.on_created(event)

        # No timer should have been scheduled
        assert str(pfile) not in handler._timers

    def test_ignores_unsupported_extensions(self, tmp_path: Path) -> None:
        """Events for files with unsupported extensions should be ignored."""
        handler = CorpusEventHandler(tmp_path)
        handler._process_file = MagicMock()  # type: ignore[assignment]

        weird = tmp_path / "data.exe"
        weird.write_text("binary-ish", encoding="utf-8")

        event = MagicMock()
        event.is_directory = False
        event.src_path = str(weird)

        handler.on_created(event)

        assert str(weird) not in handler._timers


class TestWatchDirectoryCreation:
    """Verify that watch() creates required directories."""

    @patch("corpus.ingestion.watcher.Observer")
    @patch("corpus.ingestion.watcher.migrate_forward")
    @patch("corpus.ingestion.watcher.create_db_engine")
    @patch("corpus.ingestion.watcher.get_settings")
    def test_creates_watch_and_processed_dirs(
        self,
        mock_settings: MagicMock,
        mock_engine: MagicMock,
        mock_migrate: MagicMock,
        mock_observer_cls: MagicMock,
        tmp_path: Path,
    ) -> None:
        """watch() should create watch_dir and watch_dir/processed if missing."""
        from corpus.ingestion.watcher import watch

        watch_dir = tmp_path / "new_watch"
        assert not watch_dir.exists()

        settings = MagicMock()
        settings.db_url = "sqlite:///:memory:"
        mock_settings.return_value = settings

        # Make the observer raise KeyboardInterrupt immediately
        observer_instance = MagicMock()
        mock_observer_cls.return_value = observer_instance
        observer_instance.start.side_effect = KeyboardInterrupt

        try:
            watch(watch_dir, poll_interval=0.1)
        except KeyboardInterrupt:
            pass

        assert watch_dir.exists()
        assert (watch_dir / "processed").exists()


class TestProcessedFileMove:
    """Test that _process_file moves files to processed/."""

    @patch("corpus.ingestion.watcher.get_settings")
    @patch("corpus.ingestion.watcher.create_db_engine")
    @patch("corpus.ingestion.watcher.get_session")
    def test_file_moved_to_processed(
        self,
        mock_session_ctx: MagicMock,
        mock_engine: MagicMock,
        mock_settings: MagicMock,
        tmp_path: Path,
    ) -> None:
        """After successful processing, the file should land in processed/."""
        from corpus.ingestion.watcher import CorpusEventHandler

        processed = tmp_path / "processed"
        processed.mkdir()

        handler = CorpusEventHandler(tmp_path)

        test_file = tmp_path / "sample.txt"
        test_file.write_text("Hello there", encoding="utf-8")

        settings = MagicMock()
        settings.db_url = "sqlite:///:memory:"
        mock_settings.return_value = settings

        # Mock session context manager
        mock_session = MagicMock()
        mock_session_ctx.return_value.__enter__ = MagicMock(return_value=mock_session)
        mock_session_ctx.return_value.__exit__ = MagicMock(return_value=False)

        with patch("corpus.ingestion.watcher.parse_file") as mock_parse, \
             patch("corpus.ingestion.watcher.ingest_file") as mock_ingest, \
             patch("corpus.ingestion.watcher.CorpusRepository") as mock_repo_cls:

            mock_parsed = MagicMock()
            mock_parsed.content = "Hello there"
            mock_parsed.title = "sample"
            mock_parsed.metadata = {}
            mock_parse.return_value = mock_parsed

            handler._process_file(test_file)

        # File should have been moved
        assert not test_file.exists()
        assert (processed / "sample.txt").exists()
