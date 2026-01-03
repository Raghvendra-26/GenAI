import sys

from commands.user_commands import list_users,add_user
from commands.marks_commands import add_mark,marks_summary
from commands.product_commands import add_product,inventory_value

def main():
    if len(sys.argv) < 2 :
        print("Usage: python main.py <command>")
        return
    
    command = sys.argv[1]

    if command == "list-users":
        list_users()
    elif command == "add-user":
        add_user()
    elif command == "add-mark":
        add_mark()
    elif command == "marks-summary":
        marks_summary()
    elif command == "add-product":
        add_product()
    elif command == "inventory-value":
        inventory_value()
    else:
        print("Unknown command")
        

if __name__ == "__main__":
    main()