# you can also remove elements from your list. You can do this with the del statement:
# Pay attention here: as soon as you remove an element from a list, the indexes of the elements that come after the deleted element all change!

x = ["a", "b", "c", "d"]
print(x)
del(x[1])                    # del statement
print(x)

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

print(areas)

del(areas[-4:-2])
print(areas)

"""
The ; sign is used to place commands on the same line. The following two code chunks are equivalent:

# Same line
command1; command2

# Separate lines
command1
command2
"""