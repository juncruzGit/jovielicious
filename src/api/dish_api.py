from typing import Annotated

from fastapi import FastAPI

from src import home, dish, dishes, dish_sizes, dish_size
from src import DishesService

app = FastAPI()

app.include_router(home.router)
app.include_router(dishes.router)
app.include_router(dish.router)
app.include_router(dish_sizes.router)
app.include_router(dish_size.router)