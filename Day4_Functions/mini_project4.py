
# menu driven program

def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum = ",a+b)

def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1,11):
        print(num,"x",i,"=",num*i)
        
while True:
    
    print("\n--- Utility Toolkit ---")
    print("1. Add Numbers")
    print("2. Even or Odd")
    print("3. Multiplication Table")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add()
    elif choice == 2:
        check_even_odd()
    elif choice == 3:
        multiplication_table()
    elif choice == 4:
        print("Exiting program")
        break
    else:
        print("Wrong input")