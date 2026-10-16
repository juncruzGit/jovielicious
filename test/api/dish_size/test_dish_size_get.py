from fastapi import status

from src.data import DishSizes

def act(mocked_dish_sizes_service, test_client, return_value: DishSizes | None = None):
    mocked_dish_sizes_service.get_by_size.return_value = return_value
    return test_client.get("/dishes/carbonara/sizes/small")

def test_when_invoke(mocked_dish_sizes_service, test_client):
    act(mocked_dish_sizes_service, test_client)
     
    mocked_dish_sizes_service.get_by_size.assert_called_once_with("carbonara", "small")


def test_when_dish_size_exists(mocked_dish_sizes_service, test_client, small_dish):
    response = act(mocked_dish_sizes_service, test_client, small_dish )

    assert response.status_code == status.HTTP_200_OK, "Should Ok result"
    assert response.json() == {'size': 'small', 'description': 'description for small', 'price': 100.0}


def test_when_dish_size_does_not_exists(mocked_dish_sizes_service, test_client):
    response = act(mocked_dish_sizes_service, test_client)
    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Dish size not found"}

