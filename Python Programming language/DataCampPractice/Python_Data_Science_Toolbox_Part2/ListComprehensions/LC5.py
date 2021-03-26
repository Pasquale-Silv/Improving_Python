# Creiamo una matrice generica n x m

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]
# Print the matrix
for row in matrix:
    print(row)

print()
print(matrix)

print("----------------------------------------")

matrix2 = [[col for col in range(10)]for row in range(0, 5)]
print(f"La matrice 5x10 è: { matrix2 }\n")
for row in matrix2:
    print(row)

print("\nAdesso crea una matrice 4x2 con valori non standard: ")
matrix3 = [[col for col in range(33, 33+2)]for row in range(102, 102+4)]
for r in matrix3:
    print(r)

print("\nAdesso crea una matrice 8x10: ")
matrix4 = [[col for col in range(10, 10+8)]for row in range(0, 10)]
for row in matrix4:
    print(row)
