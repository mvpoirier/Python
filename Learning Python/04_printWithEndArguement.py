"""
NAME: Mr. Poirier
DATE: August 31, 2015
PURPOSE: Print 1 to 10 using end
"""

for i in range(11):
    if i < 10:
        print(str(i), end = ", ")
    else:
        print(str(i), end = ".")

