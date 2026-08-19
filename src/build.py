"""Build the website pages and posts from their HTML templates."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(__file__).resolve().parent


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
    build(SOURCE / "pages", SOURCE / "templates" / "page.html", ROOT)
    build(SOURCE / "posts", SOURCE / "templates" / "post.html", ROOT / "notes")


if __name__ == "__main__":
    main()
