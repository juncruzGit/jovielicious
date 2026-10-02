import pytest

from src.packages.data.model.dish_size import DishSize


@pytest.fixture
def dishsize():
    """create a fresh instance of DishSize object"""
    return DishSize(size = "small", 
                    description="description for small", 
                    price = 100.00)


def test_updated_description(dishsize):
    updated_dishsize = dishsize.update(description="updated description", price=200) 
    assert updated_dishsize.description == "updated description" , "description should be equal to updated description"

def test_updated_price(dishsize):
    updated_dishsize = dishsize.update(description="updated description", price=200)
    assert updated_dishsize.price == 200, "price should be updated to 200"