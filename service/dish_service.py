from dataclasses import dataclass

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


    def add_size(self, id:str, dish_size: DishSize) -> list[DishSize]:
        result: Dish = self.__repository.find(id)
        if (result == None):
            return
        else:
            if result.sizes.add_size(dish_size):
                self.modify(result)
                return result.sizes


    def remove_size(self, id: str, size: str) -> list[DishSize]:
        dish: Dish = self.__repository.find(id)
        if (dish == None):
            return None
        else:
            if (dish.remove_dishsize(size)):
                self.modify(dish)
                return dish.sizes
                
   
    def update_size(self, id:str , dish_size: DishSize) -> list[DishSize]:
        dish: Dish = self.__repository.find(id)
        if dish == None:
            return None
        else:
            if dish.update_size(dish_size):
                self.modify(dish)
                return dish.sizes  