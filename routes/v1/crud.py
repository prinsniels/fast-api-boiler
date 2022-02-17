from fastapi import APIRouter

route = APIRouter(
    prefix="/v1/crud"
)

@route.get("/")
async def root():
    return {"message": "Hello World"}


@route.get("/{name}")
async def root(name: str):
    return {"message": f"Hello {name}"}
