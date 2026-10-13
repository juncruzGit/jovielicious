from typing import cast

from fastapi import status
from src import DishSizeResource, DishSize


def act(mocked_dish_sizes_service, test_client, dish_to_update,
        size_id: str = "small", 
        return_value: list[DishSize] | None = None):

    mocked_dish_sizes_service.update_size.return_value = return_value
    return test_client.patch(f'/dishes/carbonara/sizes/{size_id}',json=dish_to_update.__dict__)


def test_when_updated_size_is_invalid(mocked_dish_sizes_service, test_client, small_dish):
    response = act(mocked_dish_sizes_service, test_client, small_dish, size_id="medium")

    assert response.status_code == status.HTTP_400_BAD_REQUEST, "Should return Ok result"
    assert response.json() == {"detail": "Updated size name is not equal to medium"}


def test_when_updated_size_is_valid(mocked_dish_sizes_service, test_client, small_dish):
    updated_size: DishSizeResource = DishSizeResource(size='small', 
                                                      description='description for small', 
                                                      price=100.0)

    response = act(mocked_dish_sizes_service, test_client, small_dish, size_id="small")
    
    mocked_dish_sizes_service.update_size.assert_called_once_with("carbonara", DishSize(**updated_size.model_dump()))


def test_when_size_to_be_updated_does_exists(mocked_dish_sizes_service, test_client, small_dish):
    response = act(mocked_dish_sizes_service, test_client, small_dish, size_id="small")
        
    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Dish size not found"}


def test_when_size_to_be_updated_exists(mocked_dish_sizes_service, test_client, medium_dish, dish_sizes):
    response = act(mocked_dish_sizes_service, test_client, medium_dish, size_id="medium", return_value=dish_sizes.items)
    assert response.status_code == status.HTTP_202_ACCEPTED, "Should return accepted Result"



    
    