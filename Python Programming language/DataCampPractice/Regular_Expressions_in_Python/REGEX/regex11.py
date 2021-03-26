"""
Let's imagine that you want to extract the number contained in the sentence I was born on April 24th.
A lazy quantifier will make the regex return 2 and 4, because they will match as few characters as needed.
However, a greedy quantifier will return the entire 24 due to its need to match as much as possible.
"""

import re

sentiment_analysis = 'Was intending to finish editing my 536-page novel manuscript tonight, ' \
                    'but that will probably not happen. And only 12 pages are left '
print(sentiment_analysis)

# Use a lazy quantifier to match all numbers that appear in the variable sentiment_analysis.
# Write a lazy regex expression
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

print("-----------------------------------------------")

# Now, use a greedy quantifier to match all numbers that appear in the variable sentiment_analysis.
# Write a greedy regex expression
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)
