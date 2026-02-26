from pathlib import Path
from typing import Any

from sqlalchemy import text
from sqlalchemy.engine import Engine


VERSIONS_DIR = Path(__file__).parent / "versions"

_INIT_TRACKING = """
CREATE TABLE IF NOT EXISTS _schema_versions (
    version TEXT PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


def _get_applied_versions(engine: Engine) -> list[str]:
    with engine.connect() as conn:
        conn.execute(text(_INIT_TRACKING))
        conn.commit()
        rows = conn.execute(text("SELECT version FROM _schema_versions ORDER BY version")).fetchall()
    return [r[0] for r in rows]


def _parse_sql_file(path: Path) -> tuple[str, str]:
    content = path.read_text(encoding="utf-8")
    parts = content.split("-- rollback:")
    forward = parts[0].strip()
    rollback = parts[1].strip() if len(parts) > 1 else ""
    return forward, rollback


def _get_version_files() -> list[tuple[str, Path]]:
    files = sorted(VERSIONS_DIR.glob("*.sql"))
    result = []
    for f in files:
        version = f.stem
        result.append((version, f))
    return result


def migrate_forward(engine: Engine) -> list[str]:
    applied = _get_applied_versions(engine)
    version_files = _get_version_files()
    newly_applied: list[str] = []

    for version, path in version_files:
        if version in applied:
            continue
        forward_sql, _ = _parse_sql_file(path)
        with engine.connect() as conn:
            conn.execute(text("PRAGMA foreign_keys=OFF"))
            for stmt in forward_sql.split(";"):
                stmt = stmt.strip()
                if stmt:
                    conn.execute(text(stmt))
            conn.execute(text("INSERT INTO _schema_versions (version) VALUES (:v)"), {"v": version})
            conn.execute(text("PRAGMA foreign_keys=ON"))
            conn.commit()
        newly_applied.append(version)

    return newly_applied


def migrate_rollback(engine: Engine) -> str | None:
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
        conn.execute(text("PRAGMA foreign_keys=OFF"))
        for stmt in rollback_sql.split(";"):
            stmt = stmt.strip()
            if stmt:
                conn.execute(text(stmt))
        conn.execute(text("DELETE FROM _schema_versions WHERE version = :v"), {"v": last_version})
        conn.execute(text("PRAGMA foreign_keys=ON"))
        conn.commit()

    return last_version
