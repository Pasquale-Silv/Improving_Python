import numpy as np

list1 = [3, 6, 9, 15]

list2 = [5, 9, 8, 22]

np_list1 = np.array(list1)

np_list2 = np.array(list2)

np_mean_list1 = np.mean(np_list1)

np_mean_list2 = np.mean(np_list2)

print(np_mean_list1)
print("Prova media lista 1: " + str((3+6+9+15) / 4))

print(np_mean_list2)

print("Calcolo mediane:")

np_median_lista1 = np.median(np_list1)

np_median_lista2 = np.median(np_list2)

print(np_median_lista1)
print(np_median_lista2)

print("Calcolo deviazione standard:")

np_std_lista1 = np.std(np_list1)

np_std_lista2 = np.std(np_list2)

print(np_std_lista1)

print(np_std_lista2)
if(np_std_lista1 > np_std_lista2):
    print("La prima lista presenta una variabilità maggiore")
elif(np_std_lista1 < np_std_lista2):
    print("La seconda lista presenta una variabilità maggiore")
elif(np_std_lista1 == np_std_lista2):
    print("Le liste presentano la medesima variabilità")

rho = np.corrcoef(np_list1 , np_list2)
print(rho)

rhoSingolo = rho[0,1]
print("\nCorrelazione tra le due liste: " + str(rhoSingolo))
if(rhoSingolo > 0.6):
    print("La correlazione è abbastanza forte ed è positiva.")
elif(rhoSingoloo > 0.85):
    print("La correlazione è molto forte ed è positiva.")
elif(rhoSingoloho == 0):
    print("Non c'è correlazione lineare tra le lista oppure sussiste un altro tipo di relazione.")
elif(rhoSingoloo < -0.85):
    print("La correlazione è molto forte ed è negativa.")
elif(rhoSingoloo < -0.6):
    print("La correlazione è abbastanza forte ed è negativa.")
else:
    print("Sussiste una debole correlazione.")
