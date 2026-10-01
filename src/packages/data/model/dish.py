from dataclasses import dataclass

from .dish_size import DishSize
from .dish_sizes import DishSizes

class Dish():

    def __init__(
            self, 
            name: str, 
            category: str,
            id: str | None = None,
            sizes: DishSizes | None = None):
        self.name = name
        self.category = category

        if id is not None:
            self.id = id
        else:
            self.id = name

        self._sizes = sizes
        

    @property
    def id(self) -> str | None:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def sizes(self):
        if self._sizes is None:
            self._sizes = DishSizes()
        
        return self._sizes 

    @sizes.setter
    def dish_id(self, value: DishSizes):
        self._sizes = value


