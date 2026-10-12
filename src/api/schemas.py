from pydantic import BaseModel

from src import Dish, DishSize, DishSizes


class DishResource (BaseModel):
    id: str | None = None  
    name: str
    category: str
    sizes : DishSizes

class DishSizeResource(BaseModel):
    size: str
    description: str
    price: float


class DishSizesResource(BaseModel):
    items : list[DishSizeResource]