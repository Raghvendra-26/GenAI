
# User profile manager with persistent saving

import json

def add_user():
    
    name = input("Enter username: ").strip()
    age = int(input("Enter user age: "))
    email = input("Enter user email: ").strip()
    
    user = {
        "name":name,
        "age":age,
        "email":email,
    }
    
    users.append(user)
    print("User added successfully")
    
    
def view_users():
    if not users:
        print("No users found")
        return
    
    # for user in users:
    #     print(user["name"],user["age"],user["email"])
    
    for index, user in enumerate(users, start=1):
        print(f"\nUser {index}")
        for key, value in user.items():
            print(key, ":", value)


def find_user():
    search_email = input("Enter email to search: ").strip()
    
    for user in users:
        if user.get("email") == search_email:
            print("User found ")
            for k,v in user.items():
                print(k,":",v)

            return
            
    print("User not found")
    

# loading from file at startup
with open("users.json","r") as file:         # will produce a error if file not present
        if file:
            users = json.load(file)
        else:
            users = []


while True:
    print("\n--- User Profile Manager ---")
    print("1. Add User")
    print("2. View Users")
    print("3. Find User")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        view_users()
    elif choice == "3":
        find_user()
    elif choice == "4":
        with open("users.json","w") as file:
            json.dump(users,file,indent=4)
        break
    else:
        print("Invalid choice")