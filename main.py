import uvicorn
from fastapi import Depends, FastAPI
from auth import authenticate_request
from config import config

from routes.v1.crud import router_v1curd

def build() -> FastAPI:
    app = FastAPI(
        dependencies=[Depends(authenticate_request)]
    )

    # attach active routes
    app.include_router(router=router_v1curd)
    
    return app


if __name__ == "__main__":
    config = config()
    uvicorn.run(build(), host=config.APP_HOST, port=config.APP_PORT)
