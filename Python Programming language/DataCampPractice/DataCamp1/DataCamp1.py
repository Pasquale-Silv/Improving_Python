# Calcolo interesse a 7 anni
montanteSetteAnni = 100 * (1 + 0.10)**7   # Regime di capitalizzazione esponenziale
# 100 * 1.1 ** 7

print(montanteSetteAnni)

print()

if (montanteSetteAnni > 200):
    print("Il montante è maggiore di 200, ottimo investimento")
else:
    print("Il montante è minore del criterio soglia fissato a 200, esso è pari a " + str(montanteSetteAnni))

print("\nCalcolo terminato.")

print("\nFacciamo lo stesso calcolo utilizzando le variabili: ")
savings = 100
fattoreMontante = (1+0.1)
result = savings * fattoreMontante**7

print(result)