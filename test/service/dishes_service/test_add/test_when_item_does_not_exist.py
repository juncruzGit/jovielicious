import pytest

from src.packages.data.model.dish import Dish
from src.packages.service.dishes_service import DishesService

__dish = Dish("carbonara", "pasta")

@pytest.fixture
def dishes_service():
    return DishesService()

def test_result(dishes_service, mocker):
    mocker.stopall()
    mocked_repo_find = mocker.patch.object(
        dishes_service._repository, 
        "find", 
        return_value = None)
    result: Dish | None = dishes_service.add(__dish)
    assert result == __dish , "Returned value should be the added item"


def test_repo_should_call_insert(dishes_service, mocker):
    mocker.stopall()
    mocked_repo_find = mocker.patch.object(
        dishes_service._repository, 
        "find", 
        return_value = None)

    mocked_repo_insert = mocker.patch.object(
            dishes_service._repository, 
            "insert", 
            return_value = None)
    
    result: Dish | None = dishes_service.add(__dish)
    mocked_repo_insert.assert_called_once_with(__dish)