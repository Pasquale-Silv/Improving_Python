"""
As a data scientist, some notions of geometry never hurt. Let's refresh some of the basics.

For a fancy clustering algorithm,
you want to find the circumference, C, and area, A, of a circle.
When the radius of the circle is r, you can calculate C and A as:

              C=2πr
              A=πr**2
To use the constant pi, you'll need the math package.
"""


# Import the math package
import math

# Definition of radius
r = 0.43

# Calculate C
C = 2*r*math.pi

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

print()
print(math.pi)
print("PiGreco dal package math = " + str(math.pi))