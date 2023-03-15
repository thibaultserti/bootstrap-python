import logging
import socketserver
import sys

from src.utils.config import load_config
from src.hello.server import MyHttpRequestHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)
std_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
std_handler.setFormatter(formatter)
logger.addHandler(std_handler)


if __name__ == "__main__":
    config = load_config()
    with socketserver.TCPServer(("", config.port), MyHttpRequestHandler) as httpd:
        logging.info(f"Serving at http://localhost:{config.port}")
        httpd.serve_forever()
