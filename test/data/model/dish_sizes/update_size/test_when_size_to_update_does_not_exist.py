from src.data import DishSize

def test_return_value(dish_sizes):
    size_to_update = DishSize(size="small", description="dish small description", price=300.00)
    result: bool = dish_sizes.update_size(size_to_update)
    assert result is False, "Should return False"
