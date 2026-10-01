import pytest

from src.packages.data.model.dish_sizes import DishSizes
from src.packages.data.model.dish_size import DishSize

@pytest.fixture
def dishsizes_add_size():
    dish_sizes = DishSizes()
    medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)
    new_item = DishSize(size="medium", description="dish medium description", price=200.00)
    dish_sizes.add_size(medium_dishsize)
    result : bool = dish_sizes.add_size(new_item)
    yield dish_sizes, new_item, result


def test_return_value_should_be_False(dishsizes_add_size):
    dish_sizes, new_size, result = dishsizes_add_size 
    assert result is False, "result should be equal to False"


def test_count_should_remains_as_one(dishsizes_add_size):
    dish_sizes, new_size, result = dishsizes_add_size 
    assert len(dish_sizes.items) == 1, "item count should be 1"


# def test_should_log_something(dishsizes_add_size):
#     dish_sizes, new_size, result = dishsizes_add_size 
#     assert new_size in dish_sizes.items, "items should contains medium_dishsize"
   
