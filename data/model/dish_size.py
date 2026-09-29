from dataclasses import dataclass

@dataclass
class DishSize:
    size: str
    description: str
    price: float

    def __init__(
            cls, 
            size: str,
            description: str,
            price: str):
        cls.size = size
        cls.description = description
        cls.price = price

    def update(self, description: str, price:str):
        self.description = description
        self.price = price
