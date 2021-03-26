# The function returns an alphabetically sorted list containing all entities' names available in the module
# identified by a name passed to the function as an argument:
# dir(module)

import math

print(dir(math))

print(math.e)

print("------------------------------------")

for name in dir(math):
    print(name, end="\t")

