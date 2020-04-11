"""
NAME: Interactive Story - Exemplar 1
TITLE: Tangled Story Tour
DATE: DEC 4th, 2015
"""


# ***********TEMPLATE CODE DO NOT DELETE**********

# Import python modules
import time
import random
import subprocess

# Define the playSound function
# Allows you to play music
def playSound(soundfile):
    subprocess.call(["afplay", soundfile])

# Define the typeWriter fuction
# Provides a typerwriter effect for printed text
def typeWriter(myStr, t):
    for index in range(len(myStr)):
        print(myStr[index], end="")
        time.sleep(t)
    print()

# ************INTERACTIVE STORY BEGINS************

print("Firstly, please extend the size of file to fit the screen.[FULL SCREEN]\n\n")
time.sleep(3)

gameOver = False
while not gameOver:
    print("\n\nWELCOME!!")

    #<INSERT THE CODE FOR YOUR GAME HERE>

    #Ask user for name
    name = input("Enter your name: ")
    while not name.isalpha():
        name = input("Invalid name. Enter again: ")

    print ("\n%s, you are invited to visit Rapunzel's house by Mina Tour" % (name))
    time.sleep(4)
    print("\n\nHere is the tower where Rapunzel and the Mother Gothel lives.\n")
    time.sleep(4)

    #Ascii art of the high tower and Old witch
    print("                |>>>")
    print("                |")
    print("            _  _|_  _")
    print("           |;|_|;|_|;|")
    print("           \\.    .  /")
    print("            \\:  .  /")
    print("             ||:   |")
    print("             ||:.  |")
    print("             ||:  .|")
    print("             ||:   |")       
    print("             ||: , |")            
    print("             ||:   |")
    print("             ||: . |")
    print("             ||_   |")
    print("        ___--``    '--``__ ")            
    print(" ._____/------------------\_____.")

    #Sound of Wow!
    playSound("wow.mp3")
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nIt was very hard to persuade Mother Gothel to let us tour around her house.")
    time.sleep(5)
    print("\n\nHere SHE is, Mother Gothel!")
    time.sleep(2)

    #Sound of Tada
    playSound("tada.mp3")
    
    # Ascii art of Old Witch = Mother Gothel
    print("         ^^          xxXXx")
    print("     /\__{^^}__/\      xxXXxx                               *")
    print("    / _        _ \     xxXXxx")
    print("    \/ \/\ww/\/ \/      xxXXxx                     {~~~~")
    print("                        xxxXxx                      ~\:::~~")
    print("                 *      xxxXxx                        ~~\:::~")
    print("                         xxXXxx                          \::::")
    print("                         xxXXxxx          *               }::::}")
    print("                         xxxXxxx                          }::::}")
    print("                         xxxXXxxx                        /::::/")
    print("   *                     xxxxXXxx                       /::::/")
    print("                         xxxxXXxx                   {~~~:::/~")
    print("                         %%xxxxx%%                   ~~~~~~")
    print("                         %%%%%%%%%")
    print("                        %%%%%%%%%%%")
    print("                        %%%%%%%%%%%       *")
    print("            *           %%%%%%%%%%%")
    print("                      xxxxxxxx%%%%%")
    print("                    xxXXXXXXXxxx%%%                ^^         *")
    print("                  xxXx/////xxXxxx%%           /\__{^^}__/\\")
    print("          xxxxxxxxxXxx////(/xxXxxx%          / _        _ \\")
    print("            XXXXXXXxx//(/(((/xxxXxx          \/ \/\ww/\/ \/")
    print("  *            xxxx////(/(/(/)\\xXxx")
    print("                ///////(/(/(/\)\\xxxx")
    print("                /((/(//(/(/((\/\)xXxxx")
    print("                /((/(//(/(/((\/\)xXxxx")
    print("                /(//((/(\  @ /@)xXxxx")  
    print("               //(/(///(\::/ \:::)xXxxx")
    print("              /(/(/(///(\:(   ):/))xXxxx")
    print("             /((/(/(/(/(\  \ /  /)xXxxx")
    print("               //(/(/(/(\\ \__/ /)xXxxx")
    print("            /////(/(/(/(\\\    /)xXxxx")
    print("               /((/(/(/(/(\\\_///)xXxxx")
    print("                ///(/(/(/(\)) ((/)xXxxx")
    print("    *          ///((/(/(/(/)) ((/)xXxxx")
    print("                 (///(/(/(//) ((/\\)xXxxx")
    print("                  ///(/(/(//      \)xXxxx")
    print("                      (/((/        \ \ )xXxxx")

    time.sleep(1)
    firstTypeWriter = """
Mother Gothel: Hi. I am the great Mother Gothel!\n"""
    typeWriter(firstTypeWriter, 0.05)
    #Sound of nasty laugther
    playSound("laugh.wav")
    
    #Sound of scary
    secondtypeWriter = """
Just go into that secret path and take the left elevator, the left one. Not on the right!! You got it?\n"""
    typeWriter(secondtypeWriter, 0.02)
    time.sleep(3)
    print("\nMother Gothel: I'm very very busy so just take a look and go!n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(4)
    
    print("\n\n\nGuide: Finally, she is gone.")
    time.sleep(2)
    print("\nGuide: Rapunzel is locked on the top of this tower by the Mother Gothel.")
    time.sleep(4)
    print("Guide: Let's go and see her!")
    time.sleep(4)
    print("Guide: Let's go along the path as the Mother Gothel told us.\n\n\n")
    
    #Sound of walking
    playSound("walking.wav")
    print("Guide: Now, you can have the free tour.")
    time.sleep(3)
    print("Guide: If you are finished touring, you can come back to our bus station.")
    time.sleep(5)
    print("Guide: Bye~, Have a nice tour^^\n\nn\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(4)
    
    # Ascii art of the elevator = Gothel's elevator
    print(" _________________________________________________________________________")
    print("|: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :|")
    print("| : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |")
    print("|: : :  Rapunzel's : : : : : : : : : : : : : : : : : : : : My secret: : : |")
    print("| : : :____Room___: : : : : : : :_________: : : : : : : :____Lab____: : : |")
    print("|: _ :|  _______  |: _ : : : : :/         \: : : : : _ :|  _______  |: _ :|")
    print("| /_\ | |   |   | | /_\ : : : :|  Secret   |: : : : /_\ | |   |   | | /_\ |")
    print("| =|= | |   |   | | =|=  : : : :\_________/: : : :  =|= | |   |   | | =|= |")
    print("|=====| |   |   |U|=====================================| |   |   |D|=====|")
    print("|: : :| |   |   |P|                                     | |   |   |O|: : :|")
    print("| : : | |   |   |:|                                     | |   |   |:| : : |")
    print("|: : :| |   |   |U|         Gothels's hahaha            | |   |   |W|: : :|")
    print("| : : | |   |   |P|                                     | |   |   |N| : : |")
    print("|: : :| |   |   | |                                     | |   |   | |: : :|")
    print("|_____|_|___|___|_|_____________________________________|_|___|___|_|_____|")

    time.sleep(2)    
    print("\n\nVoice Recorded Machine: This is a very secret elevator to go up the high tower.")
    time.sleep(5)
    print("Voice Recorded Machine: To tell you the background story of Rapunzel.....")
    time.sleep(5)       
    print("\n\n\n....When Rapunzel was borned, the old witch Mother GOthel kidnapped baby Rapunzel to her secret house and locked her on the high tower...")
    time.sleep(6)
    print("Rapunzel wanted to go outside but she could not.n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(6)
    print("\n\nOne day, a man named Ryder finds a mysterious high tower while running away from the soldiers.")
    time.sleep(4)
    print("\nHe was very curious so he climbed up the mysterious tower which took him for a long time..")
    time.sleep(6)
    
    # Ascii art of a boy = Ryder
    print("          .--..--.")
    print("         /    V   \\")
    print("      __|__________|__")
    print("     '--///      \\\--'")
    print("       (    6  6    ) ")
    print("        :     )    ;")
    print("         \   ==   /")
    print("          `-.__.-`")
    print("       __ _(\__/)_ __")
    print("     /`  / \(><)/ \  `\\")
    print("    /    \ |::::| /    \\")
    print("    |    / /::::\ \  | |")
    print("    | | /  |::::|  \ | |")
    print("    | | \  |'::'|  / | |")
    print("    | |  \_/ :: \_/  | |")
    print("    | |    |____|o   | |")
    print("    |_|    |____|o   |_|")
    print("    |_\    |    |o   /_|")
    print("    /  \___| __ |___/  \\")
    print("   ((((||    ||    ||))))")
    print("        |    ||    |")
    print("        |    ||    |")
    print("        |    ||    |")
    print("        |    ||    |")
    print("        |    ||    |")
    print("        |___ || ___|")
    print("      __[____||____]__")
    print("     (       )(       )")
    print("      `---'==  =='---'")
    time.sleep(1)
    print("Ryder and Rapunzel met and she told Ryder that she wanted to go outside.")
    time.sleep(5)
    print("So Ryder and Rapunzel made a plan to escape secretly.")
    time.sleep(3)
    #Sound of Boy and Girl Whispering
    playSound("whispering.wav")

    #Ask user for input
    choice = input("\n\nWill you..\nA) Tell to Mother Gothel that Rapunzel is trying to escape from the tower. and \nB) Just stay away and look at what they are doing. \n\nState A or B: ")
    answer = choice.upper()
    while not answer=="A" and not answer =="B":
        print("Error")
        print("\n\nWill you..\nA) Tell to Mother Gothel that Rapunzel is trying to escape from the tower. and \nB) Just stay away and look at what they are doing. \n\nState A or B: ")
        
        
    if answer == "A":
        time.sleep(2)
        print("\n\nMother Gothel became very angry and she pushed him out of the tower.")

        #Sound of scariness
        playSound("scary.wav")
            
        print("\nAlso Mother Gothel kicked you out of the tower to keep Rapunzel in there.")
        time.sleep(3)
        print("\n\n\nRapunzel was no where to be seen again.....")
        #Sound of sadness(crying)
        playSound("crying.wav")
        print("THE END")
        time.sleep(2)
        playAgain = input("\n\nDo you want to play again?(yes or no): ")

        if playAgain == "no":
            gameOver = True
            
        elif playAgain == "yes":
            gameOver = False

    elif answer == "B":
        time.sleep(2)
        print("\n\nFinally, Rapunzel and Ryder escapes from the tower using Rapunzel's long~ hair and head outside.")
        time.sleep(4)
        print("\nAfter escaping, Rapunzel jumped like a little kid and felt the freedom that she have wanted for her whole life.")
        time.sleep(5)
            
        #Sound of hapiness(freedom)
        playSound("yeah.mp3")
            
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThey went out to the city where there are many people and they sang songs, danced and did fun things that Rapunzel have not done it before.")
        time.sleep(5)
        print("\nRapunzel and Ryder falls in love with each other.")
        thridTypeWriter = """

          OOOOOOOO:       OOOOOOOO!      
       OOOO!!!!;;;;O    OO.......:;!O     
      OOO!!!;;;;;;;;O  O.......... ;!O    
     OOO!!!!;;::::::.OO.............;!O   
     OO!!!!;;:::::................. ;!O   
     OOO!!!;::::::..................;!O
     OO!!;;::::::..................;!O   
       OO!;;::::::.............::::!O     
         O!!;::::::............:::O       
           !!!;:::::..........ooO        
              !!;:::::.......O        
                ;;::::.....O       
                   :::..O       
                     ::.              
                      :                   
"""
        typeWriter(thridTypeWriter, 0.02)
 
        time.sleep(1)
        print("\nThey look so happy and you are very proud of making this decision, don't tell to the Mother Gothel.")
        time.sleep(8)
        print("\nThey enjoyed spending a wonderful day and suddenly the Mother Gothel appeared to take find Rapunzel and take her back.")
        time.sleep(6)
        
        opinion = input("\n\n\nDo you want to...\nA)Protect Ryder and Rapunzel from Mother Gothel and make them run away.\nB) Just stay away and look at what they are doing.\n\n State A or B: ")
        answer = opinion.upper()
        while not answer=="A" and not answer=="B":
            print ("Error")

        if answer == "A":
            print("\n\nYou hang on to Mother Gothel and not let her go.")
            time.sleep(4)
            print("\nThrough your effort, Ryder and Rapunzel were able to run out of the situation.")
            time.sleep(4)
            print("\nThey went out on a boat when it became dark. It was Rapunzel's birthday and Rapunzel was very happy to celebrate her birthday.")
            time.sleep(5)
            print("\n\nSoon, Rapunzel and Ryder went to the palace where the king and the queen, Rapunzel's real parents are.../n")
            time.sleep(4)
            print("\nThe King sent soldiers to defeat and kill the nasty witch; Mother Gothel.")
            time.sleep(1)

            print("    |\                |\                |\                |\\")
            print("    || .---.          || .---.          || .---.          || .---.")
            print("    ||/_____\         ||/_____\         ||/_____\         ||/_____\\")
            print("    ||( '.' )         ||( '.' )         ||( '.' )         ||( '.' )")
            print("    || \_-_/_         || \_-_/_         || \_-_/_         || \_-_/_")
            print("    .-\\`'V'//         .-\\`'V'//-.       .-\\`'V'//-.       .-\\`'V'//-.")
            print("   / ,   |// , `\    / ,   |// , `\    / ,   |// , `\    / ,   |// , `\\")
            print("  / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |")
            print(" /_/||__//   || |  /_/||__//   || |  /_/||__//   || |  /_/||__//   || |")
            print(" \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |")
            print("  \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |")
            print("  /\|_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |")
            print("  `--|`^___^`||_|   `--|`^___^`||_|   `--|`^___^`||_|   `--|`^___^`||_|")
            print("     |   |   ||/       |   |   ||/       |   |   ||/       |   |   ||/")
            print("     |   |   |         |   |   |         |   |   |         |   |   |")
            print("     |   |   |         |   |   |         |   |   |         |   |   |")
            print("     |   |   |         |   |   |         |   |   |         |   |   |")
            print("     L___l___J         L___l___J         L___l___J         L___l___J")
            print("      |_ | _|           |_ | _|           |_ | _|           |_ | _|")
            print("     (___|___)         (___|___)         (___|___)         (___|___)")

            #Sound of walking
            playSound("walking.wav")
            
            # Sound of screaming = Ahhhhh!!
            playSound("screaming.wav")

            time.sleep(3)
            print("\n\n\nEvery one including Rapunzel, Ryder, King and the Queen thanked %s for helping them to survive."% (name))
            time.sleep(4)
            
            useTypeWriter = """
            \n\nRapunzel & Ryder: %s, Thank You very much, if you did not stopped that wicked witch, we would have died.. Thank you!!""" %(name)
            typeWriter(useTypeWriter, 0.01)
            
            print("After all, you could see Rapunzel and Ryder having marriage and the tour was finished.. \n")
            time.sleep(4)
            print("While getting on to the bus, you see...  Rapunzel enjoying the time with her parents.\n\n")
            time.sleep(5)
            print("Ryder and Rapunzel lived happily after with Ryder.\n")
            time.sleep(4)

            #Sound of happiness, celebrating
            playSound("celebration.wav")

            print("THE END")
            playAgain = input("Do you want to play again (yes or no)?: ")
            if playAgain == "no":
                gameOver = True
            elif playAgain == "yes":
                gameOver = False
                

        elif answer == "B":
            print("You just stayed away and looked at what they are doing...")
            time.sleep(2)
            print("Mother Gothel took Rapunzel back to her house and she was never seen again.")
            time.sleep(2)
            #Sound of crying
            playSound("crying.wav")
            print("THE END")
            
                      
            playAgain = input("Do you want to play again (yes or no)?: ")
            if playAgain == "no":
                gameOver = True
            elif playAgain == "yes":
                gameOver = False


gameOver = True
print("GAME OVER")
