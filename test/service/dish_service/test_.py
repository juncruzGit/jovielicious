import pytest

from src.packages.data.model.dish import Dish
from src.packages.service.dish_service import DishService

@pytest.fixture
def dish_service():
    return DishService()

def test_get(dish_service, mocker):
    mocked_repo_find = mocker.patch.object(dish_service.repository, "find")
    dish_service.get("carbonara")
    mocked_repo_find.assert_called_once_with("carbonara")


def test_removed(dish_service, mocker):
    mocked_repo_delete = mocker.patch.object(dish_service.repository, "delete")
    dish_service.remove("1")
    mocked_repo_delete.assert_called_once_with("1")

 
def test_update(dish_service, mocker):
    mocked_repo_update = mocker.patch.object(dish_service.repository, "update")
    dish = Dish("carbonara", "pasta")
    dish_service.modify(dish)
    mocked_repo_update.assert_called_once_with(dish)
