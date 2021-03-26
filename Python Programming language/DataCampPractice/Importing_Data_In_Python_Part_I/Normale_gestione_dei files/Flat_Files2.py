# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    print(file.readline())                # .readline() shows just one line.
    print(file.readline())
    print(file.readline())

# if you use with ... you don't have to close the file !
