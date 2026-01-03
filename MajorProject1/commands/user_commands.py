from storage.json_store import load_json,save_json
import sys

file_path = "data/users.json"

def list_users():
    users = load_json(file_path)
    
    if not users:
        print("No users found")
        return
    
    for index,user in enumerate(users,start=1):
        print(f'\nUser {index}')
        for key,value in user.items():
            print(f"{key}: {value}")


def add_user():
    users = load_json(file_path)
    
    args = sys.argv[2:]
    flags = {}
    i = 0
    
    while i < len(args):
        
        if i + 1 >= len(args):
            print(f"Missing value for flag {args[i]}")
            return

        key = args[i]
        value = args[i+1]
        clean_key = key.lstrip('-')
        flags[clean_key] = value
        i += 2
    
    required = ["name","age","email"]
    for r in required:
        if r not in flags:
            print(f"Missing required flag: --{r}")
            return
    
    try:
        age = int(flags["age"])
    except ValueError:
        print("Age must be a number")
        return
    
    flags["age"] = age
    
    users.append(flags)
    
    save_json(file_path,users)