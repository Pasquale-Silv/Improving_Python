weight = input("Insert your weight to calculate your BMI:(definiscilo in kg, es: 80)")
height = input("Insert your height to calculate your BMI:(definiscilo in metri, es: 1.85)")

print("Tipo dato della variabile weight:")
print(type(weight))    # Input restituisce sempre un tipo stringa...Bisogna convertirlo per effettuare operazioni matematiche!

print("Tipo dato della variabile height:")
print(type(height))    # Input restituisce sempre un tipo stringa...Bisogna convertirlo per effettuare operazioni matematiche!

print("Di seguito trova il suo BMI:")
BMI = int(weight) / (float(height)**2)
print(BMI)

print("\nIl suo BMI è pari a " + str(BMI) + "\n")

print("---------------------------------------------------")

print("\nAltro BMI: (Ovviamente il metodo di calcolo cambia)")
weight = int(input("Insert your weight to calculate your BMI:(definiscilo in kg, es: 80)"))
height = float(input("Insert your height to calculate your BMI:(definiscilo in metri, es: 1.85)"))

print("Tipo dato della variabile weight:")
print(type(weight))    # Input restituisce sempre un tipo stringa...Bisogna convertirlo per effettuare operazioni matematiche!

print("Tipo dato della variabile height:")
print(type(height))    # Input restituisce sempre un tipo stringa...Bisogna convertirlo per effettuare operazioni matematiche!

BMI = weight / height**2

print(BMI)

print("\nIl suo BMI è pari a " + str(BMI))