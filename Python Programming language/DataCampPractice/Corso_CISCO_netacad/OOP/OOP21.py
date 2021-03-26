class Level1:
    var = 100
    def fun(self):
        return 101

class Level2:
    var = 200                    # OVERRIDING
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()

print(obj.var, obj.fun())

# The entity defined later (in the inheritance sense) overrides the same entity defined earlier.
# We can also say that Python looks for an entity from bottom to top,
# and is fully satisfied with the first entity of the desired name.
