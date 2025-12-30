
# Lists  (mutable ie can change) and indexing

names = ["Amit","Neha","Ravi"]

print(names[0])          #indexing starts from 0 
print(names[1])
print(names[2])

 
#modifying lists

# 1. Add
names.append("Suresh")

# 2. remove
names.remove("Amit")

# 3. check existence

if "Neha" in names:
    print("Found")


# length of lists
print(len(names))


#looping over lists

for name in names:
    print(name)
