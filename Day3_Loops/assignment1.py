
# print all even numbers bw 1 and 50

for i in range(1,51):
    if i%2==0:
        print(i)
    else:
        continue
    

# alternatively

for i in range(0,51,2):             # will include 0 , will work better for odd no printing
    print(i)