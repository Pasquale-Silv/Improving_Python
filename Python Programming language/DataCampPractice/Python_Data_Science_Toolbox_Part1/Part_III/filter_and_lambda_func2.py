listaNomi = ['Pasquale', 'Passandro', 'Bruno', 'Alfonso', 'Lucas', 'Passariello', 'Gennaro', 'Alberto', 'Anastasia', 'Antonio']

# Controlla quali nomi iniziano per 'Pa' e crea una lista ad hoc

nomiPa = filter((lambda nome: nome[0:2] == 'Pa'), listaNomi)
print(nomiPa)
nomiPaList = list(nomiPa)

print(nomiPaList)

print('-------------------------------------------------')

# Adesso controlla quali nomi iniziano per 'A'
nomiA = filter((lambda name: name[0] == 'A'), listaNomi)
print(nomiA)
nomiA_list = list(nomiA)
print(nomiA_list)