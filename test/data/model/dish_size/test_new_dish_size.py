def test_new_dishsize_size(small_dish):
    assert small_dish.size == "small", "size should be equal small"

def test_new_dishsize_descripton(small_dish):
    assert small_dish.description == "description for small"

def test_new_dishsize_price(small_dish):
    assert small_dish.price == 100, "price should be equal to 100"