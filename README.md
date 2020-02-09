# Plover Midi4Text

[Midi4Text](https://www.midi4text.com/) English orthographic system implementation for [Plover](https://github.com/openstenoproject/plover).

## Development

Update README.rst with [pandoc](https://pandoc.org/):

```bash
pandoc README.md -o README.rst
```

Install dependencies with [pipenv](https://github.com/pypa/pipenv):

```bash
pipenv install --dev
```

Build and publish to PyPI with [twine](https://twine.readthedocs.io/en/latest/):

```bash
pipenv run python setup.py sdist bdist_wheel
twine upload dist/*
```
