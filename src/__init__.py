from fastapi import Depends, FastAPI

from auth import authenticate_request
from routes.probe import route as v1_probe
from routes.v1 import route as v1_crud

from config import config


def build() -> FastAPI:
    app = FastAPI()

    # attach active routes
    app.include_router(router=v1_probe)
    app.include_router(router=v1_crud, dependencies=[Depends(authenticate_request)])

    return app


__all__ = ["build", "config"]
