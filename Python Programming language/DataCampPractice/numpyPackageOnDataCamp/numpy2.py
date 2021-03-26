import numpy as np
import math

arr1 = np.array([1,2,3,4,math.pi])         # I vettori devono avere la stessa lunghezza, altrimenti errore.
arr2 = np.array([2,2,2,2,2])         # I vettori devono avere la stessa lunghezza, altrimenti errore.

arr3 = arr1 + arr2

print(arr1)
print(arr2)
print(arr3)