"""Build the website pages and posts from their HTML templates."""

import shutil

import config


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
    shutil.rmtree(config.DIST_DIR, ignore_errors=True)
    build(config.PAGE_CONTENT_DIR, config.PAGE_TEMPLATE, config.DIST_DIR)
    build(config.NOTE_CONTENT_DIR, config.NOTE_TEMPLATE, config.NOTE_OUTPUT_DIR)
    shutil.copytree(config.STATIC_DIR, config.DIST_DIR, dirs_exist_ok=True)
    print(f"Copied static files to {config.DIST_DIR}")


if __name__ == "__main__":
    main()
