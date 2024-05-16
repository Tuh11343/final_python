from prismaConfig import get_db
from pydantic import BaseModel
from typing import Optional


class Favorite(BaseModel):
    id:Optional[int]=None
    book_id:int
    user_id:int


async def create(favorite:Favorite):
    prisma = await get_db()
    createdFavorite = await prisma.favorite.create(data=favorite.dict(exclude_none=True))
    return {"favorite": createdFavorite}


async def delete(id: int):
    prisma = await get_db()

    favorite = await prisma.favorite.find_unique(where={"id": id})
    if favorite is None:
        return {"favorite": None}

    deletedFavorite = await prisma.favorite.delete(where={"id": id})
    return {"favorite": deletedFavorite}


async def update(favorite: Favorite):
    prisma = await get_db()

    foundFavorite = await prisma.favorite.find_unique(where={"id": favorite.id})
    if foundFavorite is None:
        return {"favorite": None}

    updatedFavorite = await prisma.favorite.update(
        where={"id": favorite.id}, data=dict(favorite)
    )
    return {"favorite": updatedFavorite}


async def findAll(limit: int=None, offset: int=None):
    prisma = await get_db()
    if limit is None:
        favorites = await prisma.favorite.find_many()
        return {"favorites": favorites}
    else:
        favorites = await prisma.favorite.find_many(take=limit, skip=offset)
        length = await prisma.favorite.count()
        return {"favorites": favorites, "length": length}


async def click(user_id:int,book_id:int):
    prisma = await get_db()
    favorite = await prisma.favorite.find_first(where={
        "book_id":book_id,
        "user_id":user_id
    })
    if favorite is None:
        createdFavorite=await prisma.favorite.create(data={
            "user_id":user_id,
            "book_id":book_id
        })
        return {"favorite": createdFavorite,"action":True}
    else:
        deletedFavorite=await prisma.favorite.delete(where={
            "id":favorite.id
        })
        return {"favorite": deletedFavorite,"action":False}
