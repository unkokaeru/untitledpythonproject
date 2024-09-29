Welcome to the documentation for {{ cookiecutter.project_name }}!
=================================================================

.. image:: https://img.shields.io/github/v/tag/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}?label=version
    :target: https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}
    :alt: GitHub tag (latest by date)
.. image:: https://tokei.rs/b1/github/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}?category=code
    :target: https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}
    :alt: Lines Of Code
.. image:: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/continuous_integration.yml?label=tests
    :target: https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/actions/workflows/continuous_integration.yml
    :alt: Continuous Integration (CI) Tests
.. image:: https://img.shields.io/github/last-commit/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}
    :target: https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.__project_name_dashed }}/actions/workflows/continuous_integration.yml
    :alt: GitHub last commit

{{ cookiecutter.project_short_description }}

-  [{{ cookiecutter.project_name }}](#{{ cookiecutter.project_name }})
    -  `Features <#features>`__
    -  `Installation <#installation>`__
    -  `Usage <#usage>`__
    -  `Documentation <#documentation>`__
    -  `Contributing <#contributing>`__
    -  `License <#license>`__

Features
--------

-  ☒ Installable via pip
-  ☒ Command-line interface
{% if cookiecutter.gui_required == 'true' %}
-  ☒ Graphical interface
{% endif %}
-  ☒ Interactive documentation
-  ☐ Some new planned feature

Installation
------------

To install {{ cookiecutter.project_name }}, simply run:

.. code-block:: bash

    pip install {{ cookiecutter.__project_name_dashed }}

Usage
-----

After installation, you can use {{ cookiecutter.project_name }} by
running:

.. code:: bash

    $ python3 -m {{ cookiecutter.__project_name_dashed}}
    # or
    $ {{ cookiecutter.__project_name_dashed}}

Documentation
-------------

For more information, you can find the documentation within the
`docs <./docs/index.html>`__ directory or on the project's [GitHub
Pages](https://{{ cookiecutter.author_username }}.github.io/{{
cookiecutter.__project_name_dashed }}/).

Contributing
------------

Contributions are welcome! Please refer to our
`CONTRIBUTING.md <./CONTRIBUTING.md>`__ for more information.

License
-------

This project is licensed under the MIT License - see the
`LICENSE <./LICENSE>`__ file for details.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`