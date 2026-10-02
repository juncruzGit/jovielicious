import pytest

from src.packages.data.model.dish_sizes import DishSizes
from src.packages.data.model.dish_size import DishSize

"""Arrange dishsizes where new item already exists"""
__medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)
__new_item = DishSize(size="medium", description="dish medium description", price=200.00)


@pytest.fixture
def dish_sizes(mocker):

    __dish_sizes= DishSizes()
    __dish_sizes.add_size(__medium_dishsize)
    return __dish_sizes


def test_return_value(dish_sizes):
    __result : bool = dish_sizes.add_size(__new_item)
    assert __result is False, "result should be equal to False"


def test_items_count(dish_sizes):
    dish_sizes.add_size(__new_item)
    assert len(dish_sizes.items) == 1, "item count should be 1"

def test_logging(dish_sizes, mocker):
    mock_logging = mocker.patch('src.packages.data.model.dish_sizes.logging.info')
    dish_sizes.add_size(__new_item)
    mock_logging.assert_called_once_with("Dish medium already exists.")

   
