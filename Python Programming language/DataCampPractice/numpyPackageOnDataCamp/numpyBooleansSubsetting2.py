import numpy as np

list1 = [-2, -30, 4, 55, 102, -89, 0]

np_list1 = np.array(list1)

print("np_list1 :")
print(np_list1)

op_bool_subset = np_list1 >= 0
op_bool_subset2 = np_list1 < 0

print("\nnp_list1 >= 0 :")
print(op_bool_subset)

print("np_list1 < 0 :")
print(op_bool_subset2)

print("\nnp_list1[op_bool_subset] :")
print(np_list1[op_bool_subset])

print("np_list1[op_bool_subset2] :")
print(np_list1[op_bool_subset2])