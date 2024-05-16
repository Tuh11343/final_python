from fastapi import APIRouter
from controllers.favoriteController import (
    Favorite,
    create,
    update,
    delete,
    click,
    findAll
)

from fastapi import Request
router = APIRouter(
    prefix="/api/v1/favorite",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["Favorites"],
)

@router.get("/")
async def findAllFavorite(limit:int=None,offset:int=None):
    response = await findAll(limit,offset)
    return response

# @router.get("/id")
# async def findFavoriteByID(id:int):
#     response = await findByID(id)
#     return response

@router.post("/favoriteClick")
async def findFavoriteByBookID(user_id:int,book_id:int):
    response = await click(user_id,book_id)
    return response

@router.put("/")
async def updateFavorite(favorite:Favorite):
    response = await update(favorite)
    return response

@router.post("/")
async def createFavorite(favorite:Favorite):
    response = await create(favorite)
    return response

@router.delete("/")
async def deleteFavorite(id:int):
    response = await delete(id)
    return response

