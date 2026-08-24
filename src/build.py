"""Build the website and its feeds."""

import argparse
import json
import shutil
import webbrowser
import xml.etree.ElementTree as ET
from datetime import UTC, date, datetime, time
from email.utils import format_datetime
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urljoin

SOURCE_DIR = Path("src")
DIST_DIR = Path("dist")

PAGE_CONTENT_DIR = SOURCE_DIR / "page-content"
NOTE_CONTENT_DIR = SOURCE_DIR / "note-content"
STATIC_DIR = SOURCE_DIR / "static"

PAGE_TEMPLATE = SOURCE_DIR / "templates" / "page.html"
NOTE_TEMPLATE = SOURCE_DIR / "templates" / "note.html"
NOTE_OUTPUT_DIR = DIST_DIR / "note"

NOTES_SOURCE = PAGE_CONTENT_DIR / "notes.html"
JSON_FEED_OUTPUT = DIST_DIR / "feed.json"
RSS_FEED_OUTPUT = DIST_DIR / "rss.xml"
BASE_URL = "https://gavinw.me/"

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000


class NotesParser(HTMLParser):
    """Parse feed metadata from note articles in an HTML document."""

    def __init__(self):
        """Initialize the parser and its note collection state."""
        super().__init__()
        self.notes = []
        self.note = None
        self.field = None
        self.text = []

    def handle_starttag(self, tag, attrs):
        """Collect metadata from the start tag of a note element."""
        attributes = dict(attrs)
        classes = attributes.get("class", "").split()

        if tag == "article" and "note" in classes:
            self.note = {}
        elif self.note is not None and tag == "a" and self.field is None:
            self.note["url"] = attributes.get("href", "")
            self.field = "title"
            self.text = []
        elif self.note is not None and tag == "p" and "summary" not in self.note:
            self.field = "summary"
            self.text = []
        elif self.note is not None and tag == "time":
            self.note["date_published"] = attributes.get("datetime", "")

    def handle_data(self, data):
        """Collect text for the active note field."""
        if self.field:
            self.text.append(data)

    def handle_endtag(self, tag):
        """Finish the active field or save a completed note article."""
        if self.note is None:
            return

        if (tag == "a" and self.field == "title") or (
            tag == "p" and self.field == "summary"
        ):
            self.note[self.field] = " ".join("".join(self.text).split())
            self.field = None
            self.text = []
        elif tag == "article":
            if self.note.get("url") and self.note["url"] != "#":
                self.notes.append(self.note)
            self.note = None


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


def get_feed_items(source, base_url):
    """Parse notes from the source file and return feed items newest first."""
    parser = NotesParser()
    parser.feed(source.read_text(encoding="utf-8"))

    items = []
    for note in parser.notes:
        item_url = urljoin(base_url, note["url"])
        published = date.fromisoformat(note["date_published"]).isoformat()
        items.append(
            {
                "id": item_url,
                "url": item_url,
                "title": note["title"],
                "summary": note.get("summary", ""),
                "date_published": f"{published}T00:00:00Z",
            }
        )

    items.sort(key=lambda item: item["date_published"], reverse=True)
    return items


def generate_json_feed(items, output, base_url):
    """Write feed items to a JSON Feed 1.1 file."""
    feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": "Gavin Wiggins",
        "home_page_url": urljoin(base_url, "notes.html"),
        "feed_url": urljoin(base_url, "feed.json"),
        "items": items,
    }
    output.write_text(json.dumps(feed, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} item(s) to {output}")


def generate_rss_feed(items, output, base_url):
    """Write feed items to an RSS 2.0 file."""
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "Gavin Wiggins"
    ET.SubElement(channel, "link").text = urljoin(base_url, "notes.html")
    ET.SubElement(
        channel, "description"
    ).text = "Notes on various programming and technology-related topics."

    for feed_item in items:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = feed_item["title"]
        ET.SubElement(item, "link").text = feed_item["url"]
        ET.SubElement(item, "guid", isPermaLink="true").text = feed_item["id"]
        ET.SubElement(item, "description").text = feed_item["summary"]
        published = datetime.combine(
            date.fromisoformat(feed_item["date_published"][:10]), time.min, UTC
        )
        ET.SubElement(item, "pubDate").text = format_datetime(published, usegmt=True)

    ET.indent(rss)
    xml = ET.tostring(rss, encoding="utf-8")
    output.write_bytes(b'<?xml version="1.0" encoding="utf-8"?>\n' + xml + b"\n")
    print(f"Wrote {len(items)} item(s) to {output}")


def build_site():
    """Build the complete website and feeds into the dist directory."""
    shutil.rmtree(DIST_DIR, ignore_errors=True)
    build(PAGE_CONTENT_DIR, PAGE_TEMPLATE, DIST_DIR)
    build(NOTE_CONTENT_DIR, NOTE_TEMPLATE, NOTE_OUTPUT_DIR)
    shutil.copytree(STATIC_DIR, DIST_DIR, dirs_exist_ok=True)
    print(f"Copied static files to {DIST_DIR}")

    items = get_feed_items(NOTES_SOURCE, BASE_URL)
    generate_json_feed(items, JSON_FEED_OUTPUT, BASE_URL)
    generate_rss_feed(items, RSS_FEED_OUTPUT, BASE_URL)


def serve():
    """Serve the contents of the dist directory."""
    handler = partial(SimpleHTTPRequestHandler, directory=DIST_DIR)
    address = (SERVER_HOST, SERVER_PORT)
    with ThreadingHTTPServer(address, handler) as server:
        url = f"http://{SERVER_HOST}:{SERVER_PORT}"
        print(f"Serving website from {DIST_DIR}/ at {url}")
        webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


def main():
    """Build the website and optionally serve it locally."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--serve", action="store_true", help="serve the built website locally"
    )
    args = parser.parse_args()

    build_site()
    if args.serve:
        serve()


if __name__ == "__main__":
    main()
