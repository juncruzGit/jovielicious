import logging

from jovielicious.data.repository.dish_repository import DishRepository
from jovielicious.data.model.dish import Dish, DishSize

class DishesService():

    _repository = DishRepository()

    def add(self, item: Dish) -> Dish:
        if item.id == None or self._repository.find(item.id) == None: 
            item.id = item.name.lower()
            self._repository.insert(item)
            logging.info(f"item {item} added.")
            return item
        else:
            return None

    def get(self, criteria :dict = None) -> list[Dish]:
        result = self._repository.get(criteria)
        return self._repository.get(criteria)

    def modify(self, item: Dish) -> None:
        return self._repository.update(item)

    def remove(self, id: str) -> None:
        return self._repository.delete(id)


