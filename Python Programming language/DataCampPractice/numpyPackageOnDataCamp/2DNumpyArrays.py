import numpy as np

np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat)

np_mat2 = np_mat * 2
print(np_mat2)

np_mat3 = np_mat + np.array([10, 10])
print(np_mat3)

np_mat4 = np_mat + np_mat
print(np_mat4)