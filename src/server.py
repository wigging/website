"""Serve the built website locally."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent / "dist"
HOST = "127.0.0.1"
PORT = 8000


def main():
    """Serve the contents of the dist directory."""
    handler = partial(SimpleHTTPRequestHandler, directory=DIST)

    with ThreadingHTTPServer((HOST, PORT), handler) as server:
        print(f"Serving {DIST} at http://{HOST}:{PORT}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
