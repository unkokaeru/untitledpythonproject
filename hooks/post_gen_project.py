"""Ran after the template rendering to initialise the project asynchronously.

Re-written from:
https://github.com/zillionare/python-project-wizard/blob/master/hooks/post_gen_project.py
https://github.com/zillionare/python-project-wizard/blob/master/hooks/aioproc.py
"""

import asyncio
import functools
import os
import shlex
from asyncio.subprocess import Process
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import ParamSpec, TypeVar

from colorama import Fore, Style

Parameters = ParamSpec("Parameters")  # Type hint for the parameters of a function (generic)
ReturnType = TypeVar("ReturnType")  # Type hint for the return type of a function (generic)

PROJECT_DIRECTORY = Path.cwd().resolve()
GIT_DIRECTORY = PROJECT_DIRECTORY / ".git"


def print_with_style(message: str, color: str = Fore.BLUE, style: str = Style.NORMAL) -> None:
    """
    Print a message with a specific style and color, then reset the style.

    Parameters
    ----------
    message : str
        The message to print.
    color : str, optional
        The color of the message, by default Fore.BLUE
    style : str, optional
        The style of the message, by default Style.NORMAL

    Notes
    -----
    This function is used to print a message with a specific style and color
    to the console. It is useful for printing messages in different colors
    and styles to make them stand out from the rest of the output. It resets
    the style after printing the message to avoid affecting other output.
    """
    print(style, color, message, Style.RESET_ALL)


def run_command_with_message(
    message: str, command: list[str], working_directory: Path = None
) -> None:
    """
    Run a command with a message and print the output to the console.

    Parameters
    ----------
    message : str
        The message to print before running the command.
    command : list[str]
        The command to run.
    working_directory : Path, optional
        The working directory of the subprocess, by default None.
    """
    if working_directory is None:
        working_directory = PROJECT_DIRECTORY

    print_with_style(message)
    execute(*command, working_directory=working_directory)


async def _echo(data_stream: asyncio.StreamReader) -> None:
    """
    Echo the output of a process to the console.

    Parameters
    ----------
    data_stream : asyncio.StreamReader
        The stream of data to read from.

    Raises
    ------
    Exception
        If the process returns an error.

    Examples
    --------
    >>> await _echo(data_stream)

    Notes
    -----
    This function is an async function that reads the output of a
    process and prints it to the console. It also checks for any
    warnings or errors in the output and raises an exception if
    an error is found.
    """
    while True:
        # Read and decode a line of output from the process
        line_bytes = await data_stream.readline()
        line = line_bytes.decode("utf-8")

        # If the line is empty, break out of the loop
        if not line:
            break

        # Style the output based on the type of message
        line = line.rstrip("\n")
        if line.upper().startswith("WARNING"):
            print_with_style(line, Fore.YELLOW)
        elif line.upper().startswith("ERROR"):
            print_with_style(line, Fore.RED)
            raise Exception(line)
        else:
            print(line)


def async_run(
    func: Callable[Parameters, Awaitable[ReturnType]]
) -> Callable[Parameters, Awaitable[ReturnType]]:
    """
    Decorator to run an async function in the main thread.

    Arguments
    ---------
    func: Callable
        The function to run asynchronously.

    Returns
    -------
    Callable
        The wrapped function.

    Examples
    --------
    >>> @async_run
    ... async def main() -> None:
    ...     print("Hello, world!")
    ...
    >>> main()
    Hello, world!

    Notes
    -----
    This decorator is used to run an async function in the main
    thread. It is useful for running async functions in a synchronous
    context, such as in a script or in the main block of a module.
    """

    @functools.wraps(func)
    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> Awaitable[ReturnType]:
        return asyncio.run(func(*args, **kwargs))

    return wrapper


async def async_io_process(
    *commands: str,
    output_handler: Callable = _echo,
    error_handler: Callable = _echo,
    use_parent_environment: bool = True,
    run_detached: bool = False,
    working_directory: Path | None = None,
) -> Process:
    """
    Run a series of commands asynchronously and display their output.

    Arguments
    ---------
    *commands: str
        The commands to run.
    output_handler: Callable
        The function to handle stdout, defaults to echo.
    error_handler: Callable
        The function to handle stderr, defaults to echo.
    use_parent_environment: bool
        Whether to inherit the parent process's environment variables, defaults to True.
    run_detached: bool
        Whether to run the command independently of the parent process, defaults to False.
    working_directory: Path
        The working directory of the subprocess, defaults to None.

    Examples
    --------
    >>> async_io_process("ls")
    >>> async_io_process("ping -c 10 www.baidu.com")
    >>> async_io_process("ping", "-c", "10", "www.baidu.com")
    >>> async_io_process("python -m http.server", run_detached=True)
    """
    current_directory = Path.cwd()

    try:
        if working_directory != current_directory:
            os.chdir(working_directory)

        if len(commands) == 1 and isinstance(commands[0], str):
            commands = shlex.split(commands[0])

        environment = os.environ.copy() if use_parent_environment else None

        subprocess = await asyncio.create_subprocess_exec(
            *commands,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            start_new_session=run_detached,
            env=environment,
        )

        if output_handler:
            asyncio.ensure_future(output_handler(subprocess.stdout))
        if error_handler:
            asyncio.ensure_future(error_handler(subprocess.stderr))

        return subprocess
    finally:
        os.chdir(current_directory)  # Always return to the original directory


@async_run
async def execute(*command_to_run: str, working_directory: Path | None = None) -> None:
    """
    Run a command in a directory.

    Arguments
    ---------
    *command_to_run: str
        The command to run, given as a series of strings.
    working_directory: Path
        The working directory of the subprocess, defaults to None.

    Examples
    --------
    >>> execute("ls")
    >>> execute("ping -c 10 www.baidu.com")
    >>> execute("ping", "-c", "10", "www.baidu.com")

    Notes
    -----
    This function is a wrapper around the async_io_process function,
    which is a coroutine that runs a command asynchronously.
    """
    if working_directory is None:
        working_directory = Path.cwd()

    try:
        proc = await async_io_process(*command_to_run, working_directory=working_directory)
        await proc.wait()
    except Exception as e:
        print(e)
        print_with_style(
            f"Failed to run command: {' '.join(command_to_run)} in {working_directory}. "
            f"You may need to re-run the command.",
            Fore.YELLOW,
        )
    else:
        print_with_style(
            f"Command {' '.join(command_to_run)} ran successfully in {working_directory}.",
            Fore.GREEN,
        )


if __name__ == "__main__":
    # Initialise and configure the git repository
    if not GIT_DIRECTORY.exists():
        run_command_with_message(
            "Initialising git repository...",
            ["git", "init"],
        )
        run_command_with_message(
            "Configuring git user name...",
            ["git", "config", "user.name", "{{ cookiecutter.author_username }}"],
        )
        run_command_with_message(
            "Configuring git user email...",
            ["git", "config", "user.email", "{{ cookiecutter.author_email }}"],
        )
        run_command_with_message(
            "Configuring default git branch name...",
            ["git", "config", "init.defaultBranch", "main"],
        )

    # Create a virtual environment to handle dependencies
    run_command_with_message(
        "Creating virtual environment and installing dependencies...",
        ["poetry", "install"],
    )

    # Export the requirements to relevant files
    run_command_with_message(
        "Exporting requirements to files...",
        ["bash", "scripts/export_requirements.sh"],
    )

    # Add and commit the changes to the git repository
    run_command_with_message(
        "Adding changes to the git repository...",
        ["git", "add", "."],
    )
    run_command_with_message(
        "Committing changes to the git repository...",
        ["git", "commit", "-m", "Initial commit"],
    )

    # Run the release script (hardcoded to minor initial release)
    run_command_with_message(
        "Running the release script...",
        ["bash", "scripts/release.sh", "minor", "{{ cookiecutter.PYPI_TOKEN }}"],
    )
