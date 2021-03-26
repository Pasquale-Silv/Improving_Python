"""
Selecting single values from a list is just one part of the story. It's also possible to slice your list,
which means selecting multiple elements from your list. Use the following syntax:

my_list[start:end]
The start index will be included, while the end index is not.
"""

x = ["a", "b", "c", "d"]
slicing = x[1:3]
print(slicing)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
# Use slicing to create downstairs
downstairs = areas[0:6]

# Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
