from prismaConfig import get_db
from pydantic import BaseModel
from typing import Optional


class BookGenre(BaseModel):
    id:Optional[int]=None
    book_id:int
    genre_id:int

async def findAll():
    prisma=await get_db()
    bookGenres=await prisma.bookauthor.find_many()
    return {
        "bookGenres":bookGenres
    }

async def findByID(id:int):
    prisma=await get_db()
    bookGenre = await prisma.bookauthor.find_unique(
        where={
            "id":id
        }
    )
    return {
        "bookGenre":bookGenre
    }

async def delete(id:int):
    prisma=await get_db()
    foundBookGenre=await prisma.bookauthor.find_unique(where={
        "id":id
    })
    if foundBookGenre is None:
        return {
            "bookGenre":None
        }
    else:
        deletedBookGenre= await prisma.bookauthor.delete(
        where={
            "id":id
        })
        return {
            "bookGenre":deletedBookGenre
        }
    

async def update(bookGenre:BookGenre):
    prisma=await get_db()
    foundBookGenre=await prisma.bookauthor.find_unique(where={
        "id":bookGenre.id
    })
    if foundBookGenre is None:
        return{
            "bookGenre":None
        }
    else:
        updatedBookGenre= await prisma.account.update(where={
        "id":bookGenre.id
        },data=dict(bookGenre))
    return {
        "bookGenre":updatedBookGenre
    }

async def create(bookGenre:BookGenre):
    prisma=await get_db()
    createdBookGenre=await prisma.bookauthor.create(data=dict(bookGenre))
    return {
        "bookGenre":createdBookGenre
    }
    

