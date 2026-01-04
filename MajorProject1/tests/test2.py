def calculate_inventory(products):
    if not products:
        raise ValueError("Products list cannot be empty")

    total = 0
    
    for product in products:
        price = product["price"]
        quantity = product["quantity"]

        total += price*quantity

    return total

def test_calculate_inventory_valid():
    total = calculate_inventory([
        {"name":"phone","price":100,"quantity":50},
        {"name":"tablet","price":1000,"quantity":10}
        ])
    
    assert total == 15000
    
def test_calculate_inventory_invalid():
    try:
        total = calculate_inventory([])
        assert False
    except ValueError:
        assert True