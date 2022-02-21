

from typing import Callable, Type

from fastapi import Depends
from src.config import Config, config

from src.db.item_repo import ItemRepo
from src.db.pgcon import PGConfig, PGConnection


def get_pg_connection(config: Config = Depends(config())) -> PGConnection:
    """create a postgres connecter out of thin air"""
    return PGConnection(config=PGConfig())


def get_repo(repo_type: Type[ItemRepo]) -> Callable[[], ItemRepo]:
    """
    Factory function that offers the possibility to 
        spawns a repository from scratch

    To make this work in a the context of Depends, it needs to return a callable
        signature Depends => Depends(... => x)

    TODO intergrate the possibility to configure for
        different repo types

    :param repo_type: callable that spawns a repo
    :return: ItemRepo
    """
    def constructor():
        return repo_type(get_pg_connection())
    
    # return a callable, to make sure it can work in Depends(...)
    return constructor
