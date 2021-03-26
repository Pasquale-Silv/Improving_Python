def mediaFunction(*args):        # args può chiamarsi anche pippo: è una tupla con quel nome!
    print(args)
    print(type(args))
    sum = 0
    media = 0

    for i in args:
        sum += i

    media = sum / len(args)

    print("La somma dei numeri è:", sum)
    print(f"La media dei valori inseriti è: { media }")

mediaFunction(3, 3, 3)
print()
mediaFunction(4, 5, 9, 80, 54)

print("----------------------------------------------------------")

def print_all(**kwargs):          # kwargs è un dizionario
    print(type(kwargs))
    for k, v in kwargs.items():       # key:value
        print(k + ": " + v)

print_all(nome="Pasquale", mestiere="Data Scientist", years="23")

def print_all_due(**pippo):        # Adesso il dict è pippo(kwargs)
    print(type(pippo))
    print(pippo)
    print(pippo.items())        # il metodo .items() su un dict restituisce le tuple corrispondenti ai key:value pairs
    for key, value in pippo.items():
        print(key + ": " + value)

print("--------------- pippo: --------------------------------------")
print_all_due(film="Guerre stellari", incassi="300000")