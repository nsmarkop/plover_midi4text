# Plover Midi4Text

[Midi4Text](https://www.midi4text.com/) English orthographic system implementation for [Plover](https://github.com/openstenoproject/plover).

**Warning:** Updating the plugin does not always update the default dictionaries to their latest versions. Check in the [plugin repository](https://github.com/nsmarkop/plover_midi4text) or [here](https://github.com/Sillabix/Midi4Text-ortographic-system) for the most up to date versions of the dictionary files.

## Development

Update README.rst with [pandoc](https://pandoc.org/):

```bash
pandoc README.md -o README.rst
```

Set up the virtual environment and install dependencies via [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Update dictionary files:

```bash
uv run update_dictionaries.py
```

Build and publish to PyPI:

```bash
uv build
uv publish --publish-url https://test.pypi.org/legacy/ --dry-run
uv publish --publish-url https://test.pypi.org/legacy/
uv publish
```

NOTE: You will be prompted to enter your token, which you can create / find under Account Settings -> API tokens on PyPI.
