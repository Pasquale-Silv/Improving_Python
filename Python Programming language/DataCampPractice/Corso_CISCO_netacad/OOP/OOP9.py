class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

# Python provides a function which is able to safely check if any object/class contains a specified property.
# The function is named hasattr, and expects two arguments to be passed to it:
# the class or the object being checked;
# the name of the property whose existence has to be reported
# (note: it has to be a string containing the attribute name, not the name alone)

if hasattr(exampleObject, 'b'):
    print(exampleObject.b)

print(hasattr(exampleObject, 'b'))
