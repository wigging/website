"""Serve the built website locally."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

import config


def main():
    """Serve the contents of the dist directory."""
    handler = partial(SimpleHTTPRequestHandler, directory=config.DIST_DIR)

    address = (config.SERVER_HOST, config.SERVER_PORT)
    with ThreadingHTTPServer(address, handler) as server:
        print(
            f"Serving {config.DIST_DIR} at "
            f"http://{config.SERVER_HOST}:{config.SERVER_PORT}"
        )
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
