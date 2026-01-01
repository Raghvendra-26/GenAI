# calculate inventory value and saving it to file

import json

#loading products at startup
with open("products.json","r") as file:      # will produce a error if file is not present
    products = json.load(file)
    

def calculate_inventory_value(products):
    totalPrice = 0
    for item in products:
        price = item.get("price",0)
        quantity = item.get("quantity",0)
        totalPrice += price*quantity
    
    return totalPrice


def add_product():
    
    name = input("Enter product name: ").strip()
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    product = {
        "name":name,
        "price":price,
        "quantity":quantity,
    }
    
    products.append(product)
    print("Product added successfully")


while True:
    print("\n--- Product Manager ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. View inventory value")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        print(products)
    elif choice == "3":
        print(calculate_inventory_value(products))
    elif choice == "4":
        with open("products.json","w") as file:
            json.dump(products,file,indent=4)
        break
    else:
        print("Invalid choice")