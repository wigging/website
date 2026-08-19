"""Shared configuration for the website scripts."""

from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SOURCE_DIR.parent
DIST_DIR = PROJECT_ROOT / "dist"

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
