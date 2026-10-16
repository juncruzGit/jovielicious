from src.data import DishSize

def test_when_invoked(dish_sizes_service, mocked_repo):
    mocked_repo.find.return_value = None
    dish_sizes_service.get("carbonara")
    mocked_repo.find.assert_called_once_with("carbonara")

def test_when_dish_does_not_exist(dish_sizes_service, mocked_repo):
    mocked_repo.find.return_value = None
    result: list[DishSize] = dish_sizes_service.get("carbonara")
    assert result is None


def test_when_dish_exist_and_has_no_sizes(dish_sizes_service,
                                          mocked_repo, sample_dish):
    mocked_repo.find.return_value = sample_dish
    result: list[DishSize] = dish_sizes_service.get("carbonara")
    assert result is None

def test_when_dish_exist_and_has_sizes(dish_sizes_service, 
                                       mocked_repo, sample_dish_with_sizes, 
                                       dish_sizes):
    mocked_repo.find.return_value = sample_dish_with_sizes
    result: list[DishSize] = dish_sizes_service.get("carbonara")
    assert result is dish_sizes.items

