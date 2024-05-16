from prismaConfig import get_db
from pydantic import BaseModel
from typing import Optional


class Account(BaseModel):
    id:Optional[int]=None
    user_id:int
    subscription_id:int
    email:str
    password:str
    is_verified:bool

async def getAllAccount():
    prisma=await get_db()
    accounts=await prisma.account.find_many()
    return {
        "accounts":accounts
    }

async def findByID(id:int):
    prisma=await get_db()
    account = await prisma.account.find_unique(
        where={
            "id":id
        }
    )
    return {
        "account":account
    }

async def deleteByID(id:int):
    prisma=await get_db()
    foundAccount=await prisma.account.find_unique(where={
        "id":id
    })
    if foundAccount is None:
        return {
            "account":None
        }
    else:
        account= await prisma.account.delete(
        where={
            "id":id
        })
        return {
            "account":account
        }

async def updateByID(account:Account):
    prisma=await get_db()
    foundAccount=await prisma.account.find_unique(where={
        "id":account.id
    })
    if foundAccount is None:
        return{
            "account":None
        }
    else:
        accountUpdate= await prisma.account.update(where={
        "id":account.id
        },data=dict(account))
    return {
        "account":accountUpdate
    }


async def findByEmail(email:str):
    prisma=await get_db()
    foundAccount=await prisma.account.find_first(where={
        "email":email
    })
    return {
        "account":foundAccount
    }

async def signIn(email:str,password:str):
    prisma=await get_db()
    foundAccount=await prisma.account.find_first(where={
        "email":email,
        "password":password
    })
    return {
        "account":foundAccount
    }

async def create(account:Account):
    prisma=await get_db()
    createdAccount=await prisma.account.create(data=account.dict(exclude_none=True))
    return {
        "account":createdAccount
    }
    

