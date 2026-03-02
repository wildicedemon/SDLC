from pathlib import Path

import pytest
from git import Repo

from corpus.ingestion.enumerator import enumerate_changes


@pytest.fixture()
def git_repo(tmp_path: Path) -> tuple[Path, str]:
    repo = Repo.init(str(tmp_path))
    repo.config_writer().set_value("user", "name", "Test").release()
    repo.config_writer().set_value("user", "email", "test@test.com").release()

    base_file = tmp_path / "existing.md"
    base_file.write_text("# Existing\noriginal content")
    txt_file = tmp_path / "readme.txt"
    txt_file.write_text("not markdown")
    to_delete = tmp_path / "to_delete.md"
    to_delete.write_text("# Will be deleted")
    repo.index.add([str(base_file), str(txt_file), str(to_delete)])
    repo.index.commit("initial commit")

    repo.create_head("main")

    branch_name = "feature/test-branch"
    repo.create_head(branch_name)
    repo.heads[branch_name].checkout()

    added_file = tmp_path / "added.md"
    added_file.write_text("# Added\nnew content")
    repo.index.add([str(added_file)])

    base_file.write_text("# Existing\nmodified content")
    repo.index.add([str(base_file)])

    to_delete.unlink()
    repo.index.remove([str(to_delete)])

    new_txt = tmp_path / "new.txt"
    new_txt.write_text("also not markdown")
    repo.index.add([str(new_txt)])

    repo.index.commit("feature changes")

    return tmp_path, branch_name


def test_added_file(git_repo: tuple[Path, str]) -> None:
    repo_path, branch = git_repo
    changes = enumerate_changes(repo_path, branch, "main")
    added = [c for c in changes if c.change_type == "added"]
    assert len(added) >= 1
    added_paths = [c.path for c in added]
    assert "added.md" in added_paths
    for c in added:
        if c.path == "added.md":
            assert c.content is not None
            assert len(c.content) > 0


def test_modified_file(git_repo: tuple[Path, str]) -> None:
    repo_path, branch = git_repo
    changes = enumerate_changes(repo_path, branch, "main")
    modified = [c for c in changes if c.change_type == "modified"]
    modified_paths = [c.path for c in modified]
    assert "existing.md" in modified_paths


def test_deleted_file(git_repo: tuple[Path, str]) -> None:
    repo_path, branch = git_repo
    changes = enumerate_changes(repo_path, branch, "main")
    deleted = [c for c in changes if c.change_type == "deleted"]
    deleted_paths = [c.path for c in deleted]
    assert "to_delete.md" in deleted_paths
    for c in deleted:
        if c.path == "to_delete.md":
            assert c.content is None


def test_non_md_excluded(git_repo: tuple[Path, str]) -> None:
    repo_path, branch = git_repo
    changes = enumerate_changes(repo_path, branch, "main")
    paths = [c.path for c in changes]
    assert not any(p.endswith(".txt") for p in paths)


def test_nonexistent_branch(git_repo: tuple[Path, str]) -> None:
    repo_path, _ = git_repo
    with pytest.raises(ValueError, match="Branch not found"):
        enumerate_changes(repo_path, "nonexistent-branch", "main")
