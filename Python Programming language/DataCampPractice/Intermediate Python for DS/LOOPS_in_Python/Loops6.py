# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

print(house[1])
print(house[0][1])

# Build a for loop from scratch
for element in house:
    print("the " + element[0] + " is " + str(element[1]) + " sqm")

