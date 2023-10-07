"""Main."""
import logging
import socketserver
import sys

from utils.config import load_config
from hello.server import MyHttpRequestHandler


if __name__ == "__main__":
    config = load_config()

    # Logging
    logger = logging.getLogger()
    std_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)

    if config.env not in ["prod", "prd"]:
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    else:
        formatter = logging.Formatter(
            "{'time':'%(asctime)s', 'name': '%(name)s', 'level': '%(levelname)s', 'message': '%(message)s'}"
        )
    try:
        logger.setLevel(config.logLevel.upper())
    except ValueError:
        logger.critical("Cannot read config: logLevel")
        sys.exit(1)

    std_handler.setFormatter(formatter)
    logger.addHandler(std_handler)

    with socketserver.TCPServer(("", config.port), MyHttpRequestHandler) as httpd:
        logger.info("Serving at http://localhost:%s", config.port)
        httpd.serve_forever()
