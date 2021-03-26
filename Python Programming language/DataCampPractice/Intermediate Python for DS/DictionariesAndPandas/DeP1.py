# To see why dictionaries are useful, have a look at the two lists defined on the right.
# countries contains the names of some European countries.
# capitals lists the corresponding names of their capital.

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")
print(ind_ger)

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Same result with a dictionary:

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', 'france':'paris', "germany":'berlin','norway':'oslo'}

# Print europe
print(europe)

print(europe["germany"])

# Print out the keys in europe
print(europe.keys())           # Per printare le chiavi del dict
print(europe.values())         # Per printare i valori del dict

# Print out value that belongs to key 'norway'
print(europe["norway"])