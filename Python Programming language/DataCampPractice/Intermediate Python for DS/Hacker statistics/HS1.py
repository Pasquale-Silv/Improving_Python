# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
random_float = np.random.rand()
print(random_float)


print(np.random.randint(4, 8))

np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randint() again
print(np.random.randint(1, 7))