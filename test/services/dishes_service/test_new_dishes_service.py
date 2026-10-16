from src.data import DishRepository
from src.service import DishesService


def test_repository_type():
    dishes_service = DishesService()
    assert type(dishes_service.repository) is DishRepository
