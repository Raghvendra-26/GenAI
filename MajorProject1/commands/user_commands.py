from storage.json_store import load_json,save_json
from utils.logger import logger
from core.user_ops import validate_user
import sys

file_path = "data/users.json"

def list_users():
    users = load_json(file_path)
    
    if not users:
        logger.error("No users found")
        return
    
    for index,user in enumerate(users,start=1):
        logger.info(f'\nUser {index}')
        for key,value in user.items():
            logger.info(f"{key}: {value}")


def add_user():
    users = load_json(file_path)
    
    args = sys.argv[2:]
    flags = {}
    i = 0
    
    while i < len(args):
        
        if i + 1 >= len(args):
            logger.error(f"Missing value for flag {args[i]}")
            return

        key = args[i]
        value = args[i+1]
        clean_key = key.lstrip('-')
        flags[clean_key] = value
        i += 2
    
    required = ["name","age","email"]
    for r in required:
        if r not in flags:
            logger.error(f"Missing required flag: --{r}")
            return
    
    try:
        flags["age"] = int(flags["age"])
    except ValueError:
        logger.error("Age must be a number")
        return
    
    #validation
    try:
        validate_user(flags)
    except ValueError as e:
        logger.error(str(e))
        return
    
    users.append(flags)
    
    save_json(file_path,users)
    logger.info("User added successfully")