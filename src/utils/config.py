import logging
import yaml

from ..models import ConfigModel

logger = logging.getLogger(__name__)


def load_config(file: str = "./config/config.yaml") -> ConfigModel:
    logging.info(f"Loading config from file {file}")
    with open(file, "r") as f:
        conf = yaml.safe_load(f)
        return ConfigModel.parse_obj(conf)
