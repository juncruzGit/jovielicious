from fastapi import status
from src import DishSize


def act(mocked_dish_sizes_service, test_client, sample_dish, return_value: list[DishSize] | None = None):
    mocked_dish_sizes_service.add_size.return_value = return_value
    return test_client.put("/dishes/carbonara/sizes", json=sample_dish.__dict__)


def test_when_invoked(mocked_dish_sizes_service, test_client, small_dish):
    # mocked_dish_sizes_service.add_size.return_value = None
    # size_to_add = DishSizeResource(size='small',
    #                                description='description for small', 
    #                                price=100.0)
        
    # test_client.put("/dishes/carbonara/sizes", json=small_dish.__dict__)

    response = act(mocked_dish_sizes_service, test_client, small_dish)
    mocked_dish_sizes_service.add_size.assert_called_once_with("carbonara", small_dish)


def test_add_size_returns_none(mocked_dish_sizes_service, test_client, small_dish):
    response = act(mocked_dish_sizes_service, test_client, small_dish)

    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Item not found"}


def test_when_item_exist(mocked_dish_sizes_service, test_client, medium_dish, dish_sizes):
    response = act(mocked_dish_sizes_service, test_client, medium_dish, dish_sizes.items)
    
    assert response.status_code == status.HTTP_202_ACCEPTED, "Should return Accepted result"
    assert response.json() ==[
        {'size': 'medium', 'description': 'dish medium description', 'price': 200.0},
        {'size': 'large', 'description': 'dish large description', 'price': 500.0}]
    