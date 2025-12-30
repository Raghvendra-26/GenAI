marks = []

def add_marks():
    mark = int(input("Enter student marks: "))
    if mark < 0:
        print("Marks cannot be negative")
    else:
        marks.append(mark)
        print("Marks added")

def total_marks():
    if not marks:
        return 0
    total = 0
    for mark in marks:
        total += mark
    return total

def average_marks():
    if not marks:
        return 0
    return total_marks() / len(marks)

def highest_marks():
    if not marks:
        return None
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest

while True:
    print("\n--- Student Scoring System ---")
    print("1. Add Marks")
    print("2. Total Marks")
    print("3. Average Marks")
    print("4. Highest Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_marks()
    elif choice == "2":
        print("Total marks =", total_marks())
    elif choice == "3":
        print("Average marks =", average_marks())
    elif choice == "4":
        highest = highest_marks()
        if highest is None:
            print("Marks list is empty")
        else:
            print("Highest marks =", highest)
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
