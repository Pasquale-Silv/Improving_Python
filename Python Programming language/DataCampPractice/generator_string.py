stringa1 = 'dgdjgs'

sss = iter(stringa1)
print(type(sss))
print(sss)
for elemento in sss:
    print(elemento)

print("--------------------")

for elemento in sss:
    print(elemento)

print("\nCon lista:")
l1 = [1, 2, 3]
l1_it = iter(l1)
print(type(l1_it))
print(l1_it)

for elemento in l1_it:
    print(elemento)

print("Seconda volta:")
for elemento in l1_it:
    print(elemento)
