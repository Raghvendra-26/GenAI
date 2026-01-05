from storage.json_store import load_json, save_json
from core.product_ops import calculate_inventory
from utils.logger import logger
import sys

file_path = "data/products.json"

def add_product():
    products = load_json(file_path)

    args = sys.argv[2:]
    flags = {}
    i = 0
    
    while i < len(args):
        if i+1 >= len(args):
            logger.error(f"Missing value for flag {args[i]}")
            return
        
        key = args[i]
        value = args[i+1]
        clean_key = key.lstrip("-")
        flags[clean_key] = value
        i+=2

    required = ['name','price','quantity']

    for r in required:
        if r not in flags:
            logger.error(f"Missing required flag: --{r}")
            return
    
    try:
        price = int(flags["price"])
        quantity = int(flags["quantity"])
    except ValueError:
        logger.error(f"Price and Quantity must be a number")
        return

    flags["price"] = price
    flags["quantity"] = quantity

    products.append(flags)
    save_json(file_path,products)


def inventory_value():
    products = load_json(file_path)
    
    if not products:
        logger.error("No products in inventory")
        return

    total = calculate_inventory(products)      
    logger.info("Total inventory value: %s",total)