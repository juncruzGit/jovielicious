from dataclasses import dataclass

@dataclass
class DishSize:
    size: str
    description: str
    price: float

    def __init__(
            self, 
            size: str,
            description: str,
            price: float):
        self.size = size
        self.description = description
        self.price = price

    def update(self, description: str, price: float):
        self.description = description
        self.price = price
