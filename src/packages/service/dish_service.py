from dataclasses import dataclass

from ..data.model.dish_sizes import DishSizes
from ..data.model.dish import Dish, DishSize
from ..data.repository.dish_repository import DishRepository


class DishService():

    __repository = DishRepository()

    @property
    def repository(self) -> DishRepository: 
        return self.__repository

    def get(self, id: str) -> Dish:
        return self.__repository.find(id)


    def modify(self, item: Dish) -> Dish:
        return self.__repository.update(item)


    def remove(self, id: str) -> bool:
        return self.__repository.delete(id)