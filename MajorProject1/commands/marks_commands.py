from storage.json_store import load_json,save_json
from core.marks_ops import calculate_marks_summary
from utils.logger import logger
from utils.arg_parser import parse_flags
import sys

file_path = "data/marks.json"

def add_mark():
    marks = load_json(file_path)
    
    args = sys.argv[2:]
    
    #flag parser
    try:
        flags = parse_flags(args)
    except ValueError as e:
        logger.error(str(e))
        return
    
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
    
    total_marks,average_marks = calculate_marks_summary(marks)

    logger.info("Total marks: %s",total_marks)
    logger.info("Average marks: %s",average_marks)