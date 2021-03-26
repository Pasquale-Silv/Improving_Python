# The parameterless method named
# isalnum()
# checks if the string contains only digits or alphabetical characters (letters),
# and returns True or False according to the result.
# Note: any string element that is not a digit or a letter causes the method to return False. An empty string does, too

# Demonstrating the isalnum() method

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())
# Hint: the cause of the first result is a space - it's neither a digit nor a letter.
