# Questo è solo un file di esempio, non importa nulla con pandas

# we can easily import files of mixed data types as DataFrames using the pandas functions:
# read_csv()
# and
# read_table()

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())             # To see the first 5 rows of the 'df' DataFrame
