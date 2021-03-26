# Solo file di prova

import pandas as pd
import numpy as np

# Assign the filename: file
file = 'digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)
# nrows per decidere le righe del file da importare, in questo caso si importano solo le prime 5 righe
# header=None per dire a PY che il DF non ha header

# Build a numpy array from the DataFrame: data_array
data_array= data.values     # Trasforma il DF in numpy array

# Print the datatype of data_array to the shell
print(type(data_array))
