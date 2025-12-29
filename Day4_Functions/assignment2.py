import math

# check prime 

def check_prime():
    n = int(input("Enter a number: "))
    
    if n < 2:
        print("Not Prime")
        return 

    i=2
    while i <= math.sqrt(n):
        if n%i == 0:
            print("Not Prime")
            return
        i += 1
    
    print("Prime")
        

check_prime()