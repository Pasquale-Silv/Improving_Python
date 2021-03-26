"""
'assert' evaluates the expression;
if the expression evaluates to True, or a non-zero numerical value, or a non-empty string,
or any other value different than None, it won't do anything else;
otherwise,
it automatically and immediately raises an exception named AssertionError
(in this case, we say that the assertion has failed)
"""

import math

x = float(input("Enter a number: "))

# The program runs flawlessly if you enter a valid numerical value greater than or equal to zero
assert x >= 0.0

x = math.sqrt(x)

print(x)