# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///DB3.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Album;")        # Per eseguire la query e vedere tutte le colonne della tabella 'Album'

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())                # Per salvare il risultato della query in un pandas DF  (fetchall() = tutto rs)

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
