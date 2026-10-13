from typing import cast

from fastapi import status
from src import DishResource

def act(mocked_dish_service, test_client, sample_dish, return_value: DishResource | None = None ):
    mocked_dish_service.modify.return_value = return_value
    response = test_client.put("dishes/carbonara", json=sample_dish.__dict__)
    return response


def test_when_invoked(mocked_dish_service, test_client, sample_dish):
    response = act(mocked_dish_service, test_client, sample_dish)

    mocked_dish_service.modify.assert_called_once_with(sample_dish)


def test_when_new_item_already_exist(mocked_dish_service, test_client, sample_dish):
    response = act(mocked_dish_service, test_client, sample_dish, 
                   return_value=cast(DishResource, sample_dish))

    assert response.status_code == status.HTTP_200_OK, "Should return Ok result"
    assert response.json() == {'id': 'carbonara', 'name': 'carbonara', 'category': 'pasta', 'sizes': {'items':[]}}

def test_when_new_item_not_exist(mocked_dish_service, test_client, sample_dish):
    response = act(mocked_dish_service, test_client, sample_dish)
   
    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Item not found"}