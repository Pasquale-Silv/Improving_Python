def diverseDeputation(m, w):
    if (m == 0 or w == 0 or (m == 1 and w==1)):
        return 0

    listM = ["m{}".format(i) for i in range(1, m + 1)]
    listW = ["w{}".format(i) for i in range(1, w + 1)]

    print(listM)
    print(listW)

    listaNew = mAggingi(listM, listW)
    print(listaNew)

    listaNew2 = mAggingi(listW, listM)
    print(listaNew2)

    return len(listaNew) + len(listaNew2)

def mAggingi(listM, listW):
    listaNew = []
    if(len(listM) % 2 == 0):
        for i in range(0, len(listM), 2):
            for woman in listW:
                listaNew.append([listM[i], listM[i + 1], woman])
    elif(len(listM) % 2 != 0):
        for i in range(0, len(listM), 2):
            for woman in listW:
                try:
                    listaNew.append([listM[i], listM[i + 1], woman])
                except:
                    continue

    return listaNew


esito1 = diverseDeputation(3, 0)
esito2 = diverseDeputation(2, 2)
esito3 = diverseDeputation(3, 9)    # 135

print(esito1)
print(esito2)
print(esito3)
