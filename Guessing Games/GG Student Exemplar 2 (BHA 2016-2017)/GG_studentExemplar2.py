"""
NAME: Y.C. - Guessing Game Exemplar #2
DATE: September 18th
PURPOSE: Job World 
"""
#Import the module time
import time

#Import subprocess to use afplay and call soundfiles
import subprocess

#Define the typerWriter function which accepts a string and an integer
def typeWriter(myStr, t):

    for index in range(len(myStr)):
        print(myStr[index], end="")
        time.sleep(t)

    print()

#Define the playSound function which accepts the filename in the same folder
def playSound(soundfile):
    subprocess.call(["afplay", soundfile])

# Part 1 (Input three jobs and ask a name
typeWriter("WELCOME TO YESEO's JOB WORLD!",0.05)
playSound("welcome.m4a")
time.sleep (0.5)
name = input("\nWhat is your name?(No SPACE) ")
while not name.isalpha():
    name = input("Oops! Enter a correct name.")

print ("Welcome %s!" % str(name))
job = input("\nChoose a job (Type a number): \n1.Soccer player \n2.Professor \n3.Babysitter\n: ")
while job != "1" and job != "2" and job != "3":
    print("Oops! Please choose a number from given options.")
    job = input("\nChoose a job (Type a number): \n1.Soccer player \n2.Professor \n3.Babysitter\n: ")

#Soccer Player
if job == "1":
    typeWriter("\nYou are now a soccer player in Arsenal!",0.03)
    time.sleep (0.5)
        
    typeWriter("\nSituation! You have to determine your best choice.",0.03)
    typeWriter("\nYou are a defender in Arsenal.\nYou are holding a ball at the middle of the court.\nIn front of you, there are two offenders from Manchester City.\nFrom 3 meters away to your right, you have one teammate, Ozil.\nBehind you, there is Gabriel but none of the offenders are waiting.\nWho should you be passing to?\n and how should you be passing?",0.03)
    time.sleep (1)
    soccerPlayer = input("\nChoose a number (1.Ozil and High and slow or 2.Gabriel and Low and fast): ")
    while soccerPlayer != "1" and soccerPlayer != "2":
        print("Oops! Please choose a number from given options.")
        soccerPlayer = input("\nChoose a number (1.Ozil and High and slow or 2.Gabriel and Low and fast): ")
        

    if soccerPlayer == "2":
        playSound("applause.mp3")
                
        print("                       _,aaadP\"\"\"\"\"\"Ybaaaa,,_ ")
        print("                   ,adP,__,,,aaaadP\"\"\"\"\"Y888888a,_ ")
        print("                ,a8888888P\"''             \"Y8888888b, ") 
        print("             _a888888888\"                   `Y88888888b, ")
        print("           ,d888888888P'                       \"888888888b, ")
        print("         ,88888888P\"Y8,                       ,P'   `\"\"Y888b, ") 
        print("       ,d8888P\"'     \"Ya,                    ,P'         `Ya`b, ")
        print("      ,P88\"'           `Ya,                 ,P'            `b`Yi ")
        print("     d\",P                `\"Y,              ,P'              `Y \"i ") 
        print("   ,P' P'                   \"888888888888888b                `b \"i ")
        print("  ,P' d'                    d8888888888888888b                `b `b ")
        print("  d' d'                    ,888888888888888888b                I, Y, ")
        print(" ,f ,f                    ,88888888888888888888b               `b, b ")
        print(" d' d'                    d888888888888888888888b              ,88,I ")
        print(",P  8                    ,88888888888888888888888b,_          ,d8888 ")
        print("d'  8,                   d8888888888888888888888P'`\"Ya,_     ,d88888 ")
        print("8  d88b,             ,adP\"\"Y888888888888888888P'      `\"\"Ya, d88888P ") 
        print("8 ,88888b,       ,adP\"'     `\"Y8888888888888\"'             `\"888888I ")
        print("Y,88888888b, ,adP\"'             \"\"Y888888P\"                  888888' ")
        print("`888888888888P'                     \"\"YP\"                    888888 ")
        print(" I88888888888                          8                     88888I ")
        print(" `Y8888888888                          8                     88888' ")
        print("  `Y888888888        Normand           8                     8888I ")
        print("   `Y88888888        Veilleux          8                     8P\"8' ")
        print("    `Y8888888,                         8                   ,d',d' ")
        print("     `b\"\"\"\"Y8b                         8                 ,d\" ,d' ") 
        print("       \"b,   \"Y,                       8               ,P\" ,d\" ")
        print("         \"b,   \"Ya,_                 ,d88ba,,___   _,aP\" ,P\" ")
        print("           \"Ya_   \"\"Ya,_       _,,ad88888888888888P\"' _,d\" ")
        print("             `\"Ya_    \"\"Yaaad88888888888888888888P _,d\"' ")
        print("                 `\"Ya,_     \"Y888888888888888888P\",d\"' ")
        print("                    `\"\"Ya,__`Y888888888888888P\"\"\"  ")
        print("                         ``\"\"\"\"\"\"\"\"\"\"\"\"\"'' ") 
        
        time.sleep (0.5)
        typeWriter("\nFabulous. You are such a great soccer player(100 Point)!",0.03)
        time.sleep (0.3)


    elif soccerPlayer == "1":
        playSound("uhoh.mp3")
                
        typeWriter("\nA ball has taken away by one of offenders from Manchester city. Then...he scores a goal! Sorry, you have to learn more.(0 Point)",0.03)
    
        print ("           _...----.._")
        print ("        ,:':::::.     `>.")
        print ("      ,' |:::::;'     |:::.")       
        print ("     /    `'::'       :::::\ ")
        print ("    /         _____     `::;\ ")
        print ("   :         /:::::\      `  :")
        print ("   | ,.     /::SSt::\        |")
        print ("   |;:::.   `::::::;'        |")
        print ("   ::::::     `::;'      ,.  ;")
        print ("    \:::'              ,::::/")
        print ("     \                 \:::/")
        print ("      `.     ,:.        :;'")
        print ("        `-.::::::..  _.''")
        print ("           ```----'''")


        
#Professor

if job == "2":
    typeWriter("\nYou are now a professor in Harvard University.",0.03)
    time.sleep (0.5)
        
    typeWriter("\nSituation! You have to determine your best choice.",0.03)
    typeWriter("\nYou are a professor in Harvard University.\nYou gave an assignment to write one paragraph about a bacon recipe to your students.\nYour student, Jasmine copied and pasted one of bacon recipes from Google.\nIt is illegal and teachers should be strict on it.\nWhat is this called?\nand what is a consequence for it?",0.04)
    time.sleep (1)
    professor = input("\nChoose a number (1.Duplication and Suspension or 2.Plagiarism and Withdraw from a college): ")
    while professor != "1" and professor != "2":
        print("Oops! Please choose a number from given options.")
        professor = input("\nChoose a number (1.Duplication and Suspension or 2.Plagiarism and Withdraw from a college): ")
        
   
    if professor == "2":
        playSound("best.mp3")
                
        print("     .----------------------------------------------------. ")
        print("       |                                                    | ")
        print("       |       _  .-\"-.  .-\"-. .--.    _   _      _   ____  | ")
        print("       |    ,'` | | ._ `.| ._ \\|  /  ,' '\\| | _ .' ) |   _|_|__ ")
        print("      _|_  / /| | | | \\ '| | \\ | ;  / ., || || || ;  |  |_(]___`\\ ")
        print("    /___[)' | | | | '-`/ | '-`/| | / /_| || || | \\ `\\|  '(]____ ' ")
        print("   | ____[) '-' | | |-'  | .-' | |/      || `' |  ;  |  |\"(]___ | ")
        print("   ; ___[)| .-. | | |    | |   | '-./`|  ||    | /  /|  |__(]_ / ")
        print("    \\ _[) |_| \\_' '_|    ._|   '---'  '--'`.__.'(_,' |_____||-` ")
        print("     `-|                                                    | ")
        print("       '----------------------------------------------------' ")
        print("        \\      '   /|//  /|/\\,>7/|\\>/\\ \\         /      ,' ")
        print("         \\     '; |/|;  |  .--.  .--. \\ |       /     ,' ")
        print("          '     |  |\\| /  '__________' ||   ,-'     ,' ")
        print("          |     | .-' [    \\\"\" /:  \"/  ]'.,'       / ")
        print("          '.    '|     |    `-'  \\-'  |  |       ,' ")
        print("           |     .'.__.'     |    |   '._'      / ")
        print("           |      `\\||       \\    /    |      .` ")
        print("           |        ||        `--'     |     / ")
        print("           |        \\\\__  __           |     ' ")
        print("           '.        `===(__)`.__.'    ;     | ")
        print("            |         \\ \\             /|     | ")
        print("           .|          \\ `._        ,' |     | ")
        print("           |            .   `-.__,-'   ;     . ")
        print("           |             \\    ,\\_/\\   /      ' ")
        print("           |              `..' |\\\\ `-'   _.-\\ \\ ")
        print("          ,'._                 | :`.  .-`    \\ ; ")
        print("          |   `                | '  \\ \\ __,-' \\| ")
        print("          /                    |  \\  \\ \\      || ")
        print("          `-._                 |   '-'  \\   _,'| ")
        print("              `--.             :   |     `'`  ,/ ")
        print("                  `--._        '.__;         _/ mx ")
        print("                      ``-.___..___....----'\"` ")

        typeWriter("\nWow, you are correct. You are such a smart professor!",0.03)
        time.sleep (0.5)


        
    elif professor == "1":
        playSound("uhoh.mp3")
                
        typeWriter("\nUh,oh! You are incorrect. Sorry, you have to learn more.",0.03)


#Babysitter

if job == "3":
    typeWriter("\nYou are now a babysitter in Mrs.Black's house!",0.03)
    time.sleep (0.5)
    typeWriter("\nSituation! You have to determine your best choice!", 0.03)
    time.sleep (1)

    typeWriter("\nYou are caring Jason and Sophie.\nJason is suddenly crying while he is eating his powdered milk.\nThen, he throws a bottle and cries.\nWhy is he crying?\nand how are you going to soothe Jason?",0.05)
    babySitter = input("\nChoose a number (1. Milk tastes bad and Remake it or 2.Milk is hot and Cools it down): ")
    while babySitter != "1" and babySitter != "2":
        print("Oops! Please choose a number from given options.")
        babySitter = input("\nChoose a number (1. Milk tastes bad and Remake it or 2.Milk is hot and Cools it down): ")
    

    if babySitter == "2":
        playSound("laughingbaby.mp3")
        
        print("            .-\"''-.  _ ")
        print("                 .'       `( \\ ")
        print("        @/            ')   ,--,__,-\"")
        print("        /        /      \\ /     /   _/ ")
        print("      __|           ,   |/         / ")
        print("    .~  `\\   / \\ ,  |   / ")
        print("  .~      `\\    `  /  _/   _/ ")
        print(".~          `\\  ~~`__/    / ")
        print("~             `--'/  ")

        time.sleep (0.5)
        typeWriter("\nGood decision! You are such a skilled babysitter!",0.03)
        time.sleep (0.3)



    elif babySitter == "1":
        playSound("annoyingbaby.mp3")
        
        print("         . ")
        print("      .  :  . ")
        print("       '.@.' ")
        print("        /^\\ ")
        print("       /   \\ ")
        print("      /1997 \\ ")
        print("     @@@@@@@@@ ")
        print("    /  6 6    \\ ")
        print("   (    ^     ,) ")
        print("    \\   __,   /-._ ")
        print("     `._____.'\\   `--.__ ")
        print("            \\\\/         `/``\"\"\"'-. ")
        print("             /    )     /         : ")
        print("             |   /\\    |  .--.     : ")
        print("             /  /\\1`\\   \\/    `.__.:.____.-. ")
        print("            /  / /`\\9`\\`/    .-\"..____.-.   \\ ")
        print("        _.-'  /_/   `\\9`\\                \\-. \\ ")
        print("       `=----'        `\\7`\\--------'\"\"`-. \\ `\" ")
        print("                        `-./             `\" ")

        time.sleep (0.5)
        typeWriter("\nUh,oh. Jason is still crying. Sorry, you have to learn more.",0.03)
        time.sleep (0.5)

#Retry a game
        
gameOver = False

time.sleep (1)
playAgain = input ("\nDo you want to play again? 1.Yes or 2.No: ")
if playAgain == "2":
    gameOver = True
    print ("Good bye!")

while not gameOver:
    #(Input three jobs and ask a name)
    typeWriter("\nWELCOME TO YESEO's JOB WORLD!",0.05)
    playSound("welcome.m4a")
    time.sleep (0.5)
    name = input("\nWhat is your name?(No SPACE) ")
    while not name.isalpha():
        name = input("Oops! Enter a correct name.")

    print ("Welcome %s!" % str(name))
    job = input("\nChoose a job (Type a number): \n1.Soccer player \n2.Professor \n3.Babysitter\n: ")
    while job != "1" and job != "2" and job != "3":
        print("Oops! Please choose a number from given options.")
        job = input("\nChoose a job (Type a number): \n1.Soccer player \n2.Professor \n3.Babysitter\n: ")

# Soccer Player
    if job == "1":
        typeWriter("\nYou are now a soccer player in Arsenal!",0.03)
        time.sleep (0.5)
        
        typeWriter("\nSituation! You have to determine your best choice.",0.03)
        typeWriter("\nYou are a defender in Arsenal.\nYou are holding a ball at the middle of the court.\nIn front of you, there are two offenders from Manchester City.\nFrom 3 meters away to your right, you have one teammate, Ozil.\nBehind you, there is Gabriel but none of the offenders are waiting.\nWho should you be passing to?\n and how should you be passing?",0.03)
        time.sleep (1)
        soccerPlayer = input("\nChoose a number (1.Ozil and High and slow or 2.Gabriel and Low and fast): ")
        while soccerPlayer != "1" and soccerPlayer != "2":
            print("Oops! Please choose a number from given options.")
            soccerPlayer = input("\nChoose a number (1.Ozil and High and slow or 2.Gabriel and Low and fast): ")
        

        if soccerPlayer == "2":
            playSound("applause.mp3")
                
            print("                       _,aaadP\"\"\"\"\"\"Ybaaaa,,_ ")
            print("                   ,adP,__,,,aaaadP\"\"\"\"\"Y888888a,_ ")
            print("                ,a8888888P\"''             \"Y8888888b, ") 
            print("             _a888888888\"                   `Y88888888b, ")
            print("           ,d888888888P'                       \"888888888b, ")
            print("         ,88888888P\"Y8,                       ,P'   `\"\"Y888b, ") 
            print("       ,d8888P\"'     \"Ya,                    ,P'         `Ya`b, ")
            print("      ,P88\"'           `Ya,                 ,P'            `b`Yi ")
            print("     d\",P                `\"Y,              ,P'              `Y \"i ") 
            print("   ,P' P'                   \"888888888888888b                `b \"i ")
            print("  ,P' d'                    d8888888888888888b                `b `b ")
            print("  d' d'                    ,888888888888888888b                I, Y, ")
            print(" ,f ,f                    ,88888888888888888888b               `b, b ")
            print(" d' d'                    d888888888888888888888b              ,88,I ")
            print(",P  8                    ,88888888888888888888888b,_          ,d8888 ")
            print("d'  8,                   d8888888888888888888888P'`\"Ya,_     ,d88888 ")
            print("8  d88b,             ,adP\"\"Y888888888888888888P'      `\"\"Ya, d88888P ") 
            print("8 ,88888b,       ,adP\"'     `\"Y8888888888888\"'             `\"888888I ")
            print("Y,88888888b, ,adP\"'             \"\"Y888888P\"                  888888' ")
            print("`888888888888P'                     \"\"YP\"                    888888 ")
            print(" I88888888888                          8                     88888I ")
            print(" `Y8888888888                          8                     88888' ")
            print("  `Y888888888        Normand           8                     8888I ")
            print("   `Y88888888        Veilleux          8                     8P\"8' ")
            print("    `Y8888888,                         8                   ,d',d' ")
            print("     `b\"\"\"\"Y8b                         8                 ,d\" ,d' ") 
            print("       \"b,   \"Y,                       8               ,P\" ,d\" ")
            print("         \"b,   \"Ya,_                 ,d88ba,,___   _,aP\" ,P\" ")
            print("           \"Ya_   \"\"Ya,_       _,,ad88888888888888P\"' _,d\" ")
            print("             `\"Ya_    \"\"Yaaad88888888888888888888P _,d\"' ")
            print("                 `\"Ya,_     \"Y888888888888888888P\",d\"' ")
            print("                    `\"\"Ya,__`Y888888888888888P\"\"\"  ")
            print("                         ``\"\"\"\"\"\"\"\"\"\"\"\"\"'' ") 
            
            time.sleep (0.5)
            typeWriter("\nFabulous. You are such a great soccer player(100 Point)!",0.03)
            time.sleep (0.3)
            typeWriter("\nGood bye.",0.05)
    
        elif soccerPlayer == "1":
            playSound("uhoh.mp3")
                    
            typeWriter("\nA ball has taken away by one of offenders from Manchester city. Then...he scores a goal! Sorry, you have to learn more.(0 Point)",0.03)
        
            print ("           _...----.._")
            print ("        ,:':::::.     `>.")
            print ("      ,' |:::::;'     |:::.")       
            print ("         /    `'::'       :::::\ ")
            print ("    /         _____     `::;\ ")
            print ("   :         /:::::\      `  :")
            print ("   | ,.     /::SSt::\        |")
            print ("   |;:::.   `::::::;'        |")
            print ("   ::::::     `::;'      ,.  ;")
            print ("    \:::'              ,::::/")
            print ("     \                 \:::/")
            print ("      `.     ,:.        :;'")
            print ("        `-.::::::..  _.''")
            print ("           ```----'''")
    
            typeWriter("\nGood bye.",0.05)
            
#Professor

    if job == "2":
        typeWriter("\nYou are now a professor in Harvard University.",0.03)
        time.sleep (0.5)
        
        typeWriter("\nSituation! You have to determine your best choice.",0.03)
        typeWriter("\nYou are a professor in Harvard University.\nYou gave an assignment to write one paragraph about a bacon recipe to your students.\nYour student, Jasmine copied and pasted one of bacon recipes from Google.\nIt is illegal and teachers should be strict on it.\nWhat is this called?\nand what is a consequence for it?",0.04)
        time.sleep (1)
        professor = input("\nChoose a number (1.Duplication and Suspension or 2.Plagiarism and Withdraw from a college): ")
        while professor != "1" and professor != "2":
            print("Oops! Please choose a number from given options.")
            professor = input("\nChoose a number (1.Duplication and Suspension or 2.Plagiarism and Withdraw from a college): ")
        
   
        if professor == "2":
            playSound("best.mp3")
                
            print("     .----------------------------------------------------. ")
            print("       |                                                    | ")
            print("       |       _  .-\"-.  .-\"-. .--.    _   _      _   ____  | ")
            print("       |    ,'` | | ._ `.| ._ \\|  /  ,' '\\| | _ .' ) |   _|_|__ ")
            print("      _|_  / /| | | | \\ '| | \\ | ;  / ., || || || ;  |  |_(]___`\\ ")
            print("    /___[)' | | | | '-`/ | '-`/| | / /_| || || | \\ `\\|  '(]____ ' ")
            print("   | ____[) '-' | | |-'  | .-' | |/      || `' |  ;  |  |\"(]___ | ")
            print("   ; ___[)| .-. | | |    | |   | '-./`|  ||    | /  /|  |__(]_ / ")
            print("    \\ _[) |_| \\_' '_|    ._|   '---'  '--'`.__.'(_,' |_____||-` ")
            print("     `-|                                                    | ")
            print("       '----------------------------------------------------' ")
            print("        \\      '   /|//  /|/\\,>7/|\\>/\\ \\         /      ,' ")
            print("         \\     '; |/|;  |  .--.  .--. \\ |       /     ,' ")
            print("          '     |  |\\| /  '__________' ||   ,-'     ,' ")
            print("          |     | .-' [    \\\"\" /:  \"/  ]'.,'       / ")
            print("          '.    '|     |    `-'  \\-'  |  |       ,' ")
            print("           |     .'.__.'     |    |   '._'      / ")
            print("           |      `\\||       \\    /    |      .` ")
            print("           |        ||        `--'     |     / ")
            print("           |        \\\\__  __           |     ' ")
            print("           '.        `===(__)`.__.'    ;     | ")
            print("            |         \\ \\             /|     | ")
            print("           .|          \\ `._        ,' |     | ")
            print("           |            .   `-.__,-'   ;     . ")
            print("           |             \\    ,\\_/\\   /      ' ")
            print("           |              `..' |\\\\ `-'   _.-\\ \\ ")
            print("          ,'._                 | :`.  .-`    \\ ; ")
            print("          |   `                | '  \\ \\ __,-' \\| ")
            print("          /                    |  \\  \\ \\      || ")
            print("          `-._                 |   '-'  \\   _,'| ")
            print("              `--.             :   |     `'`  ,/ ")
            print("                  `--._        '.__;         _/ mx ")
            print("                      ``-.___..___....----'\"` ")
    
            typeWriter("\nWow, you are correct. You are such a smart professor!",0.03)
            time.sleep (0.5)

        
        elif professor == "1":
            playSound("uhoh.mp3")
                    
            typeWriter("\nUh,oh! You are incorrect. Sorry, you have to learn more.",0.03)
            typeWriter("\nGood bye.",0.05)

#Babysitter

    if job == "3":
        typeWriter("\nYou are now a babysitter in Mrs.Black's house!",0.03)
        time.sleep (0.5)
        typeWriter("\nSituation! You have to determine your best choice!", 0.03)
        time.sleep (1)
    
        typeWriter("\nYou are caring Jason and Sophie.\nJason is suddenly crying while he is eating his powdered milk.\nThen, he throws a bottle and starts crying.\nWhy is he crying?\nand how are you going to soothe Jason?",0.04) 
        babySitter = input("\nChoose a number (1.Milk tastes bad and Remake it or 2.Milk is hot and Cools it down): ")
        while babySitter != "1" and babySitter != "2":
            print("Oops! Please choose a number from given options.")
            babySitter = input("\nChoose a number (1.Milk tastes bad and Remake it or 2.Milk is hot and Cools it down): ")
    

        if babySitter == "2":
            playSound(laughingbaby.mp3)
            
            print("            .-\"''-.  _ ")
            print("                 .'       `( \\ ")
            print("        @/            ')   ,--,__,-\"")
            print("        /        /      \\ /     /   _/ ")
            print("      __|           ,   |/         / ")
            print("    .~  `\\   / \\ ,  |   / ")
            print("  .~      `\\    `  /  _/   _/ ")
            print(".~          `\\  ~~`__/    / ")
            print("~             `--'/  ")
    
            time.sleep (0.5)
            typeWriter("\nGood decision. You are such a skilled babysitter!",0.03)
            time.sleep (0.3)
            typeWriter("\nGood bye.",0.05) 
    
    
        elif babySitter == "1":
            playSound(annoyingbaby.mp3)
            
            print("         . ")
            print("      .  :  . ")
            print("       '.@.' ")
            print("        /^\\ ")
            print("       /   \\ ")
            print("      /1997 \\ ")
            print("     @@@@@@@@@ ")
            print("    /  6 6    \\ ")
            print("   (    ^     ,) ")
            print("    \\   __,   /-._ ")
            print("     `._____.'\\   `--.__ ")
            print("            \\\\/         `/``\"\"\"'-. ")
            print("             /    )     /         : ")
            print("             |   /\\    |  .--.     : ")
            print("             /  /\\1`\\   \\/    `.__.:.____.-. ")
            print("            /  / /`\\9`\\`/    .-\"..____.-.   \\ ")
            print("        _.-'  /_/   `\\9`\\                \\-. \\ ")
            print("       `=----'        `\\7`\\--------'\"\"`-. \\ `\" ")
            print("                        `-./             `\" ")
    
            time.sleep (0.5)
            typeWriter("\nUh,oh. Jason is still crying. Sorry, you have to learn more.",0.03)
            time.sleep (0.5)
            typeWriter("\nGood bye.",0.05)
        
    
    
    
    

