"""
To check if an item is in a list,
the in operator can be used.
It returns True if the item occurs one or more times in the list, and False if it doesn't.
The in operator is also used to determine whether or not a string is a substring of another string.
"""

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("Spam" in words)
print("egg" in words)
print("tomato" in words)
print("tomato" not in words)

print("--------------------------")

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])

print("-----------------------------------")

# not in
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)