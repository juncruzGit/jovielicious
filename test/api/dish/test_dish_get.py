from fastapi import status

from src import Dish

def act(mocked_dish_service, test_client, return_value : Dish | None = None):
    mocked_dish_service.get.return_value = return_value
    return test_client.get('/dishes/carbonara')


def test_when_invoked(mocked_dish_service, test_client):
    response = act(mocked_dish_service, test_client)
    mocked_dish_service.get.assert_called_once_with("carbonara")


def test_when_dish_does_not_exists(mocked_dish_service, test_client):
    response = act(mocked_dish_service, test_client)

    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Item not found"}


def test_when_dish_exists(mocked_dish_service, test_client, sample_dish):
    response = act(mocked_dish_service, test_client, sample_dish)
    
    assert response.status_code == status.HTTP_200_OK, "Should return Ok Status"
    assert response.json() == {'id': 
                               'carbonara', 'name': 
                               'carbonara', 'category': 
                               'pasta',
                                'sizes': {'items': []}}