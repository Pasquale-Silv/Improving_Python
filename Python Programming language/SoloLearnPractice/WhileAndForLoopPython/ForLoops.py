words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter += 1

print("\nSame:\n")
for w in words:            # Like foreach in java
   print(w + "!")

print("-----------------------")

for i in range(5):
   print("hello!")

print("-----------------------")

for i in range(0,20,2):         # Only even numbers
    print(i)
