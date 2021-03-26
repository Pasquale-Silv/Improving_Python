"""
n = int(input())
array = list(map(int, input().strip().split()))
freq = list(map(int, input().strip().split()))
"""
array = [6, 12, 8, 10, 20, 16]
freq = [5, 4, 3, 2, 1, 5]

import statistics as st

completeList = []
for i in range(len(array)):
    for j in range(freq[i]):
        completeList.append(array[i])
print(completeList)

completeList.sort()
print(completeList)
if(len(completeList) % 2 == 0):
    lowerList = [completeList[i] for i in range((len(completeList) // 2))]
    upperList = [completeList[i] for i in range((len(completeList) // 2), len(completeList))]
else:
    lowerList = [completeList[i] for i in range((len(completeList) // 2))]
    upperList = [completeList[i] for i in range((len(completeList) // 2) + 1, len(completeList))]


def trovaQ(lista):
    lung = len(lista)
    q = 0
    if len(lista) % 2 == 0:
        q = (lista[(lung // 2) - 1] + lista[(lung // 2)]) / 2
    else:
        q = st.median(lista)
    return q

print(lowerList)
print(upperList)
firstQ = trovaQ(lowerList)
thirdQ = trovaQ(upperList)

print(round(thirdQ - firstQ, 1))

print("-----------------------")

array = [3, 4, 5]
freq = [1, 2, 2]
completeList = []
for i in range(len(array)):
    for j in range(freq[i]):
        completeList.append(array[i])
print(completeList)

completeList.sort()
print(completeList)

if(len(completeList) % 2 == 0):
    lowerList = [completeList[i] for i in range((len(completeList) // 2))]
    upperList = [completeList[i] for i in range((len(completeList) // 2), len(completeList))]
else:
    lowerList = [completeList[i] for i in range((len(completeList) // 2))]
    upperList = [completeList[i] for i in range((len(completeList) // 2) + 1, len(completeList))]

print(lowerList)
print(upperList)
