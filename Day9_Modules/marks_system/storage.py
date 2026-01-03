import json

def load_file():
    try:
        with open("marks.json","r") as file:          
            try:
                marks = json.load(file)
            except json.JSONDecodeError:
                marks=[]
    except FileNotFoundError:
        marks=[]
        
    return marks

def save_file(marks):
    with open("marks.json","w") as file:
            json.dump(marks,file,indent=4)