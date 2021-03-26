# An iterable is an object that can return an iterator,
# while an iterator is an object that keeps state and produces the next value when you call next() on it.

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for parola in flash:
    print(parola)

print("\nWith an iterator:")
# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))