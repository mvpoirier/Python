"""
NAME:    Interactive Story - Exemplar 2
DATE:    December 1st, 2015
PURPOSE: Interactive Story 
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

gameOver = False
while not gameOver:
    typeWriter("Hi there, Welcome to Branksome Zoo!",0.05)
    print("   ___      ___ ")
    print("  /   \\____/   \\ ")
    print(" /    / __ \\    \\ ")
    print("/    |  ..  |    \\")
    print("\\___/|      |\\___/\\")
    print("   | |_|  |_|      \\ ")
    print("   | |/|__|\\|       \\ ")
    print("   |   |__|         |\\ ")
    print("   |   |__|   |_/  /  \\ ")
    print("   | @ |  | @ || @ |   ")
    print("   |   |~~|   ||   |    Branksome Zoo ") 
    print("   'ooo'  'ooo''ooo' ")

    
### Title: Poby In the Zoo ###
    
    

#Part 1: Introduction and First situation
    playSound("intro.mov")
    time.sleep (1)
    typeWriter("\nYou are a zookeeper in Branksome Zoo.\nYou are wearing a green suit and long black boots.",0.04)
    time.sleep (0.8)
    typeWriter("\nHow cool you are!",0.05)
    time.sleep(0.5)

    print("  __...--~~~~~-._   _.-~~~~~--...__ ")   
    print("    //               `V'               \"\"\"\" ")
    print("   //                 |                 \"\"\"\" ")
    print("  //__...--~~~~~~-._  |  _.-~~~~~~--...__\"\"\"\" ")
    print(" //__.....----~~~~._\"\" | /_.~~~~----.....__\"\"\"\"")
    print("====================\"\"\"\"|//====================")
    print("                    `---`  ") 
    
    typeWriter("\nYou discover that there's a paper where you have to write your first name.\n\"Please write your first name.\"",0.04)
    firstName = input("\n: ")
    while not firstName.isalpha():
        typeWriter("\nOnly Alphabets! No space! No last name!",0.04)
        firstName = input("\n: ")
               
    typeWriter("\nSince this is your first day of working in Branksome Zoo, you have a lot of work to do.",0.04)
    typeWriter("\nYou have to organize your stuff in zookeepers' office and\nyou have to get to know your colleagues, who will be working with you for the next several years.\nYou also have to see your animal that you are going to take care.\nWhat are you going to do first?",0.05)
    typeWriter("\n\nChoose a number (1.Organize stuff or 2.Interact with colleagues or 3.Go to see your animal) ",0.04)

    firstJob = input("\n: ")

    while firstJob != "1" and firstJob != "2" and firstJob != "3":
        typeWriter("\nOops! Type a correct number(1.Organize stuff or 2.Interact with colleagues or 3.Go to see your animal)",0.04)
        firstJob = input("\n: ")

    if firstJob == "1":
        typeWriter("\n\nYou go to the office to organize your stuff.",0.04)

        print("          HH ")
        print("          HH ")
        print("BBB       HH ")                                       
        print("=== .___. HH     %%%%                   .o.       ,zZZZ> ")
        print('BBB |   | HH 838 \\\\\\\\\\ EEE    AAAAA     ,0X0'    "") 
        print("BBB |<<<| HH 838 %%%% EEE ## DDDDD    ,0X0'   ,zZZZ\" ")
        print("BBB | Z | HH 838 %GR% +++ ## AAAAA   ,0X0'  ,zZZZ\" ")
        print("BBB | O | HH 838 %%%% EEE ## <<v>>  ,0X0' ,zZZZ\" ")
        print("BBB | O | HH 838 %%%% EEE ## AAAAA ,0X0',zZZZ\"HH$HHHHHHHDDHH$HH ")
        print("=== |<<<| HH 838 //// EEE ## AAAAA.0X0;zZZZ\"  EE$EEEEEEEDDEE$EE ")
        print("BBB |___| HH 838 %%%% EEE ## AAAAA'\"0' \"Z\"    HH$HHHHHHHDDHH$HH ")
    

        typeWriter("\nYou have piles of books, documents and pictures. You also have several working dresses.\nThere are many things to organize.\nYou take a whole day to organize your stuff.\nSo you haven't got time to meet your collegues and animal.",0.04)
        typeWriter("\nYour first day as a zookeeper in Branksome Zoo has passed.",0.04)
        playSound("night.mp3")
        time.sleep (2)
        typeWriter("\n\nDo you want to turn back time? (1.Yes or 2.No)",0.04)
        playAgain = input ("\n: ")

        while playAgain != "1" and playAgain != "2":
            playAgain = input("Oops! Type a number(1.Yes or 2.No)?")
        if playAgain == "2":
            gameOver = True
            typeWriter("Good bye %s."%str(firstName),0.04)
            
#Part 2 (Second situation) 


    elif firstJob == "2" or "3":
        typeWriter("\nYou are going to the office to get information about the zoo. One man walks toward you.",0.04)
        time.sleep(0.5)
        typeWriter("\n\"Nice to meet you %s!\nMy name is Brian.\nI heard that you are a new zookeeper. Is that right?\""%(firstName),0.04)
        typeWriter("\nYou: \"Yes, I am new here. Nice to meet you,too.\"",0.04)
        typeWriter("\nBrian: \"Are you excited to see your animal, Poby? He's a baby polar bear.\"",0.04)
        typeWriter("\nYou: \"I am excited but nervous as well.\"",0.04)
        typeWriter("\nBrian: \"You will be fine. Let me know if you have any troubles.Hope you enjoy first meeting with Poby!\"",0.04)

        time.sleep (1)
        typeWriter("\nYou: \"Hi Poby!\"",0.04)
        print("              (\\\\  _                      ___ ")
        print("             .-\\""\"(\\\\                _.\"\"`   `\"-. ")
        print("            /      ` `-._        _.-\"            `\\__ ")
        print("           6   6)        `-.__.-'                    `\",")
        print("          /                                         `;-` ")
        print("         /     ,                                     |")
        print("        ()    /  /`                                  |")
        print("         `---`\"~``\\                                  |")
        print("                   \\                                 |")
        print("                    \\            \\      /           / ")
        print("                    /`,   ,      |     |           / ")
        print("                   /   \"-.|      |     |         /'")
        print("                  /     / |     /,__   |       /`\\ ")
        print("                 /    /'  |    /    `\"'\\      (   \\ ")
        print("              __/   /'    |   |         `\\     \\   \\ ")
        print("              \\    /      |   |           `\\    \\   \\ ")
        print("               `-,/      /    |            /     |-\"`")
        print("                        `\"\"\"^^^           `^^\"\"\"\"`")

        time.sleep (0.5)
        playSound ("bearNoise.mp3")

        typeWriter("\n\nPoby is standing alone in the cage, growling to you.\nWhat are you going to do?(1.Loudly say \"Shhhhhhhh!\" or 2.Lure him with food)",0.04)
        typeWriter("\nChoose a number (1 or 2)",0.04)

        growling = input("\n: ")

        while growling != "1" and growling != "2":
            typeWriter("\nOops! Type a correct number (1.Loudly say \"Shhhhhhhh!\" or 2.Lure him with food)",0.04)
            growling = input("\n: ") 

        if growling == "1":
            typeWriter("\nYou: \"Shhhhhhhh! Be quiet Poby! I am going to take care of you for the next several years!\"",0.04)
            typeWriter("\nPoby: \"Grrrrrrrr....Grrrrrrrrrr!\"",0.04)
            typeWriter("Poby turns aggressive and runs toward you.",0.04)
            typeWriter("\nYou: \"Ahhhhhhh! Help! Brian!\"",0.04)
            time.sleep (1)
            typeWriter("\nBrian: \"Are you okay? What happened? Poby stop!\"",0.04)
            typeWriter("\nBrian makes Poby stop running toward you and you safely escape from aggressive Poby.\"",0.04)
            typeWriter("\nBrian: \"That wasn't a good start. Have some rests in the office. I think you have to take a rest for today.\"",0.04)
            typeWriter("\nYour day has passed so quickly and badly. What was the problem? Did you miscommunicate with Poby?",0.04)
            playSound ("sadEnding.mov")

            print("\n/$$$$$$$$ /$$                       /$$$$$$$$                 /$$ ")
            print("|__  $$__/| $$                      | $$_____/                | $$ ")
            print("   | $$   | $$$$$$$   /$$$$$$       | $$       /$$$$$$$   /$$$$$$$ ")
            print("   | $$   | $$__  $$ /$$__  $$      | $$$$$   | $$__  $$ /$$__  $$ ")
            print("   | $$   | $$  \\ $$| $$$$$$$$      | $$__/   | $$  \\ $$| $$  | $$ ")
            print("   | $$   | $$  | $$| $$_____/      | $$      | $$  | $$| $$  | $$ ")
            print("   | $$   | $$  | $$|  $$$$$$$      | $$$$$$$$| $$  | $$|  $$$$$$$ ")
            print("   |__/   |__/  |__/ \\_______/      |________/|__/  |__/ \\_______/ ") 

            typeWriter("\n\nDo you want to turn back time? (1.Yes or 2.No)",0.04)
            playAgain = input ("\n: ")

            while playAgain != "1" and playAgain != "2":
                playAgain = input("Oops! Type a number(1.Yes or 2.No)?")
            if playAgain == "2":
                gameOver = True
                typeWriter("\nGood bye %s."%str(firstName),0.04)

#Part 3 (Third situation) 


        elif growling == "2":
            playSound ("crowded.mov")
            typeWriter("\nYou: \"Poby! Come here! Get some food!\"",0.04)
            typeWriter("Poby slowly walks toward you and starts eating food.",0.04)
            typeWriter("\nYou: \"Good boy. I will come closer to you and don't be scared of me.\"",0.04)
            typeWriter("You walk toward Poby closer. Poby starts growling.\nYou hide food behind you until Poby stops growling.",0.04)
            time.sleep (0.5)
            typeWriter("Poby stops growling and waits for you to show food to him.",0.04)
            typeWriter("\nYou: \"Okay,good boy. If you growl again, I will not give you a food. I won't hurt you.\"",0.04)
            typeWriter("\nBrian: \"Wow, %s! I'm amazed that you already learned how to communicate with animals! Good job!\""%(firstName),0.04)
            typeWriter("\nYou: \"Thanks, Brian. Poby is very young. I can see that from how he's reacting to food.\"",0.04)
            typeWriter("\nBrian: \"Smart! You better go to the office now. I think your ID card has arrived.\"",0.04)
            typeWriter("\nYou run to the office because you are very excited to have your ID card, which proves that you are a \"real\" zookeeper.",0.04)
            time.sleep(1)
            typeWriter("\nAfter you picked up your ID card, you see people are crowded in Polar Bear Zone, where Poby lives.",0.04)
            typeWriter("\n\n\"Hey,little boy! Come here! I will give you my favorite snack!\"",0.04)
            time.sleep (0.5)
            print("                    ,.- 'Y _^-,")
            print("               ,.-'^H E ,-^ ^-,\\")
            print("          ,.-'^ R S ,.-^       \\|")
            print("          \\ H E ,.-^            k")
            print("           \\,.-^                 i")
            print("                                 ss")
            print("                                 kis")
            print("                                skiss")
            print("                                kissk")
            print("                               isskiss")
            print("                              kisskisskis")
            print("                           skisskisskisski")
            print("                        sskisskisskisskissk")
            print("                      isskisskisskisskisskiss")
            print("                   kisskisskisskisskisskisskis")
            print("              skisskisskisskisskisskisskisskiss")
            print("            kisskisskisskisskisskisskisskisskissk")
            print("           isskisskisskisskisskisskisskisskisskiss")
            print("          kisskisskisskisskisskisskisskisskisskiss")
            print("           kisskisskisskisskisskisskisskisskisskis")
            print("            skisskisskisskisskisskisskisskisskiss")

            typeWriter("\n\nOnce boy threw snacks to Poby, other children starts throwing snacks to him.\nPoby happily catches food with his mouth and enjoyes snacks.\nHis cage is now full of sweets and chips.",0.04)
            typeWriter("\nYou:\"1.Should I let Poby eat snacks? or 2.Should I stop the children?\"",0.04)
            typeWriter("\n\nChoose a number(1 or 2)",0.04) 

            snacks = input("\n: ")

            while snacks != "1" and snacks != "2":
                typeWriter("\nOops! Type a correct number (1.Should I let Poby eat snacks? 2.Should I stop the children?)",0.04)
                snacks = input("\n: ")

            if snacks == "1":
                time.sleep (1)
                typeWriter("\n\nBrian: \"Hey, Poby is very sick. What happened?\"",0.04)
                typeWriter("\nPoby gets a serious trouble in digestive system because he ate \"bad\" snacks.\nHe keeps vomiting and collapsing.",0.04)
                typeWriter("\nBrian: \"You better be careful next time. \nIt becomes a serious issue in Branksome Zoo that people throw food to animals, which are harmful to animals.\"",0.04)
                typeWriter("\nPoby is sleeping because he is sick so you go to the office. You are regretting.\"Why did I let Poby eat those snacks?\"",0.04)
                playSound("sadEnding.mov")

                print("\n/$$$$$$$$ /$$                       /$$$$$$$$                 /$$ ")
                print("|__  $$__/| $$                      | $$_____/                | $$ ")
                print("   | $$   | $$$$$$$   /$$$$$$       | $$       /$$$$$$$   /$$$$$$$ ")
                print("   | $$   | $$__  $$ /$$__  $$      | $$$$$   | $$__  $$ /$$__  $$ ")
                print("   | $$   | $$  \\ $$| $$$$$$$$      | $$__/   | $$  \\ $$| $$  | $$ ")
                print("   | $$   | $$  | $$| $$_____/      | $$      | $$  | $$| $$  | $$ ")
                print("   | $$   | $$  | $$|  $$$$$$$      | $$$$$$$$| $$  | $$|  $$$$$$$ ")
                print("   |__/   |__/  |__/ \\_______/      |________/|__/  |__/ \\_______/ ") 


                typeWriter("\n\nDo you want to turn back time? (1.Yes or 2.No)",0.04)
                playAgain = input ("\n: ")

                while playAgain != "1" and playAgain != "2":
                    playAgain = input("Oops! Type a number(1.Yes or 2.No)?")
                if playAgain == "2":
                    gameOver = True
                    typeWriter("\nGood bye %s."%str(firstName),0.04)



            elif snacks == "2":
                time.sleep (1)
                typeWriter("\n\nYou: \"Hey guys, stop throwing foood! Please!\"",0.04)
                typeWriter("\nBoy: \"Why? Is there a problem?\"",0.04)
                typeWriter("\nYou: \"Those snacks might make Poby sick because snacks that you're eating are not good for polar bears.\"",0.04)
                typeWriter("\nBoy: \"Oh really? Sorry, little cute bear!\"",0.04)
                typeWriter("\nYou: \"His name is Poby. If you call his name out, he will look at you.\"",0.04)
                typeWriter("\nBoy: \"Pooooooooooobyyyyyyyyyyy!\"",0.04)
                time.sleep (0.5)
                typeWriter("\nBrian: \"Good decision-making.\nMany zookeepers are afraid of telling children to stop throwing foods to animals\nbecause zookeepers think that children will be crying if they’ve said that.\"",0.04)
                typeWriter("\nSpeak out loud your answer! You don't have to type!",0.04)
                time.sleep (2)
                typeWriter("\nBrian: \"No matter if you were scared or not, you did a right thing.\nEating humans' snacks cause a big problem to animals.\nBut a lot of people don't know that.\"",0.04)
                typeWriter("\nYou: \"I will try to make people aware of that. That's a zookeepers' job!\"",0.04)
                typeWriter("\nBrian: \"Yes, you're right. Good job today, %s! Go have some rests.\""%(firstName),0.04)
                typeWriter("\n\nExpress your grateful and meaningful day to Brian in one sentence!",0.04)

                freeWords = input("\n: ")

                typeWriter("\n\nBrian: Okay, see you!\"",0.04)
                typeWriter("\n\nYour first day as a zookeeper is over. What a successful day!",0.05)

                playSound("happyEnding.mov")
                print("\n/$$$$$$$$ /$$                       /$$$$$$$$                 /$$ ")
                print("|__  $$__/| $$                      | $$_____/                | $$ ")
                print("   | $$   | $$$$$$$   /$$$$$$       | $$       /$$$$$$$   /$$$$$$$ ")
                print("   | $$   | $$__  $$ /$$__  $$      | $$$$$   | $$__  $$ /$$__  $$ ")
                print("   | $$   | $$  \\ $$| $$$$$$$$      | $$__/   | $$  \\ $$| $$  | $$ ")
                print("   | $$   | $$  | $$| $$_____/      | $$      | $$  | $$| $$  | $$ ")
                print("   | $$   | $$  | $$|  $$$$$$$      | $$$$$$$$| $$  | $$|  $$$$$$$ ")
                print("   |__/   |__/  |__/ \\_______/      |________/|__/  |__/ \\_______/ ") 


                typeWriter("Do you want to read again? (1.Yes or 2.No)",0.04)
                playAgain = input ("\n: ")

                while playAgain != "1" and playAgain != "2":
                    playAgain = input("Oops! Type a number(1.Yes or 2.No)?")
                if playAgain == "2":
                    gameOver = True
                    typeWriter("\nGood bye %s."%str(firstName),0.04)


                
                    


            
            
    

 
