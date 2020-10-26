'''
NAME:    
DATE:    
SCHOOL:  Branksome Hall Asia
TEACHER: Mr. Poirier
PURPOSE: Python Template
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



#**********************************************
#************GAME LOOP FUNCTIONS***************
#***************DO NOT DELETE!*****************    
#**********************************************

def gameCode():
    print("GAME CODE GOES HERE.")

def gameOverMessage():
    print("GAME OVER MESSAGE.")


#*********************************************
#********************GAME LOOP****************
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
