"""
NAME: Mr. Poirier
DATE: September 2, 2015
PURPOSE: A "typewriter" function for printing Strings, and a demo with ASCII art
"""

#Import the time module to use the sleep() function
import time


#Define the typerWriter function which accepts a string and an integer
def typeWriter(myStr, t):

    for index in range(len(myStr)):
        print(myStr[index], end="")
        time.sleep(t)

    print()


#Create the ASCII art from Chris.com, and removed any \ or " from the image:
#A backslash \ must become \\
#A doublequote " must become \"
    
asciiArt = """
      db         db
    d88           88
   888            888
  d88             888b
  888             d88P
  Y888b  /``````\\8888
,----Y888        Y88P`````\\
|        ,'`\\_/``\\ |,,    |
 \\,,,,-| | o | o / |  ```'
       |  """ """  |
      /             \\
     |               \\
     |  ,,,,----'''```|
     |``   @    @     |
      \\,,    ___    ,,/
         \\__|   |__/
            | | |
            \\_|_/

"""

#Demo the typewriter function with the asciiArt string - Moooo!
typeWriter(asciiArt, 0.01)
