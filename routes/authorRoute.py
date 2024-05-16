from fastapi import APIRouter
from controllers.authorController import (
    Author,
    findAll,
    findByID,
    findByBookID,
    findOneByBookID,
    update,
    create,
    delete
)

from fastapi import Request
router = APIRouter(
    prefix="/api/v1/author",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["Authors"],
)

@router.get("/")
async def findAllAuthor(limit:int=None,offset:int=None):
    response = await findAll(limit,offset)
    return response

@router.get("/id")
async def findAuthorByID(id:int):
    response = await findByID(id)
    return response

@router.get("/bookID")
async def findAuthorByBookID(id:int):
    response = await findByBookID(id)
    return response

@router.get("/bookAuthorOne")
async def findOneAuthorByBookID(id:int):
    response = await findOneByBookID(id)
    return response

@router.put("/")
async def updateAuthor(author:Author):
    response = await update(author)
    return response

@router.post("/")
async def createAuthor(author:Author):
    response = await create(author)
    return response

@router.delete("/")
async def deleteAuthor(id:int):
    response = await delete(id)
    return response

