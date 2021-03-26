def myFunction(myList1):
    print(myList1)
    myList1 = [0, 1]          # La lista passata come argomento non ne risentirà.

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

print("-------------------------------")

def myFunction(myList1):
    print(myList1)
    del myList1[0]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)

"""
1. if the argument is a list, then changing the value of the corresponding parameter doesn't affect the list 
   (remember: variables containing lists are stored in a different way than scalars)

2. but if you change a list identified by the parameter 
   (note: the list, not the parameter!), the list will reflect the change.

"""