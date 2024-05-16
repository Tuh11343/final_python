from fastapi import APIRouter
from controllers.subscriptionHistoryController import (
    SubscriptionHistory,
    create,
    delete,
    findAll,
    findBySubscriptionID,
    findByID,
    update,
)

router = APIRouter(
    prefix="/api/v1/subscriptionHistory",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["SubscriptionHistorys"],
)

@router.get("/")
async def findAllSubscriptionHistory(limit:int=None,offset:int=None):
    response = await findAll(limit,offset)
    return response

@router.get("/id")
async def findSubscriptionHistoryByID(id:int):
    response = await findByID(id)
    return response

@router.get("/subscriptionID")
async def findSubscriptionHistoryBySubscriptionID(id:int):
    response = await findBySubscriptionID(id)
    return response

@router.put("/")
async def updateSubscriptionHistory(subscriptionHistory:SubscriptionHistory):
    response = await update(subscriptionHistory)
    return response

@router.post("/")
async def createSubscriptionHistory(subscriptionHistory:SubscriptionHistory):
    response = await create(subscriptionHistory)
    return response

@router.delete("/")
async def deleteSubscriptionHistory(id:int):
    response = await delete(id)
    return response

