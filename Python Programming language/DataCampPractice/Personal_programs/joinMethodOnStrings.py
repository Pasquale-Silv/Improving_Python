names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = 'Hello there ' + name
    print(statement)

print("\nCon il metodo .join:")

for name in names:
    statement = ' '.join(['Hello there', name])
    print(statement)

print()

for name in names:
    statement = ', dear '.join(['Hello there', name])
    print(statement)

print("\nStringa.join([]), dove Stringa fa da separatore fra gli elementi di un 'iterable'")
print(', '.join(names))
print(" -faccio da separatore- ".join(['Pasquale', "Alfonso", "Bruno"]))
print(" ".join('abcdefghilmnopqrstuvz'))
print(".".join("AEIOU"))
print(" separatore ".join(("6", "Marco", "True", "False", "8.5")))             # .join può concatenare solo stringhe !
print("      ".join(("La vita", "è", "bella", ".")))

print("\n\nOra torniamo al metodo .format:")
who = 'Gary'
how_many = 12

print('{} bought {} apples today!'.format(who, how_many))