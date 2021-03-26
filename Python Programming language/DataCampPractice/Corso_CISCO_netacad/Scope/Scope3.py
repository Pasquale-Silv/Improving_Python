"""
Hopefully, you should now have arrived at the following question:
does this mean that a function is not able to modify a variable defined outside it?
This would create a lot of discomfort.

Fortunately, the answer is no.

There's a special Python method which can extend a variable's scope in a way which includes the functions' bodies
(even if you want not only to read the values, but also to modify them).

Such an effect is caused by a keyword named global
global name
global name1, name2, ...
"""

def myFunction():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)
