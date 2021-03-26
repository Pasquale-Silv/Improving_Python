# Here, you're going to fire up your very first SQL engine. You'll create an engine to connect to the SQLite database
# >>> engine = create_engine('sqlite:///Northwind.sqlite')
# Here, 'sqlite:///Northwind.sqlite' is called the connection string to the SQLite database Northwind.sqlite.

# Import necessary module
from sqlalchemy import create_engine     # pip install sqlalchemy

# Create engine: engine
engine = create_engine('sqlite:///MIODATABASE.sqlite')   # 'TipoDB:///MioDB.sqlite'

print(engine)

print(engine.table_names())         # Per mostrare i nomi delle tabelle contenute nel DB
