def test_when_size_exist(dish_sizes):
    result: bool = dish_sizes.remove_size("medium")
    assert result is True, "Should return True"

def test_when_size_does_exist(dish_sizes):
    result: bool = dish_sizes.remove_size("small")
    assert result is False, "Should return False"