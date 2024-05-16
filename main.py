from typing import Union
import uvicorn

from fastapi import FastAPI
from prismaConfig import get_db
from routes.authorRoute import router as authorRoute
from routes.accountRoute import router as accountRoute
from routes.bookAuthorRoute import router as bookAuthorRoute
from routes.bookGenreRoute import router as bookGenreRoute
from routes.bookRoute import router as bookRoute
from routes.favoriteRoute import router as favoriteRoute
from routes.genreRoute import router as genreRoute
from routes.paymentRoute import router as paymentRoute
from routes.subscriptionHistoryRoute import router as subscriptionHistoryRoute
from routes.subscriptionRoute import router as subscriptionRoute
from routes.userRoute import router as userRoute


app = FastAPI()
app.include_router(authorRoute)
app.include_router(accountRoute)
app.include_router(bookAuthorRoute)
app.include_router(bookGenreRoute)
app.include_router(bookRoute)
app.include_router(favoriteRoute)
app.include_router(genreRoute)
app.include_router(paymentRoute)
app.include_router(subscriptionHistoryRoute)
app.include_router(subscriptionRoute)
app.include_router(userRoute)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)