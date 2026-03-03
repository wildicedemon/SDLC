"""SQL migration runner for the corpus pipeline database.

Implements a lightweight, file-based migration system. Each migration
lives as a ``.sql`` file under the ``versions/`` directory. Forward
and rollback SQL are separated by a ``-- rollback:`` marker within
the same file.

Applied versions are tracked in a ``_schema_versions`` table so that
:func:`migrate_forward` only applies pending migrations and
:func:`migrate_rollback` undoes the most recent one.
"""

from pathlib import Path

from sqlalchemy import text
from sqlalchemy.engine import Engine

# Directory containing numbered .sql migration files
VERSIONS_DIR = Path(__file__).parent / "versions"

# DDL for the migration-tracking table (idempotent)
_INIT_TRACKING = """
CREATE TABLE IF NOT EXISTS _schema_versions (
    version TEXT PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


def _get_applied_versions(engine: Engine) -> list[str]:
    """Return an ordered list of migration versions already applied.

    Ensures the ``_schema_versions`` tracking table exists before
    querying it.

    Args:
        engine: The SQLAlchemy engine to query.

    Returns:
        Version strings sorted in ascending order.
    """
    with engine.connect() as conn:
        conn.execute(text(_INIT_TRACKING))
        conn.commit()
        rows = conn.execute(text("SELECT version FROM _schema_versions ORDER BY version")).fetchall()
    return [r[0] for r in rows]


def _parse_sql_file(path: Path) -> tuple[str, str]:
    """Split a migration file into forward and rollback SQL.

    The file format uses ``-- rollback:`` as a delimiter.  Everything
    before the marker is the forward (upgrade) SQL; everything after
    is the rollback (downgrade) SQL.

    Args:
        path: Filesystem path to the ``.sql`` migration file.

    Returns:
        A ``(forward_sql, rollback_sql)`` tuple.  *rollback_sql* is
        an empty string if no rollback section is present.
    """
    content = path.read_text(encoding="utf-8")
    parts = content.split("-- rollback:")
    forward = parts[0].strip()
    rollback = parts[1].strip() if len(parts) > 1 else ""
    return forward, rollback


def _get_version_files() -> list[tuple[str, Path]]:
    """Discover and sort all migration files in the versions directory.

    Returns:
        A list of ``(version_stem, path)`` tuples sorted by filename
        (e.g. ``[("001_initial", Path(...))]``).
    """
    files = sorted(VERSIONS_DIR.glob("*.sql"))
    result = []
    for f in files:
        version = f.stem  # e.g. "001_initial"
        result.append((version, f))
    return result


def migrate_forward(engine: Engine) -> list[str]:
    """Apply all pending migrations in order.

    Skips versions that are already recorded in ``_schema_versions``.
    Each migration is executed inside its own transaction with
    foreign-key checks temporarily disabled to allow schema changes.

    Args:
        engine: The SQLAlchemy engine to run migrations against.

    Returns:
        A list of version strings that were newly applied.
    """
    applied = _get_applied_versions(engine)
    version_files = _get_version_files()
    newly_applied: list[str] = []

    for version, path in version_files:
        if version in applied:
            continue
        forward_sql, _ = _parse_sql_file(path)
        with engine.connect() as conn:
            # Disable FK checks during schema migration to avoid
            # ordering issues when creating interrelated tables.
            conn.execute(text("PRAGMA foreign_keys=OFF"))
            for stmt in forward_sql.split(";"):
                stmt = stmt.strip()
                if stmt:
                    conn.execute(text(stmt))
            # Record that this version has been applied
            conn.execute(text("INSERT INTO _schema_versions (version) VALUES (:v)"), {"v": version})
            conn.execute(text("PRAGMA foreign_keys=ON"))
            conn.commit()
        newly_applied.append(version)

    return newly_applied


def migrate_rollback(engine: Engine) -> str | None:
    """Roll back the most recently applied migration.

    If no migrations have been applied or the latest migration has no
    rollback section, returns ``None`` without making changes.

    Args:
        engine: The SQLAlchemy engine to run the rollback against.

    Returns:
        The version string that was rolled back, or ``None``.
    """
    applied = _get_applied_versions(engine)
    if not applied:
        return None

    last_version = applied[-1]
    version_files = dict(_get_version_files())
    path = version_files.get(last_version)
    if path is None:
        return None

    _, rollback_sql = _parse_sql_file(path)
    if not rollback_sql:
        return None

    with engine.connect() as conn:
        # Disable FK checks during rollback for the same reason as forward
        conn.execute(text("PRAGMA foreign_keys=OFF"))
        for stmt in rollback_sql.split(";"):
            stmt = stmt.strip()
            if stmt:
                conn.execute(text(stmt))
        conn.execute(text("DELETE FROM _schema_versions WHERE version = :v"), {"v": last_version})
        conn.execute(text("PRAGMA foreign_keys=ON"))
        conn.commit()

    return last_version
