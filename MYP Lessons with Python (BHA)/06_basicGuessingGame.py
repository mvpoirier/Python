"""
NAME: Mr. Poirier
DATE: September 2, 2015
PURPOSE: Guessing game
"""
print("WELCOME TO MR.POIRIER'S GUESSING GAME!\n\n")

secret = 8
guess = input("Guess a number: ")
guess = int(guess)

if guess == secret:
    print("YOU ARE THE WINNER!")
    print("WOOHOO!")
else:
    print("YOU GUESSED WRONG!")
    print("BOOOO!")

print("\n\nGAME OVER!")
