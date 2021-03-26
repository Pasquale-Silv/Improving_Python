class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof woof!")

class LittleDog(Dog):
    def bark(self):
        print("I'm a little dog\n"
              "Woof woof!")

dog1 = Dog("Rex Big Dalton", 3)

dog2 = LittleDog("Maggie", 2)

print(dog1.name)
dog1.bark()

print(f"\n{dog2.name}")
dog2.bark()
