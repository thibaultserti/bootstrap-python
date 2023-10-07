"""Config."""
import yaml

from models import ConfigModel


def load_config(file: str = "./config/config.yaml") -> ConfigModel:
    """Config loader."""
    with open(file, "r", encoding="utf-8") as fil:
        conf = yaml.safe_load(fil)
        return ConfigModel.parse_obj(conf)
