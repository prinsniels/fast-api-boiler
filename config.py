from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class Config:
    API_KEY = "letmein"

@lru_cache()
def configuration() -> Config:
    """
    Factory method for building configuration objects
    """
    return Config()
