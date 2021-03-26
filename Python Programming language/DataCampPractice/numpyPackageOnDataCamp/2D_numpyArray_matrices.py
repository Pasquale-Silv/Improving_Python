import numpy as np

list1 = [[10, 11, 12],          # Nota la differenza grafica con la numpyArray
         [13, 14, 15],
         [20, 30, 33]]

print(list1)
print(type(list1))

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [30, 20, 82]])

print()
print(matrix1)
print(type(matrix1))

sub1 = matrix1[0, 2]
print(sub1)

print(matrix1[2, 0])

print(matrix1[1, 2])
