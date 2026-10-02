import pytest

from src.packages.service.dishes_service import DishesService
from src.packages.data.repository.dish_repository import DishRepository

@pytest.fixture
def dishes_service():
    """create a fresh instance of Dish object"""
    return DishesService()

def test_repository_type(dishes_service):
    assert type(dishes_service._repository) is DishRepository
