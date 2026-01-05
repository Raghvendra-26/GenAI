def calculate_marks_summary(marks):
    
    if not marks:
        raise ValueError("Marks list is empty")
    
    total = sum(marks)
    
    average = total/len(marks)
    
    return total,average