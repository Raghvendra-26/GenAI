from core.product_ops import calculate_inventory

def test_calculate_inventory_valid():
    total = calculate_inventory([
        {"name":"phone","price":10000,"quantity":10},
        {"name":"tablet","price":20000,"quantity":5}
    ])
    
    assert total == 200000
    
def test_calculate_inventory_empty():
    try:
        calculate_inventory([])
        assert False
    except ValueError:
        assert True
        