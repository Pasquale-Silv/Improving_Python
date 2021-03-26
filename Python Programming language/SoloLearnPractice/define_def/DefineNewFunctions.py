def add(x, y):
    return x + y

def multiply(x, t):
    print("I due valori saranno moltiplicati")
    print(str(x * t))


def add2(x):
    return x + 1

def printaaa(word):
    print("La parola scelta è: '" + word + "'.")



printaaa("Pasquale")

multiply(3, 9)

print("Funzione con return:")
add(2, 4)     # Non printa perchè return
num = add(5, 5)
n1 = add(3, 4)
print(num)
print(n1)

n2 = add2(10.0)
print(n2)