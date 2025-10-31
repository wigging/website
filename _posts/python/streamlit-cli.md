---
title: Streamlit CLI Entry Point
date: September 4, 2025
tags: python
---

Putting a Streamlit app in a Python package provides a nice user interface to the package's features. However, a Streamlit app is typically run as an individual Python script instead of a package's command line entry point. To call the Streamlit app using a package's command line interface (CLI), the cli module in Streamlit can be invoked to run the app from within the Python code.

Below is the file structure of a project named "streamlit-pkg" that contains a Python package named "stpkg".

```text
streamlit-pkg/
├── src/
│   └── stpkg/
│       ├── __init__.py
│       ├── adder.py
│       ├── app.py
│       └── cli.py
├── tests/
│   └── test_adder.py
├── pyproject.toml
├── README.md
└── uv.lock
```

The contents of the `__init__.py`, `adder.py`, and `app.py` files are shown below. More information about each file is provided in the comments.

```python
# __init__.py
# Make the `add` function available to users.

from .adder import add

__all__ = ["add"]
```

```python
# adder.py
# Provides an `add` function in the `stpkg` package.

def add(x: float, y: float) -> float:
    """Add two numbers."""
    z = x + y
    return z
```

```python
# app.py
# Streamlit app within the `stpkg` package.

import streamlit as st
from stpkg.adder import add


def main():
    """Create content for the streamlit app."""

    st.markdown("""
    # Streamlit app

    Hello there!
    """)

    total = add(12, 5.5)
    st.markdown(f"Total is {total}")


if __name__ == "__main__":
    main()
```

The content of the `cli.py` file is shown below. Notice the use of the cli module from the Streamlit package which is used to run `app.py` that contains the Streamlit application code. The Streamlit documentation does not mention the use of this module so it may not be supported for public use; however, this seems to be the only way to run a Streamlit app from within Python code.

```python
# cli.py
# The command-line interface for the `stpkg` package.

import argparse
import importlib.resources
from streamlit.web import cli


def main():
    """Command line entry point for the package."""

    parser = argparse.ArgumentParser(description="CLI package with Streamlit app")
    parser.add_argument("run", help="enter 'go' to run streamlit app")
    args = parser.parse_args()

    if args.run == "go":
        print("Run the Streamlit app ...")

        with importlib.resources.path("stpkg", "app.py") as app_file:
            cli.main_run([str(app_file)])
```

Below is the content of the `pyproject.toml` file. Notice the CLI entry point for the package is defined as the main function in the `src/stpkg/cli.py` file. This allows the `stpkg` package to be installed as a command line tool. As such, the Streamlit app in the package can be run by doing `stpkg go` in the terminal.

```toml
# pyproject.toml

[build-system]
requires = ["uv_build>=0.8.11,<0.9.0"]
build-backend = "uv_build"

[project]
name = "stpkg"
version = "0.1.0"
description = "Streamlit app in a package"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "streamlit>=1.48.1",
]

[dependency-groups]
dev = [
    "pytest>=8.4.1",
    "ruff>=0.12.9",
]

[project.scripts]
stpkg = "stpkg.cli:main"
```

## Further reading

More information about Streamlit is available at <https://streamlit.io>. All of the Python code discussed in this article is available in the `pythonic/projects/streamlit-pkg` directory in the [pythonic](https://github.com/wigging/pythonic) GitHub repo. 
