import pytest

from src.data import Dish, DishSize, DishSizes

@pytest.fixture
def sample_dish() -> Dish:
    return Dish("carbonara", "pasta")

@pytest.fixture
def dish_sizes(medium_dish, large_dish)->DishSizes:
    __dish_sizes = DishSizes()
    __dish_sizes.add_size(medium_dish)
    __dish_sizes.add_size(large_dish)
    return __dish_sizes
    

@pytest.fixture
def sample_dish_with_sizes(dish_sizes) -> Dish:
    return Dish("carbonara", "pasta", sizes=dish_sizes)


@pytest.fixture
def small_dish():
    """create a fresh instance of DishSize object"""
    return DishSize(size = "small", 
                    description="description for small", 
                    price = 100.00)


@pytest.fixture
def medium_dish():
    return DishSize(size="medium", 
                    description="dish medium description", 
                    price=200.00)

@pytest.fixture
def large_dish():
    return DishSize(size="large", 
                    description="dish large description", 
                    price=500.00)


