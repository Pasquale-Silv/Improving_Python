"""
The insert method is similar to append,
except that it allows you to insert a new item at any position in the list,
as opposed to just at the end.
"""

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
words.insert(0, "Sentence:")
print(words)

print("---------------------------")

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))
print(nums)