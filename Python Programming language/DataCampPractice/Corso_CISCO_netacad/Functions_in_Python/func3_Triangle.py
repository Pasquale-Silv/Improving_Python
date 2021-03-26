"""
Let's play with triangles now.
We'll start with a function to check whether three sides of given lengths can build a triangle.
We know from school that the sum of two arbitrary sides has to be longer than the third side.

It will return True if the sides can build a triangle, and False otherwise.
In this case, isItATriangle is a good name for such a function.
"""

def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

print("--------------------------------------------")


def isItATriangle(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

print("--------------------------------------------")

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))
