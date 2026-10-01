import logging



from ..data.repository.dish_repository import DishRepository
from ..data.model.dish import Dish, DishSize

class DishesService():

    _repository = DishRepository()

    def add(self, item: Dish) -> Dish | None:
        if (item.id is None or 
            self._repository.find(item.id) is None): 
                item.id = item.name
                self._repository.insert(item)
                logging.info(f"item {item} added.")
                return item
        else:
            return None

    def get(self, criteria: dict | None = None) -> list[Dish] | None:
        return self._repository.get(criteria)

    def modify(self, item: Dish) -> None:
        return self._repository.update(item)

    def remove(self, id: str) -> None:
        return self._repository.delete(id)


