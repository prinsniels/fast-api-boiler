from fastapi import APIRouter

router_v1curd = APIRouter(
    prefix="/v1/crud"
)

@router_v1curd.get("/")
async def root():
    return {"message": "Hello World"}


@router_v1curd.get("/{name}")
async def root(name: str):
    return {"message": f"Hello {name}"}
