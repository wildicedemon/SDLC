from __future__ import annotations

from pathlib import Path

from sqlalchemy import text
from sqlalchemy.engine import Engine

VERSIONS_DIR = Path(__file__).parent / "versions"

_SCHEMA_VERSION_DDL = """
CREATE TABLE IF NOT EXISTS _schema_version (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


def _ensure_version_table(engine: Engine) -> None:
    with engine.begin() as conn:
        conn.execute(text(_SCHEMA_VERSION_DDL))


def _current_version(engine: Engine) -> int:
    with engine.begin() as conn:
        row = conn.execute(text("SELECT MAX(version) FROM _schema_version")).fetchone()
        return row[0] if row and row[0] is not None else 0


def _available_migrations() -> list[tuple[int, Path, Path | None]]:
    results: list[tuple[int, Path, Path | None]] = []
    for f in sorted(VERSIONS_DIR.glob("*.sql")):
        name = f.stem
        if name.endswith("_rollback"):
            continue
        version = int(name.split("_")[0])
        rollback = f.parent / f"{name}_rollback.sql"
        results.append((version, f, rollback if rollback.exists() else None))
    return results


def migrate(engine: Engine) -> list[int]:
    _ensure_version_table(engine)
    current = _current_version(engine)
    applied: list[int] = []
    for version, path, _ in _available_migrations():
        if version <= current:
            continue
        sql = path.read_text(encoding="utf-8")
        with engine.begin() as conn:
            for statement in _split_statements(sql):
                conn.execute(text(statement))
            conn.execute(
                text("INSERT INTO _schema_version (version) VALUES (:v)"),
                {"v": version},
            )
        applied.append(version)
    return applied


def rollback(engine: Engine) -> int | None:
    _ensure_version_table(engine)
    current = _current_version(engine)
    if current == 0:
        return None
    for version, _, rollback_path in reversed(_available_migrations()):
        if version == current and rollback_path is not None:
            sql = rollback_path.read_text(encoding="utf-8")
            with engine.begin() as conn:
                for statement in _split_statements(sql):
                    conn.execute(text(statement))
                conn.execute(
                    text("DELETE FROM _schema_version WHERE version = :v"),
                    {"v": version},
                )
            return version
    return None


def _split_statements(sql: str) -> list[str]:
    return [s.strip() for s in sql.split(";") if s.strip()]
