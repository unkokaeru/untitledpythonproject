# {{ cookiecutter.project_name }}

[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}?label=version)](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }})
[![Lines Of Code](https://tokei.rs/b1/github/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}?category=code)](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }})
[![Continuous Integration (CI) Tests](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/continuous_integration.yml?label=tests)](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }})
[![GitHub last commit](https://img.shields.io/github/last-commit/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }})](https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }})

{{ cookiecutter.project_short_description }}

- [{{ cookiecutter.project_name }}](#{{ cookiecutter.project_name }})
    - [Features](#features)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Documentation](#documentation)
    - [Contributing](#contributing)
    - [License](#license)

## Features

- [x] Installable via pip
- [x] Command-line interface
{% if cookiecutter.gui_required == 'true' %}
- [x] Graphical interface
{% endif %}
- [x] Interactive documentation
- [ ] Some new planned feature

## Installation

To install {{ cookiecutter.project_name }}, simply run:

```bash
pip install {{ cookiecutter.__project_name_dashed }}
```

## Usage

After installation, you can use {{ cookiecutter.project_name }} by running:

```bash
$ python3 -m {{ cookiecutter.__project_name_dashed}}
# or
$ {{ cookiecutter.__project_name_dashed}}
```

## Documentation
For more information, you can find the documentation within the [docs](./docs/index.html) directory or on the project's [GitHub Pages](https://{{ cookiecutter.author_username }}.github.io/{{ cookiecutter.__project_name_dashed }}/).

## Contributing

Contributions are welcome! Please refer to our [CONTRIBUTING.md](./CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.