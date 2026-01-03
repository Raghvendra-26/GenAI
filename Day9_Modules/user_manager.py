
def add_user(users,user):
    users.append(user)

def find_user(users,email):
    for user in users:
        if user["email"] == email:
            return user
    return None

