from fastapi import APIRouter
from controllers.bookAuthorController import (
    BookAuthor,
    create,
    update,
    delete,
    findByID,
    findAll
)

from fastapi import Request
router = APIRouter(
    prefix="/api/v1/bookAuthor",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["BookAuthors"],
)

@router.get("/")
async def findAllBookAuthor():
    response = await findAll()
    return response

@router.get("/id")
async def findBookAuthorByID(id:int):
    response = await findByID(id)
    return response

@router.put("/")
async def updateAuthor(bookAuthor:BookAuthor):
    response = await update(bookAuthor)
    return response

@router.post("/")
async def createAuthor(bookAuthor:BookAuthor):
    response = await create(bookAuthor)
    return response

@router.delete("/")
async def deleteBookAuthor(id:int):
    response = await delete(id)
    return response

