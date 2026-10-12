from fastapi import status


def test_when_invoke(mocked_dish_sizes_service, test_client):
     mocked_dish_sizes_service.get_by_size.return_value = None
     test_client.get("/dishes/carbonara/sizes/small")
     mocked_dish_sizes_service.get_by_size.assert_called_once_with("carbonara", "small")


def test_when_dish_size_exists(mocked_dish_sizes_service, test_client, small_dish):
    mocked_dish_sizes_service.get_by_size.return_value = small_dish
    response = test_client.get("/dishes/carbonara/sizes/small")

    assert response.status_code == status.HTTP_200_OK, "Should Ok result"
    assert response.json() == {'size': 'small', 'description': 'description for small', 'price': 100.0}


def test_when_dish_size_does_not_exists(mocked_dish_sizes_service, test_client):
    mocked_dish_sizes_service.get_by_size.return_value = None
    response = test_client.get("/dishes/carbonara/sizes/small")

    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Dish size not found"}

