from dataclasses import dataclass

from .dish_size import DishSize

@dataclass
class DishSizes():
    
    def __init__(self, items: list[DishSize] | None = None):
        if items is not None:
            self._items = items
        else:
            self._items = []
             

    @property
    def items(self) -> list[DishSize]: 
        return self._items
        
    @items.setter
    def items(self, value: list[DishSize]):
        self._items = value

        
    def add_size(self, dish_size: DishSize)->bool:
        if self.get_size(dish_size.size) is None:
            self.items.append(dish_size)
            return True
        else:
            return False
        
    def update_size(self, dish_size: DishSize) -> bool:
            updated_size: DishSize | None = self.get_size(dish_size.size)

            if updated_size is not None:
                 updated_size.update(description=dish_size.description,
                                     price = dish_size.price)
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
            idx: int | None = self.__get_size_index(size)
            if (idx == None):
                return None
            else:
                return self.items[idx] 

            
    def __get_size_index(self, size:str) -> int | None:
            try:
                result: int = [i for i,
                               x in enumerate(self.items) 
                               if x.size.lower() == size][0]
            except IndexError:
                 return None
            else:
                return result
                



