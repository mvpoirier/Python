"""
NAME: Mr. Poirier
DATE: 2020-09-28
PURPOSE: Exploring conditionals
"""
myFavoriteNumber = 8

x = input("Guess my favorite Integer: ")

if x.isnumeric():
    x = int(x)
    if x == myFavoriteNumber:
        print("Wow great guess!")
        print("That's my favorite number!")
        print("YOU WIN!")
    elif x > myFavoriteNumber:
        print("Your guess was TOO BIG!")
    elif x < myFavoriteNumber:
        print("Your guess was TOO SMALL!")
else:
    print("ERROR: You must provide a number!")
