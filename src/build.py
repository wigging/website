"""Build the website pages and posts from their HTML templates."""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(__file__).resolve().parent
DIST = ROOT / "dist"

PAGE_DIR = SOURCE / "page-content"
PAGE_TEMPLATE = SOURCE / "templates" / "page.html"
PAGE_OUTPUT = DIST

NOTE_DIR = SOURCE / "note-content"
NOTE_TEMPLATE = SOURCE / "templates" / "note.html"
NOTE_OUTPUT = DIST / "note"

STATIC_DIR = SOURCE / "static"


def build(source_directory, template_path, output_directory):
    """Render each HTML source file into the output directory."""
    template = template_path.read_text(encoding="utf-8")
    output_directory.mkdir(parents=True, exist_ok=True)

    for source_path in sorted(source_directory.glob("*.html")):
        content = source_path.read_text(encoding="utf-8").strip()
        output_path = output_directory / source_path.name
        output_path.write_text(
            template.replace("      {{ content }}", content), encoding="utf-8"
        )
        print(f"Built {output_path}")


def main():
    """Build the complete website into the dist directory."""
    shutil.rmtree(DIST, ignore_errors=True)
    build(PAGE_DIR, PAGE_TEMPLATE, PAGE_OUTPUT)
    build(NOTE_DIR, NOTE_TEMPLATE, NOTE_OUTPUT)
    shutil.copytree(STATIC_DIR, DIST, dirs_exist_ok=True)
    print(f"Copied static files to {DIST}")


if __name__ == "__main__":
    main()
