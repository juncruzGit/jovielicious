from dataclasses import dataclass

from common.base_object import BaseObject
from data.model.dish_size import DishSize
from data.model.dish_sizes import DishSizes

class Dish(BaseObject):
    id: str | None = None  
    name: str
    category: str
    sizes: DishSizes 

    def __init__(
            cls, 
            name: str, 
            category: str,
            id: str = None,
            sizes: DishSizes = None):
        cls.name = name
        cls.category = category
        cls._id = id
        cls._sizes = sizes
        
        if (id == None):
            cls.id = name

        if cls._sizes == None:
            cls.sizes = DishSizes()


    @property
    def sizes(self):
       if (self._sizes == None):
           self.sizes == DishSizes()
           return self._sizes 


    @sizes.setter
    def id(self, value: DishSizes):
        self._sizes = value


