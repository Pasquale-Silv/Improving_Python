# Dictionary Comprehensions - DC
# Recall that the main difference between a list comprehension and a dict comprehension is the use of curly braces {} instead of []

dc1 = {num: -num for num in range(11)}
print(dc1)
print()

print(dc1.keys())

print(dc1.values())

print(dc1.items())
