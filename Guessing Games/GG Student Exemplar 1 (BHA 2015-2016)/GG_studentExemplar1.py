"""
NAME: M.K. - Guessing Game Exemplar #1
TITLE: Earn the high degree certificate on the making crepe!
DATE: SEP 24th, 2015
"""

#Import the module
import time
import subprocess

def playSound(soundfile):
    subprocess.call(["afplay", soundfile])
    
#Game Loops
gameOver = False
while not gameOver:
    
    #Game starts
    print("Welcome!")
    #Play Sound File
    playSound ("Welcome.wav")
    time.sleep(2)
    play = input ("Do you want to play this game?(answer y or n): ")
    answer = play.lower()

    if answer == "y":
        print("\n\nYou need to get all the rounds correctly to receive the high degree certificate!")
        print("When you get all the questions correct and earn all the ingredients of crepe,")
        print("you will be able to receive the high degree certificate.\n")
        time.sleep(2)
        print("Remember, You should get all the quizzes correct.")
        time.sleep(2)
        
        #Print Ascii Art
        print("                                                                          ,---. ")
        print(",--.            ,--.  ,--.           ,---.   ,--.                   ,--.  |   | ")
        print("|  |    ,---. ,-'  '-.|  |,---.     '   .-',-'  '-. ,--,--.,--.--.,-'  '-.|  .' ")
        print("|  |   | .-. :'-.  .-'`-'(  .-'     `.  `-.'-.  .-'' ,-.  ||  .--''-.  .-'|  |  ")
        print("|  '--.\   --.  |  |     .-'  `)    .-'    | |  |  \ '-'  ||  |     |  |  `--'  ")
        print("`-----' `----'  `--'     `----'     `-----'  `--'   `--`--'`--'     `--'  .--.  ")
        print("                                                                          '--'  ")
        time.sleep(1)
        #Round 1 starts
        print ("\n\nRound 1:\n\n")
        time.sleep(2)
        print ("What is the name of the poison in a potato sprout?")
        print ("state from these 2; Solanin and Ammonia")
        time.sleep(1)

        poison = input ("\nanswer: ")
        answer = poison.upper()
        if answer == "SOLANIN":        
            print("Correct!!")
            
            #Play Sound File
            playSound ("Yeah.wav")

            #Print Ascii Art
            print("You received whipped cream.\n")        
            print(" __   __  _______  _______  __   __  __   __     __   __  __   __  __   __ ")
            print("|  | |  ||       ||   _   ||  | |  ||  | |  |   |  | |  ||  | |  ||  |_|  |")
            print("|  |_|  ||    ___||  |_|  ||  |_|  ||  | |  |   |  |_|  ||  | |  ||       |")
            print("|       ||   |___ |       ||       ||  | |  |   |       ||  |_|  ||       |")
            print("|_     _||    ___||       ||       ||__| |__|   |_     _||       ||       |")
            print("  |   |  |   |___ |   _   ||   _   | __   __      |   |  |       || ||_|| |")
            print("  |___|  |_______||__| |__||__| |__||__| |__|     |___|  |_______||_|   |_|")
    
            time.sleep(1)
            #Round 2 starts
            print("\n\nRound 2:")
            time.sleep(2)
            print("\n\nTomato is a fruit.")
            time.sleep(0.5)
            boolean = input("State T(true) or F(false): ")
            answer = boolean.upper()
            if answer == "F":
                print("Excellent!!")
                time.sleep(1)
                print("For prize, you received banana.\n")

                #Print Ascii Art
                print(" _")
                print("//\\")
                print("V  \\")
                print(" \  \_")
                print("  \,'.`-.")
                print("   |\ `. `. ")      
                print("   ( \  `. `-.                        _,.-:\\")
                print("    \ \   `.  `-._             __..--' ,-';/")
                print("     \ `.   `-.   `-..___..---'   _.--' ,'/")
                print("      `. `.    `-._        __..--'    ,' /")
                print("        `. `-_     ``--..''       _.-' ,'")
                print("          `-_ `-.___        __,--'   ,'")
                print("             `-.__  `----""\"    __.-'")
                print("                  `--..____..--'")
    
                time.sleep(2)
                #Round 3 starts
                print("\n\nRound 3:")
                time.sleep(1)
                answer = input("A famous chef, Julia Child is from USA. \nState how many stars are in American flag.: ")
                stringAnswer = str(answer)
                
                #Print Ascii Art
                print("         |~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         | * * * * * * * * * |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |  * * * * * * * *  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |  * * * * * * * *  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |  * * * * * * * *  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |  * * * * * * * *  |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         | * * * * * * * * * |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                print("         |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
                
                if stringAnswer == "51":
                    print("Hooray!! Correct!")
                    print("For prize, you received chocolate and strawberry~\n")
                    time.sleep(1)
                    #Play Sound File
                    playSound ("umm.wav")

                    #Print Ascii Art
                    print("    ___  ___  ___  ___  ___.---------------.")
                    print("  .'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \\")
                    print("  |\/ __\/ __\/ __\/ __\/ _:\   |:.  \  \___ \\")
                    print("   \\'\__\'\__\'\__\'\__\'\_`.__|  `. \  \___ \\")
                    print("    \\/ __\/ __\/ __\/ __\/ __:                \\")
                    print("     \\'\__\'\__\'\__\ \__\'\_;-----------------`")
                    print("      \\/   \/   \/   \/   \/ :                 |")
                    print("       \|______________________;________________|\n")
                    time.sleep(1)
    
                    #Print Ascii Art
                    print("           _  ")           
                    print("         _.\\-.__  ") 
                    print("       _/__/\  _/.   ") 
                    print("       /`. ' \| .'\    ")
                    print("      |' '' '  ' ' |   ")
                    print("      | ' ' '' '' '|   ")
                    print("      \' '  ' '' ''/  ")
                    print("       \ ' '' ' ' /  ")
                    print("        \''  '' '/   ")
                    print("         \ ' ' '/    ")
                    print("          `--'-' ")
                    time.sleep(1)
    
                    print("....... processing.....")
                    time.sleep(2)
                    
                    #Play Sound File
                    playSound ("Tada.wav")
                    
                    print("\nYour crepe is finished!")
                    time.sleep(0.5)
                    print("It has 'whipped cream' and 'banana' for stuffings!")
                    time.sleep(0.5)
                    print("Chocolate syrup and strawberries for toppings.")
                    time.sleep(0.5)
                    print("\nOh!! Yummy~")
                    #Play Sound File
                    playSound ("Oooh yeah.wav")
                    time.sleep(0.1)
                    print("You are a nice cook!")
                    time.sleep(0.2)
                    print("\n\n\nYou received certificate for accomplishing \nthe high degree of cooking and baking!")
                    print("Congratulations!!")
                    print("\n\n....... printing......\n\n")
                    time.sleep(3)

                    #Print Ascii Art                         
                    print(" ------------------- ")
                    print("|                   |")
                    print("|    Certificate    |")
                    print("|                   |")                    
                    print("|                   |")
                    print("|                   |")
                    print("|  YOU HAVE         |")
                    print("|  FINISHED THE     |")
                    print("|  HIGH DEGREE      |")
                    print("|  OF COOKING       |")                      
                    print("|  IN THIS GAME     |")
                    print("|                   |")
                    print("|                   |")
                    print("|                   |")
                    print("|         Mina Kim  |")
                    print("|                   |")
                    print(" ------------------- ")
                    #Play Sound File
                    playSound ("Woohoo.wav")
                    print("The End!")
                    time.sleep(1)
                       
                else:
                    print("You failed on the quiz!! Game ends")
                    time.sleep(2)
                    print("Bye Bye!")
                    time.sleep(2)
                    print("The End!")
                    time.sleep(1)
                    
                
            elif answer == "T":
                    print("You failed on the quiz!! Game ends")
                    time.sleep(2)
                    print("Bye Bye!")
                    time.sleep(2)
                    print("The End!")
                    time.sleep(1)

                    
            else:
                    print("Error. You typed something wrong")
                    time.sleep(2)

        else:
            print("You failed on the quiz!! Game ends")
            #Play Sound File
            playSound ("OhNo.wav")
            
            print("Bye Bye!")
            time.sleep(2)
            print("The End!")

    elif answer == "n":
        print ("Really? You don't want to play this game?? Okay... Bye")
        time.sleep(3)

    else:
        print("Error. You typed something wrong")
        time.sleep(2)
        
        playAgain = input("Do you want to play again (y or n)?: ")
        if playAgain == "n":
            gameOver = True
            print("Game over!")

            #Play Sound File
            playSound ("OhNo.wav")
            
            #Print Ascii Art
            print("  _____    _____    __   __   ______      _____   _     _  ______  _____   ")
            print("  (_____)  (_____)  (__)_(__) (______)    (_____) (_)   (_)(______)(_____) ")
            print(" (_)  ___ (_)___(_)(_) (_) (_)(_)__      (_)   (_)(_)   (_)(_)__   (_)__(_)")
            print(" (_) (___)(_______)(_) (_) (_)(____)     (_)   (_)(_)   (_)(____)  (_____) ")
            print(" (_)___(_)(_)   (_)(_)     (_)(_)____    (_)___(_) (_)_(_) (_)____ ( ) ( ) ")
            print("  (_____) (_)   (_)(_)     (_)(______)    (_____)   (___)  (______)(_)  (_)")
    
  
