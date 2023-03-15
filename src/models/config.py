"""Config."""
from pydantic import BaseModel


class ConfigModel(BaseModel):
    """Config Model."""

    hostname: str
    port: int
