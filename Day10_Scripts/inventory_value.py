import sys
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file>")
        sys.exit(1)
        
    file_path = sys.argv[1]

    try:
        with open(file_path,"r") as file:
            try:
                products = json.load(file)
            except json.JSONDecodeError:
                products=[]
    except FileNotFoundError:
        products=[]


    inventory_value = 0
    for product in products:
        price = product["price"]
        quantity = product["quantity"]

        inventory_value += price*quantity

    print("Total inventory value: ",inventory_value)
    
    
if __name__ == "__main__":
    main()