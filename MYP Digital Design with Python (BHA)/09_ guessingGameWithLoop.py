"""
NAME: Mr. Poirier
DATE: September 2, 2015
PURPOSE: Testing if statements
"""

import random

secret = random.randint(1,10)

gameOver = False

while gameOver == False:

    guess = input("Guess a number: ")
    guess = int(guess)

    if guess == secret:
        print("YOU WIN! YOU GUESSED MY NUMBER!")
        print("YOU WIN A CHOCOLATE!")
        secret = random.randint(1,10)
        
    else:
        print("YOU LOSE! MUWAHAHAHAHAHA!")
        print("BETTER LUCK NEXT TIME!")

    if input("Do you want to play again (y or n)?") == "n":
        gameOver = True

print("GAME OVER.")
