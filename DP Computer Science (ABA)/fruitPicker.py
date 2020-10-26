"""
DATE: 2020-10-21
NAME: Mr. Poirier
PURPOSE: Choose and remember fruit picker
"""

from fruitPickerChoices import fruits
#import fruitPickersChoices must use fruitPickerChoices.fruits
import random

gameOver = False
while not gameOver:
    # Determine number of fruits to pick, store as integer
    num = input("How many fruits to pick? ")
    while not num.isnumeric():
        num = input("Error! How many fruits to pick? ")
    num = int(num)

    # Print a random selection of num fruits
    print("\nOK! " + str(num) + " fruits coming right up!")
    for i in range (num):
        fruitIndex = random.randint(0,len(fruits)-1)
        print(fruits[fruitIndex])

    # Determine if we play again or not
    playAgain = input("\nDo you want to play again (y/n)? ")
    while not (playAgain == "y" or playAgain == "n"):
        num = input("Error! Do you want to play again (y/n)? ")
    if playAgain == "n":
        gameOver = True
        print("\nBye Bye!")
