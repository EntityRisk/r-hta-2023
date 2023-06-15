# Python for HTA: Why R shouldn't be the only language at the table

This repository contains the code used for the 2023 R for HTA workshop held on
June 12, 2023.

## Slides

The slides are contained in the [slides.pdf](slides.pdf) file.

## Dependencies

### Python

Python package dependencies are managed with
[poetry](https://github.com/python-poetry/poetry). If this is your first time
working with `poetry`, you will need to install it:

```commandline
pip install pipx
pipx install poetry
```

You can then install the required packages with:

```commandline
poetry install
```

and work from within the created virtual environment with:

```commandline
poetry shell
```

You can use a specific version of Python with:

```commandline
poetry env use /full/path/to/python
```

### R

While we recommend using [renv](https://github.com/rstudio/renv) to manage
R dependencies, all analyses are conducted with base R so it is not
needed here.

## Git

### Conventional commits

Commit message conventions not only make it easier to understand a commit
history, but make it easier to create automated tools. We like the
[conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
standard.

### Pre-commit

It's a good idea to use pre-commit hooks to catch bad style, files,
commit messages, etc. before making a commit. After you install dependencies
with `poetry`, you should install [pre-commit](https://pre-commit.com/), a
framework for managing pre-commit hooks in multiple languages.

```commandline
pre-commit install
```

## Run the analyses in the slides

The scripts to run the Python analyses are contained in `aa_run.py` and the
scripts to run the R analyses are contained in `aa_run.R`.
