import pytest

from src.packages.data.model.dish import Dish
from src.packages.service.dishes_service import DishesService

__dish = Dish("carbonara", "pasta")

@pytest.fixture
def dishes_service():
    return DishesService()

def test_result(dishes_service, mocker):
    mocked_repo_find = mocker.patch.object(dishes_service._repository, "find", return_value = __dish)

    result: Dish | None = dishes_service.add(__dish)
    assert result is None , "Returned value should be None"