"""
NAME: Mr. Poirier
DATE: September 7, 2015
PURPOSE: Testing different loops
"""
# A basic while loop
count = 2

while count <= 10:
    print("count = %s" % (count))
    count = count + 2

print("\nEnd.\n\n")


# A basic test for entering only letters
name = input("Enter your name: ")

while not name.isalpha():
    name = input("Error! Please enter your name again: ")

print("\nEnd.\n\n")


# We are going to make an infinite while loop!
"""
num = 0

while num != 1:
    print("Oops! I'm going to print forever!")
"""

