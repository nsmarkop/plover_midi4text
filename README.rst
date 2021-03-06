Plover Midi4Text
================

`Midi4Text <https://www.midi4text.com/>`__ English orthographic system
implementation for
`Plover <https://github.com/openstenoproject/plover>`__.

**Warning:** Updating the plugin does not always update the default
dictionaries to their latest versions. Check in the `plugin
repository <https://github.com/nsmarkop/plover_midi4text>`__ or
`here <https://github.com/Sillabix/Midi4Text-ortographic-system>`__ for
the most up to date versions of the dictionary files.

Development
-----------

Update README.rst with `pandoc <https://pandoc.org/>`__:

.. code:: bash

    pandoc README.md -o README.rst

Install dependencies with `pipenv <https://github.com/pypa/pipenv>`__:

.. code:: bash

    pipenv install --dev

Build and publish to PyPI with
`twine <https://twine.readthedocs.io/en/latest/>`__:

.. code:: bash

    pipenv run python setup.py sdist bdist_wheel
    pipenv run twine upload dist/*
