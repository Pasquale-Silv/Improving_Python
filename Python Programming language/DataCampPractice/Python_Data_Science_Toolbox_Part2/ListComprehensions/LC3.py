doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

# list comprehensions can be built over iterables.
# How would a list comprehension that produces a list of the first character of each string in doctor look like?
# Note that the list comprehension uses doc as the iterator variable.

first_char_doctor = [stringa[0] for stringa in doctor]
print(first_char_doctor)