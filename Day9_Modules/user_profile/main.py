
from user_ops import add_user,view_users,find_user
from storage import load_file,save_file

users = load_file()

while True:
    print("\n--- User Profile Manager ---")
    print("1. Add User")
    print("2. View Users")
    print("3. Find User")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user(users)
    elif choice == "2":
        view_users(users)
    elif choice == "3":
        find_user(users)
    elif choice == "4":
        save_file(users)
        break
    else:
        print("Invalid choice")