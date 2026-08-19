"""Generate JSON and RSS feeds."""

import json
import xml.etree.ElementTree as ET
from datetime import date, datetime, time, timezone
from email.utils import format_datetime
from html.parser import HTMLParser
from urllib.parse import urljoin

import config


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


def get_items(source, base_url):
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
        "title": "Gavin Wiggins — Notes",
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
    ET.SubElement(channel, "title").text = "Gavin Wiggins — Notes"
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
            date.fromisoformat(feed_item["date_published"][:10]), time.min, timezone.utc
        )
        ET.SubElement(item, "pubDate").text = format_datetime(published, usegmt=True)

    ET.indent(rss)
    xml = ET.tostring(rss, encoding="utf-8")
    output.write_bytes(b'<?xml version="1.0" encoding="utf-8"?>\n' + xml + b"\n")
    print(f"Wrote {len(items)} item(s) to {output}")


def main():
    """Generate the JSON and RSS feeds from the notes page."""
    config.DIST_DIR.mkdir(parents=True, exist_ok=True)
    items = get_items(config.NOTES_SOURCE, config.BASE_URL)
    generate_json_feed(items, config.JSON_FEED_OUTPUT, config.BASE_URL)
    generate_rss_feed(items, config.RSS_FEED_OUTPUT, config.BASE_URL)


if __name__ == "__main__":
    main()
