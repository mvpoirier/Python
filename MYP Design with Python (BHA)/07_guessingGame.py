"""
NAME: Mr. Poirier
DATE: February 17, 2016
PURPOSE: Simple guessing game example
FILNAME: guessingGame.py
"""
import random

myNum = random.randint(1, 10)
myGuess = int(input("Guess a number: "))

if myGuess == myNum:
    print("WOOHOO!")
    print("YOU WIN!")
elif myGuess > myNum:
    print("You guessed too high! The number was %s." % (str(myNum)))
    print("YOU LOSE!")
else:
    print("You guessed too low! The number was %s." % (str(myNum)))
    print("YOU LOSE!")
   

    
