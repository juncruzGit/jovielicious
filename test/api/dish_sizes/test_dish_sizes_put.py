from typing import cast

from fastapi import status
from src import Routes, DishSizeResource



def test_when_invoked(mocked_dish_sizes_service, test_client, small_dish):
    mocked_dish_sizes_service.add_size.return_value = None
    size_to_add = DishSizeResource(size='small',
                                   description='description for small', 
                                   price=100.0)
        
    test_client.put("/dishes/carbonara/sizes", json=small_dish.__dict__)
    mocked_dish_sizes_service.add_size.assert_called_once_with("carbonara", size_to_add)


def test_add_size_returns_none(mocked_dish_sizes_service, test_client, small_dish):
    mocked_dish_sizes_service.add_size.return_value = None
    response = test_client.put("/dishes/carbonara/sizes", json=small_dish.__dict__)

    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Item not found"}


def test_when_item_exist(mocked_dish_sizes_service, test_client, medium_dish, dish_sizes):
    mocked_dish_sizes_service.add_size.return_value = dish_sizes.items
    response = test_client.put("dishes/carbonara/sizes", json=medium_dish.__dict__)
    assert response.status_code == status.HTTP_202_ACCEPTED, "Should return Accepted result"
    assert response.json() ==[
        {'size': 'medium', 'description': 'dish medium description', 'price': 200.0},
        {'size': 'large', 'description': 'dish large description', 'price': 500.0}]
    