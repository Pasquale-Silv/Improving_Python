# COIN TOSS (Lancio della moneta)

import numpy as np

coin = np.random.randint(0, 2)
print(coin)

if coin == 0:
    print("head")
else:
    print("tail")

print("\nCon il settaggio del seed, invece:")

np.random.seed(123)

coin = np.random.randint(0, 2)
print(coin)

if coin == 0:
    print("head")
else:
    print("tail")

