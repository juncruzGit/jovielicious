import pytest

from src.packages.data.model.dish_sizes import DishSizes
from src.packages.data.model.dish_size import DishSize

@pytest.fixture
def dishsizes():
      return DishSizes()


def test_new_instance_items_not_None(dishsizes):
    assert dishsizes.items is not None


def test_new_instance_items_count(dishsizes):
    assert len(dishsizes.items) == 0


@pytest.fixture
def dishsizes_add_item(dishsizes):
    medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)
    result : bool = dishsizes.add_size(medium_dishsize)
    return dishsizes

def test_dishsizes_add_size_result(dishsizes):
    medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)
    result : bool = dishsizes.add_size(medium_dishsize)

    assert result is True, "result should be equal to True"

def test_dishsizes_count_after_add_size(dishsizes):
    medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)
    result : bool = dishsizes.add_size(medium_dishsize)
    assert len(dishsizes.items) == 1, "item count should be 1"

def test_dishsizes_item_after_add_size_item(dishsizes):
    medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)
    result : bool = dishsizes.add_size(medium_dishsize)
    assert medium_dishsize in dishsizes.items, "items should contains medium_dishsize"
   
