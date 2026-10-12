from fastapi import status


def test_when_invoked(mocked_dish_service, test_client):
    mocked_dish_service.get.return_value = None
    response = test_client.get('/dishes/carbonara')
    mocked_dish_service.get.assert_called_once_with("carbonara")


def test_when_dish_does_not_exists(mocked_dish_service, test_client):
    mocked_dish_service.get.return_value = None

    response = test_client.get('/dishes/carbonara')
    
    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Item not found"}


def test_when_dish_exists(mocked_dish_service, test_client, sample_dish):
    mocked_dish_service.get.return_value = sample_dish
    
    response = test_client.get('/dishes/carbonara')
    
    assert response.status_code == status.HTTP_200_OK, "Should return Ok Status"
    assert response.json() == {'id': 'carbonara', 'name': 'carbonara', 'category': 'pasta', 'sizes': {}}
