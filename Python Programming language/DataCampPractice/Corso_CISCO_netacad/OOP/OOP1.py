# When any class component has a name starting with two underscores (__),
# it becomes private - this means that it can be accessed only from within the class.
# You cannot see it from the outside world. This is how Python implements the encapsulation concept.

class Stack:
    def __init__(self):
        self.__stackList = []

stackObject = Stack()
print(len(stackObject.__stackList))
