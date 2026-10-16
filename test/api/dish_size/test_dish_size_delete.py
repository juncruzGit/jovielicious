from fastapi import status
from src.data import DishSizes


def act(mocked_dish_sizes_service, test_client, return_value: DishSizes | None = None):
    mocked_dish_sizes_service.remove_size.return_value = return_value
    return test_client.delete('/dishes/carbonara/sizes/small')
    

def test_when_invoked(mocked_dish_sizes_service, test_client):
    act(mocked_dish_sizes_service, test_client)

    mocked_dish_sizes_service.remove_size.assert_called_once_with("carbonara", "small")


def test_when_delete_returned_list_of_dish_sizes(mocked_dish_sizes_service, test_client, dish_sizes):
    response = act(mocked_dish_sizes_service, test_client, dish_sizes)
    
    assert response.status_code == status.HTTP_200_OK, "Should return Ok Status"
    assert response.json() == {"message": "Success"}


def test_when_delete_returned_None(mocked_dish_sizes_service, test_client):
    response = act(mocked_dish_sizes_service, test_client)
    
    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Dish size not found"}