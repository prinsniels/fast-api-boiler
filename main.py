import uvicorn
from fastapi import Depends, FastAPI
from auth import authenticate_request

from routes.v1.crud import router_v1curd

app = FastAPI(dependencies=[Depends(authenticate_request)])

app.include_router(router=router_v1curd)


@app.on_event("startup")
def startup_event():
    # this is the place where 
    #   we chech de database version ... 
    #   init the cached config file ...

    pass


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5004)
