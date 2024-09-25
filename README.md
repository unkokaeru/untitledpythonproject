# untitledpythonproject

[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/unkokaeru/untitledpythonproject?label=version)](https://github.com/unkokaeru/untitledpythonproject)
[![Lines Of Code](https://tokei.rs/b1/github/unkokaeru/untitledpythonproject?category=code)](https://github.com/unkokaeru/untitledpythonproject)
[![Continuous Integration (CI) Tests](https://img.shields.io/github/actions/workflow/status/unkokaeru/untitledpythonproject/continuous_integration.yml?label=tests)](https://github.com/unkokaeru/untitledpythonproject)
[![GitHub last commit](https://img.shields.io/github/last-commit/unkokaeru/untitledpythonproject)](https://github.com/unkokaeru/untitledpythonproject)

Yet another Python project template.

- [untitledpythonproject](#untitledpythonproject)
    - [Features](#features)
    - [Installation and Usage](#installation-and-usage)
    - [Usage](#usage)
    - [Documentation](#documentation)
    - [Contributing](#contributing)
    - [License](#license)

## Features

- [x] Installable via Cookiecutter
- [x] Command-line interface
- [x] Interactive documentation
- [ ] Project validation and auto-upgrading
- [ ] Automatic test generation
- [ ] GUI generation

## Installation and Usage

Before starting, you'll need a GitHub account and Poetry account. For Poetry, you should go to your account settings and click on "Add API token" within the "API tokens" section where you can then name and add a token. Once created, copy the token and add it Poetry's config with this command:

```bash
poetry config pypi-token.pypi your-api-token
```

To create a project with untitledpython project, simply run:

```bash
pip install cookiecutter
```

and then

```bash
cookiecutter gh:unkokaeru/untitledpythonproject
```

## Documentation
For more information, you can find the documentation within the [docs](./docs/index.html) directory or on the project's [GitHub Pages](https://unkokaeru.github.io/untitledpythonproject/).

## Contributing

Contributions are welcome! Please refer to our [CONTRIBUTING.md](./CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.