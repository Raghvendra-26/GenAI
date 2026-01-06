def calculate_marks_summary(marks):
    
    if not marks:
        raise ValueError("Marks list is empty")
    
    total = 0    

    for mark in marks:
        total += mark["score"]
    
    average = total/len(marks)
    
    return total,average



def validate_mark(marks):
    if "name" not in marks or not marks["name"]:
        raise ValueError("Student name is required")

    if not isinstance(marks["score"], int) or marks["score"] < 0:
        raise ValueError("Invalid marks")

    return True