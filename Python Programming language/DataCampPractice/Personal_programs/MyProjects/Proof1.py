print("Questo è un programma che stampa una tabellina di un numero scelto dall'utente")

num = int(input("Scegli il numero:\n"))

for i in range(0, 11):
    print(num * i)

bool = True
list1 = []

while bool:
    risposta = input("Vuoi vederlo anche in linea retta? (risposte consentite: s/n)\n")
    risposta = risposta.lower()

    if (risposta == "s" or risposta == "si"):
        for i in range(0, 11):
            list1.append(i * num)
        print(list1)
        bool = False
    elif (risposta == "n" or risposta == "no"):
        bool = False
    else:
        print("Non hai inserito nessuna tra le due risposte contemplate, riprova.")


print("\nProgramma terminato.")