from pydantic import BaseModel

from jovielicious.data.model.dish_size import DishSize
from jovielicious.data.model.dish_sizes import DishSizes

class DishResource (BaseModel):
    id: str | None = None  
    name: str
    category: str
    sizes : DishSizes | None = None  


# class DishSizesResource(BaseModel, DishSizes):
#     pass


class DishSizeResource(BaseModel, DishSize):
    pass