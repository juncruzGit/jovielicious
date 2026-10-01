import logging

from dataclasses import dataclass
from data.model.dish_size import DishSize

@dataclass
class DishSizes:
    
    def __init__(self, items: list[DishSize] | None = None):
        self._items = items

    @property
    def items(self) -> list[DishSize]:
        if self._items is None:
            self._items = []

        return self._items
        
    @items.setter
    def items(self, value: list[DishSize]):
        self.items = value

        
    def add_size(self, dishSize: DishSize)->bool:
        if (dishSize in self.items):
            logging.info(f"Dish {dishSize.size} already exists")
            return False
        else:
            logging.info(f'Adding {dishSize}')
            self.items.append(dishSize)
            return True


    def update_size(self, dish_size: DishSize) -> bool:
            updated_size: DishSize | None = self.get_size(dish_size.size)

            if updated_size is not None:
                 updated_size.update(description = dish_size.description, price = dish_size.price)
                 return True
            else:
                 return False

    
    def remove_size(self, size: str) -> bool:
            size_to_remove = self.get_size(size)
            if (size_to_remove) == None:
                return False
            else:
                self.items.remove(size_to_remove)
                return True

        
    def get_size(self, size: str) -> DishSize | None:
            idx = self.__get_size_index(size)
            if (idx == None):
                return None
            else:
                return self.items[idx] 

            
    def __get_size_index(self, size:str) -> int:
            return [i for i, x in enumerate(self.items) if x.size.lower() == size][0]



