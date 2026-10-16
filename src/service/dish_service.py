from src.containers import Container, DishRepository
from src.data import Dish
from .base_service import BaseService


class DishService(BaseService):

    __repository: DishRepository

    def __init__(self, repository: DishRepository = Container.dish_repository()):
        self.repository = repository

    @property
    def repository(self) -> DishRepository: 
        return self.__repository

    @repository.setter
    def repository(self, value:DishRepository):
        self.__repository = value


    def get(self, id: str) -> Dish:
        return self.repository.find(id)


    def modify(self, item: Dish) -> Dish | None:
        return self.repository.update(item)


    def remove(self, id: str) -> bool:
        return self.repository.delete(id)
