# save marks list to a file and load it back
import json


# loading marks at startup
try:
    with open("marks.json","r") as file:          
        try:
            marks = json.load(file)
        except json.JSONDecodeError:
            marks=[]
except FileNotFoundError:
    marks=[]


def add_marks():
    try:
        mark = int(input("Enter student marks: "))
    except ValueError:
        print("Enter a valid number")
        return
    if mark < 0:
        print("Marks cannot be negative")
    else:
        marks.append(mark)
        print("Marks added")
        
        
while True:
    print("\n--- Student Scoring System ---")
    print("1. Add Marks")
    print("2. View Marks")
    print("3. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_marks()
    elif choice =="2":
        print(marks)
    elif choice == "3":
        with open("marks.json","w") as file:
            json.dump(marks,file,indent=4)
        print("Exiting program")
        break
    else:
        print("Invalid choice")