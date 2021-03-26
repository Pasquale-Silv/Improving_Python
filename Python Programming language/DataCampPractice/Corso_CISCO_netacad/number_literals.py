# Python 3.6 has introduced underscores in numeric literals,
# allowing for placing single underscores between digits and after base specifiers for improved readability.
# This feature is not available in older versions of Python.

"""
If you'd like to quickly comment or uncomment multiple lines of code,
select the line(s) you wish to modify and use the following keyboard shortcut:
CTRL + /              ------------------------->  (Windows)
or
CMD + /               -------------------   --->  (Mac OS).
 It's a very useful trick, isn't it?
"""

print(11_111_111 * 2)
print(11111111)
print(11_111_111)

print("/" == "/")         # Col 7 e non

print("------------------------------------")

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
print("Concateno:", 33, hypo, 3.33, True)
