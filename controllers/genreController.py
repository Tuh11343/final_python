from prismaConfig import get_db
from pydantic import BaseModel
from typing import Optional


class Genre(BaseModel):
    id:Optional[int]=None
    name: str
    image: Optional[str]=None


async def create(genre: Genre):
    prisma = await get_db()
    createdGenre = await prisma.genre.create(data=genre.dict(exclude_none=True))
    return {"genre": createdGenre}


async def delete(id: int):
    prisma = await get_db()

    genre = await prisma.genre.find_unique(where={"id": id})
    if genre is None:
        return {"genre": None}

    deletedGenre = await prisma.genre.delete(where={"id": id})
    return {"genre": deletedGenre}


async def update(genre: Genre):
    prisma = await get_db()

    foundGenre = await prisma.genre.find_unique(where={"id": genre.id})
    if foundGenre is None:
        return {"genre": None}

    updatedGenre = await prisma.genre.update(where={"id": genre.id}, data=dict(genre))
    return {"genre": updatedGenre}


async def findAll(limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        genres = await prisma.genre.find_many()
        return {"genres": genres}
    else:
        genres = await prisma.genre.find_many(take=limit, skip=offset)
        length = await prisma.genre.count()
        return {"genres": genres, "length": length}


async def findByID(id: int):
    prisma = await get_db()
    genre = await prisma.genre.find_unique(where={
        "id":id
    })
    return {"genre": genre}


async def findByBookID(id:int,limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        genres = await prisma.genre.find_many(where={
            "bookGenres":{
                "some":{
                    "book_id":id
                }
            }
        },include={
            "bookGenres":True
        })
        return {"genres": genres}
    else:
        genres = await prisma.genre.find_many(where={
            "bookGenres":{
                "some":{
                    "book_id":id
                }
            }
        },take=limit,skip=offset,include={
            "bookGenres":True
        })
        length = await prisma.genre.count(where={
            "bookGenres":{
                "some":{
                    "book_id":id
                }
            }
        })
        return {"genres": genres, "length": length}