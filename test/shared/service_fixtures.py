import pytest

from src.service import DishService, DishesService, DishSizesService
from src.data import DishRepository

@pytest.fixture
def mocked_repo(mocker):
    return mocker.Mock(spec=DishRepository)

     
@pytest.fixture
def dish_service(mocked_repo) -> DishService:
    """create a fresh instance of DishService object"""
    dish_service = DishService(mocked_repo)
    return dish_service


@pytest.fixture
def dishes_service(mocked_repo) -> DishesService:
    """create a fresh instance of DishesService object"""
    dishes_service = DishesService(mocked_repo)
    return dishes_service


@pytest.fixture
def dish_sizes_service(mocked_repo) -> DishSizesService:
    """create a fresh instance of DishesService object"""
    dish_sizes_service = DishSizesService(mocked_repo)
    return dish_sizes_service

