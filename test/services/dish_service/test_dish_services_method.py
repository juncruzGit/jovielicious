from src.service import DishService
from src.data import Dish


def test_get(dish_service: DishService, mocked_repo):
    dish_service.get("carbonara")
    mocked_repo.find.assert_called_once_with("carbonara")


def test_removed(dish_service: DishService, mocked_repo):
    dish_service.remove("1")
    mocked_repo.delete.assert_called_once_with("1")

 
def test_update(dish_service: DishService, sample_dish: Dish, mocked_repo):  
    dish_service.modify(sample_dish)
    mocked_repo.update.assert_called_once_with(sample_dish)
