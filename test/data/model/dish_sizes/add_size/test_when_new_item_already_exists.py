def test_return_value(dish_sizes, medium_dish):
    __result : bool = dish_sizes.add_size(medium_dish)
    assert __result is False, "result should be equal `to False"

def test_items_count(dish_sizes, medium_dish):
    dish_sizes.add_size(medium_dish)
    assert len(dish_sizes.items) == 2, "item count should remain should be 2"

   
