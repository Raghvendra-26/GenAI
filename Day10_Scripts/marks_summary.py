import sys
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    try:
        with open(file_path,"r") as file:
            try:
                marks = json.load(file)
            except json.JSONDecodeError:
                marks=[]
    except FileNotFoundError:
        marks=[]
    
    total_marks = 0
    
    for mark in marks:
        total_marks += mark
    
    print("Total marks: ",total_marks)
    
    if len(marks) == 0:
        print("No data in marks file")
    else:
        print("Average marks: ",total_marks/len(marks))

if __name__ == "__main__":
    main()