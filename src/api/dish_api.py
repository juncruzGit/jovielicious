from fastapi import FastAPI
from .routers import dishes

app = FastAPI()

app.include_router(dishes.router)
# app.include_router(dish.router)
# app.include_router(dish_sizes.router)
# app.include_router(dish_size.router)