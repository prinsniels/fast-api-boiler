from fastapi import APIRouter

route = APIRouter(
    prefix="/healthcheck"
)

@route.get("/")
async def root():
    return {"alive": True}


@route.get("/{name}")
async def root(name: str):
    return {"message": f"Hello {name}"}
