data1 = "{}/{}/{}".format(21, 12, 1995)
print("La data è: " + data1)

print("Stringa: {}, int: {}, float: {}, bool: {}".format("Ciao", 33, 5.67, True))
print(f"\nint: { 44 }, float: { 6.8 }, variabile: { data1 }, lista: { [12, 3.3, True, 'Silvestre'] }, tupla: { (2, 3.3) }")

lista1 = [3.36, "Silv", 8]
tupla1 = (2, "Pasq", 7)
dict1 = {"Pasquale": "Programmer",
         "Alfonso":"Medico"}

print(tupla1[2])

metodo1 = "\n\nLista: {}, tupla: {}, altra lista: {}, dict: {}, moooolto bene".format(lista1, tupla1, [3, 4, 5.5], {"Pasquale": "Programmer", "Alfonso":"Medico"})
metodo2 = f"\nLista: { lista1 }, tupla: { tupla1 }, dizionario: { dict1 }, good"

print(metodo1)
print(metodo2)