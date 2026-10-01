import pytest

from src.packages.data.model.dish_size import DishSize

@pytest.fixture
def dishsize():
    """create a fresh instance of DishSize object"""
    return DishSize(size = "small", 
                    description="description for small", 
                    price = 100.00)


def test_new_dishsize(dishsize):
    # size should be equal small
    assert dishsize.size == "small"
    # description should be equal to "description for small"
    assert dishsize.description == "description for small"
    #  price should be equal to 100
    assert dishsize.price == 100


def test_update_dishsize(dishsize):
    updated_dishsize = dishsize.update(description="updated description", price=200)

    # description should be equal to updated description
    assert updated_dishsize.description == "updated description"
    
    # price should be updated to 200
    assert updated_dishsize.price == 200