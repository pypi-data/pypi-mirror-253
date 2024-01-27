# yayaml

The `yayaml` package provides extensions to `ruamel.yaml` that allow creating some often-needed Python objects directly via YAML tags and making it easier to represent custom objects when writing YAML files.

yay 🥳

[Visit the project repository][repository].


## Installation
First, create and/or enter a Python virtual environment in which you would like to install this package.

The package can then be installed using [pip]:

```bash
pip install git+https://gitlab.com/blsqr/yayaml
```



## Use

```python
import yayaml as yay

yay.yaml.load("{foo: bar}")
yay.load_yml("path/to/file.yml")
yay.write_yml(dict(foo="bar"), path="path/to/output.yml")
```

🚧


## For developers
If you plan on developing for this project, installation should be done from a local `git clone` of the repository.
After having the project cloned, you may want to enter a virtual environment for development.

To then install the package (in editable mode), run:

```
cd yayaml
pip install -e .[dev]
```

which will include development-related dependencies (for tests and building of the documentation).

To automatically run [pre-commit][pre-commit] hooks, install the configured git hooks using `pre-commit install`.


### Running tests
Enter the virtual environment, then run [pytest][pytest]:

```bash
python -m pytest -v tests/ --cov=yayaml --cov-report=term-missing
```

### Building the documentation
```bash
cd doc
make doc
make linkcheck  # optional
make doctest    # optional
```

The documentation can then be found in [`doc/_build/html`](doc/_build/html/).

To automatically generate figures, set the `YAYAML_USE_TEST_OUTPUT_DIR` environment variable before invoking `make doc`.

```bash
export YAYAML_USE_TEST_OUTPUT_DIR=yes
```


## License
The `yayaml` package is open-source software licensed under BSD 2-clause, see [`LICENSE`](LICENSE).

### Copyright holders

- Yunus Sevinchan (*maintainer*)


[repository]: https://gitlab.com/blsqr/yayaml
[pip]: https://pip.pypa.io/en/stable/
[pytest]: https://pytest.org/
[pre-commit]: https://pre-commit.com
