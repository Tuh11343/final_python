from prismaConfig import get_db
from pydantic import BaseModel
from stripe import StripeClient
import os

# stripe = StripeClient(os.getenv("STRIPE_SECRET_KEY"))
stripe = StripeClient("sk_test_51OoLwVIJd6dqOcnLa4vhiHbej0owQHGL4GtVcmzjBGidhHiGF9Ac8ElGYIXLr7rkFalGIqME9iRh7Y2MzEyjtt3A00E53uZOZK")

async def pay(accountID:int,total:float):
    prisma = await get_db()
    account=await prisma.account.find_first(where={
        'id':accountID
    },include={
        'User':True
    })
    if account is None:
        return {
            "status":"Loi"
        }
    customer= stripe.customers.create({
        "email":account.email,
        "name":account.User.name,
    })
    ephemeralKey=stripe.ephemeral_keys.create({
        "customer":customer.id,
    })
    paymentIntent=stripe.payment_intents.create({
        "amount":int(total),
        "currency":'usd',
        "customer":customer.id,
        "description":"Thanh toán phiên bản nâng cấp sách EBook",
        "automatic_payment_methods":{
            "enabled":True
        }
    })
    return {
        "paymentIntent": paymentIntent.client_secret,
        "ephemeralKey": ephemeralKey.secret,
        "customer": customer.id,
        "publishableKey": "pk_test_51OoLwVIJd6dqOcnLrG4klKc7bdtkzs8B4n2uR4LKcLDF63MW8wgZFBanyyorUf2QQ68y55RKoM2ehhM9VqJlZAfw00YmwYVffH"
    }

