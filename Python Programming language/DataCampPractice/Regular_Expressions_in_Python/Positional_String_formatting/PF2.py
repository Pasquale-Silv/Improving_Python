# For accessing elements in a dictionary when using the str.format() method,
# you need to use dict[index] without using quotes for index.
# The method converts it automatically to the string "index" when it is looked up in the dict.

courses = ['artificial intelligence', 'neural networks']
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys
my_message = "If you are interested in {dictionary[field]}, you can take the course related to {dictionary[tool]}"

# Use dictionary to replace placehoders
print(my_message.format(dictionary=plan))
