from fastapi import status
from src import Routes, DishResource

def test_when_invoked(mocked_dish_service, test_client, sample_dish):
    mocked_dish_service.modify.return_value = None

    response = test_client.put("dishes/carbonara", json=sample_dish.__dict__)

    dish_to_add = DishResource(name="carbonara", category="pasta")
    mocked_dish_service.modify.assert_called_once_with(dish_to_add)

def test_when_new_item_already_exist(mocked_dish_service, test_client, sample_dish):
    mocked_dish_service.modify.return_value = sample_dish

    response = test_client.put("dishes/carbonara", json=sample_dish.__dict__)

    assert response.status_code == status.HTTP_200_OK, "Should return Ok result"
    assert response.json() == {'id': 'carbonara', 'name': 'carbonara', 'category': 'pasta', 'sizes': {}}

def test_when_new_item_not_exist(mocked_dish_service, test_client, sample_dish):
    mocked_dish_service.modify.return_value = None
    
    response = test_client.put("dishes/carbonara", json=sample_dish.__dict__)

    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Item not found"}



