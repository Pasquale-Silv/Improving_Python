import re

risp = input("Insert:\n")

print(re.search(r"[a-zA-Z]+\d{2,3}", risp))
print(re.match(r"[a-zA-Z]+\d{2,3}", risp))

if re.search(r"[a-zA-Z]+\d{2,3}", risp):
    print("re.search riempito")

if re.match(r"[a-zA-Z]+\d{2,3}", risp):
    print("re.match riempito!")
