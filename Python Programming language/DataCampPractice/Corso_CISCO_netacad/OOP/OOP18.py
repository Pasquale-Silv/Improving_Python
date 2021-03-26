class SuperClass1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(SuperClass1):
    def __init__(self, name):
        SuperClass1.__init__(self, name)


obj = Sub("Andy")

print(obj)

print("-----------------------------------")

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)

print("-----------------------")

# Testing properties: class variables
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()

print(obj.subVar)
print(obj.supVar)

print("-------------------------------")

# Testing properties: instance variables
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()

print(obj.subVar)
print(obj.supVar)
