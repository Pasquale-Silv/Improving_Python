import numpy as np

# List input: my_matrix
my_matrix = [[1, 2, 3, 4],
             [5, 6, 7, 8]]


# Function that converts lists to arrays: return_array
def return_array(list_matrix):
    array = np.array(list_matrix, dtype=float)
    return array


# Call return_array on my_matrix, and print the output
print(return_array(my_matrix))