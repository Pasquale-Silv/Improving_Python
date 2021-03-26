import numpy as np

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

print("------------------------------------------------")

# regular list of lists
x = [["a", "b"],
     ["c", "d"]]
a = [x[0][0], x[1][0]]

# numpy
np_x = np.array(x)
b = np_x[:,0]

print(a)
print(b)