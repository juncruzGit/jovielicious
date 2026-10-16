from src.data import DishSize

def test_when_size_exist(dish_sizes, medium_dish):
    result: DishSize | None = dish_sizes.get_size("medium")
    assert result is medium_dish, "Should return the size requested"

def test_when_size_does_exist(dish_sizes):
    result: DishSize | None = dish_sizes.get_size("small")
    assert result is None, "Should return None"