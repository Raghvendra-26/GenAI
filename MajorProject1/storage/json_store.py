import json

def load_json(file_path):
    try:
        with open(file_path,"r") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
    except FileNotFoundError:
        users = []
        
    return users

def save_json(file_path,data):
    with open(file_path,"w") as file:
        json.dump(data,file,indent=4)