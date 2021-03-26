x = 20

assert x >= 10          # Se True non succede nulla e vai avanti, altrimenti lancia l'assertion error

stringa1 = "Hai passato l'assert!" if x >= 10 else "Spiacente."
print(stringa1)
