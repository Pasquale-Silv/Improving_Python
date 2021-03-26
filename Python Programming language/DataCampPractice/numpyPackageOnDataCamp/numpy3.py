import numpy as np

arraySoloUnTipoConNumpy = [1.1, 2, True, "Pasquale"]
np_arraySoloUnTipoConNumpy = np.array(arraySoloUnTipoConNumpy)   # L'array in numpy può contenere elementi solo dello stesso tipo!

print(arraySoloUnTipoConNumpy)

print(np_arraySoloUnTipoConNumpy)       # numpy automaticamente trasforma tutti i tipi in stringhe