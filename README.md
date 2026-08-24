# Website

This repository contains my personal website <https://gavinw.me>. Pull requests are not accepted but Issues can be submitted regarding content on the website.

## Installation

Install uv using the instructions at <https://docs.astral.sh/uv/>.

## Build

Build the website along with JSON and RSS feeds using the `build.py` script. This will create a `dist/` directory in the project for all the generated website files.

```bash
uv run src/build.py
```

Use the `--serve` option to serve the website locally from the `dist/` directory. This will automatically open the web browser to view the website.

```bash
uv run src/build.py --serve
```

## Project structure

All HTML, CSS, templates, and static files needed to build the website reside in the `src/` directory. All build output is placed in the `dist/` directory. Contents of the `dist/` directory is used by GitHub Pages to host the website.
