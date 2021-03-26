"""
If you want to extract a word starting with a and ending with e in the string I like apple pie,
you may think that applying the greedy regex a.+e will return apple. However, your match will be apple pie.
A way to overcome this is to make it lazy by using ? which will return apple.
"""

import re

sentiment_analysis = "Put vacation photos online (They were so cute) a few yrs ago. " \
                     "PC crashed, and now I forget the name of the site (I'm crying). "
print(sentiment_analysis)

# Use a greedy quantifier to match text that appears within parentheses in the variable sentiment_analysis.
# Write a greedy regex expression to match
sentences_found_greedy = re.findall(r"\(.*\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

print("-------------------------------------")

# Now, use a lazy quantifier to match text that appears within parentheses in the variable sentiment_analysis.
# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)

"""
Well done! Notice that using greedy quantifiers always leads to longer matches that sometimes are not desired. 
Making quantifiers lazy by adding ? to match a shorter pattern is a very important consideration to keep in mind 
when handling data for text mining. Cool!
"""
