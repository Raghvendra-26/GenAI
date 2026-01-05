def calculate_inventory(products):
    
    if not products:
        raise ValueError("Product list cannot be empty")
    
    total = 0
    
    for product in products:

        total += product["price"] * product["quantity"]
        
    return total