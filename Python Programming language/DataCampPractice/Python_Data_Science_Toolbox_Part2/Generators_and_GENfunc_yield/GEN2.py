# [ LIST COMPREHENSION ]
# ( GENERATOR )

# Recall that generator expressions basically have the same syntax as list comprehensions,
# except that it uses parentheses () instead of brackets []

# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)
