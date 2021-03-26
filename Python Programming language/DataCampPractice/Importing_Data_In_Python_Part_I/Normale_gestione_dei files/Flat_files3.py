filename = 'Pasquale_primo_file.txt'

file_open = open(filename, mode='w')

print(file_open.closed)

file_open.write("Ciao Pasquale, complimenti per aver scritto il tuo primo file!")
file_open.write("\nTi senti fiero adesso? bravo!")

file_open.close()

print(file_open.closed)

with open(filename, mode='r') as fileOp:
    print(fileOp.read())
    print("\nInvece, per leggere una sola riga alla volta:")
    print(fileOp.readline())    # Ricorda che è un iterator, le ha esaurite!

# Con il context manager (with) non devi chiudere il file!