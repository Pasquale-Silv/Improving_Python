# you can't go below 0!

import numpy as np

np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = step - 1
        if (step < 0):
            step = 0
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
print(len(random_walk))

# Let's visualize this random walk! Remember how you could use matplotlib to build a line plot?
# If you pass only one argument,
# Python will know what to do and will use the index of the list to map onto the x axis,
# and the values in the list onto the y axis.

import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)        # Con un solo argomento, Python saprà cosa fare mettendo sulle x gli indici della lista.

# Show the plot
plt.show()
