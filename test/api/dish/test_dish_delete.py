from fastapi import status

def act(mocked_dish_service, test_client, return_value: bool):
    mocked_dish_service.remove.return_value = return_value
    return test_client.delete('/dishes/carbonara')


def test_when_invoked(mocked_dish_service, test_client):
    # mocked_dish_service.remove.return_value = True

    # response = test_client.delete('/dishes/carbonara')
    act(mocked_dish_service, test_client, True)

    mocked_dish_service.remove.assert_called_once_with("carbonara")


def test_when_successful(mocked_dish_service, test_client):
    mocked_dish_service.remove.return_value = True

    response = test_client.delete('/dishes/carbonara')
    
    assert response.status_code == status.HTTP_200_OK, "Should return Ok Status"
    assert response.json() == {"message": "Success"}


def test_when_usuccessful(mocked_dish_service, test_client):
    mocked_dish_service.remove.return_value = False

    response = test_client.delete('/dishes/carbonara')
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST, "Should return Bad Request"
    assert response.json() == {"detail": "Item not found."}