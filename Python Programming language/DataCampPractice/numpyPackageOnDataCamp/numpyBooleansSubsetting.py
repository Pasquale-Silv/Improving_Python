"""
For numpy specifically, you can also use boolean numpy arrays:

high = y > 5
y[high]

this thing will subset your numpyArray according to the specified boolean comparison.
"""
import numpy as np

list1 = [1, 30, 700, 2, 3, 6, 80, 60, 9, 10, 82, 1, 100, 123, 150, 309]
print(list1)
# print(list1[list1 > 50])    ---------> Questo non è possibile poichè funziona solo su numpyArrays il subsetting con booleani

print("Ordiniamo la lista:")
list1Ord = sorted(list1)
print(list1Ord)

print("\nConversione della lista in numpyArray:")
np_list1 = np.array(list1)
print(np_list1)

print("Subsetting secondo np_list1 > 102 :")
print(np_list1[np_list1 > 102])

np_list1Ord = np.array(list1Ord)
np_bool = np_list1Ord > 50
print(np_bool)
print(np_list1Ord[np_bool])

print("\nSubsetting secondo np_list1Ord[np_list1Ord < 0] :")
print(np_list1Ord[np_list1Ord < 0])
print("Non ci sono elementi negativi nella lista specificata, cosi restituisce una lista vuota.")