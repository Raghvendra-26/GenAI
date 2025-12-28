
# number guessing game

secret_number = 5

# guess = int(input("Enter a number : "))

# while guess != secret_number :
#     print("Wrong guess, Try again! ")
#     guess = int(input("Enter a number : "))
    

# print("You guessed it correct, the number is ",secret_number)


                                # alternative approach

attempts = 0

while True:
    guess = int(input("Guess a number : "))
    attempts = attempts+1
    
    if guess == secret_number:
        print("Correct!, The number is ",secret_number)
        print("You guessed it in", attempts, "attempts")
        break
    
    else:
        print("Wrong guess, try again")