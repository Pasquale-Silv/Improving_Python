import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///DB7.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000;', engine)

# Print head of DataFrame
print(df.head())
