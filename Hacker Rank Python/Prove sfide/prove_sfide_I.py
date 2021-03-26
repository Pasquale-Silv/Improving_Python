def diverseDeputation(m, w):
    if (m == 0 or w == 0):
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
    for i in range(0, len(listM), 2):
        for woman in listW:
            listaNew.append([listM[i], listM[i + 1], woman])
    return listaNew


diverseDeputation(3, 0)
diverseDeputation(2, 2)
