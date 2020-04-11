"""
NAME: Mr. Poirier
DATE: August 30, 2016
PURPOSE: if, else, and elif
"""

print("WELCOME TO MR. POIRIER'S AWESOME GAME OF AWESOME!\n\n")

guess = input("Guess my secret number: ")
guess = int(guess)
print("\n\n")

while guess != 888:
    if guess > 888:
        print("The number is too big! Try again.\n\n")
    elif guess < 888:
        print("The number is too small! Try again.\n\n")

    guess = input("Guess my secret number: ")
    guess = int(guess)
    print("\n\n")

print("Wow! You won!")
print("Congratulations!\n\n")

print("GAME OVER.")
