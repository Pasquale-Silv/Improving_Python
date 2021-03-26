stringa1 = "Pasquale"

for lettera in stringa1:
    print(lettera)

stringa1Splittata = stringa1.split()                              # split sep=" "

print(stringa1Splittata)

stringa1SplittataNonDefault = stringa1.split(sep=' ')             # same as previous

print(stringa1SplittataNonDefault)

print("\nPer splittare la stringa:")
print([lettera for lettera in stringa1])

print("----------------")

parola_splittata2 = list("Mangio la mela")
print(parola_splittata2)

join1 = "".join(parola_splittata2)
print(join1)

print("------------------")

sentence = "Pasquale è qui!"
splitSentence = list(sentence)
print(splitSentence)
ricomponi = ''.join(splitSentence)
print(ricomponi)
