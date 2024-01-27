from pathlib import Path
from unittest import mock

from cappa.testing import CommandRunner


def generated_project_files(project_name) -> list[str]:
    return [
        project_name,
        "pyproject.toml",
        "README.md",
        ".gitignore",
        "config",
        ".github",
        "deploy",
        "tests",
        "manage.py",
        ".env.template",
    ]


def test_start_project(runner: CommandRunner):
    runner.invoke("start-project", "dotfm", "--skip-new-version-check")
    assert Path("dotfm").exists()
    # sourcery skip: no-loop-in-tests
    project_files = [file.name for file in Path("dotfm").iterdir()]
    for file_name in generated_project_files("dotfm"):
        assert file_name in project_files


def test_user_name_and_email(runner: CommandRunner, git_user_infos):
    name, email = git_user_infos
    runner.invoke("start-project", "dotfm", "--skip-new-version-check")
    pyproject_content = (Path("dotfm") / "pyproject.toml").read_text()
    assert name in pyproject_content
    assert email in pyproject_content


def test_no_internet_access(runner: CommandRunner):
    with mock.patch("socket.socket", side_effect=OSError("Network access is cut off")):
        runner.invoke("start-project", "dotfm", "--skip-new-version-check")
    assert Path("dotfm").exists()
    # sourcery skip: no-loop-in-tests
    project_files = [file.name for file in Path("dotfm").iterdir()]
    for file_name in generated_project_files("dotfm"):
        assert file_name in project_files
