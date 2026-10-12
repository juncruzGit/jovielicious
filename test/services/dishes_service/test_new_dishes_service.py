
from src import DishesService
from src.containers import DishRepository

def test_repository_type():
    dishes_service = DishesService()
    assert type(dishes_service.repository) is DishRepository
