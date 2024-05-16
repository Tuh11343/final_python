from fastapi import APIRouter
from controllers.userController import (
    User,
    create,
    delete,
    findAll,
    findByAccountID,
    findByID,
    update,
)

router = APIRouter(
    prefix="/api/v1/user",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["Users"],
)

@router.get("/")
async def findAllUser(limit:int=None,offset:int=None):
    response = await findAll(limit,offset)
    return response

@router.get("/id")
async def findUserByID(id:int):
    response = await findByID(id)
    return response

@router.get("/accountID")
async def findUserByAccountID(id:int):
    response = await findByAccountID(id)
    return response

@router.put("/")
async def updateUser(user:User):
    response = await update(user)
    return response

@router.post("/")
async def createUser(user:User):
    response = await create(user)
    return response

@router.delete("/")
async def deleteUser(id:int):
    response = await delete(id)
    return response

