import os                                                      # os.path.join(...)

filename = 'Pasquale scrive anche nel FileSystem.txt'

with open(filename, mode='w') as fileOp:
    fileOp.write("Caro Pasquale...\n")
    fileOp.write("Sei entrato pure qui adesso...")
    fileOp.write("\nMa bravo...")

