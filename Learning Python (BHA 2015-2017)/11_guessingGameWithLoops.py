"""
NAME: Mr. Poirier
DATE: February 22, 2016
PURPOSE: Random number guessing game with while loops
FILENAME: guessingGameWithLoops.py
"""

import random

gameOver = False
answer = random.randint(1, 10)
guesses = 0

while not gameOver:
    guesses = guesses + 1
    num = input("Guess a number between 1 and 10: ")
    if int(num) == answer:
        gameOver = True
        print("You won! It took you %s guesses." % (str(guesses)))
    else:
        print("That's not the number, try again!")
        
