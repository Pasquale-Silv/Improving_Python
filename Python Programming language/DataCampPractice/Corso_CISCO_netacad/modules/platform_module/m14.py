# If you need to know what version of Python is running your code,
# you can check it using a number of dedicated functions - here are two of them:

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():       # major.minor.patch
    print(atr)

print(python_version_tuple())

version_p = [letter + "." for letter in python_version_tuple()]
print(version_p)
version_p = "".join(version_p).strip(".")
print(version_p)
