def diverseDeputation(m, w):
    if (m == 0 or w == 0 or (m == 1 and w==1)):
        return 0
    listM = ["m{}".format(i) for i in range(1, m + 1)]
    listW = ["w{}".format(i) for i in range(1, w + 1)]
    listaNew = mAggingi(listM, listW)
    listaNew2 = mAggingi(listW, listM)
    print(listaNew)
    print(listaNew2)
    listaNew.extend(listaNew2)
    listaNew.sort()
    listaResult = [sorted(lista) for lista in listaNew]
    print(listaNew)
    print(listaResult)
    listaFinal = []
    listaUsed = []
    for element in listaResult:
        if(element not in listaUsed):
            listaFinal.append(element)
            listaUsed.append(element)

    return len(listaFinal)

def mAggingi(listM, listW):
    listaNew = []
    for i in range(0, len(listM)):
        for j in range(i, len(listM)):                                            # ottimizzato range da i, non da zero
            if(i != j):
                for woman in listW:
                    listaNew.append([listM[i], listM[j], woman])
    return listaNew

esito1 = diverseDeputation(3, 0)
esito2 = diverseDeputation(2, 2)
esito3 = diverseDeputation(1, 1)
esito4 = diverseDeputation(3, 9)    # 135
esito5 = diverseDeputation(1, 3)
esito6 = diverseDeputation(3, 1)
esito7 = diverseDeputation(9, 3)

print("\nTest cases esiti:")
print(esito1)
print(esito2)
print(esito3)
print(esito4)
print(esito5)
print(esito6)
print(esito7)
