from prismaConfig import get_db
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:Optional[int]=None
    name:str
    phone_number:Optional[str]=None
    address:Optional[str]=None
    

async def create(user: User):
    prisma = await get_db()
    createdUser = await prisma.user.create(data=user.dict(exclude_none=True))
    return {"user": createdUser}


async def delete(id: int):
    prisma = await get_db()

    user = await prisma.user.find_unique(where={"id": id})
    if user is None:
        return {"user": None}

    deletedUser = await prisma.user.delete(where={"id": id})
    return {"user": deletedUser}


async def update(user: User):
    prisma = await get_db()

    foundUser = await prisma.user.find_unique(
        where={"id": user.id}
    )
    if foundUser is None:
        return {"user": None}

    updatedUser = await prisma.user.update(
        where={"id": user.id}, data=dict(user)
    )
    return {"user": updatedUser}


async def findAll(limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        users = await prisma.user.find_many()
        return {"users": users}
    else:
        users = await prisma.user.find_many(take=limit, skip=offset)
        length = await prisma.user.count()
        return {"users": users, "length": length}


async def findByID(id: int):
    prisma = await get_db()
    user = await prisma.user.find_unique(where={"id": id})
    return {"user": user}


async def findByAccountID(id: int):
    prisma = await get_db()
    account = await prisma.account.find_unique(
        where={"id": id}, include={"User": True}
    )
    if account is None:
        return {
            "status":"Loi"
        }
    return {
        "user":account.User
    }
