import random
number=random. randint (1,100)
print("Welcome to the guess number game!")
while True:
    guess=int(input("Enter your guess:"))
    if guess<number:
        print("Number is too small , try again.")
    elif guess>number:
        print("Number is too big, try again.")
    else:
        print("Congratulatin! , You gaussed the correct number.")
        breakpoint

    