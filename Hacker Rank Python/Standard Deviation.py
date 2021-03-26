n = int(input())
values = list(map(int, input().strip().split()))


def mean(lista):
    return sum(lista) / len(lista)

def std(lista):
    meanLista = mean(lista)
    val = sum([(el - meanLista) ** 2 for el in lista]) / len(lista)
    return round(val ** (1 / 2), 1)


print(std(values))
