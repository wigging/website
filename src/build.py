"""Build the website pages and posts from their HTML templates."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(__file__).resolve().parent

PAGE_DIR = SOURCE / "page-content"
PAGE_TEMPLATE = SOURCE / "templates" / "page.html"
PAGE_OUTPUT = ROOT

NOTE_DIR = SOURCE / "note-content"
NOTE_TEMPLATE = SOURCE / "templates" / "note.html"
NOTE_OUTPUT = ROOT / "note"


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
        print(f"Wrote {output_path}")


def main():
    """Build pages into the project root and posts into the notes directory."""
    build(PAGE_DIR, PAGE_TEMPLATE, PAGE_OUTPUT)
    build(NOTE_DIR, NOTE_TEMPLATE, NOTE_OUTPUT)


if __name__ == "__main__":
    main()
