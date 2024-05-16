from fastapi import APIRouter
from controllers.subscriptionController import (
    Subscription,
    create,
    delete,
    findAll,
    findByAccountID,
    findByID,
    update,
)

router = APIRouter(
    prefix="/api/v1/subscription",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["Subscriptions"],
)

@router.get("/")
async def findAllSubscription(limit:int=None,offset:int=None):
    response = await findAll(limit,offset)
    return response

@router.get("/id")
async def findSubscriptionByID(id:int):
    response = await findByID(id)
    return response

@router.get("/accountID")
async def findSubscriptionByAccountID(id:int):
    response = await findByAccountID(id)
    return response

@router.put("/")
async def updateSubscription(subscription:Subscription):
    response = await update(subscription)
    return response

@router.post("/")
async def createSubscription(subscription:Subscription):
    response = await create(subscription)
    return response

@router.delete("/")
async def deleteSubscription(id:int):
    response = await delete(id)
    return response

