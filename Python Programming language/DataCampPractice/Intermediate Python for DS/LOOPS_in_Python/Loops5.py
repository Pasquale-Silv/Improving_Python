fam = [1.73, 1.68, 1.71, 1.89]

for index, height in enumerate(fam) :
    print("person " + str(index) + ": " + str(height))

print("----------------------")

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas):
    print("room " + str(index) + ": " + str(a))

# For non-programmer folks, room 0: 11.25 is strange. Wouldn't it be better if the count started at 1?

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))