"""
NAME: Mr. Poirier
DATE: September 1, 2020
PURPOSE: Basics of Python 3
"""

# We assign data to memory address with variables and '=' sign
# Variable names are written using camelCase for increased readability
myCurrentSchool = "ABA Oman International School"

# Example of 'weakly typed' variable assignments in Python
# In Java, we would have to define the data type of myAge
myAge = 72
myAge = "Thirty Five"
myAge = 20 + 21

# Data Types
myBoolean = True
myOtherBoolean = False
myFloat = 3.14
myInteger = 18
myString = "Hello World!"

# Example of an if statement with whitespace
coldOutside = False
if (not coldOutside):
    print("Bring a hat to wear!")
if (coldOutside):
    print("This will NEVER print!")

# Math Operations
addNumbers = 2 + 3
subNumbers = 2 - 3
multNumbers = 2 * 3
divNumber = 11 / 5
expNumbers = 2 ** 3 # 2 to the power of 3
modNumber = 11 % 5 # Returns the remainder
