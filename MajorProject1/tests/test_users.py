from core.user_ops import validate_user

def test_validate_user_valid():
    user = {
        "name" : "Amit",
        "age" : 23,
        "email" : "amit@gmail.com"
    }
    
    assert validate_user(user) is True
    
def test_validate_user_invalid_age():
    try:
        validate_user({"name":"Amit","age": -5,"email": "amit@gmail.com"})
        assert False
    except ValueError:
        assert True
        
def test_validate_user_invalid_email():
    try:
        validate_user({"name": "Amit", "age": 21, "email": "invalid"})
        assert False
    except ValueError:
        assert True