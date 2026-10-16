from src.service import DishService
from src.containers import DishRepository

def test_repository_type():
    dish_service = DishService()
    assert type(dish_service.repository) is DishRepository