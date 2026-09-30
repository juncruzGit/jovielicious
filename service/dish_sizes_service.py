import logging

from data.model.dish import Dish
from data.model.dish_size import DishSize
from data.model.dish_sizes import DishSizes
from data.repository.dish_repository import DishRepository

class DishSizesService():

    __repository = DishRepository()

    def get(self, id: str) -> list[DishSize] | None:
        dish: Dish | None = self.__get_dish(id)
                
        if (dish is None or dish.sizes is None):
            return None

        dish_sizes: DishSizes = dish.sizes
        return dish_sizes.items


    def get_by_size(self, id: str, size: str) -> DishSize | None:
        dish: Dish | None = self.__get_dish(id)

        if (dish is None or dish.sizes is None):
            return None

        dish_sizes: DishSizes = dish.sizes
        return dish_sizes.get_size(size)

    def add_size(self, id: str, new_size: DishSize) -> list[DishSize] | None: 
        dish: Dish | None = self.__get_dish(id)
        
        if dish is None:
            return None

        return self.__save_size("add", dish, new_size)     

    
    def update_size(self, id: str, new_size: DishSize) -> list[DishSize] | None: 
        dish: Dish | None = self.__get_dish(id)
                
        if dish is None:
            return None
        
        return self.__save_size("update", dish, new_size)    


    def remove_size(self, id: str, size: str) -> list[DishSize] | None: 
        dish: Dish | None = self.__get_dish(id)

        if (dish is None or dish.sizes is None):
            return None

        dish_sizes: DishSizes = dish.sizes
        dish_size: DishSize = dish_sizes.get_size(size)

        if dish_size is None:
            return None

        return self.__save_size("remove", dish, dish_size)    


    def __get_dish(self, id: str) -> Dish | None:
        dish: Dish = self.__repository.find(id)

        if dish is None:
            logging.info(f'Dish {id} does not exists.')

        return dish


    def __save_size(self, 
                    action: str, 
                    dish: Dish, 
                    dish_size: DishSize
                    ) -> list[DishSize] | None: 
        dish_sizes: DishSizes = dish.sizes

        if dish_sizes is None:
            dish_sizes = DishSizes()
            dish.sizes = dish_sizes
    
        if action == "add":
            dish_sizes.add_size(dish_size)
        elif action == "update":
            dish_sizes.update_size(dish_size)
        elif action == "remove":
            dish_sizes.remove_size(dish_size.size)
   
        self.__repository.update(dish)
        return dish_sizes.items
