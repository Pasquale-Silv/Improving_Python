dict1 = {
    'Paky': 1,
    'Alfy': 98,
    'Bryan': 81
}
print(dict1)
print(dict1.items())

list1 = ['a', 'b', 'c']
print(enumerate(list1))
print(list(enumerate(list1)))
for index, element in enumerate(list1):
    print("Element:", element, ",index:" , index)
list2 = ['uno', 'due', 'tre']
print(zip(list1, list2))
print(list(zip(list1, list2, ['altro', 'again', 'altroAncora', 'neverDisplayed'])))
print(dict(list(zip(list1, list2))))

for element1, element2 in zip(list1, list2):
    print("Elemento1:", element1, ",elemento2:", element2)

print("----------------------")

zip1 = zip(list1, list2)
print(dict(zip1))
for element1, element2 in zip1:
    print("Elemento1:", element1, ",elemento2:", element2)
print("Seconda volta:(Non mostra nulla poichè 'zip object' è un iterator! Devi ricrearlo!)")
for element1, element2 in zip1:
    print("Elemento1:", element1, ",elemento2:", element2)
