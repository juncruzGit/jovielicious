from dataclasses import dataclass

from data.model.dish_size import DishSize
from data.model.dish_sizes import DishSizes

class Dish():

    def __init__(
            self, 
            name: str, 
            category: str,
            id: str | None = None,
            sizes: DishSizes | None = None):
        self.name = name
        self.category = category
        self._id = id
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


