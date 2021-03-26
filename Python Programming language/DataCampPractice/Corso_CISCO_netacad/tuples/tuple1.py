tuple1 = (1, 2, 4, 8)
tuple2 = 1., .5, .25, .125
print(tuple1)
print(tuple2)
print(type(tuple1))
print(type(tuple2))

emptyTuple = ()
print(emptyTuple)
print(type(emptyTuple))

# If you want to create a one-element tuple,
# you have to take into consideration the fact that, due to syntax reasons
# (a tuple has to be distinguishable from an ordinary, single value), you must end the value with a comma:

print("\nTuple di un solo elemento:")
oneElementTuple1 = (1, )
oneElementTuple2 = 1.,
print(oneElementTuple1)
print(oneElementTuple2)
print(type(oneElementTuple1))
print(type(oneElementTuple2))
print(len(oneElementTuple1))
print(len(oneElementTuple2))

oneElementTuple3 = 5,
print(oneElementTuple3)
print(type(oneElementTuple3))
