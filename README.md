# Website

This repository contains my personal website <https://gavinw.me>. Pull requests are not accepted but Issues can be submitted regarding content on the website.

## Installation

Install uv using the instructions at <https://docs.astral.sh/uv/>.

## Build the website

Build the website along with its JSON and RSS feeds using the `build.py` script. This will create a `dist/` directory in the project for all the generated website files.

```bash
uv run src/build.py
```

Use the `--serve` option to serve the website locally from the `dist/` directory. This will automatically open the web browser to view the website.

```bash
uv run src/build.py --serve
```

## Project directories

All HTML, CSS, templates, and static files needed to build the website reside in the `src/` directory. All build output is placed in the `dist/` directory. Contents of the `dist/` directory is used by GitHub Pages to host the website.

## Add notes

Use the HTML structure shown below to add a note to the website. Give a short description about the note at the top of the HTML file as a comment. The title of the note is the `<h2>` element and the published date is represented by the `<time>` element. This information provides the metadata used to generate the notes page and JSON/RSS feeds. Place the content of the note after the `<time>` element.

```html
<!--
Description of the note goes in this comment.
-->

<h2>Title of the Note</h2>

<time datetime="2026-07-12">July 12, 2026</time>
```

All notes go in the `src/note-content/` directory.
