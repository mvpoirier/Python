"""
NAME: Mr. Poirier
DATE: September 17, 2015
PURPOSE: Simple game loop to replay a game
"""
gameOver = False

while not gameOver:
    #Game starts
    print("Welcome to my game!")
    
    #<INSERT THE CODE FOR YOUR GAME HERE>

    #Ask if the user wants to play again
    playAgain = input("Do you want to play again (y or n)?")
    if playAgain == "n":
        gameOver = True

#Game ends
print("Game over!")
