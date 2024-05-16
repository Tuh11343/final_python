from prismaConfig import get_db
from pydantic import BaseModel
from typing import Optional


class BookAuthor(BaseModel):
    id:Optional[int]=None
    book_id:int
    author_id:int

async def findAll():
    prisma=await get_db()
    bookAuthors=await prisma.bookauthor.find_many()
    return {
        "bookAuthors":bookAuthors
    }

async def findByID(id:int):
    prisma=await get_db()
    bookAuthor = await prisma.bookauthor.find_unique(
        where={
            "id":id
        }
    )
    return {
        "bookAuthor":bookAuthor
    }

async def delete(id:int):
    prisma=await get_db()
    foundBookAuthor=await prisma.bookauthor.find_unique(where={
        "id":id
    })
    if foundBookAuthor is None:
        return {
            "bookAuthor":None
        }
    else:
        deletedBookAuthor= await prisma.bookauthor.delete(
        where={
            "id":id
        })
        return {
            "bookAuthor":deletedBookAuthor
        }
    

async def update(bookAuthor:BookAuthor):
    prisma=await get_db()
    foundBookAuthor=await prisma.bookauthor.find_unique(where={
        "id":bookAuthor.id
    })
    if foundBookAuthor is None:
        return{
            "bookAuthor":None
        }
    else:
        updatedBookAuthor= await prisma.account.update(where={
        "id":bookAuthor.id
        },data=dict(bookAuthor))
    return {
        "bookAuthor":updatedBookAuthor
    }

async def create(bookAuthor:BookAuthor):
    prisma=await get_db()
    createdBookAuthor=await prisma.bookauthor.create(data=dict(bookAuthor))
    return {
        "bookAuthor":createdBookAuthor
    }
    

