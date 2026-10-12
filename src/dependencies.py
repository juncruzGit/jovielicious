from typing import Annotated

from fastapi import Depends

from src import DishService, DishesService, DishSizesService
from src import DishRepository

def get_repository():
    repository = DishRepository()
    try:
        yield repository
    finally:
        print("Closing DB connection")

def get_dishes_service(db: Annotated[DishRepository, Depends(get_repository)]) ->DishesService:
    return DishesService(repository=db)

def get_dish_service(db: Annotated[DishRepository, Depends(get_repository)]) -> DishService:
    return DishService(repository=db)

def get_dish_sizes_service(db: Annotated[DishRepository, Depends(get_repository)]) -> DishSizesService:
    return DishSizesService(repository=db)

dishes_service_dep = Annotated[DishesService, Depends(get_dishes_service)]
dish_service_dep = Annotated[DishService, Depends(get_dish_service)]
dish_sizes_service_dep = Annotated[DishSizesService, Depends(get_dish_sizes_service)]

   

