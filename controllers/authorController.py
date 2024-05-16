from prismaConfig import get_db
from pydantic import BaseModel
from typing import Optional
from fastapi import Request
import json


class Author(BaseModel):
    id:Optional[int]=None
    name: str
    image: Optional[str] = None
    description: Optional[str] = None


async def create(author: Author):
    prisma = await get_db()
    createdAuthor = await prisma.author.create(data=author.dict(exclude_none=True))
    return {"author": createdAuthor}


async def delete(id: int):
    prisma = await get_db()

    author = await prisma.author.find_unique(where={"id": id})
    if author is None:
        return {"author": None}

    deletedAuthor = await prisma.author.delete(where={"id": id})
    return {"author": deletedAuthor}


async def update(author: Author):
    prisma = await get_db()

    foundAuthor = await prisma.author.find_unique(where={"id": author.id})
    if foundAuthor is None:
        return {"author": None}

    updatedAuthor = await prisma.author.update(
        where={"id": author.id}, data=dict(author)
    )
    return {"author": updatedAuthor}


async def findAll(limit: int, offset: int):
    prisma = await get_db()
    if limit is None:
        authors = await prisma.author.find_many()
        return {"authors": authors}
    else:
        authors = await prisma.author.find_many(take=limit, skip=offset)
        length = await prisma.author.count()
        return {"authors": authors, "length": length}


async def findByID(id: int):
    prisma = await get_db()
    author = await prisma.author.find_unique(where={"id": id})
    return {"author": author}


async def findByBookID(id: int):
    prisma = await get_db()
    bookAuthors = await prisma.bookauthor.find_many(
        where={"book_id": id}, include={"author": True}
    )
    authors = [bookAuthor.author for bookAuthor in bookAuthors]

    return {"authors": authors}


async def findOneByBookID(id: int):
    prisma = await get_db()
    book = await prisma.book.find_unique(where={"id": id}, include={"bookAuthor": True})
    if len(book.bookAuthor) == 0:
        return {"author": "Không rõ"}
    else:
        author = await prisma.author.find_first(
            where={"id": book.bookAuthor[0].author_id}
        )
        if author is None:
            return {"author": "Không rõ"}
        else:
            return {"author": author.name}
