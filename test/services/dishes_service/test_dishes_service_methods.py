from src.data import Dish


def test_get(dishes_service, mocked_repo):
    dishes_service.get()
    mocked_repo.get.assert_called_once_with(None)


def test_removed(dishes_service,  mocked_repo):
    dishes_service.remove("1")
    mocked_repo.delete.assert_called_once_with("1")

 
def test_update(dishes_service, mocked_repo):
    dish = Dish("carbonara", "pasta")
    dishes_service.modify(dish)
    mocked_repo.update.assert_called_once_with(dish)