from typing import cast

from fastapi import status
from src import DishSizeResource


def test_when_updated_size_is_invalid(mocked_dish_sizes_service, test_client, small_dish):
    response = test_client.patch('/dishes/carbonara/sizes/medium', json=small_dish.__dict__)

    assert response.status_code == status.HTTP_400_BAD_REQUEST, "Should return Ok result"
    assert response.json() == {"detail": "Updated size name is not equal to medium"}


def test_when_updated_size_is_valid(mocked_dish_sizes_service, test_client, small_dish):
    mocked_dish_sizes_service.update_size.return_value = None
    response = test_client.patch('/dishes/carbonara/sizes/small', json=small_dish.__dict__)

    updated_size: DishSizeResource = DishSizeResource(size='small', 
                                                      description='description for small', 
                                                      price=100.0)
    
    mocked_dish_sizes_service.update_size.assert_called_once_with("carbonara", updated_size)


def test_when_size_to_be_updated_does_exists(mocked_dish_sizes_service, test_client, small_dish):
    mocked_dish_sizes_service.update_size.return_value = None
    response = test_client.patch('/dishes/carbonara/sizes/small', json=small_dish.__dict__)

    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Dish size not found"}


def test_when_size_to_be_updated_exists(mocked_dish_sizes_service, test_client, medium_dish, dish_sizes):
    mocked_dish_sizes_service.update_size.return_value = dish_sizes.items
    response = test_client.patch('/dishes/carbonara/sizes/medium', json=medium_dish.__dict__)

    assert response.status_code == status.HTTP_202_ACCEPTED, "Should return accepted Result"



    
    