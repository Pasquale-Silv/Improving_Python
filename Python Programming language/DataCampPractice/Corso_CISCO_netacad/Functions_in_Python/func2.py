# Take a look at the way the
# backslash (\) symbol is used.
# If you use it in Python code and end a line with it,
# it will tell Python to continue the line of code in the next line of code.

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(85, 1.65))
