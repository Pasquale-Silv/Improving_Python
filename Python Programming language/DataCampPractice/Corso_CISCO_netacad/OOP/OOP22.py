"""
We can say that Python looks for object components in the following order:

1- inside the object itself;
2- in its superclasses, from bottom to top;
3- if there is more than one class on a particular inheritance path, Python scans them from left to right.
"""

class Left:
    var = "L"
    varLeft = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    varRight = "RR"
    def fun(self):
        return "Right"

# Multiple inheritance, prima più importante per l'override.
class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.varLeft, obj.varRight, obj.fun())
