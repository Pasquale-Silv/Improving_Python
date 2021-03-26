# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)

listaNum = [3, 5, 2, 10]
somma = reduce(lambda x, y: x + y, listaNum)    # Printa la somma di tutti i numeri della lista
print(somma)