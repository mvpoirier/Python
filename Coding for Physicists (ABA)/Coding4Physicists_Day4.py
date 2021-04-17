'''
NAME:     Mr. Poirier
DATE:     April 14, 2021
PURPOSE:  Coding for Physicists - Day 4

Continue our Calculator:
- Complete our basic calculator: add/sub, mult/div, mod
- Add additional modules for increased functionality (math, numpy, scipy, matplotlib)
- Add additional menu options (e.g. trigonometry, plotting functions, averages, random numbers)
'''

# https://docs.python.org/3/library/math.html
import math

# https://numpy.org/
import numpy as np 

# https://matplotlib.org/
import matplotlib.pyplot as plt

# Addition Function
def addNum ():
  cont = True
  print("\n*** ADDITION ***\n")

  while (cont):
    num1 = int(input("Input number #1: "))
    num2 = int(input("Input number #2: "))
    print("Sum = " + str(num1 + num2))
    
    user = input("Would you like to try again (y)? ")
    if (user.lower() != "y" and user.lower() != "yes"):
      cont = False
    else:
      print()

# Multiply Function
def multNum ():
  cont = True
  print("\n*** MULTIPLY ***\n")

  while (cont):
    # Float is a number with decimals (e.g. 0.5)
    num1 = float(input("Input number #1: "))
    num2 = float(input("Input number #2: "))
    print("Product = " + str(num1 * num2))
    
    user = input("Would you like to try again (y)? ")
    if (user.lower() != "y" and user.lower() != "yes"):
      cont = False
    else:
      print()

# Mod Function (Find the Remainder)
def modNum ():
  cont = True
  print("\n*** DIVIDE & MOD ***\n")

  while (cont):
    num1 = float(input("Input number #1 (Dividend): "))
    num2 = float(input("Input number #2 (Divisor): "))
    
    if (num2 != 0):
      print("Quotient = " + str(int(num1 / num2)))
      print("Remainder = " + str(int(num1 % num2)))
    else:
      print("ERROR: Cannot divide by zero!")
    
    user = input("Would you like to try again (y)? ")
    if (user.lower() != "y" and user.lower() != "yes"):
      cont = False
    else:
      print()

# Trigonometry Function
def trigNum():
  cont = True
  print("\n*** RIGHT-ANGLE TRIGONOMETRY: FIND ANGLE ***\n")

  while (cont):
    opp = float(input("Length of opposite side (0 if unknown): "))
    adj = float(input("Length of adjacent side (0 if unknown): "))
    hyp = float(input("Length of hypotenuse (0 if unknown): "))

    # Rounding floats: https://stackoverflow.com/q/455612
    if (opp == 0 and hyp > adj):
      # inverse cosine (e.g. arccosine, acos)
      print("Angle (radians): %.2f" % math.acos(adj/hyp))
      print("Angle (degrees): %.2f" % math.degrees(math.acos(adj/hyp)))
    elif (adj == 0 and hyp > opp):
      # inverse sine (e.g. arcsine, asin)
      print("Angle (radians): %.2f" % math.asin(opp/hyp))
      print("Angle (degrees): %.2f" % math.degrees(math.asin(opp/hyp)))
    elif (hyp == 0):
      # inverse tan (e.g. arctan, atan)
      print("Angle (radians): %.2f" % math.atan(opp/adj))
      print("Angle (degrees): %.2f" % math.degrees(math.atan(opp/adj)))
    else:
      print("ERROR: Incorrect input provided.")

    user = input("Would you like to try again (y)? ")
    if (user.lower() != "y" and user.lower() != "yes"):
      cont = False
    else:
      print()

# Scatter Plot Function
def graphNum():
  cont = True
  xValues = []
  yValues = []
  print("\n*** PLOTTING A GRAPH ***\n")

  while (cont):
    size = int(input("How many data points are you plotting? "))

    for i in range(size):
      xValues.append(float(input("x" + str(i+1) + ": ")))
      yValues.append(float(input("y" + str(i+1) + ": ")))
      print()

    graphTitle = input("Graph Title: ")
    xTitle = input ("X-Axis Label: ")
    yTitle = input("Y-Axis Label: ")
    filename = input("Save graph as (filename): ")

    # Using pyplot:
    # https://stackabuse.com/save-plot-as-image-with-matplotlib/
    # https://matplotlib.org/stable/api/pyplot_summary.html
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

    plt.plot(xValues, yValues, 'ro') #red circles
    plt.title(graphTitle)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.savefig(filename + ".png")

    # Determining Line of Best Fit (LOBF) without Error Bars
    # https://stackoverflow.com/a/31800660
    x = np.array(xValues) # Convert Python list object into a numerical array using numpy
    y = np.array(yValues)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'g-.') # LOBF green dotted line
    plt.title(graphTitle + " (with Line of Best Fit)")
    plt.savefig(filename + "_LOBF.png")
    
    user = input("Would you like to try again (y)? ")
    if (user.lower() != "y" and user.lower() != "yes"):
      cont = False
    else:
      xValues.clear()
      yValues.clear()
      print()

# MAIN FUNCTION (i.e. 'The Game Loop')
keepRunning = True
print("Welcome to Mr. Poirier's \"Coding for Physicists\" Calculator!")

while (keepRunning):
  print("\nPlease choose one of the following options:")
  print("1 - Addition")
  print("2 - Multiply")
  print("3 - Divide & Mod")
  print("4 - Right-Angle Trigonmetry")
  print("5 - Scatter Plot & LOBF")
  print("Q - Quit\n")
  user = input("Enter choice: ")
  
  if (user == "1"):
    addNum()
  elif (user == "2"):
    multNum()
  elif (user == "3"):
    modNum()
  elif (user == "4"):
    trigNum()
  elif (user == "5"):
    graphNum()
  elif (user.lower() == "q"):
    keepRunning = False
  else:
    print("ERROR: Incorrect input! Please try again.")

print("\nGood bye!")