# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda stringa: len(stringa) > 6, fellowship)

# Convert result to a list: result_list
print(result)
result_list = list(result)

# Print result_list
print(result_list)