
def add_user(users):
    
    name = input("Enter username: ").strip()
    try:
        age = int(input("Enter user age: "))
    except ValueError:
        print("Please enter a valid number")
        return
    email = input("Enter user email: ").strip()
    
    user = {
        "name":name,
        "age":age,
        "email":email,
    }
    
    users.append(user)
    print("User added successfully")
    
    
def view_users(users):
    if not users:
        print("No users found")
        return
    
    # for user in users:
    #     print(user["name"],user["age"],user["email"])
    
    for index, user in enumerate(users, start=1):
        print(f"\nUser {index}")
        for key, value in user.items():
            print(key, ":", value)


def find_user(users):
    search_email = input("Enter email to search: ").strip()
    
    for user in users:
        if user.get("email") == search_email:
            print("User found ")
            for k,v in user.items():
                print(k,":",v)

            return
            
    print("User not found")