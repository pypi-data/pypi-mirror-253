"""Sets up the yayaml package installation"""

from setuptools import find_packages, setup

# .. Dependency lists .........................................................

INSTALL_DEPS = [
    "numpy < 2.0",
    "ruamel.yaml",
]

# Dependencies for running tests and general development of utopya
TEST_DEPS = [
    "pytest",
    "pytest-cov",
    "pre-commit",
]

# Dependencies for building the utopya documentation
DOC_DEPS = [
    "sphinx>=5.3,<6",
    "sphinx-book-theme",
    "sphinx-togglebutton",
    "ipython>=7.0",
    "myst-parser[linkify]",
    "pytest",
]

# .............................................................................


def find_version(*file_paths) -> str:
    """Tries to extract a version from the given path sequence"""
    import codecs
    import os
    import re

    def read(*parts):
        """Reads a file from the given path sequence, relative to this file"""
        here = os.path.abspath(os.path.dirname(__file__))
        with codecs.open(os.path.join(here, *parts), "r") as fp:
            return fp.read()

    # Read the file and match the __version__ string
    file = read(*file_paths)
    match = re.search(r"^__version__\s?=\s?['\"]([^'\"]*)['\"]", file, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string in " + str(file_paths))


# .............................................................................

DESCRIPTION = "yayaml makes yaml nicer. yay!"

LONG_DESCRIPTION = """
The `yayaml` package provides extensions to `ruamel.yaml` that allow creating
some often-needed Python objects directly via YAML tags and making it easier
to represent custom objects when writing YAML files.
"""
# .............................................................................


setup(
    name="yayaml",
    #
    # Package information
    version=find_version("yayaml", "__init__.py"),
    #
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    #
    url="https://gitlab.com/blsqr/yayaml",
    author="Yunus Sevinchan",
    author_email="Yunus Sevinchan <yunussevinchan@gmail.com>",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        #
        "Development Status :: 5 - Production/Stable",
        #
        "Topic :: Utilities",
    ],
    #
    # Package content
    packages=find_packages(exclude=("tests",)),
    data_files=[("", ["README.md", "LICENSE", "CHANGELOG.md"])],
    #
    # Dependencies
    install_requires=INSTALL_DEPS,
    extras_require=dict(
        test=TEST_DEPS,
        doc=DOC_DEPS,
        dev=TEST_DEPS + DOC_DEPS,
    ),
)
