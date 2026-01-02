# reading and writing JSON in python

import json

users = [
    {"name": "Amit", "age": 22, "email": "amit@email.com"},
    {"name": "Neha", "age": 21, "email": "neha@email.com"},
    {"name": "Raghvendra", "age": 22, "email": "raghu@gmail.com"}
]

#writing data into json file
with open("users.json","w") as file:
    json.dump(users,file,indent=4)

# reading data from a json file

with open("users.json","r") as file:
    users1 = json.load(file)

print(users1)