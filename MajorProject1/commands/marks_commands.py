from storage.json_store import load_json,save_json
import sys

file_path = "data/marks.json"

def add_mark():
    marks = load_json(file_path)
    
    args = sys.argv[2:]
    flags = {}
    i = 0
    
    while i < len(args):
        if i+1 >= len(args):
            print(f"Missing value for flag {args[i]}")
            return
        
        key = args[i]
        value = args[i+1]
        clean_key = key.lstrip('-')
        flags[clean_key] = value
        i+=2

    if "value" not in flags:
        print(f"Missing required flag: --value")
        return
    
    try:
        mark = int(flags["value"])
        marks.append(mark)
    except ValueError:
        print("Mark value must be a number")
        return

    save_json(file_path,marks)
    
    
def marks_summary():
    marks = load_json(file_path)
    
    if not marks:
        print("No marks data found")
        return
    
    total_marks = 0
    
    for mark in marks:
        total_marks += mark
    
    average_marks = total_marks/len(marks)

    print("Total marks: ",total_marks)
    print("Average marks: ",average_marks)