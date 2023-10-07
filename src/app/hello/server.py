"""Server."""
import http.server
import logging

logger = logging.getLogger(__name__)


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP Request handler."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello World")
