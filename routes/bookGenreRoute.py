from fastapi import APIRouter
from controllers.bookGenreController import (
    BookGenre,
    create,
    delete,
    findAll,
    findByID,
    update,
)

router = APIRouter(
    prefix="/api/v1/bookGenre",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["BookGenres"],
)

@router.get("/")
async def findAllBookGenre(limit:int=None,offset:int=None):
    response = await findAll(limit,offset)
    return response

@router.get("/id")
async def findBookGenreByID(id:int):
    response = await findByID(id)
    return response

@router.put("/")
async def updateBookGenre(bookGenre:BookGenre):
    response = await update(bookGenre)
    return response

@router.post("/")
async def createBookGenre(bookGenre:BookGenre):
    response = await create(bookGenre)
    return response

@router.delete("/")
async def deleteBookGenre(id:int):
    response = await delete(id)
    return response

