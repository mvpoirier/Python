"""
NAME: Mr. Poirier
DATE: August 30, 2016
PURPOSE: if, else, elif
"""

print("WELCOME TO MR. POIRIER'S GAME OF AWESOMENESS!")

guess = input("Guess a number: ")
guess = int(guess)

while guess != 623:
    if guess > 623:
        print("Wrong number! It was too BIG!")
        print("Try a SMALLER number!")
    else:
        print("Wrong number! It was too SMALL!")
        print("Try a BIGGER number!")

    guess = input("Guess a number: ")
    guess = int(guess)
        
print("Wow! You guess it right!")
print("Congratulations!")

print("GAME OVER.")
