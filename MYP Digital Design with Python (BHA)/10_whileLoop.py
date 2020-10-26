"""
NAME: Mr. Poirier
DATE: February 23, 2016
PURPOSE: Praciting with While Loops (Lesson 24)
FILENAME: whileLoops.py
"""

# Example 1: Counting with While Loops
count = 0

print("start loop")

while count <= 10:
    
    if count < 10:
        print(count, end = ", ")
    else:
        print(count, end = ".\n")
              
    count = count + 1
              
print("end loop")



# Example 2: Do you want to play again?

gameOver = False

while not gameOver:
    print("PLAYING THE GAME... :)")
    userChoice = input("Play again (yes/no)? ")
    if userChoice.lower() == "no":
        gameOver = True

print("GAME OVER.")


# Example 3: Random number guessing game

import random

answer = random.randint(1, 10)
guesses = 1

guess = input("Guess a number between 1 and 10: ")
while guess != str(answer):
    print("That's not the answer! Try again!")
    guess = input("Guess a number between 1 and 10: ")
    guesses = guesses + 1

print("Wow! You guessed the right number!")
print("It took you %s guesses." % (str(guesses)))











