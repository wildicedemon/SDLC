"""SQLAlchemy engine creation and session management.

Provides factory functions for creating database engines with
SQLite-specific pragmas (e.g. foreign-key enforcement) and
context-managed sessions with automatic commit/rollback semantics.
"""

from collections.abc import Generator
from contextlib import contextmanager
from typing import Any

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


def create_db_engine(url: str) -> Engine:
    """Create a SQLAlchemy engine with SQLite foreign-key support.

    Registers a ``connect`` event listener that issues
    ``PRAGMA foreign_keys=ON`` on every new raw DBAPI connection,
    ensuring referential-integrity checks are always active.

    Args:
        url: SQLAlchemy database URL (e.g. ``sqlite:///corpus.db``).

    Returns:
        A configured :class:`~sqlalchemy.engine.Engine` instance.
    """
    engine = create_engine(url, echo=False)

    @event.listens_for(engine, "connect")
    def _set_sqlite_pragma(dbapi_conn: Any, _connection_record: Any) -> None:
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    return engine


def make_session_factory(engine: Engine) -> sessionmaker[Session]:
    """Build a :class:`~sqlalchemy.orm.sessionmaker` bound to *engine*.

    Args:
        engine: The SQLAlchemy engine to bind sessions to.

    Returns:
        A session factory callable that produces new :class:`Session` objects.
    """
    return sessionmaker(bind=engine)


@contextmanager
def get_session(engine: Engine) -> Generator[Session, None, None]:
    """Provide a transactional session scope around a block of operations.

    Commits on clean exit, rolls back on exception, and always
    closes the session when the context manager exits.

    Args:
        engine: The SQLAlchemy engine to create a session from.

    Yields:
        A :class:`~sqlalchemy.orm.Session` bound to a transaction.

    Raises:
        Exception: Re-raises any exception after performing a rollback.
    """
    factory = make_session_factory(engine)
    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
