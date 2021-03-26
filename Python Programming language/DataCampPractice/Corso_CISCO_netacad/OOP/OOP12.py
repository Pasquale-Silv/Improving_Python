class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

print("--------------------------")

class Classy:
    pass

print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

print("--------------------------------")

class Classy:
    pass

print(Classy.__module__)
obj = Classy()
print(obj.__module__)
