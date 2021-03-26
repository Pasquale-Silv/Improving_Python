import numpy as np

weight = [77, 80, 99, 85, 63, 55, 85]
height = [1.78, 1.83, 2.06, 1.70, 1.55, 1.65, 1.70]

np_weight = np.array(weight)
np_height = np.array(height)

np_bmi = np_weight / (np_height ** 2)
np_bmiRound = np.round(np_bmi, 2)

print(np_bmi)
print(np_bmiRound)