# dictionary basics

student = {
    "name": "Amit",
    "age": "20",
    "branch": "CSE",
    "grade": "A"
}

print(student["name"])
print(student["age"])
print(student["branch"])

print(student.get("grade", "Not assigned")) # return grade , if not assigned than return default ("not assigned" in this case)

# add 
student["marks"] = "85"

#update 
student["age"] = "22"

#delete
del student["branch"]

# looping over dictionaries

for key,value in student.items():
    print(key, ":",value)