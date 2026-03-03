"""Git branch cleanup after a successful consolidation run.

After a run completes, the source branch can be either *archived*
(tagged then optionally kept) or *deleted*.  This module performs
the Git operations and records the chosen action on the run record.

Key function: :func:`retire_branch`.
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


def retire_branch(
    session: Session,
    run_id: str,
    action: str,
    repo_path: str = ".",
) -> None:
    """Archive or delete the source branch of a completed run.

    Args:
        session: Active SQLAlchemy session.
        run_id: ID of the consolidation run.
        action: Either ``"archived"`` (creates a tag and keeps the
            branch) or ``"deleted"`` (force-deletes the branch).
        repo_path: Filesystem path to the Git repository.

    Raises:
        ValueError: If the run doesn't exist, isn't completed, the
            action is invalid, *repo_path* isn't a Git repo, or the
            branch is currently checked out.
    """
    repo = CorpusRepository(session)
    run = repo.get_run(run_id)

    if run is None:
        raise ValueError(f"Run {run_id} not found")

    if str(run.status) != "completed":
        raise ValueError(f"Cannot retire branch for run {run_id}: status is '{run.status}', expected 'completed'")

    if action not in ("archived", "deleted"):
        raise ValueError(f"Invalid action: {action}. Must be 'archived' or 'deleted'.")

    from git import InvalidGitRepositoryError, Repo

    try:
        git_repo = Repo(repo_path)
    except InvalidGitRepositoryError:
        raise ValueError(f"Not a git repository: {repo_path}")

    branch_name = str(run.source_branch)

    if action == "archived":
        # Create an archive tag pointing at the branch tip
        tag_name = f"archive/{branch_name}"
        if tag_name not in [t.name for t in git_repo.tags]:
            git_repo.create_tag(tag_name, ref=branch_name)

    if action == "deleted":
        # Force-delete the branch (cannot delete the active branch)
        if branch_name in [h.name for h in git_repo.heads]:
            if git_repo.active_branch.name == branch_name:
                raise ValueError(f"Cannot delete active branch: {branch_name}")
            git_repo.delete_head(branch_name, force=True)

    run.retirement_action = action  # type: ignore[assignment]
    session.flush()
