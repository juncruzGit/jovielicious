from fastapi import FastAPI

# from routers import dish, dishes, dish_sizes, dish_size
from .routers import dishes

app = FastAPI()

app.include_router(dishes.router)
# app.include_router(dish.router)
# app.include_router(dish_sizes.router)
# app.include_router(dish_size.router)