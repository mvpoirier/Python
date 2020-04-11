'''
NAME:    Michael Poirier
DATE:    September 29, 2016
SCHOOL:  Branksome Hall Asia
TEACHER: Mr. Poirier
PURPOSE: Guessing Game: St. Patrick's Day
'''

#**************************************************
#************TEACHER-PROVIDED FUNCTIONS************
#*************DO NOT CHANGE OR DELETE!*************
#**************************************************

import time
import random
import subprocess

def playSound(soundfile):
    subprocess.call(["afplay", soundfile])

def typeWriter(myStr, t):
    for index in range(len(myStr)):
        print(myStr[index], end="")
        time.sleep(t)
    print()

def playAgain():
    playAgain = input("Do you want to play again (y or n)? ").lower()
    while playAgain != "y" and playAgain != "n":
        playAgain = input("Input Error!\nDo you want to play again (y or n)? ")
    if playAgain == "n":
        return True
    else:
        return False

#**********************************************
#************USER-DEFINED FUCNTIONS************
#**********************************************

def potOfGold():
    print("                    ________")
    print("                 .##@@&&&@@##.")
    print("              ,##@&::%&&%%::&@##.")
    print("             #@&:%%000000000%%:&@#")
    print("           #@&:%00'         '00%:&@#")
    print("          #@&:%0'             '0%:&@#")
    print("         #@&:%0                 0%:&@#")
    print("        #@&:%0                   0%:&@#")
    print("        #@&:%0                   0%:&@#")
    print("        \"\" ' \"                   \" ' \"\"")
    print("      _oOoOoOo_                   .-.-.")
    print("     (oOoOoOoOo)                 (  :  )")
    print("      )`\"\"\"\"\"`(                .-.`. .'.-.")
    print("     /         \\              (_  '.Y.'  _)")
    print("    | #         |             (   .'|'.   )")
    print("    \\           /              '-'  |  '-'")
    print("     `=========`")


#**********************************************
#************GAME LOOP FUNCTIONS***************
#************ADD GAME CODE HERE!***************    
#**********************************************

def gameCode():
    points = 0

    typeWriter("\n\n\n\nWELCOME TO MR. POIRIER'S ST. PATRICK'S DAY GAME!",0.1)
    guess = input("\n\nQuestion #1: What colour is worn in St. Patrick's Day? ")

    if guess.lower() == "green":
        print("YOU WIN!")
        playSound("tada.wav") 
        points = points + 10
    else:
        print("YOU LOSE!")
        playSound("evilLaugh.mp3")
        points = points - 10

    print("\n\nYou currently have %s points!" % (str(points)))

    guess = input("\n\nQuestion #2: Which small people who love gold are famous on St. Patrick's Day? ")

    if guess.lower() == "leprechaun" or guess.lower() == "leprechauns":
        print("YOU WIN!")
        playSound("tada.wav") 
        points = points + 10
    else:
        print("YOU LOSE!")
        playSound("evilLaugh.mp3")
        points = points - 10

    print("\n\nYou have earned a total of %s points!" % (str(points)))

    if points == 20:
        print("\n\nWOW! You got all questions correct!\n\n")
        potOfGold()
        playSound("tada.wav")
    elif points == 0:
        print("\n\nHmmm, that's ok. You got one correct, but you could do better!")
    else:
        print("\n\nOUCH! You didn't get any questions correct!")
        playSound("evilLaugh.mp3")

def gameOverMessage():
    print("GAME OVER!")


#*********************************************
#******************GAME LOOP******************
#***********DO NOT CHANGE OR DELETE!**********   
#*********************************************

gameOver = False
while not gameOver:

    # GUESSING GAME CODE
    gameCode()

    # ASK USER IF THEY WANT TO PLAY AGAIN
    gameOver = playAgain()

# GAME OVER MESSAGE
gameOverMessage()
