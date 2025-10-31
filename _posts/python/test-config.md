---
title: Testing a Python Configuration Module
date: September 21, 2025
tags: python
---

A configuration (config) module is useful for storing configuration settings in a Python package or application. Values such as API keys and passwords are often defined as environment variables which are used in the module. An example of a config module is shown below. For this example, the module is part of a Python package named `mypkg`.

```python
# config.py in mypkg

import os

api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL", "http://localhost:8090")
save_path = "~/Desktop/downloads"
```

```text
my-project/
├── src/
│   └── mypkg/
│       ├── __init__.py
│       ├── config.py
│       └── downloader.py
├── tests/
│   ├── test_config.py
│   └── test_downloader.py
└── pyproject.toml
```

Other modules in the Python package or app can import the config module as shown next. Notice the `api_key` is checked to make sure the associated environment variable was set otherwise an error is raised.

```python
# downloader.py in mypkg

from . import config


def download_file():
    if config.api_key is None:
        raise RuntimeError("API_KEY environment variable is not set")

    print("API_KEY is", config.api_key)
    print("Saved file to", config.save_path)
```

The default values for the config module are not difficult to test. But testing with environment variables requires the `monkeypatch` fixture in pytest. This is demonstrated in the test functions given here. Notice the config module must be reloaded to pick up the new environment variables.

```python
# test_config.py

import importlib
from mypkg import config


def test_config_defaults():
    assert config.api_key is None
    assert config.api_url == "http://localhost:8090"
    assert config.save_path == "~/Desktop/downloads"


def test_config_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "12345")
    monkeypatch.setenv("API_URL", "https://www.apple.com")

    importlib.reload(config)

    assert config.api_key == "12345"
    assert config.api_url == "https://www.apple.com"
    assert config.save_path == "~/Desktop/downloads"
```

And here are the tests for the `download_file` function. To make sure the environment variables are reset, the config module is reloaded in these tests too.

```python
# test_downloader.py

import importlib

import pytest

import mypkg
from mypkg import config


def test_downloader_defaults():
    importlib.reload(config)

    err = "API_KEY environment variable is not set"
    with pytest.raises(RuntimeError, match=err):
        mypkg.download_file()


def test_downloader_env(monkeypatch, capsys):
    monkeypatch.setenv("API_KEY", "12345")

    importlib.reload(config)
    mypkg.download_file()

    captured = capsys.readouterr()
    assert "Saved file to ~/Desktop/downloads\n" in captured.out
```

The example code discussed in this article is available in the GitHub [pythonic](https://github.com/wigging/pythonic) repo at `pythonic/projects/test-config/`.

