# If you want to know a specific character's ASCII/UNICODE code point value,
# you can use a function named ord() (as in ordinal).
# Demonstrating the ord() function

ch1 = 'a'                      # 97
ch2 = ' ' # space                32

print(ord(ch1))
print(ord(ch2))

# If you know the code point (number) and want to get the corresponding character, you can use a function named chr().
# The function takes a code point and returns its character.
# Demonstrating the chr() function

print(chr(97))
print(chr(32))         # space
print(chr(945))