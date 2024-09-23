"""main.py: Called when the package is ran as a script."""

from logging import shutdown as shutdown_logging

from .config.constants import Constants
from .interface.command_line import command_line_interface
from .logs.setup_logging import setup_logging


def main() -> None:
    """
    Overall control flow of the application.

    Notes
    -----
    This function is the entry point for the application, so only really
    contains overall control flow logic. The actual work is done in the
    other modules.
    """
    # Get the arguments from the command line
    user_arguments = command_line_interface()

    # Setup logging
    setup_logging(
        user_arguments["log_output_location"],
        console_logging_level=(
            "DEBUG" if user_arguments["verbose"] else Constants.LOGGING_LEVEL_CONSOLE_DEFAULT
        ),
    )

    # Main application logic
    # TODO: Implement the main application logic

    shutdown_logging()


if __name__ == "__main__":
    main()
