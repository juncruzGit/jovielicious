from fastapi import status

def test_when_invoked(mocked_dish_service, test_client):
    mocked_dish_service.remove.return_value = True

    response = test_client.delete('/dishes/carbonara')

    mocked_dish_service.remove.assert_called_once_with("carbonara")


def test_when_successfuly(mocked_dish_service, test_client):
    mocked_dish_service.remove.return_value = True

    response = test_client.delete('/dishes/carbonara')
    
    assert response.status_code == status.HTTP_200_OK, "Should return Ok Status"
    assert response.json() == {"message": "Success"}

def test_when_usuccessfuly(mocked_dish_service, test_client):
    mocked_dish_service.remove.return_value = False

    response = test_client.delete('/dishes/carbonara')
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST, "Should return Bad Request"
    assert response.json() == {"detail": "Item not found."}


