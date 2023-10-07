"""Config."""
from pydantic import BaseModel


class ConfigModel(BaseModel):
    """Config Model."""

    env: str
    logLevel: str

    hostname: str
    port: int
