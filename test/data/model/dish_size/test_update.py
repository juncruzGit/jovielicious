def test_updated_description(small_dish):
    updated_dishsize = small_dish.update(description="updated description", price=200) 
    assert updated_dishsize.description == "updated description" , "description should be equal to updated description"

def test_updated_price(small_dish):
    updated_dishsize = small_dish.update(description="updated description", price=200)
    assert updated_dishsize.price == 200, "price should be updated to 200"