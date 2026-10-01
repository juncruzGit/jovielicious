import pytest

from src.packages.data.model.dish_sizes import DishSizes
from src.packages.data.model.dish_size import DishSize

@pytest.fixture
def dishsizes_add_size():
    dish_sizes = DishSizes()
    medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)
    result : bool = dish_sizes.add_size(medium_dishsize)
    yield dish_sizes, medium_dishsize, result


def test_return_value_should_be_true(dishsizes_add_size):
    dish_sizes, new_size, result = dishsizes_add_size 
    assert result is True, "result should be equal to True"


def test_count_should_increment_by_one(dishsizes_add_size):
    dish_sizes, new_size, result = dishsizes_add_size 
    assert len(dish_sizes.items) == 1, "item count should be 1"


def test_item_should_have_new_size_item(dishsizes_add_size):
    dish_sizes, new_size, result = dishsizes_add_size 
    assert new_size in dish_sizes.items, "items should contains medium_dishsize"
   
