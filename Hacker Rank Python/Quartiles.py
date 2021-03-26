import statistics as st

n = int(input())
arrayInt = list(map(int, input().strip().split()))

import statistics as st

def calculateQuartiles(listaFirstQuart, listaThirdQuart):
    first = st.median(listaFirstQuart)
    third = st.median(listaThirdQuart)
    return (first, third)


def calculateMedian(listValues):
    listValues.sort()
    numerosity = len(listValues)
    listaFirstQuartile = []
    listaThirdQuartile = []
    if (numerosity % 2 != 0):  # Odd numerosity
        position = int((numerosity + 1) / 2)
        median = listValues[position - 1]
        for i in range(position - 1):
            listaFirstQuartile.append(listValues[i])
        for i in range(position, numerosity):
            listaThirdQuartile.append(listValues[i])
    elif (numerosity % 2 == 0):  # Even numerosity
        position = int(numerosity / 2)
        median = (listValues[position] + listValues[position - 1]) / 2
        for i in range(position):
            listaFirstQuartile.append(listValues[i])
        for i in range(position, numerosity):
            listaThirdQuartile.append(listValues[i])

    first, third = calculateQuartiles(listaFirstQuartile, listaThirdQuartile)

    return median, first, third


mediana, first, third = calculateMedian(arrayInt)

print(int(first))
print(int(mediana))
print(int(third))
