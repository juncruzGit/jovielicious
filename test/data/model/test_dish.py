import pytest

from src.data import Dish, DishSizes


@pytest.mark.parametrize("id_val, expected",
                         [("carbonara", "carbonara"),
                          (None, "carbonara"),
                         ] )
def test_id_for_new_dish(id_val, expected):
    dish = Dish(name="carbonara", category="pasta", id=id_val)
    assert dish.id == expected, f'id should be equal to name {expected}'

def test_sizes_for_new_dish():
     dish = Dish(name="carbonara", category="pasta")
     assert type(dish.sizes) is DishSizes

    
