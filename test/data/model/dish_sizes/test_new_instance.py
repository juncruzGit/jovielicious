import pytest

from src.packages.data.model.dish_sizes import DishSizes
from src.packages.data.model.dish_size import DishSize

@pytest.fixture
def dishsizes():
      return DishSizes()


def test_items_not_None(dishsizes):
    assert dishsizes.items is not None


def test_items_count(dishsizes):
    assert len(dishsizes.items) == 0

