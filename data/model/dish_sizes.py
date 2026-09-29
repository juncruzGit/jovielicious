import logging
from dataclasses import dataclass
from data.model.dish_size import DishSize

@dataclass
class DishSizes:
    items: list[DishSize] | None = None

    def __init__(self, items: list[DishSize] = None):
        self.items = items

        if (self.items == None):
            self.items : list[DishSize] = [] 

        
    def add_size(self, dishSize: DishSize)->bool:
        if (dishSize in self.items):
            logging.info(f"Dish {dishSize.size} already exists")
            return False
        else:
            logging.info(f'Adding {dishSize}')
            self.items.append(dishSize)
            return True


    def update_size(self, dish_size: DishSize) -> bool:
            updated_size = self.get_size(dish_size.size)
            if (self.update_size == None):
                return False
            else:
                updated_size.update(
                    description = dish_size.description,
                    price = dish_size.price
                )
                return True


    def remove_size(self, size: str) -> bool:
            size_to_remove = self.get_size(size)
            if (size_to_remove) == None:
                return False
            else:
                self.items.remove(size_to_remove)
                return True

        
    def get_size(self, size: str) -> DishSize:
            idx = self.__get_size_index(size)
            if (idx == None):
                return None
            else:
                return self.items[idx] 

            
    def __get_size_index(cls, size:str) -> int:
            return [i for i, x in enumerate(cls.items) if x.size.lower() == size][0]



