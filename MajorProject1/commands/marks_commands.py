from storage.json_store import load_json,save_json
from utils.logger import logger
import sys

file_path = "data/marks.json"

def add_mark():
    marks = load_json(file_path)
    
    args = sys.argv[2:]
    flags = {}
    i = 0
    
    while i < len(args):
        if i+1 >= len(args):
            logger.error(f"Missing value for flag {args[i]}")
            return
        
        key = args[i]
        value = args[i+1]
        clean_key = key.lstrip('-')
        flags[clean_key] = value
        i+=2

    if "value" not in flags:
        logger.error(f"Missing required flag: --value")
        return
    
    try:
        mark = int(flags["value"])
        marks.append(mark)
    except ValueError:
        logger.error("Mark value must be a number")
        return

    save_json(file_path,marks)
    
    
def marks_summary():
    marks = load_json(file_path)
    
    if not marks:
        logger.error("No marks data found")
        return
    
    total_marks = 0
    
    for mark in marks:
        total_marks += mark
    
    average_marks = total_marks/len(marks)

    logger.info("Total marks: %s",total_marks)
    logger.info("Average marks: %s",average_marks)