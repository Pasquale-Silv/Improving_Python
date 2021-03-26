"""
In the previous exercise,
the square brackets around imag in the documentation showed us that the imag argument is optional.
But Python also uses a different way to tell users about arguments being optional.

Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

You'll see that sorted() takes three arguments: iterable, key and reverse.

key=None means that if you don't specify the key argument, it will be None.
reverse=False means that if you don't specify the reverse argument, it will be False.

In this exercise,
you'll only have to specify iterable and reverse, not key.
The first input you pass to sorted() will be matched to the iterable argument, but what about the second input?
To tell Python you want to specify reverse without changing anything about key, you can use =:

sorted(___, reverse = ___)

Two lists have been created for you on the right. Can you paste them together and sort them in descending order?

Note: For now, we can understand an iterable as being any collection of objects, e.g. a List.
"""

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second
print(full)
print()

# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse=True)
full_sorted2 = sorted(full,reverse=False)           # reverse=False by default
full_sorted3 = sorted(full)                         # demonstration

# Print out full_sorted
print(full_sorted)
print(full_sorted2)
print(full_sorted3)