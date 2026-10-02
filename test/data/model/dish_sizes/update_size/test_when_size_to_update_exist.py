import pytest

from src.packages.data.model.dish_sizes import DishSizes
from src.packages.data.model.dish_size import DishSize

"""Arrange dishsizes with one item"""
__dish_sizes= DishSizes()
__medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)


@pytest.fixture
def dish_sizes():
    __dish_sizes.add_size(__medium_dishsize)
    return __dish_sizes


def test_return_value(dish_sizes):
    size_to_update = DishSize(size="medium", description="dish medium description", price=300.00)
    result: bool = dish_sizes.update_size(size_to_update)

    assert result is True, "Should return True"

def test_updated_price(dish_sizes):
    size_to_update = DishSize(size="medium", description="dish medium description", price=300.00)
    dish_sizes.update_size(size_to_update)

    updated_size = dish_sizes.get_size("medium")

    assert updated_size.price == 300

def test_updated_description(dish_sizes):
    size_to_update = DishSize(size="medium", description="updated dish medium description", price=300.00)
    dish_sizes.update_size(size_to_update)

    updated_size = dish_sizes.get_size("medium")

    assert updated_size.description == "updated dish medium description"
