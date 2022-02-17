from dataclasses import dataclass, replace
from functools import lru_cache
from os import getenv


@dataclass(frozen=True)
class Config:
    API_KEY: str = "letmein"
    APP_HOST: str = "localhost"
    APP_PORT: int = 5432


def overwrite_from_file(base: Config) -> Config:
    """
    load from file source, parse and overload the base config
    """
    return replace(base)


def overwrite_from_env(base: Config) -> Config:
    """extend with env variabels"""
    return replace(base, 
        API_KEY=getenv("API_KEY", base.API_KEY),
        APP_HOST=getenv("APP_HOST", base.APP_HOST),
        APP_PORT=int(getenv("APP_PORT", base.APP_PORT)),
    )


@lru_cache()
def config() -> Config:
    """
    Factory method for building configuration objects
    """
    return overwrite_from_env(overwrite_from_file(Config()))
