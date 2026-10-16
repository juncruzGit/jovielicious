from src.data import DishSizes


def test_items_not_None():
    dish_sizes  = DishSizes()
    assert dish_sizes.items is not None


def test_items_count():
    dish_sizes  = DishSizes()
    assert len(dish_sizes.items) == 0