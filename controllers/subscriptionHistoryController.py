from prismaConfig import get_db
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from dateutil.parser import parse

class SubscriptionHistory(BaseModel):
    id:Optional[int]=None
    name:str
    price:float
    start:Optional[str]=None
    end:Optional[str]=None

async def create(subscriptionHistory: SubscriptionHistory):
    prisma = await get_db()
    start_datetime = parse(subscriptionHistory.start)
    end_datetime = parse(subscriptionHistory.end)
    subscriptionHistory.start = datetime.fromisoformat(start_datetime.isoformat())
    subscriptionHistory.end = datetime.fromisoformat(end_datetime.isoformat())

    createdSubscriptionHistory = await prisma.subscriptionhistory.create(data=subscriptionHistory.dict(exclude_none=True))
    return {"subscriptionHistory": createdSubscriptionHistory}


async def delete(id: int):
    prisma = await get_db()

    subscriptionHistory = await prisma.subscriptionhistory.find_unique(where={"id": id})
    if subscriptionHistory is None:
        return {"subscriptionHistory": None}

    deletedSubscriptionHistory = await prisma.subscriptionhistory.delete(where={"id": id})
    return {"subscriptionHistory": deletedSubscriptionHistory}


async def update(subscriptionHistory: SubscriptionHistory):
    prisma = await get_db()
    start_datetime = parse(subscriptionHistory.start)
    end_datetime = parse(subscriptionHistory.end)
    subscriptionHistory.start = datetime.fromisoformat(start_datetime.isoformat())
    subscriptionHistory.end = datetime.fromisoformat(end_datetime.isoformat())

    foundSubscriptionHistory = await prisma.subscriptionhistory.find_unique(
        where={"id": subscriptionHistory.id}
    )
    if foundSubscriptionHistory is None:
        return {"subscriptionHistory": None}

    updatedSubscriptionHistory = await prisma.subscriptionhistory.update(
        where={"id": subscriptionHistory.id}, data=dict(subscriptionHistory)
    )
    return {"subscriptionHistory": updatedSubscriptionHistory}


async def findAll(limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        subscriptionHistorys = await prisma.subscriptionhistory.find_many()
        return {"subscriptionHistorys": subscriptionHistorys}
    else:
        subscriptionHistorys = await prisma.subscriptionhistory.find_many(take=limit, skip=offset)
        length = await prisma.subscriptionhistory.count()
        return {"subscriptionHistorys": subscriptionHistorys, "length": length}


async def findByID(id: int):
    prisma = await get_db()
    subscriptionHistory = await prisma.subscriptionhistory.find_unique(where={"id": id})
    return {"subscriptionHistory": subscriptionHistory}


async def findBySubscriptionID(id: int):
    prisma = await get_db()
    subscription = await prisma.subscription.find_unique(
        where={"id": id}, include={"subcription_history": True}
    )
    if subscription is None:
        return {
            "status":"Loi"
        }
    return {
        "subscriptionHistory":subscription.subcription_history
    }
