"""Git diff enumerator for changed markdown files.

Compares a *source* branch against a *base* branch to discover
added, modified, and deleted ``.md`` files.  For non-deleted files
the blob content is read from the source branch's tree so that
ingestion can proceed without checking out the branch.

Key function: :func:`enumerate_changes`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from git import InvalidGitRepositoryError, Repo


@dataclass
class ChangedFile:
    """A single file change detected between two branches.

    Attributes:
        path: Repository-relative file path.
        change_type: One of ``added``, ``modified``, or ``deleted``.
        content: Raw bytes of the file on the source branch,
            or ``None`` for deletions (or if the blob is missing).
    """

    path: str
    change_type: str
    content: bytes | None


def enumerate_changes(
    repo_path: str | Path,
    source_branch: str,
    base_branch: str = "main",
) -> list[ChangedFile]:
    """List ``.md`` files that differ between *source_branch* and *base_branch*.

    Performs a two-dot diff (``base..source``) and returns only
    Markdown files.  Renamed files are treated as modifications.

    Args:
        repo_path: Filesystem path to the Git repository.
        source_branch: The branch containing new/changed research.
        base_branch: The baseline branch to diff against (default ``main``).

    Returns:
        A list of :class:`ChangedFile` instances for every changed
        ``.md`` file.

    Raises:
        ValueError: If *repo_path* is not a Git repository or either
            branch name cannot be found.
    """
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
        # Determine the effective file path and change type
        file_path: str
        if diff.new_file:
            file_path = diff.b_path or ""
            change_type = "added"
        elif diff.deleted_file:
            file_path = diff.a_path or ""
            change_type = "deleted"
        elif diff.renamed_file:
            file_path = diff.b_path or ""
            change_type = "modified"
        else:
            file_path = diff.b_path or diff.a_path or ""
            change_type = "modified"

        # Only process Markdown files
        if not file_path or not file_path.endswith(".md"):
            continue

        # Read blob content from the source branch for non-deletions
        content: bytes | None = None
        if change_type != "deleted":
            try:
                blob = source_commit.tree / file_path
                content = blob.data_stream.read()
            except KeyError:
                content = None

        results.append(ChangedFile(path=file_path, change_type=change_type, content=content))

    return results
