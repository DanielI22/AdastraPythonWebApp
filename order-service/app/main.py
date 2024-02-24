from fastapi import FastAPI
from .routers import users, products, orders, reviews

app = FastAPI()

app.include_router(users.router, tags=["Users"])
app.include_router(products.router, tags=["Products"])
app.include_router(orders.router, tags=["Orders"])
app.include_router(reviews.router, tags=["Reviews"])