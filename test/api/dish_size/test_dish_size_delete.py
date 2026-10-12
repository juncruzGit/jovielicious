from fastapi import status

def test_when_invoked(mocked_dish_sizes_service, test_client):
    mocked_dish_sizes_service.remove_size.return_value = None

    test_client.delete('/dishes/carbonara/sizes/small')

    mocked_dish_sizes_service.remove_size.assert_called_once_with("carbonara", "small")


def test_when_delete_returned_list_of_dish_sizes(mocked_dish_sizes_service, test_client, dish_sizes):
    mocked_dish_sizes_service.remove_size.return_value = dish_sizes

    response = test_client.delete('/dishes/carbonara/sizes/small')
    
    assert response.status_code == status.HTTP_200_OK, "Should return Ok Status"
    assert response.json() == {"message": "Success"}


def test_when_delete_returned_None(mocked_dish_sizes_service, test_client):
    mocked_dish_sizes_service.remove_size.return_value = None
    
    response = test_client.delete('/dishes/carbonara/sizes/small')
    
    assert response.status_code == status.HTTP_404_NOT_FOUND, "Should return Not found"
    assert response.json() == {"detail": "Dish size not found"}
    

