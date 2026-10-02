import logging

from ..data.repository.dish_repository import DishRepository
from ..data.model.dish import Dish, DishSize

class DishesService():
    __repository = DishRepository()

    def add(self, item: Dish) -> Dish | None:
        if (item.id is None or 
            self.__repository.find(item.id) is None): 
                item.id = item.name
                self.__repository.insert(item)
                return item
        else:
            return None

    @property
    def repository(self) -> DishRepository:
         return self.__repository;


    def get(self, criteria: dict | None = None) -> list[Dish] | None:
        return self.__repository.get(criteria)


    def modify(self, item: Dish) -> None:
        return self.__repository.update(item)


    def remove(self, id: str) -> bool:
        return self.__repository.delete(id)