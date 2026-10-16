from src.service import DishSizesService
from src.containers import DishRepository

def test_repository_type():
    dish_sizes_service = DishSizesService()
    assert type(dish_sizes_service.repository) is DishRepository