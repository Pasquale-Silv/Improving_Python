# A random number generator takes a value called a seed, treats it as an input value,
# calculates a "random" number based on it (the method depends on a chosen algorithm) and produces a new seed value.
#
# The length of a cycle in which all seed values are unique may be very long,
# but it isn't infinite - sooner or later the seed values will start repeating,
# and the generating values will repeat, too. This is normal. It's a feature, not a mistake, or a bug.
#
# The initial seed value, set during the program start, determines the order in which the generated values will appear.

from random import random

for i in range(5):
    print(random())

print("-------------------------\nCon seed fissato:")

from random import random, seed

seed(0)
# Due to the fact that the seed is always set with the same value,
# the sequence of generated values always looks the same.

for i in range(5):
    print(random())
