# The index() method (it's a method, not a function) searches the sequence from the beginning,
# in order to find the first element of the value specified in its argument.
# Note: the element searched for must occur in the sequence - its absence will cause a ValueError exception.
# The method returns the index of the first occurrence of the argument
# (which means that the lowest possible result is 0, while the highest is the length of argument decremented by 1).

# Demonstrating the index() method
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

print("-------------------------")
# The find() method is similar to index(),
# which you already know - it looks for a substring and returns the index of first occurrence of this substring, but:
# it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
# it works with strings only - don't try to apply it to any other sequence.

# Demonstrating the find() method
print("Eta".find("ta"))
print("Eta".find("mma"))

print('kappa'.find('a', 2))

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
