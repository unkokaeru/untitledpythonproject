# Contributing to {{ cookiecutter.project_name }}

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Share with your following
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues


## Table of Contents

- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Styleguides](#styleguides)
- [Best Practices](#best-practices)
- [Commit Messages](#commit-messages)
- [Documentation Strings](#documentation-strings)


## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](https://{{ cookiecutter.author_username }}.github.io/{{ cookiecutter.__project_name_dashed }}/).

Before you ask a question, it is best to search for existing [Issues](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.


## I Want To Contribute

> ### Legal Notice
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.


### Reporting Bugs

#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://{{ cookiecutter.author_username }}.github.io/{{ cookiecutter.__project_name_dashed }}/). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?


#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <{{ cookiecutter.author_email }}>.

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be implemented by someone.


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for {{ cookiecutter.project_name }}, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.


#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://{{ cookiecutter.author_username }}.github.io/{{ cookiecutter.__project_name_dashed }}/) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.


#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
{% if cookiecutter.gui_required == 'true' %}
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
{% endif %}
- **Explain why this enhancement would be useful** to most {{ cookiecutter.project_name }} users. You may also want to point out the other projects that solved it better and which could serve as inspiration.


### Making a Direct Contribution

Contributing directly to the codebase is a fantastic way to engage with the project and help improve it.

Before starting, you'll need [git](https://git-scm.com/), [poetry](https://python-poetry.org/), and [tox](https://tox.wiki/en/latest/). Then you can clone the repository and instal the development dependencies like so:

```bash
$ git clone https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}
$ cd {{ cookiecutter.__project_name_dashed }}
$ poetry install --with dev
```

Run tests like this:

```bash
$ tox
```

And lint and format your code like this:

```bash
$ tox -e lint
```

#### Best Practices

1. **Follow the Code Style**: Ensure that your code adheres to the project's coding standards. This includes using descriptive variable, function, and class names, and avoiding shorthand. All code should be well-typed and easy to read without the need for extensive comments.

2. **Use Semantic Versioning**: When making changes, be mindful of the versioning scheme. Increment the version number appropriately based on the nature of your changes (major, minor, or patch).

3. **Avoid Magic Numbers and Strings**: All constants should be defined in a dedicated `Constants` class or similar structure within the `config` directory. This makes the code more maintainable and understandable.

4. **Implement Logging**: Include logging statements throughout your code to facilitate debugging. Use appropriate logging levels (e.g., `logger.debug`, `logger.info`, `logger.warning`, etc.) to capture relevant information about the execution flow and state.

5. **Write Tests**: Ensure that your contributions are covered by tests. This helps maintain the integrity of the codebase and prevents regressions. Follow the existing testing framework and conventions used in the project.

6. **Document Your Code**: Use numpy-style docstrings for all public functions and classes. Include sections for parameters, return/raise values, examples, and notes where applicable. This enhances the usability of your code and helps other contributors understand your work.

7. **Review Your Changes**: Before submitting your contribution, review your code for any potential issues, such as unused imports, formatting inconsistencies, or logical errors. Run the tests to ensure everything passes.

8. **Engage with the Community**: If you have questions or need clarification while working on your contribution, feel free to reach out through the appropriate channels.

#### Commit Messages

When committing your changes, please adhere to the Angular commit message format. This structure enhances the readability of the commit history. Normally, this includes a body and an optional footer, as well as an optional scope within the header, but for simplicity we just use the header section. This may change in the future.

**Note**: This isn't standard, but I to signifying a breaking change (e.g. one that will update the version from 0.x.x to 1.0.0), I add an exclamation mark after the type. For example,

```
feat!: breaking feature
```

##### Commit Message Header

The header is mandatory and must follow this format:

```
<type>: <short summary>
```

- **type**: Must be one of the following:
  - **build**: Changes that affect the build system or external dependencies.
  - **ci**: Changes to CI configuration files and scripts.
  - **docs**: Documentation only changes.
  - **feat**: A new feature.
  - **fix**: A bug fix.
  - **perf**: A code change that improves performance.
  - **refactor**: A code change that neither fixes a bug nor adds a feature.
  - **test**: Adding missing tests or correcting existing tests.

- **short summary**: A concise description of the change in present tense. Do not capitalize the first letter and do not end with a period.

Example header:
```
feat: add logging functionality to data processing module
```

#### Documentation Strings

All new code should include comprehensive documentation strings. Follow these guidelines:

- Start each module with a docstring that provides a brief description of its purpose.
- For each function and class, include:
  - A summary of what it does.
  - A description of parameters and return/raise values, if applicable.
  - An "Examples" section demonstrating how to use the function or class.
  - A "Notes" section for any additional information that may be relevant.

Example of a function docstring:
```python
def calculate_mean(values: list[float]) -> float:
    """
    Calculate the mean of a list of numbers.

    Parameters
    ----------
    values : list[float]
        A list of numerical values.

    Returns
    -------
    float
        The mean of the provided values.

    Raises
    ------
    ValueError
        Returned if the input lsit is empty.

    Examples
    --------
    >>> calculate_mean([1, 2, 3, 4, 5])
    3.0

    Notes
    -----
    Sums each number within the inputted list and then divides
    by the length of the list to find an arithmetic mean.
    """
    if not values:
        raise ValueError("The input list cannot be empty.")

    return sum(values) / len(values)
```

By adhering to these best practices, you will help maintain the quality and consistency of the project, making it easier for everyone to collaborate effectively. Thank you for your contributions! 🎉


## Attribution
This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!