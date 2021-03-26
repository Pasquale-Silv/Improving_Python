# .csv and .txt are two examples of flat files!

# Open a file: file
file = open('moby_dick.txt', mode='r')       # read-only mode 'r'

# Print it
print(file.read())            # .read() shows all the file                   .readline() shows just a line of the file.

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
