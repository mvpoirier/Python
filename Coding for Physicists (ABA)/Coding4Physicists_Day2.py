"""
NAME:     Mr. Poirier
DATE:     2021-04-11
PURPOSE:  Coding for Physicists - Day 2
          - Mathematical coding & importing functions
          - math, numpty, & matplotlib with pyplot
"""

# https://docs.python.org/3/library/math.html
import math 

# https://numpy.org/
import numpy as np 

# https://matplotlib.org/
import matplotlib.pyplot as plt


# Basic math in Python
print(1 + 1)
print(2*2)
print(2**3)
print(3/2)

#modulus - what is the remainder after div?
print(3%2)
print(8%3)
print(4%2) # if num % 2 == 0, then even
print(5%2) # if num % 2 == 1, then odd

# math function
print("Sine of 30 degrees: " + str(math.sin(math.radians(30))))
print(math.sqrt(16))

# numpy: https://numpy.org/doc/stable/reference/index.html
# Finding the roots for a polynomial: -4.9x**2 + 3x + 10
coeff = [-4.9, 3, 10]
print(np.roots(coeff))

# Data for plotting with matplotlib and pyplot
# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
# https://matplotlib.org/stable/gallery/index.html#pyplot
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
#plt.show()
plt.savefig("test1.png")

plt.plot([1,2,3,4], [2, 4, 6, 8], 'ro')
plt.ylabel('MORE numbers!')
#plt.show()
plt.savefig("test2.png")

plt.clf() # clear plot cache, otherwise will print next on the same figure

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
plt.ylabel('EVEN MORE numbers!')
# red dashes, blue squares and green triangles
# t vs t, t vs t**2, and t vs t***3
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()
plt.savefig("test3.png")
plt.clf()

# User defined exponential graph
num = int(input("Exponent to graph? "))
x = np.arange(0., 10., 1.) # x is from 0 to 10, 1 intervals
plt.xlabel('x')
plt.ylabel('x^' + str(num))
plt.title('User-defined: x to the power of ' + str(num))
plt.grid(True)
plt.plot(x,x**num, 'rs') #red squares
plt.savefig("test4.png")
plt.show()
