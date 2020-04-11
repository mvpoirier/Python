"""
NAME: Mr. Poirier
DATE: September 17, 2015
PURPOSE: Simple game loop to replay a game
"""
gameOver = False

while not gameOver:
    #Enter all the code for your game below
    print("Welcome to my game!")
    
    #This game asks for a number until it's greater than 22
    num = input("Give me a number: ")
    while int(num) < 22:
        num = input("Too low, give me another new number: ")

    #This game asks until you are hungry
    hungry = input("Are you hungry (yes or no)? ")
    while hungry == "yes":
        hungry = input("Eat more food! Try again!")

    #Ask if the user wants to play again
    playAgain = input("Do you want to play again (y or n)?")
    if playAgain == "n":
        gameOver = True

#Game is now over, print game over text or ASCII art
print("Game over!")
