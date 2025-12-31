# checking age

def check_user_type(user):
    if user.get("age") < 18:
        return "Minor"
    else:
        return "Adult"


user1 = {"name": "Amit", "age": 17}
user2 = {"name": "Neha", "age": 21}

print(check_user_type(user1))  # Minor
print(check_user_type(user2))  # Adult
