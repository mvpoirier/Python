'''
H.S. - OSX port by Michael Poirier
CMIS, Songdo, Incheon, South Korea
3/19/14
tells a interactive story
'''


# imports all the modules
import random
import time
#import winsound REMOVED WINDOWS DEPENDENCY
import subprocess #use afplay for subprocess


# these are the sounds later played!!
def soundEffect (sound):
    
    if sound == 1:
        soundfile = "laugh.wav"
    if sound == 2:
        soundfile = "tada.wav"
    if sound == 3:
        soundfile = "drown.wav"
    if sound == 4:
        soundfile = "smack.wav"
    if sound == 5:
        soundfile = "win.wav"
    if sound == 6:
        soundfile = "bye.wav"

    subprocess.call(["afplay", soundfile])



# the ascii arts later used
def asciiArt(art):
    if art == 1:
        time.sleep(1)
        print (" \n           __________            __________            __________        ")
        print ("          |  __  __  |          |  __  __  |          |  __  __  |       ")
        print ("          | |  ||  | |          | |  ||  | |          | |  ||  | |       ")
        print ("          | |  ||  | |          | |  ||  | |          | |  ||  | |       ")
        print ("          | |__||__| |          | |__||__| |          | |__||__| |       ")
        print ("          |  __  __()|          |  __  __()|          |  __  __()|       ")
        print ("          | |  ||  | |          | |  ||  | |          | |  ||  | |       ")
        print ("          | |  ||  | |          | |  ||  | |          | |  ||  | |       ")
        print ("          | |  ||  | |          | |  ||  | |          | |  ||  | |       ")
        print ("          | |  ||  | |          | |  ||  | |          | |  ||  | |       ")
        print ("          | |__||__| |          | |__||__| |          | |__||__| |       ")
        print ("          |__________|          |__________|          |__________|       \n")
        print ("               1                      2                     3            \n\n")

    if art == 2:
        time.sleep(1)
        print('\n\n                            . ')
        print('                      .     :     .')
        print('           _           \'. _.:._ .\'')
        print('          (_)       \'-. .\'     \'. .-\'')
        print('          _;_     \' - ./         \. - \' ')
        print('         / | \    - - |           | - -')
        print('    """" \ |  \ """"""""""""""""""""""""""""""""')
        print('          `|\  `')
        print('           | \\')
        print('          /  /')
        print('         /_ /_\n\n\n')

    if art == 3:
        time.sleep(1)
        print(" \n\n :::::::::::::::::::::::::::::::::::::::::::::::::::::: ")
        print(" :::::::::::::::::::::::::::::::::::::::::::::::::::::: ")
        print(" :::::::::::::::::::::::::::::::::::::::::::::::::::::: ")
        print(" ::::::::::::::::::::::::::_::::::::::::::::::::::::::: ")
        print(" :::::::::::::::::::::::::/ |:::::::::::::::::::::::::: ")
        print(" :::::::::::::::::::::/ \ | | /\::::::::::::::::::::::: ")
        print(" ::::::::::::::::::::::\ \| |/ /::::::::::::::::::::::: ")
        print(" :::::::::::::::::::::::\ V | /___::::::::::::::::::::: ")
        print(" :::::::::::::::::::::.-.) '. `__/::::::::::::::::::::: ")
        print(" ::::::::::::::::::::(.-.   / /:::::::::::::::::::::::: ")
        print(" ~^~_-~^^-^~^_~^_^-~^~^-~| ' |~^~_-~^_^-^~^_~^_^-~^~^-~ ")
        print(" ~^-_~^-~^_~^-~^_~^-_ _^,|___| ,~_ _~^-_~^-~^_~^-~^_~^- ")
        print(" ~^-~^~-_~^__.===~'`__..[_____]-..__`'~===.__~^-~^~-_~^ ")
        print(" ~_~^_.=~~'   ~_.==~-.-~|     |~=.-~==._~^-^'~~=._~_~^ ")
        print(" ~-:`-~^-~^_~^:-~^~-_~-.`-===-'_.=~-_~^-_:~^-~^-_~`;-~ ")
        print("  ~-'._~^-~^-_^~=._~-~_~-'~~'~`_^-~_^_.=~-~^-_~^-_.'^- ")
        print(" _~^-~^~=._~^-~^_-^~~==..,~_^_,..==~~-_~^-~^-_.=~_~^-~^ ")
        print(" _-~^-~^_~^`~==.__-~^_~^-_~^-_~^-_~^-~__.==~`_-~^-~^_~^ ")
        print(" -~_~^~-~^-~^~_~^~`~~~==,,....,,==~~~`-~_~^~-~^-~^~_~^~ ")
        print("  ~~~^-~^-_~^~^_-^~^-~^~-_~^-~^-~^_~^~-~^~-~^-~^-~^-~^ ")
        print("  ~^~^-~^-~^_~^~-^~_~^-^~^~^-~^-~^~^~-^~-~^-~^~~-^~-^~^ \n\n\n")

    if art == 4:
        print("     /``\    .-''-.")
        print("     \  |  /      \\")
        print("     / /   |      |")
        print("    / /     \   _.'")
        print("    \\ `----.'  '._   /`\\")
        print("     `--.         \\  \  |")
        print("       /       /\  \\ / /")
        print("      /       /  \  ` /")
        print("     |       /__  `--'")
        print("     |    _     `\\")
        print("      \   \`--.  |")
        print("       |  |   |  |")
        print("      /  /    |  |")
        print("     /  /     |  \\")
        print("     \  \\      \\__|")
        print("      \_/\n\n\n")


    if art == 5:
        print("---      ---   --------   ----    ----      ---      ---   --------   ----    ---- ")
        print(" ***    ***   **********  ****    ****      ***  **  ***  **********  *****   **** ")
        print("  ---  ---   ----    ---- ----    ----      ---  --  --- ----    ---- ------  ---- ")
        print("   ******    ***      *** ****    ****      ***  **  *** ***      *** ************ ")
        print("    ----     ---      --- ----    ----      ---  --  --- ---      --- ------------ ")
        print("    ****     ****    **** ************      ************ ****    **** ****  ****** ")
        print("    ----      ----------  ------------       ----------   ----------  ----   ----- ")
        print("    ****       ********   ************        ********     ********   ****    **** \n\n\n")

    if art == 6:
    
        print ("     ___      .___  ___. .__   __.  _______     _______. __       ___       __   __   __         ")
        print ("    /   \\     |   \\/   | |  \\ |  | |   ____|   /       ||  |     /   \\     |  | |  | |  |        ") 
        print ("   /  ^  \\    |  \\  /  | |   \\|  | |  |__     |   (----`|  |    /  ^  \\    |  | |  | |  |        ")
        print ("  /  /_\  \\   |  |\\/|  | |  . `  | |   __|     \\   \\    |  |   /  /_\\  \\   |  | |  | |  |        ")
        print (" /  _____  \\  |  |  |  | |  |\\   | |  |____.----)   |   |  |  /  _____  \\  |__| |__| |__|        ")
        print ("/__/     \__\\ |__|  |__| |__| \\__| |_______|_______/    |__| /__/     \__\\ (__) (__) (__)        ")
        print ("                                                                                                 ")
        print (".___________. __    __  .______      .__   __.    .______        ___       ______  __  ___       ")
        print ("|           ||  |  |  | |   _  \\     |  \\ |  |    |   _  \\      /   \\     /      ||  |/  /       ")
        print ("`---|  |----`|  |  |  | |  |_)  |    |   \|  |    |  |_)  |    /  ^  \\   |  ,----'|  '  /        ")
        print ("    |  |     |  |  |  | |      /     |  . `  |    |   _  <    /  /_\  \\  |  |     |    <         ")
        print ("    |  |     |  `--'  | |  |\\  \----.|  |\\   |    |  |_)  |  /  _____  \\ |  `----.|  .  \\        ")
        print ("    |__|      \\______/  | _| `._____||__| \\__|    |______/  /__/     \__\\ \______||__|\__\\       ")
        print ("                                                                                                 ")
        print (".______    _______  _______   ______   .______       _______     __  .___________.__     _______.")
        print ("|   _  \\  |   ____||   ____| /  __  \\  |   _  \\     |   ____|   |  | |           (_ )   /       |")
        print ("|  |_)  | |  |__   |  |__   |  |  |  | |  |_)  |    |  |__      |  | `---|  |----`|/   |   (----`")
        print ("|   _  <  |   __|  |   __|  |  |  |  | |      /     |   __|     |  |     |  |           \\   \\    ")
        print ("|  |_)  | |  |____ |  |     |  `--'  | |  |\\  \\----.|  |____    |  |     |  |       .----)   |   ")
        print ("|______/  |_______||__|      \\______/  | _| `._____||_______|   |__|     |__|       |_______/    ")      
        print ("                                                                                                 ")
        print (".___________.  ______     ______       __          ___   .___________. _______  __   __          ")
        print ("|           | /  __  \\   /  __  \\     |  |        /   \\  |           ||   ____||  | |  |         ")
        print ("`---|  |----`|  |  |  | |  |  |  |    |  |       /  ^  \\ `---|  |----`|  |__   |  | |  |         ")
        print ("    |  |     |  |  |  | |  |  |  |    |  |      /  /_\  \\    |  |     |   __|  |  | |  |         ")
        print ("    |  |     |  `--'  | |  `--'  |    |  `----./  _____  \\   |  |     |  |____ |__| |__|         ")
        print ("    |__|      \______/   \\______/     |_______/__/     \\__\\  |__|     |_______|(__) (__)         \n\n\n\n")

    if art == 7:
        print(" _______  _______  _______  ______     _______  __   __  _______  __   __   __  ")
        print("|       ||       ||       ||      |   |  _    ||  | |  ||       ||  | |  | |  | ")
        print("|    ___||   _   ||   _   ||  _    |  | |_|   ||  |_|  ||    ___||  | |  | |  | ")
        print("|   | __ |  | |  ||  | |  || | |   |  |       ||       ||   |___ |  | |  | |  | ")
        print("|   ||  ||  |_|  ||  |_|  || |_|   |  |  _   | |_     _||    ___||__| |__| |__| ")
        print("|   |_| ||       ||       ||       |  | |_|   |  |   |  |   |___  __   __   __  ")
        print("|_______||_______||_______||______|   |_______|  |___|  |_______||__| |__| |__| \n\n\n")


# this is the scary sounding song in the beginning with the dots            
def loadingSound():
    print("Loading .", end = " ")
'''
    winsound.Beep(165,500)
    print(".", end = " ")
    winsound.Beep(196,500)
    print(".", end = " ")
    winsound.Beep(247,500)
    print(".", end = " ")
    winsound.Beep(196,500)
    print(".", end = " ")
    winsound.Beep(156,500)
    print(".", end = " ")
    winsound.Beep(185,500)
    print(".", end = " ")
    winsound.Beep(220,500)
    print(".", end = " ")
    winsound.Beep(185,500)
    print(".", end = " ")
    winsound.Beep(165,500)
    print(".", end = " ")
    winsound.Beep(196,500)
    print(".", end = " ")
    winsound.Beep(247,500)
    print(".", end = " ")
    winsound.Beep(196,500)
    print(".", end = " ")
    winsound.Beep(156,500)
    print(".", end = " ")
    winsound.Beep(185,500)
    print(".", end = " ")
    winsound.Beep(220,500)
    print(".")
    winsound.Beep(185,500)
'''

# this is the intro
def displayIntro():
    name = input("What is your name?\n")
    print ("You wake up in a dark room and you look around and find a note.... \n")
    time.sleep(2)
    print ("It reads, \""+ name + " I hope it is you reading this note.\"\n")
    time.sleep(2)
    print ("\"You must find him\" \n")
    time.sleep(2)
    print("You see three doors infront of you. \n")
    time.sleep(1)
    asciiArt(1)
    print ()


# like you said i brought them together and made it into one function..... makes them choose a door    
def chooseDoor(choice):

    if choice == 1:
        door = " "
        while door != "1" and door != "2" and door != "3":
            print ("All of the doors seem unlocked.\nWhich door do you choose? \n(1, 2 or 3)")
            door = input()


    if choice == 2:
        door = " "
        while door != "1" and door != "2" and door != "3":
            print ("Which door do you choose now? (1, 2 or 3)")
            door = input()

    return door


# this is the part that is shown before entering the door
def doorFound():
    print ("You walk in through the door...")
    time.sleep(1)
    print("You look left and right...")
    time.sleep(1)
    print ("You hear a loud screech from the door...")
    print ()
    time.sleep(1)
        
# this is the story part!
def checkDoor(chosenDoor):


    theBadDoor = random.randint(1,3)

    if int(chosenDoor) != theBadDoor :
        print ("You find another set of doors!")
        asciiArt(1)
        chosenDoor = chooseDoor(2)
        theBadDoor2 = random.randint(1,3)
# door within door for the first time
        chosenDoor = 0    
        if int(chosenDoor) != theBadDoor2:
            doorFound()
            print ("You look around and you see again three more doors!")
            time.sleep(1)
            asciiArt(1)
            chosenDoor = chooseDoor(2)
            theBadDoor3 = random.randint(1,3)

# door within door for the second time
            chosenDoor = 0                    
            if int(chosenDoor) != theBadDoor3:
                doorFound()
                print ("You find the room mentioned in the note and you wonder if you should go in.\n")
                time.sleep(1)
                print ("You walk into the room very slowly...\n")
                time.sleep(1)
                print ("You see a man sitting on a chair with a pipe...\n")
                time.sleep(1)
                print ("You walk over to him and tap him gently on the shoulder..\n")
                time.sleep(.75)
                print ("He turns around but all you see is?....\n")
                time.sleep(1)
                print ("A bag of money and a machine that says the words.\n\n\n")
                time.sleep(2)
                soundEffect(2)
                time.sleep(.5)
                asciiArt(5)
                    
            if int(chosenDoor) == theBadDoor3:
                doorFound()
                print("You see a door with bright light coming out!")
                time.sleep(1)
                print("You feel the warm summer air as well as the glowing red sunlight...")
                soundEffect(5)
                asciiArt(2)
                time.sleep(1)
                
        if int(chosenDoor) == theBadDoor2:
            doorFound()
            print ("You find yourself drowning in a deep pool of water...")
            time.sleep(1)
            soundEffect(3)
            asciiArt(3)
    if int(chosenDoor) == theBadDoor :
        doorFound()
        print("You see something in the corner of your eyes!")
        time.sleep(1)
        soundEffect(4)
        print("You feel a sharp pain in your head and you fall to the ground...")
        asciiArt(4)
        time.sleep(1)
# in total there are 4 different endings... I had more before but the code got ugly so i got rid of many.... -.-


# this is where my actual code starts
playAgain = "YES"
while playAgain == "YES" or playAgain == "Y":

# the loading sound is called here
    loadingSound()
    
    time.sleep(1)

# the intro laughter and the art saying turn back is here
    soundEffect(1)
    asciiArt(6)

    displayIntro()

    doorNumber = chooseDoor(1)

    checkDoor(doorNumber)

    time.sleep(1)
    print ("Would you like to play again? (yes or no)")
    playAgain = input()
    playAgain = playAgain.upper()


# this makes it say goodbye when the story completly ends.
soundEffect(6)
asciiArt(7)



