lista_for = []

for num1 in range(0, 2):
    for num2 in range(6, 8):
        lista_for.append((num1, num2))       # Il metodo .append takes only one argument, per questo tupla.

print(lista_for)

print("-------------------------------------------\nLC:")

lista_LC = [(x, y) for x in range(0, 2) for y in range(6, 8)]
print(lista_LC)
