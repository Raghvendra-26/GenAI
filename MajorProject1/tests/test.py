def calculate_marks_summary(marks):
    
    if not marks:
        raise ValueError("Marks list is empty")
    
    total = sum(marks)
    avg = total/len(marks)
    return total,avg

# def calculate_test_marks():
#     total,avg = calculate_marks_summary([])
#     assert total == 60
#     assert avg == 20
    
def test_calculate_marks_summary_valid():
    total, avg = calculate_marks_summary([10, 20, 30])
    assert total == 60
    assert avg == 20


def test_calculate_marks_summary_empty():
    try:
        calculate_marks_summary([])
        assert False  # should not reach here
    except ValueError:
        assert True
