from dataclasses import dataclass

from data.model.dish_sizes import DishSizes
from data.repository.dish_repository import DishRepository
from data.model.dish import Dish, DishSize
from service.dish_sizes_service import DishSizesService

class DishService():

    __repository = DishRepository()

    def get(self, id: str) -> Dish:
        return self.__repository.find(id)


    def modify(self, item: Dish) -> Dish:
        return self.__repository.update(item)


    def remove(self, id: str) -> bool:
        return self.__repository.delete(id)