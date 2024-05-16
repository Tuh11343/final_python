from prismaConfig import get_db
from pydantic import BaseModel
from controllers.bookController import BookType
from typing import Optional


class Subscription(BaseModel):
    id:Optional[int]=None
    subscription_history_id: int
    duration: float
    price_per_month: float
    type: str
    limit_book_mark: int
    book_type: BookType
    class Config:
        use_enum_values = True


async def create(subscription: Subscription):
    prisma = await get_db()
    createdSubscription = await prisma.subscription.create(data=subscription.dict(exclude_none=True))
    return {"subscription": createdSubscription}


async def delete(id: int):
    prisma = await get_db()

    subscription = await prisma.subscription.find_unique(where={"id": id})
    if subscription is None:
        return {"subscription": None}

    deletedSubscription = await prisma.subscription.delete(where={"id": id})
    return {"subscription": deletedSubscription}


async def update(subscription: Subscription):
    prisma = await get_db()

    foundSubscription = await prisma.subscription.find_unique(
        where={"id": subscription.id}
    )
    if foundSubscription is None:
        return {"subscription": None}

    updatedSubscription = await prisma.subscription.update(
        where={"id": subscription.id}, data=dict(subscription)
    )
    return {"subscription": updatedSubscription}


async def findAll(limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        subscriptions = await prisma.subscription.find_many()
        return {"subscriptions": subscriptions}
    else:
        subscriptions = await prisma.subscription.find_many(take=limit, skip=offset)
        length = await prisma.subscription.count()
        return {"subscriptions": subscriptions, "length": length}


async def findByID(id: int):
    prisma = await get_db()
    subscription = await prisma.subscription.find_unique(where={"id": id})
    return {"subscription": subscription}


async def findByAccountID(id: int):
    prisma = await get_db()
    account = await prisma.account.find_unique(
        where={"id": id}, include={"Subscription": True}
    )
    if account is None:
        return {
            "status":"Loi"
        }
    return {
        "subscription":account.Subscription
    }
