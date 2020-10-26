"""
NAME: Mr. Poirier
DATE: February 18, 2016
PURPOSE: Animal guessing game.
FILENAME: animalGuess.py
"""

myGuess = input("What animal barks? ")
myGuess = myGuess.lower()

if myGuess == "dog":
    print("YOU WIN!\n")
    answer1 = True
else:
    print("YOU LOSE!\n")
    answer1 = False


myGuess = input("What animal likes cheese? ")
myGuess = myGuess.lower()

if myGuess == "mouse":
    print("YOU WIN!\n")
    answer2 = True
else:
    print("YOU LOSE!\n")
    answer2 = False

if answer1 and answer2:
    print("WOW! You answered both questions correct!")
elif answer1 or answer2:
    print("Good job! You answered one question correct!")
else:
    print("Ouch! You didn't answer any correct! Try again!")


print("\n\nGAME OVER.")

