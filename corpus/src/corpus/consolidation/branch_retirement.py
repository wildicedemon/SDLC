from __future__ import annotations

from sqlalchemy.orm import Session

from corpus.db.repository import CorpusRepository


def retire_branch(
    session: Session,
    run_id: str,
    action: str,
    repo_path: str = ".",
) -> None:
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
        tag_name = f"archive/{branch_name}"
        if tag_name not in [t.name for t in git_repo.tags]:
            git_repo.create_tag(tag_name, ref=branch_name)

    if action == "deleted":
        if branch_name in [h.name for h in git_repo.heads]:
            if git_repo.active_branch.name == branch_name:
                raise ValueError(f"Cannot delete active branch: {branch_name}")
            git_repo.delete_head(branch_name, force=True)

    run.retirement_action = action  # type: ignore[assignment]
    session.flush()
