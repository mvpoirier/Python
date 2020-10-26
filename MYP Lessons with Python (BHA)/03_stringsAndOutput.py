"""
NAME: Mr. Poirier
DATE: February 15, 2016
PURPOSE: Strings & Output
FILENAME: stringsTest.py
"""

# Example 1 - Using the end arguement in print()
print("one")
print("two")
print("three", end = "\n\n")

print("four", end = " ")
print("five", end = " ")
print("six", end = "\n\n")

print("seven", end = ", ")
print("eight", end = ", ")
print("nine", end = ".\n\n\n")


# Example 2 - String Concatenation
mySchool = "Branksome Hall"
myContinent = "Asia"
gradYear = 2019

print(mySchool + " " + myContinent + " class of " + str(gradYear) + "!")


# Example 3 - String Concatentation with the %s Placeholder
print("%s %s class of %s!" % (mySchool, myContinent, str(gradYear)))






