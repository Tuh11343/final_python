from fastapi import APIRouter
from controllers.accountController import getAllAccount
from controllers.accountController import findByID
from controllers.accountController import deleteByID
from controllers.accountController import updateByID
from controllers.accountController import findByEmail
from controllers.accountController import signIn
from controllers.accountController import create
from controllers.accountController import Account

from fastapi import Request

router = APIRouter(
    prefix="/api/v1/account",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["Accounts"],
)


@router.get("/")
async def findAllAccount(limit:int=None,offset:int=None):
    response = await getAllAccount()
    return response

@router.get("/id")
async def findAcountByID(id:int):
    response = await findByID(id)
    return response

@router.get("/email")
async def findAcountByEmail(email:str):
    response = await findByEmail(email)
    return response

@router.get("/signIn")
async def signInAccount(email:str,password:str):
    response = await signIn(email,password)
    return response

@router.delete("/")
async def deleteAccount(id:int):
    response = await deleteByID(id)
    return response

@router.put("/")
async def updateAccount(account:Account):
    response = await updateByID(account)
    return response

@router.post("/")
async def createAccount(account:Account):
    response = await create(account)
    return response