from pydantic import BaseModel

from ..data.model.dish_size import DishSize
from ..data.model.dish_sizes import DishSizes

class DishResource (BaseModel):
    id: str | None = None  
    name: str
    category: str
    sizes: DishSizes | None = None  

class DishSizeResource(BaseModel, DishSize):
    pass