#Questo è un generico metodo per importare un file come pandas DataFrame. Sostituisci il file se vuoi farlo funzionare.

# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# .info() restituisce informazioni molto dettagliate sul DataFrame.
print(df.info())
