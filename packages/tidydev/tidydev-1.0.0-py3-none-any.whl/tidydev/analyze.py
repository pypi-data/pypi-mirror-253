'''
Analyzes a directory and its subdirectories for git repositories and build files.
'''

from dataclasses import dataclass
from os import sep, listdir
from os.path import isdir, isfile


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
class Directory:
    '''Represents an analyzed directory.'''

    path: str
    is_git: bool
    build_labels: list[str]

    def __init__(self, path: str):
        self.path = path
        self.is_git = False
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


def print_result(analysis: Analysis) -> None:
    '''Prints the result of the analysis to the console.'''

    print(f'Analysis result of {analysis.path}:')
    print()

    git = [directory for directory in analysis.directories if directory.is_git]
    longest_label = max(len(f'{", ".join(directory.build_labels)}') for directory in git)
    print(f'The following directories are git repositories ({len(git)} of {len(analysis.directories)}):')
    for directory in git:
        _print_single_directory(directory, longest_label)

    print()

    non_git = [directory for directory in analysis.directories if not directory.is_git]
    longest_label = max(len(f'{", ".join(directory.build_labels)}') for directory in non_git)
    print(f'The following directories are not git repositories ({len(non_git)} of {len(analysis.directories)}):')
    for directory in non_git:
        _print_single_directory(directory, longest_label)


def _analyze_labels(sub: set[str], directory: Directory, labels: dict[str, set[str]]):
    for label, directory_names in labels.items():
        if sub & directory_names:
            directory.build_labels.append(label)


def _print_single_directory(directory: Directory, padding: int) -> None:
    labels = f'{", ".join(directory.build_labels)}'.ljust(padding, '·')
    print(f'{labels} {directory.path}')
