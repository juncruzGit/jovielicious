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


    # def add_size(self, id:str, dish_size: DishSize) -> list[DishSize] | None:
    #     result: Dish = self.__repository.find(id)
    #     if result is None:
    #         return None
    #     else:
    #         dish_sizes: DishSizes = result.size
    #         if dish_sizes.add_size(dish_size):
    #             self.modify(result)
    #             return result.sizes


    # def remove_size(self, id: str, size: str) -> list[DishSize] | None:
    #     dish: Dish = self.__repository.find(id)
    #     if dish is None:
    #         return None
    #     else:
    #         if (dish.remove_dishsize(size)):
    #             self.modify(dish)
    #             return dish.sizes
                
   
    # def update_size(self, id:str , dish_size: DishSize) -> list[DishSize] | None:
    #     dish: Dish = self.__repository.find(id)
    #     if dish is None:
    #         return None
    #     else:
    #         if dish.update_size(dish_size):
    #             self.modify(dish)
    #             return dish.sizes  