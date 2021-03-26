# Python's strings are immutable. This is a very important feature.

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

print("-----------------------------")

name = "Pasquale"

print(name[::-1])
print(name[::2])
print(name[2:10:2])
