# * unpacks an iterable such as a list or a tuple into positional arguments in a function call.
# you will use * in a call to zip() to unpack the tuples produced by zip().

mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
powers = ['telepathy',
 'thermokinesis',
 'teleportation',
 'magnetokinesis',
 'intangibility']

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)

print("--------------------------------------------\nPuoi anche unpacking liste o stringhe: (*string o *list)")

stringa1 = "Pasquale"
lista1 = ["Pasquale", "Bruno", "Alfonso"]
print(*stringa1)
print(*lista1)