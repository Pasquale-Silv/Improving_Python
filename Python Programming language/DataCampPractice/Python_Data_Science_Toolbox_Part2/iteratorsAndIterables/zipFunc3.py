# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

nomi = ['Pasquale', 'Alfonso', 'Bruno', 'Mario']
punti = [130, 98, 23, 69]

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(nomi, punti)

# Print rs_fxn
print(rs_fxn)

print("-------------------------------\nConferma:")
tupla1 = 'Pasquale', 'Alfonso', 'Bruno', 'Mario'
tupla2 = 130, 98, 23, 69
print(tupla1)
print(tupla2)
print(f"Tipo tupla1: { type(tupla1) }, tipo tupla2: { type(tupla2) }")
# Ora trasformiamolo in dict dove {tupla1:tupla2}
tupleZip = zip(tupla1, tupla2)
print(tupleZip)
print(type(tupleZip))
print(list(tupleZip))
print(type(tupleZip))
print("Con for loop: ")

for t1, t2 in zip(tupla1, tupla2):
    print("Valore prima tupla: ", t1, ",valore seconda tupla:", t2)

dict_tuplaZip = dict(tupleZip)
print(dict_tuplaZip)                 # Ricorda che un iterator esaurisce gli elementi una volta stampati!
tupleZip = zip(tupla1, tupla2)       # Cosi ti tocca ricomporlo
dict_tuplaZip = dict(tupleZip)
print(dict_tuplaZip)