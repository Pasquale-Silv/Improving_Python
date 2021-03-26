from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///DB4.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:                 # come con file non hai bisogno di chiudere la connessione in questo modo.
    rs = con.execute('SELECT LastName, Title FROM Employee;')
    df = pd.DataFrame(rs.fetchmany(size=3))   # fetchmany(size=3) considere aolamente le prime 3 righe, fetchall() considera tutto.
    df.columns = rs.keys()                    # Va a settore il nome delle colonne del DF, altrimenti solo indici.

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())
