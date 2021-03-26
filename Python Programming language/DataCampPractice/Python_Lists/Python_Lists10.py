# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas)

# Correct the bathroom area
areas[-1] = 10.50
print(areas)

# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)

print("---------------------------")
x = ["a", "b", "c", "d"]
print(x)
y = x + ["e", "f"]
print(x)
print(y)
z = y + [4, 6, 7] + x
print(z)

print("--------------------------------------------")

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]
print(areas)

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
print(areas_1)

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)