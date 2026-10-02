import pytest

from src.packages.data.model.dish import Dish
from src.packages.service.dishes_service import DishesService

@pytest.fixture
def dishes_service():
    return DishesService()

def test_get(dishes_service, mocker):
    mocked_repo_get = mocker.patch.object(dishes_service._repository, "get")
    dishes_service.get()
    mocked_repo_get.assert_called_once()


def test_removed(dishes_service, mocker):
    mocked_repo_delete = mocker.patch.object(dishes_service._repository, "delete")
    dishes_service.remove("1")
    mocked_repo_delete.assert_called_once_with("1")

 
def test_update(dishes_service, mocker):
    mocked_repo_update = mocker.patch.object(dishes_service._repository, "update")
    dish = Dish("carbonara", "pasta")
    dishes_service.modify(dish)
    mocked_repo_update.assert_called_once_with(dish)
