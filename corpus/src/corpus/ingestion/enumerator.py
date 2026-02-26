from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from git import InvalidGitRepositoryError, Repo


@dataclass
class ChangedFile:
    path: str
    change_type: str
    content: bytes | None


def enumerate_changes(
    repo_path: str | Path,
    source_branch: str,
    base_branch: str = "main",
) -> list[ChangedFile]:
    try:
        repo = Repo(str(repo_path))
    except InvalidGitRepositoryError:
        raise ValueError(f"Not a git repository: {repo_path}")

    if source_branch not in [r.name for r in repo.references]:
        raise ValueError(f"Branch not found: {source_branch}")
    if base_branch not in [r.name for r in repo.references]:
        raise ValueError(f"Branch not found: {base_branch}")

    base_commit = repo.commit(base_branch)
    source_commit = repo.commit(source_branch)

    diffs = base_commit.diff(source_commit)

    results: list[ChangedFile] = []
    for diff in diffs:
        if diff.new_file:
            path = diff.b_path
            change_type = "added"
        elif diff.deleted_file:
            path = diff.a_path
            change_type = "deleted"
        elif diff.renamed_file:
            path = diff.b_path
            change_type = "modified"
        else:
            path = diff.b_path or diff.a_path
            change_type = "modified"

        if not path.endswith(".md"):
            continue

        content: bytes | None = None
        if change_type != "deleted":
            try:
                blob = source_commit.tree / path
                content = blob.data_stream.read()
            except KeyError:
                content = None

        results.append(ChangedFile(path=path, change_type=change_type, content=content))

    return results
