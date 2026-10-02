import pytest

from src.packages.data.model.dish_size import DishSize

@pytest.fixture
def dishsize():
    """create a fresh instance of DishSize object"""
    return DishSize(size = "small", 
                    description="description for small", 
                    price = 100.00)


def test_new_dishsize_size(dishsize):
    assert dishsize.size == "small", "size should be equal small"

def test_new_dishsize_descripton(dishsize):
    assert dishsize.description == "description for small"

def test_new_dishsize_price(dishsize):
    assert dishsize.price == 100, "price should be equal to 100"