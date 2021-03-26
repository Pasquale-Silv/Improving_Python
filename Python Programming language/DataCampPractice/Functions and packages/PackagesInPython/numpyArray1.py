import numpy as np

l1 = [[1,2,3],
       [8,55,9],
       [5, 11, 77],
       [10,11,23]]

print(l1)

np_l1 = np.array(l1)

print(np_l1)

print(np_l1[0, :])      # Tutta la prima riga

terza_colonna = np_l1[:, 2]
print(terza_colonna)

quarta_riga = np_l1[3, :]
print(quarta_riga)
