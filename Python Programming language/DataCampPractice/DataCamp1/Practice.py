# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

rendimento = result - savings
rateOfYield = (rendimento / savings) * 100
rateOfYield = str(rateOfYield) + "%"

print("\nHai guadagnato " + str(rendimento))
print("ciò  corrisponde a un tasso di rendimento pari a "+ rateOfYield + " in sette anni")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
print()
print(pi_float)

print("\nI said " + ("Hey " * 2) + "Hey!")  # una stringa * 2 restituisce due volte la stessa stringa