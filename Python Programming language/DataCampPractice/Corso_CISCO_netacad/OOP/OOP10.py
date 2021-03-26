# Don't forget that the hasattr() function can operate on classes, too.
# You can use it to find out if a class variable is available, just like here in the example in the editor.
# The function returns True if the specified class contains a given attribute, and False otherwise.

class ExampleClass:
    attr = 1

print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

print("------------------------")

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2

exampleObject = ExampleClass()

print(hasattr(exampleObject, 'b'))
print(hasattr(exampleObject, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))
