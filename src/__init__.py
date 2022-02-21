from fastapi import Depends, FastAPI

from src.auth import authenticate_request
from src.routes.probe import route as v1_probe
from src.routes.v1 import route as v1_crud

from src.config import config


def build() -> FastAPI:
    app = FastAPI()

    # attach active routes
    app.include_router(router=v1_probe)
    app.include_router(
        router=v1_crud, 
        prefix="/v1/todo", 
        #dependencies=[Depends(authenticate_request)]
    )

    return app


__all__ = ["build", "config"]
