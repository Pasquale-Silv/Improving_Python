# La funzione input(...) restituisce un tipo stringa, anche se viene passato un numero int o float
# Puoi rappresentare una stringa concatenata in diversi modi:
# 1- Concatenandola con + e convertendo i numeri con str()  ----> 'numero: ' + str(3.6)
# 2- Utilizzando la virgola( , ) come separatore tra stringhe e numeri o altre stringhe: 'numero' , ':' , 5
# 3- Mediante Formatted-String Literal ---->   f"Il numero è { 5 }"

print('numero: ' + str(3.6))

print('numero', ':', 5)

print(f"Il numero è { 5 }")
print(f"numero uno: { 10 }, numero2: { 22 }, loro somma: { 10 + 22 } \n")

prova = input('Inserisci qualcosa: \n')

print(f"Hai inserito '{ prova }', complimenti!'")