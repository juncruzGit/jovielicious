from src import DishRepository, DishesService, Dish

def test_when_invoked(dishes_service: DishesService, mocked_repo, sample_dish: Dish):
    dishes_service.add(sample_dish)
    mocked_repo.find.assert_called_once_with(sample_dish.id), "Should find dish id from repo"


def test_when_item_already_exist(dishes_service:DishesService, mocked_repo, sample_dish: Dish):
    mocked_repo.find.return_value = sample_dish
    result: Dish | None = dishes_service.add(sample_dish)
    assert result is None , "Returned value should be None"


def test_when_item_does_not_exist(
        dishes_service:DishesService,
        mocked_repo, 
        sample_dish: Dish):

    mocked_repo.find.return_value = None
    result: Dish | None = dishes_service.add(sample_dish)
    mocked_repo.insert.assert_called_once_with(sample_dish)
    assert result is sample_dish , "Returned value should be the sample dish"
   
