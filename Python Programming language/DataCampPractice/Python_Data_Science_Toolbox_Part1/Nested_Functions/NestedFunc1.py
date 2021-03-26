# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

print()
tupla_prova = three_shouts('Pasquale', 'Ignazio', 'Laura')
print(tupla_prova)
var1, var2, var3 = tupla_prova
print(var1, var2, var3)