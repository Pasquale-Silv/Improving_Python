def diverseDeputation(m, w):
    if (m == 0 or w == 0 or (m == 1 and w==1)):
        return 0
    listM = ["m{}".format(i) for i in range(1, m + 1)]
    listW = ["w{}".format(i) for i in range(1, w + 1)]
    listaNew = mAggingi(listM, listW)
    listaNew2 = mAggingi(listW, listM)
    return len(listaNew) + len(listaNew2)

def mAggingi(listM, listW):
    listaNew = []
    for i in range(0, len(listM), 2):
        for woman in listW:
            listaNew.append([listM[i], listM[i + 1], woman])
    return listaNew

esito1 = diverseDeputation(3, 0)
esito2 = diverseDeputation(2, 2)
esito3 = diverseDeputation(1, 1)
# esito4 = diverseDeputation(3, 9)    # 135

print(esito1)
print(esito2)
print(esito3)
# print(esito4)
