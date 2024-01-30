'''Main module for the CLI.'''

from os.path import abspath
from sys import argv, exit as _exit

from tidydev import __version__, analyze, ProgramError


def main():
    '''Main.'''
    command = argv[1:]
    match command:
        case ['help']: _handle_help()
        case ['version']: _handle_version()
        case ['analyze', path]: _handle_analyze(path)
        case ['analyze-git', path]: _handle_analyze_git(path)
        case _: raise ProgramError.command_not_found(' '.join(command))


def _handle_help() -> None:
    print('''Usage: tidydev <commands>

Available commands:
    help              - show this help
    version           - show version
    analyze <path>    - analyze the given path for git repositories and build files
    analyze-git <path>- analyze the given path for git repositories and build files and show git status
''')


def _handle_version() -> None:
    print(f'tidydev {__version__.VERSION}')


def _handle_analyze(path: str) -> None:
    analysis = analyze.analyze(abspath(path))
    analyze.print_result(analysis)


def _handle_analyze_git(path: str) -> None:
    analysis = analyze.analyze(abspath(path))
    for directory in analysis.directories:
        print(f'Analyzing git repository {directory.path}')
        analyze.analyze_git(directory)

    print()
    analyze.print_git_result(analysis)


if __name__ == '__main__':
    try:
        main()
    except ProgramError as e:
        print(e.message)
        _exit(e.exit_code)
    except KeyboardInterrupt:
        print('Program was interrupted by user')
        _exit(1)
