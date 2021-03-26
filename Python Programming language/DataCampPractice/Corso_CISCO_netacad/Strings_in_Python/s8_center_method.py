# The one-parameter variant of the center() method makes a copy of the original string,
# trying to center it inside a field of a specified width.
# The centering is actually done by adding some spaces before and after the string.
# Demonstrating the center() method
print('[' + 'alpha'.center(10) + ']')

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

# The two-parameter variant of center() makes use of the character from the second argument,
# instead of a space. Analyze the example below:

print('[' + 'gamma'.center(20, '*') + ']')

s1 = "Pasquale".center(30)
print(s1)
print("length:", len(s1))
s2 = "Pasquale Silvestre".center(50, "-")
print(s2)
print(len(s2))
