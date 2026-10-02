import pytest

from src.packages.data.model.dish_sizes import DishSizes
from src.packages.data.model.dish_size import DishSize


"""Arrange dishsizes where size exists"""
__dish_sizes= DishSizes()
__medium_dishsize = DishSize(size="medium", description="dish medium description", price=200.00)


@pytest.fixture
def dish_sizes():
    __dish_sizes.add_size(__medium_dishsize)
    return __dish_sizes


def test_when_size_exist(dish_sizes):
    result: DishSize | None = dish_sizes.get_size("medium")

    assert result is __medium_dishsize, "Should return the size requested"

def test_when_size_does_exist(dish_sizes):
    result: DishSize | None = dish_sizes.get_size("small")

    assert result is None, "Should return None"