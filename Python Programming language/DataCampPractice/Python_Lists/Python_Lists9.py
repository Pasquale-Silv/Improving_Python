x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
elemento1 = x[2][0]
elemento2 = x[2][:2]

print(elemento1)
print(elemento2)
print()

# x[2] results in a list, that you can subset again by adding additional square brackets.

print(x[2])   # Terza riga (Index 2 row)
print(x[0])  # Prima riga
print(x[1])   # Seconda riga

print("------------------------------------------------")
x = ["a", "b", "c", "d"]
print(x)
x[1] = "r"
print(x)
x[2:] = ["s", "t"]
print(x)