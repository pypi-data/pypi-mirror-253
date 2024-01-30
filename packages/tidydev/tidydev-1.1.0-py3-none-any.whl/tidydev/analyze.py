'''
Analyzes a directory and its subdirectories for git repositories and build files.
'''

from dataclasses import dataclass
from os import sep, listdir
from os.path import basename, isdir, isfile
from typing import Any, Optional

from git import Repo
from tabulate import tabulate


LABEL_FILES: dict[str, set[str]] = {
    'npm': {'package.json'},
    'maven': {'pom.xml'},
    'gradle': {'build.gradle', 'build.gradle.kts'},
    'make': {'Makefile'},
    'cmake': {'CMakeLists.txt'},
    'ant': {'build.xml'},
    'sbt': {'build.sbt'},
    'cargo': {'Cargo.toml'},
    'go': {'go.mod'},
    'bundler': {'Gemfile'},
    'pip': {'requirements.txt'},
    'pipenv': {'Pipfile'},
    'python': {'setup.py'},
}

LABEL_DIRECTORIES: dict[str, set[str]] = {
    'python': {'venv'}
}


@dataclass
class GitStatus:
    '''Represents the status of a git directory.'''

    uncommitted_changes: bool
    current_branch: str
    remotes: list[str]


@dataclass
class Directory:
    '''Represents an analyzed directory.'''

    path: str
    is_git: bool
    git_status: Optional[GitStatus]
    build_labels: list[str]

    def __init__(self, path: str):
        self.path = path
        self.is_git = False
        self.git_status = None
        self.build_labels = []


@dataclass
class Analysis:
    '''Represents the result of an analysis.'''

    path: str
    directories: list[Directory]


def analyze(path: str) -> Analysis:
    '''Analyzes the given path for git repositories and build files and returns the result.'''

    directories = []

    for element in sorted(listdir(path)):
        directory_path = sep.join([path, element])
        if isdir(directory_path):
            directory = Directory(directory_path)
            directory.is_git = isdir(sep.join([directory_path, '.git']))

            files = {file for file in listdir(directory_path) if isfile(sep.join([directory_path, file]))}
            _analyze_labels(files, directory, LABEL_FILES)

            sub_directories = {directory for directory in listdir(directory_path) if isdir(sep.join([directory_path, directory]))}
            _analyze_labels(sub_directories, directory, LABEL_DIRECTORIES)

            directories.append(directory)

    return Analysis(path, directories)


def analyze_git(directory: Directory) -> None:
    '''Analyzes the given directory for git status.'''

    if not directory.is_git:
        return

    repo = Repo(directory.path)
    directory.git_status = GitStatus(
        uncommitted_changes=repo.is_dirty(untracked_files=True),
        current_branch=repo.active_branch.name,
        remotes=[remote.name for remote in repo.remotes]
    )


def print_result(analysis: Analysis) -> None:
    '''Prints the result of the analysis to the console.'''

    print(f'Analysis result of {analysis.path} ({len(analysis.directories)} projects):')
    print()

    print(tabulate(
        _transform_to_basic_tabulate_list(analysis.directories),
        headers=['Project', 'Git', 'Labels'],
        tablefmt='psql',
        showindex=False
    ))


def print_git_result(analysis: Analysis) -> None:
    '''Prints the result of the git analysis to the console.'''

    print(f'Analysis result of {analysis.path} ({len(analysis.directories)} projects):')
    print()

    print(tabulate(
        _transform_to_git_tabulate_list(analysis.directories),
        headers=['Project', 'Labels', 'Uncommitted Changes', 'Current Branch', 'Remotes'],
        tablefmt='psql',
        showindex=False
    ))


def _analyze_labels(sub: set[str], directory: Directory, labels: dict[str, set[str]]):
    for label, directory_names in labels.items():
        if sub & directory_names:
            directory.build_labels.append(label)

    directory.build_labels = list(set(directory.build_labels))


def _join_labels(labels: list[str]) -> str:
    return f'{", ".join(labels)}'


def _transform_to_basic_tabulate_list(directories: list[Directory]) -> list[list[Any]]:
    data: list[list[Any]] = []
    for directory in directories:
        data.append([
            basename(directory.path),
            'yes' if directory.is_git else 'no',
            _join_labels(directory.build_labels)
        ])

    return data


def _transform_to_git_tabulate_list(directories: list[Directory]) -> list[list[Any]]:
    data: list[list[Any]] = []
    for directory in directories:
        if directory.git_status:
            data.append([
                basename(directory.path),
                _join_labels(directory.build_labels),
                'yes' if directory.git_status.uncommitted_changes else 'no',
                directory.git_status.current_branch,
                _join_labels(directory.git_status.remotes)
            ])

    return data
