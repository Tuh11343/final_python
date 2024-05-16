from fastapi import APIRouter
from controllers.paymentController import (
    pay
)

router = APIRouter(
    prefix="/api/v1/payment",  # Thiết lập tiền tố URL cho tất cả các route trong router này
    tags=["Payments"],
)

@router.post("/")
async def createGenre(accountID:int,total:float):
    response = await pay(accountID,total)
    return response


