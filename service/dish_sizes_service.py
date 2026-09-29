import logging

from jovielicious.data.model.dish import Dish
from jovielicious.data.model.dish_size import DishSize
from jovielicious.data.model.dish_sizes import DishSizes
from jovielicious.data.repository.dish_repository import DishRepository

class DishSizesService():
    __repository = DishRepository()

    def get(self, id: str) -> list[DishSize]:
        dish:Dish = self.__get_dish(id)
                
        if (dish==None or dish.sizes==None):
            return None

        dish_sizes : DishSizes = dish.sizes
        return dish_sizes.items


    def get_by_size(self, id : str, size: str) -> DishSize:
        dish :Dish = self.__get_dish(id)

        if dish == None or dish.sizes == None:
            return None

        dish_sizes : DishSizes = dish.sizes
        return dish_sizes.get_size(size)

    def add_size(self, id: str, new_size : DishSize) -> list[DishSize]: 
        dish :Dish = self.__get_dish(id)
        
        if (dish==None):
            return None

        return self.__save_size("add", dish, new_size)     

    
    def update_size(self, id: str, new_size : DishSize) -> list[DishSize]: 
        dish :Dish = self.__get_dish(id)
                
        if (dish==None):
            return None
        
        return self.__save_size("update", dish, new_size)    


    def remove_size(self, id: str, size : str) -> list[DishSize]: 
        dish: Dish=self.__get_dish(id)

        if dish == None or dish.sizes == None:
            return None

        dish_sizes : DishSizes = dish.sizes
        dish_size : DishSize = dish_sizes.get_size(size)

        if dish_size == None:
            return None

        return self.__save_size("remove", dish, dish_size)    


    def __get_dish(self, id: str) -> Dish:
        dish : Dish = self.__repository.find(id)

        if (dish==None):
            logging.info(f'Dish {id} does not exists.')

        return dish


    def __save_size(self, action: str, dish : Dish, dish_size : DishSize) -> list[DishSize]: 
        dish_sizes : DishSizes = dish.sizes

        if dish_sizes == None:
            dish_sizes = DishSizes()
            dish.sizes = dish_sizes
    
        if action=="add":
            dish_sizes.add_size(dish_size)
        elif action=="update":
            dish_sizes.update_size(dish_size)
        elif action=="remove":
            dish_sizes.remove_size(dish_size.size)
   
        self.__repository.update(dish)
        return dish_sizes.items
