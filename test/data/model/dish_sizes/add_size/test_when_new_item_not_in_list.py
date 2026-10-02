import pytest

from src.packages.data.model.dish_sizes import DishSizes
from src.packages.data.model.dish_size import DishSize


"""/
Arrange dishsizes that will have no existing item or new item does not exists
/"""
__new_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)


@pytest.fixture
def dish_sizes():
    return DishSizes()
    

def test_return_value(dish_sizes):
    __result = dish_sizes.add_size(__new_dishsize)
    assert __result is True, "result should be equal to True"


def test_items_count(dish_sizes):
    dish_sizes.add_size(__new_dishsize)  
    assert len(dish_sizes.items) == 1, "item count should be 1"


def test_items_updated_item(dish_sizes):
    dish_sizes.add_size(__new_dishsize)  
    assert __new_dishsize in dish_sizes.items, "items should contains new_dishsize"
   
