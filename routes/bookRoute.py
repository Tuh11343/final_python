from fastapi import APIRouter
from controllers.bookController import (
    Book,
    findAll,
    findByID,
    findByName,
    findByGenreID,
    findByAuthorID,
    findByFavorite,
    findByNameAndGenre,
    findNormal,
    findPremium,
    findTopRating,
    delete,
    update,
    create
)

from fastapi import Request
router = APIRouter(
    prefix="/api/v1/book",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["Books"],
)

@router.get("/")
async def findAllBook(limit:int=None,offset:int=None):
    response = await findAll(limit,offset)
    return response

@router.get("/id")
async def findBookByID(id:int):
    response = await findByID(id)
    return response

@router.get("/genre")
async def findBookByGenreID(id:int,limit:int=None,offset:int=None):
    response = await findByGenreID(id,limit,offset)
    return response

@router.get("/author")
async def findBookByAuthorID(id:int,limit:int=None,offset:int=None):
    response = await findByAuthorID(id,limit,offset)
    return response

@router.get("/favorite")
async def findBookByFavorite(id:int,limit:int=None,offset:int=None):
    response = await findByFavorite(id,limit,offset)
    return response

@router.get("/nameAndGenre")
async def findBookByNameAndGenre(name:str,genre_id:int,limit:int=None,offset:int=None):
    response = await findByNameAndGenre(name,genre_id,limit,offset)
    return response

@router.get("/name")
async def findBookByName(name:str,limit:int=None,offset:int=None):
    response = await findByName(name,limit,offset)
    return response

@router.get("/normal")
async def findNormalBook(limit:int=None,offset:int=None):
    response = await findNormal(limit,offset)
    return response

@router.get("/premium")
async def findPremiumBook(limit:int=None,offset:int=None):
    response = await findPremium(limit,offset)
    return response

@router.get("/topRating")
async def findTopRatingBook(limit:int=None,offset:int=None):
    response = await findTopRating(limit,offset)
    return response

@router.put("/")
async def updateBook(book:Book):
    response = await update(book)
    return response

@router.post("/")
async def createBook(book:Book):
    response = await create(book)
    return response

@router.delete("/")
async def deleteBook(id:int):
    response = await delete(id)
    return response

