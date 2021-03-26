"""
Multiple inheritance
occurs when a class has more than one superclass.

Syntactically, such inheritance is presented as a comma-separated list of superclasses put inside parentheses
after the new class name - just like here:
"""

class SuperA:
    varA = 10
    def funA(self):
        return 11

class SuperB:
    varB = 20
    def funB(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.varA, obj.funA())
print(obj.varB, obj.funB())

# The Sub class has two superclasses:
# SuperA and SuperB. This means that the Sub class inherits all the goods offered by both SuperA and SuperB.
