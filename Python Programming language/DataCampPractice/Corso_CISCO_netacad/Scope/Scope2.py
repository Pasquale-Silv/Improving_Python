def myFunction():
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

"""
A variable existing outside a function has a scope inside the functions' bodies, 
excluding those of them which define a variable of the same name.

It also means that the scope of a variable existing outside a function is supported only when getting its value(reading)
Assigning a value forces the creation of the function's own variable.
"""
