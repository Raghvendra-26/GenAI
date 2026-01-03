
def add_marks(marks):
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
        
