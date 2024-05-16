from fastapi import APIRouter
from controllers.genreController import (
    Genre,
    create,
    delete,
    findAll,
    findByBookID,
    findByID,
    update,
)

router = APIRouter(
    prefix="/api/v1/genre",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["Genres"],
)

@router.get("/")
async def findAllGenre(limit:int=None,offset:int=None):
    response = await findAll(limit,offset)
    return response

@router.get("/id")
async def findGenreByID(id:int):
    response = await findByID(id)
    return response

@router.get("/bookID")
async def findGenreByBookID(id:int,limit:int=None,offset:int=None):
    response = await findByBookID(id,limit,offset)
    return response

@router.put("/")
async def updateGenre(genre:Genre):
    response = await update(genre)
    return response

@router.post("/")
async def createGenre(genre:Genre):
    response = await create(genre)
    return response

@router.delete("/")
async def deleteGenre(id:int):
    response = await delete(id)
    return response

