from fastapi import status
from src.data import DishSizes


def act(mocked_dish_sizes_service, test_client, return_value:list[DishSizes] | None = None):
    mocked_dish_sizes_service.get.return_value = return_value
    
    return test_client.get("/dishes/carbonara/sizes")

def test_when_invoked(mocked_dish_sizes_service, test_client):
    act(mocked_dish_sizes_service, test_client)
    mocked_dish_sizes_service.get.assert_called_once_with("carbonara")


def test_when_no_dish_sizes_exists(mocked_dish_sizes_service, test_client):
    response = act(mocked_dish_sizes_service, test_client)
    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Item not found"}


def test_when_dishes_available(mocked_dish_sizes_service, test_client, dish_sizes):

    response = act(mocked_dish_sizes_service, test_client, dish_sizes.items)
    assert response.status_code == status.HTTP_200_OK, "Should return Ok Status"
    assert response.json() == [
        {'size': 'medium', 'description': 'dish medium description', 'price': 200.0}, 
        {'size': 'large', 'description': 'dish large description', 'price': 500.0}
        ]
    


