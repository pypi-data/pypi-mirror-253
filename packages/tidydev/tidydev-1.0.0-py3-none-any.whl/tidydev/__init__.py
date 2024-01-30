"""Initializer."""

from __future__ import annotations


class ProgramError(Exception):
    """A generic program error containing a message."""
    _message = ''
    _exit_code = 1

    def __init__(self, message='Error while executing the program', exit_code=1):
        super().__init__(message)
        self._message = message
        self._exit_code = exit_code

    @property
    def message(self) -> str:
        """Getter for the message."""
        return self._message

    @property
    def exit_code(self) -> int:
        """Getter for the exit code"""
        return self._exit_code

    @staticmethod
    def command_not_found(command: str) -> ProgramError:
        """Creates a `ProgramError` containing a message that a command could not be parsed."""
        return ProgramError(f"""
🚧 Oops! An error occurred 🚧

   Input:   call of <tidydev {command}>
   Result:  failed during parsing commands
   Reason:  unknown command "{command}" (exit code 100)
   Details: The command you entered does not exist or misses arguments.
            Try <tidydev help> to get all available commands.
""", 100)
