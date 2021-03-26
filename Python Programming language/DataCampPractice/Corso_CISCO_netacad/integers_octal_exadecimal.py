# If an integer number is preceded by an 0O or 0o prefix (zero-o),
# it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.
# 0o123 is an octal number with a (decimal) value equal to 83.

print(0o123)

# The second convention allows us to use hexadecimal numbers.
# Such numbers should be preceded by the prefix 0x or 0X (zero-x).
# 0x123 is a hexadecimal number with a (decimal) value equal to 291. The print() function can manage these values too.

print(0x123)

print(4 == 4.0)
print(.4)
print(4.)

# On the other hand, it's not only points that make a float. You can also use the letter e.
# When you want to use any numbers that are very large or very small, you can use scientific notation.

print(3e8)
print(3E8)
# The letter E (you can also use the lower-case letter e - it comes from the word exponent)
# is a concise record of the phrase times ten to the power of.

print("----------------------------------------------------------")
print(0.0000000000000000000001)
print(1e-22)
