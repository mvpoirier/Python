"""
NAME: Mr. Poirier
DATE: September 9, 2015
PURPOSE: Printing bacon using functions and loops
"""

"""
# Define the bacon printer with while loop
def baconPrinter (num):
    while num > 0:
        print("Bacon")
        num = num - 1
"""

# Define the bacon printer with a for loop
def baconPrinter (num):
    for eggs in range(num):
        print("Bacon")

# Define a generic string printer with a for loop
def stringPrinter (count, myStr):
    for i in range(count):
        print(myStr)

print("Here have 3 pieces of bacon:")
baconPrinter(3)

print("\n\nHere is 5 more pieces of bacon:")
baconPrinter(5)

print("\n\nFor dessert, 10 more bacons!")
baconPrinter(10)

# Get input from the user to print bacon
numBacon = input("\n\nHow much more bacon: ")
numBacon = int(numBacon)
baconPrinter(numBacon)

print("\n\nHEY! I almost forgot your 20 eggs!")
stringPrinter(20, "eggs")
