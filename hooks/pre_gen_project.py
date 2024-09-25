"""Ran before the template rendering to ensure the configuration is correct."""

from re import match
from sys import exit


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.__project_name_underscored }}"

if not match(MODULE_REGEX, module_name):
    print(
        f"ERROR: '{module_name}' is not a valid Python module name! "
        f"Please do not edit '__project_name_underscored' in the cookiecutter.json file, "
        f"it will be generated from 'project_name' automatically. If you need to change it, "
        f"please update the 'project_name' field in the cookiecutter.json file and ensure it does "
        f"not contain any characters that are not allowed in Python module names, "
        f"e.g. spaces, hyphens, etc. If this is not the case, please report this as a bug."
    )

    # Exit with a non-zero status to indicate failure, as documented at
    # https://cookiecutter.readthedocs.io/en/2.6.0/advanced/hooks.html#hook-execution
    exit(1)
