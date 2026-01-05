from storage.json_store import load_json, save_json
from core.product_ops import calculate_inventory
from utils.logger import logger
from utils.arg_parser import parse_flags
import sys

file_path = "data/products.json"

def add_product():
    products = load_json(file_path)

    args = sys.argv[2:]
    #flag parser
    try:
        flags = parse_flags(args)
    except ValueError as e:
        logger.error(str(e))
        return

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