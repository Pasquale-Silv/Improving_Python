"""
The range function creates a sequential list of numbers.
The code below generates a list containing all of the integers, up to 10.

If range is called with one argument, it produces an object with values from 0 to that argument.
If it is called with two arguments, it produces values from the first to the second.

range can have a third argument, which determines the interval of the sequence produced.
This third argument must be an integer.
"""

numbers = list(range(10))
print(numbers)

numbers2 = list(range(5))
print(numbers2)

numbers3 = list(range(3, 8))
print(numbers3)

print(range(20) == range(0, 20))

numbers = list(range(5, 20, 2))
print(numbers)

nums = list(range(3, 15, 3))
print(nums[2])