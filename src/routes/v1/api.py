from fastapi import APIRouter, Depends
from src.db.helper import get_repo

from src.db.item_repo import ItemRepo

route = APIRouter()


@route.get("/")
async def items(repo: ItemRepo = Depends(get_repo(ItemRepo))):
    return repo.get_all()


@route.get("/{id}")
async def item_by_id(id: str, repo: ItemRepo = Depends(get_repo(ItemRepo))):
    print(id)
    return repo.get_by_id(id)
