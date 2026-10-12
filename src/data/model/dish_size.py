from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class DishSize(BaseModel):
  
    def __init__(
            self, 
            size: str,
            description: str,
            price: float):
        self.size = size
        self.description = description
        self.price = price

    def update(self, description: str, price: float) -> DishSize:
        self.description = description
        self.price = price
        return self
