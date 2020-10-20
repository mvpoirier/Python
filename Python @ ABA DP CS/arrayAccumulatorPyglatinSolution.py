"""
NAME: Mr. Poirier
DATE: October 20, 2020
PURPOSE: Array Accumulator & Pyglatin
"""

# 1 - IMPORT MODULES

import random


# 2 - DEFINE ALL FUNCTIONS

# programLoop
# PURPOSE:  Provides the while loop repetition for the program
#           Calls the other program functions
def programLoop ():
    gameOver = False

    while not gameOver:
        print("\nProgram #1: Array Accumulator")
        value = int(input("Provide me a positive integer: "))
        arrayAccumulator(value)

        print("\nProgram #2: Pyglatin Generator")
        word = input("Provide me one word: ")
        pyglatin(word)

        response = input("\nPlay again (y or n)? ")
        if response == "n":
            gameOver = True
            print("\n\nBye!")
        else:
            print("\n\nRestarting...")

# arrayAccumulator (value)
# PURPOSE:      Increment a random array of integers by a fixed value
# PARAMETER:    value - how much the array will increase by
def arrayAccumulator (value):

    # Intialize empty array
    array = []

    # Append random integers to array (size 5)
    for i in range(5):
        array.append(random.randint(1, 100))
    print(array)

    # Add/Increment value to each element in array
    for k in range (len(array)):
        array[k] = array[k] + value
    print(array)
    

# arrayAccumulator (value)
# PURPOSE:      Convert a string to "Piglatin" --> Cheese to Heese-Cay!
# PARAMETER:    word - the word that will be coverted to pyglatin
def pyglatin (word):
    newWord = word[1].upper() + word[2:len(word)] + "-" + word[0].upper() + "ay!"
    print(newWord)

        
#3 - START PROGRAM
    
print("Hello! Welcome to Mr. Poirier's Python Program!")
programLoop()
