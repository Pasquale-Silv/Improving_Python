l = [5, 9, 10, 6, 1 , 2, 4, 3]
print(len(l))
print("La lunghezza della lista l è: " + str(len(l)))

print(l)

print(type(l))

sorted(l)    # Non influenza la lista.
print(l)
print(sorted(l))
print(max(l))
print(min(l))
help(sorted)    # help() function open up documentation    help(function you want to open up documentation)

print("Il massimo della lista l è: " + str(max(l)))
print("Il minimo della lista l è:" + str(min(l)))

print("\nFunzione round():")
print("round(1.66) = " + str(round(1.66)))
print("round(1.44) = " + str(round(1.44)))

print(round(1.78, 2))
print(round(1.78, 1))        # same as round(1.78)
print(round(1.32, 2))
print(round(1.32, 1))        # same as round(1.32)
print(round(1.78, 2))
print(round(1.78, 1))        # same as round(1.78)

l2 = [2.33, 1.68, round(33.3)]
print(l2)
print(round(l2[0], 1))
print(round(l2[0], 2))
print(round(l2[1]))
print(round(l2[1], 1))

print("-------------------------------------")
a = 3
a += 1      # a++ non esiste in Python
print(a)
a += 3
print(a)
a *= 2
print(a)

print("-----------------------------------")
result = type(3.0)
print(result)

print("----------------------------------------")
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)