myList = [17, 3, 11, 5, 1,800, 9, 7, 15, 13, 30]
largest = myList[0]

for i in range(1, len(myList)):
    if myList[i] > largest:
        largest = myList[i]

print(largest)
