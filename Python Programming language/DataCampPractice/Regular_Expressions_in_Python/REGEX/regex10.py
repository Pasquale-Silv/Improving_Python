"""
Remember that a greedy quantifier will try to match as much as possible while a non-greedy quantifier
will do it as few times as needed, expanding one character at a time and giving us the match we are looking for.
"""

# Import re
import re

string1 = 'I want to see that <strong>amazing show</strong> again!'

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string1)

print(string1)
# Print out the result
print(string_notags)