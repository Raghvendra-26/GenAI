# save marks list to a file and load it back
import json

# loading marks at startup
with open("marks.json","r") as file:          # will produce a error if file is not present
    marks = json.load(file)

def add_marks():
    mark = int(input("Enter student marks: "))
    if mark < 0:
        print("Marks cannot be negative")
    else:
        marks.append(mark)
        print("Marks added")
        
        
        
while True:
    print("\n--- Student Scoring System ---")
    print("1. Add Marks")
    print("2. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_marks()
    elif choice == "2":
        with open("marks.json","w") as file:
            json.dump(marks,file,indent=4)
        print("Exiting program")
        break
    else:
        print("Invalid choice")