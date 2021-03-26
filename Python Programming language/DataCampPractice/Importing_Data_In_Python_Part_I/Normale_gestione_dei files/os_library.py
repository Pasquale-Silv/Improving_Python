import os

wd = os.getcwd()
print()
print(wd)           # Mostra il path della current working directory

files_in_wd = os.listdir(wd)      # Mostra i files e le folders contenute nella cartella specificata.
print(files_in_wd)
