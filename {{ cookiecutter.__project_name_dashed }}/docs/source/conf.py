"""conf.py: Configuration file for the Sphinx documentation builder."""

project = "{{ cookiecutter.__project_name_dashed }}"
copyright = "{{ cookiecutter.copyright_year }}, {{ cookiecutter.author_name }}"
author = "{{ cookiecutter.author_name }}"

extensions = ["sphinx.ext.napoleon"]

html_theme = "alabaster"
