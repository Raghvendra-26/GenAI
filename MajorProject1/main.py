import sys

from commands.user_commands import list_users,add_user
from commands.marks_commands import add_mark,marks_summary
from commands.product_commands import add_product,inventory_value
from utils.logger import logger
from commands.ai_commands import summarize_users_command,summarize_marks_command

def main():
    if len(sys.argv) < 2 :
        logger.error("Usage: python main.py <command>")
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
    elif command == "summarize-users":
        summarize_users_command()
    elif command == "summarize-marks":
        summarize_marks_command()
    else:
        print("Unknown command")
        

if __name__ == "__main__":
    main()