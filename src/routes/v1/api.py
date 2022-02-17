from fastapi import APIRouter

route = APIRouter(prefix="/v1/todo")


@route.get("/")
async def items():
    return {"message": "Hello World"}


@route.get("/{id}")
async def item(id: str):
    return {"message": f"Hello {id}"}
