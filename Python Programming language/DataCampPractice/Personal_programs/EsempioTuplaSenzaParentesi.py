# Se creiamo una lista di valori senza specificare [] o (), Python lo trasforma in (tupla) !

programming_languages = "Python", "Java", "C++", "C#"

print(type(programming_languages))
print(programming_languages)

print("\nCon il for loop:")
for language in programming_languages:
    print(language)

