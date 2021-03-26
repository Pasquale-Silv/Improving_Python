import re

risp = input("Inserisci:\n")

print(re.findall(r"[0-5]", risp))
print(re.findall(r"[0-5]{2,3}", risp))

if re.findall(r"[0-5]{2,3}", risp):
    print("riempita")

