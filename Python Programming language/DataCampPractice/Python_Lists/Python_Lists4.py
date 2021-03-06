"""
As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

Instead of creating a flat list containing strings and floats, representing the names and areas of the rooms in your house,
you can create a list of lists. The script on the right can already give you an idea.
"""

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom",bed],
         ["bathroom",bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

x = ["a", "b", "c", "d"]
primo = x[1]
secondo = x[-3]     # same result!
print(primo)
print(secondo)

print(house[-1][1])
print(house[-1][0])