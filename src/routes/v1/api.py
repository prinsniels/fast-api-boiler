from fastapi import APIRouter

route = APIRouter(prefix="/v1/todo")


@route.get("/")
async def items():
    return {"message": "Hello World"}


@route.get("/{id}")
async def item(id: id):
    return {"message": f"Hello {id}"}


@route.post("/")
async def item(id: id):
    return {"message": f"Hello {id}"}


@route.delete("/{id}")
async def drop():
    pass
