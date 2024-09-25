Welcome to the documentation for untitledpythonproject!
=================================================================

.. image:: https://img.shields.io/github/v/tag/unkokaeru/untitledpythonproject?label=version
    :target: https://github.com/unkokaeru/untitledpythonproject
    :alt: GitHub tag (latest by date)
.. image:: https://tokei.rs/b1/github/unkokaeru/untitledpythonproject?category=code
    :target: https://github.com/unkokaeru/untitledpythonproject
    :alt: Lines Of Code
.. image:: https://img.shields.io/github/actions/workflow/status/unkokaeru/untitledpythonproject/continuous_integration.yml?label=tests
    :target: https://github.com/unkokaeru/untitledpythonproject/actions/workflows/continuous_integration.yml
    :alt: Continuous Integration (CI) Tests
.. image:: https://img.shields.io/github/last-commit/unkokaeru/untitledpythonproject
    :target: https://github.com/unkokaeru/untitledpythonproject/actions/workflows/continuous_integration.yml
    :alt: GitHub last commit

Yet another Python project template.

-  [untitledpythonproject](#untitledpythonproject)
    -  `Features <#features>`__
    -  `Installation and Usage <#installation-and-usage>`__
    -  `Documentation <#documentation>`__
    -  `Contributing <#contributing>`__
    -  `License <#license>`__

Features
--------

-  ☒ Installable via Cookiecutter
-  ☒ Command-line interface
-  ☒ Interactive documentation
-  ☐ Project validation and auto-upgrading
-  ☐ Automatic test generation
-  ☐ GUI generation

Installation and Usage
----------------------

Before starting, you'll need a GitHub account and Poetry account. For Poetry, you should go to your account settings and click on "Add API token" within the "API tokens" section where you can then name and add a token. Once created, copy the token and add it Poetry's config with this command:

.. code-block:: bash

    poetry config pypi-token.pypi your-api-token

To create a project with untitledpython project, simply run:

.. code-block:: bash

    pip install cookiecutter
    cookiecutter gh:unkokaeru/untitledpythonproject

Usage
-----

After installation, you can use untitledpythonproject by
running:

.. code:: bash

    $ python3 -m untitledpythonproject
    # or
    $ untitledpythonproject

Documentation
-------------

For more information, you can find the documentation within the
`docs <./docs/index.html>`__ directory or on the project's [GitHub
Pages](https://unkokaeru.github.io/untitledpythonproject/).

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