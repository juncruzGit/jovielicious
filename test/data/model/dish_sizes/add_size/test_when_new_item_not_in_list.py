def test_return_value(dish_sizes, small_dish):
    __result = dish_sizes.add_size(small_dish)
    assert __result is True, "result should be equal to True"


def test_items_count(dish_sizes, small_dish):
    current_count: int = len(dish_sizes.items)
    dish_sizes.add_size(small_dish)  
    assert len(dish_sizes.items) == (current_count + 1), "item count increment by 1"


def test_items_updated_item(dish_sizes, small_dish):
    dish_sizes.add_size(small_dish)  
    assert small_dish in dish_sizes.items, "items should contains new_dishsize"
   
