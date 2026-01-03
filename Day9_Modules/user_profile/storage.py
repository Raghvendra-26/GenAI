import json

def load_file():
    try:                                      
        with open("users.json","r") as file:         
            try:                                        
                users = json.load(file)
            except json.JSONDecodeError:
                print("Data file corrupted, starting fresh")
                users = []
    except FileNotFoundError:
        users=[]
        
    return users
        

def save_file(users):
    with open("users.json","w") as file:
            json.dump(users,file,indent=4)