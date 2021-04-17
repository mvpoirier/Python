'''
NAME:     Mr. Poirier
DATE:     April 14, 2021
PURPOSE:  Coding for Physicists - Day 3
          Creating a 'looping' program (basic calculator)
          - Code loops (for, while)
          - Conditional statements (if/else/elif)
          - Boolean operators (==, !=, and, or)
          - Defining functions (def)
'''

# Addition Function
def addNum ():
  continueAdding = True
  print("\n*** ADD/SUBTRACT NUMBERS ***")

  while (continueAdding):
    num1 = int(input("Input number #1: "))
    num2 = int(input("Input number #2: "))
    print("Sum = " + str(num1 + num2))
    user = input("Would you like to try again (y)? ")
    
    # String & built-in type functions:
    # https://docs.python.org/3/library/stdtypes.html
    # https://www.w3schools.com/python/python_ref_string.asp
    # lower() will convert the String to all lowercase
    if (user.lower() != "y" and user.lower() != "yes"):
      continueAdding = False
    else:
      print()

# Multiply Function
def multNum ():
  print("Multiply!")

# Mod Function (Find the Remainder)
def modNum ():
  print("Mod!")

# MAIN FUNCTION (i.e. 'The Game Loop')
keepRunning = True
print("Welcome to my amazing calcuator!")

while (keepRunning):
  print("\nPlease choose one of the following options:")
  print("1 - Add/Subtract Numbers")
  print("2 - Multiply/Divide Numbers")
  print("3 - Find the the remainder (mod)")
  print("4 - Quit\n")
  user = input("Enter choice (1 to 4): ")
  
  if (user == "1"):
    addNum()
  elif (user == "2"):
    multNum()
  elif (user == "3"):
    modNum()
  elif (user == "4"):
    keepRunning = False
  else:
    print("ERROR: Incorrect input! Please try again.")

print("\nGood bye!")