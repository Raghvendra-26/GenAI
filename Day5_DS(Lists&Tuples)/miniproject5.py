
# Student management system

students = []

def add_student():
    name = input("Enter student name: ").strip()
    if name:
        students.append(name)
        print("Student Added")
    else:
        print("Name cannot be empty")
    
def remove_student():
    name = input("Enter student name to remove : ").strip()
    if name in students:
        students.remove(name)
        print("Student removed")
    else:
        print("Student not found")

def view_students():
    if len(students) == 0:
        print("Student list is empty")
    else:
        print('\nStudents list:- ')
        for index, student in enumerate(students, start=1):
            print(index, "-", student)
    

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Exit")

    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Wrong input")
    