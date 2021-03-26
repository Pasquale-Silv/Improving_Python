# The inner part creates a row(cols), and the outer part builds a list of rows.

board = [[i for i in range(8)] for j in range(8)]
print(board)

print()

for row in board:
    print(row)

# Matrice 5 x 4
print("\nOra matrice 5 x 4:\n")

matrix5x4 = [[col for col in range(4)] for row in range(5)]

print(matrix5x4)

for row in matrix5x4:
    print(row)
