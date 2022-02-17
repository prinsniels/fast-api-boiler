import uvicorn
from fastapi import Depends, FastAPI

from auth import authenticate_request
from config import config
from routes.probe import route as v1_probe
from routes.v1 import route as v1_crud


def build() -> FastAPI:
    app = FastAPI()

    # attach active routes
    app.include_router(router=v1_probe)
    app.include_router(router=v1_crud, dependencies=[Depends(authenticate_request)])

    return app


if __name__ == "__main__":
    config = config()
    uvicorn.run(build(), host=config.APP_HOST, port=config.APP_PORT)
