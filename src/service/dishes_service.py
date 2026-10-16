from src.containers import Container

from src.data import DishRepository, Dish
from .base_service import BaseService

class DishesService(BaseService):

    __repository: DishRepository

    def __init__(self, repository: DishRepository = Container.dish_repository()):
        self.repository = repository


    @property
    def repository(self) -> DishRepository: 
        return self.__repository

    @repository.setter
    def repository(self, value:DishRepository):
        self.__repository = value
        
    
    def add(self, item: Dish) -> Dish | None:
        print(item.category)
        if (item.id is None or 
            self.repository.find(item.id) is None): 
                print("adding item")
                item.id = item.name
                self.repository.insert(item)
                return item
        else:
            print("item already exists")
            return None


    def get(self, criteria: dict | None = None) -> list[Dish] | None:
        return self.repository.get(criteria)


    def modify(self, item: Dish) -> None:
        return self.repository.update(item)


    def remove(self, id: str) -> bool:
        return self.repository.delete(id)