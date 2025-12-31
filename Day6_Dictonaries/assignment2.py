# calculate inventory value

def calculate_inventory_value(products):
    totalPrice = 0
    for item in products:
        price = item.get("price",0)
        quantity = item.get("quantity",0)
        totalPrice += price*quantity
    
    return totalPrice
    


products = [
  {"name": "Laptop", "price": 50000, "quantity": 10},
  {"name": "Mobile", "price": 20000, "quantity": 20}
]


print(calculate_inventory_value(products))