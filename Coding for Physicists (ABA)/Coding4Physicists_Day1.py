'''
NAME:     Mr. Poirier
DATE:     April 14, 2021
PURPOSE:  Coding for Physicists Day 1
          - Basic input and output (I/O) in Python
'''

choice = "y"

while (choice == "y"):
  name = input("What is your name? ")
  print("Hello " + name + "!")

  num = input ("What is your favorite number? ")
  # Convert the String num to an Integer
  num = int(num)

  # Square num
  print("Did you know that " + str(num) + " squared is " + str(num ** 2))

  food = input ("What is your favorite food? ")

  # Loops in Python
  # i will take a number from 0 to num-1
  for i in range(num):
    if (i == 0): # Is i equal to 0?
      print(name + " ate " + str(i + 1) + " " + food)
    else:
      print(name + " ate " + str(i + 1) + " " + food + "s")

  choice = input("Play again (y/n)? ")