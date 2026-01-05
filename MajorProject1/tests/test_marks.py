from core.marks_ops import calculate_marks_summary

def test_calculate_marks_valid():
    
    total,avg = calculate_marks_summary([10,20,30,40,50])
    assert total == 150
    assert avg == 30
    

def test_calculate_marks_invalid():
    try:
        calculate_marks_summary([])
        assert False
    except ValueError:
        assert True