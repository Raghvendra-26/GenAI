# basic file handling

# writing to file

file = open("data.txt","w")
file.write("Hello Raghvendra is the content writer here")
file.close()


# reading from a file
file = open("data.txt","r")
content = file.read()
file.close()
print(content)


# best practice
 
with open("data.txt","w") as file:
    file.write("Hello this is raghvendra")