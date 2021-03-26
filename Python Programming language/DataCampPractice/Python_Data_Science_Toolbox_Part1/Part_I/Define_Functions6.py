# Prima funzione
def raise_power(num1, num2):
    """Raise the num1 at the power of num2"""
    return num1 ** num2

# Seconda funzione
def raise_power_tuple(num1, num2):
    """Raise the num1 at the power of num2 and vice versa"""
    var1 = num1 ** num2
    var2 = num2 ** num1
    tuple_1 = (var1, var2)
    return tuple_1


n1 = raise_power(2, 3)
print(n1)

tuplina1 = raise_power_tuple(2, 3)
tuplina2 = raise_power_tuple(2, 4)
tuplina3 = raise_power_tuple(4, 5)

print(tuplina1)
print(tuplina2)
print(tuplina3)

t1 = tuplina1[0]
print("Primo elemento della tuplina1 = " + str(t1))