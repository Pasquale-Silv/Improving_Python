# The DataFrame is one of Pandas' most important data structures.
# It's basically a way to store tabular data where you can label the rows and the columns.
# One way to build a DataFrame is from a dictionary.
# In the exercises that follow you will be working with vehicle data from different countries.
# Each observation corresponds to a country and the columns give information about the number of vehicles per capita,
# whether people drive left or right, and so on.

# Each dictionary key is a column label and each value is a list which contains the column elements.

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country':names,
    "drives_right":dr,
    "cars_per_cap":cpc
}

print('Dizionario:')
print(my_dict)

print("\nOra trasformiamo il dizionario in DataFrame con pandas")
print('DataFrame:\n')

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

print('\nQuesto processo genera un DataFrame a partire da un dizionario, manualmente...')
print("Se sussiste la necessità di lavorare con 'tons of data', è molto più conveniente generare un DataFrame a partire da fonti terze leggendo un file .csv")

print('\nVuoi cambiare gli index del DataFrame?')
risposta = input('Rispondi si oppure no... o s/n\n').lower()
print(risposta)

if (risposta == 'si' or risposta == 's'):
    cars.index = ['USA', 'AUS', 'JAP', 'IND', "RUS", 'MOR', 'EGY']
    print(cars)
