# Note: the situation in which the subclass is able to modify its superclass behavior
# (just like in the example) is called polymorphism.

class One:
    def doit(self):
        print("doit from One")

    def doanything(self):
        self.doit()

class Two(One):
    def doit(self):                     # OVERRIDE - POLIMORFISMO
        print("doit from Two")

one = One()
two = Two()

one.doanything()
two.doanything()
