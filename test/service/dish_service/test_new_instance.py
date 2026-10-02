import pytest

from src.packages.service.dish_service import DishService
from src.packages.data.repository.dish_repository import DishRepository

@pytest.fixture
def dish_service():
    """create a fresh instance of DishService object"""
    return DishService()

def test_repository_type(dish_service):
    assert type(dish_service.repository) is DishRepository
