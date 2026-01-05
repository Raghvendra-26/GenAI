
def validate_user(user):
    if "name" not in user or not user["name"]:
        raise ValueError("User name is required")

    if "age" not in user:
        raise ValueError("User age is required")

    if not isinstance(user["age"], int) or user["age"] < 0:
        raise ValueError("Invalid age")

    if "email" not in user or "@" not in user["email"]:
        raise ValueError("Invalid email")

    return True
