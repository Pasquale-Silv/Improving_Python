# Define shout with the parameter, word
def shout(word):                    # header or signature of the function
    """Print a string with three exclamation marks"""         # Docstring for documentation of the function
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout("congratulations")