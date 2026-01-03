
from storage import save_file,load_file
from ops import add_marks

marks = load_file()

while True:
    print("\n--- Student Scoring System ---")
    print("1. Add Marks")
    print("2. View Marks")
    print("3. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_marks(marks)
    elif choice =="2":
        print(marks)
    elif choice == "3":
        save_file(marks)
        print("Exiting program")
        break
    else:
        print("Invalid choice")