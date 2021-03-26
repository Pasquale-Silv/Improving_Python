import re

sentiment_analysis = 'He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready'

# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
# Replace regex_sentence with a space " " in the variable sentiment_analysis. Assign it to sentiment_sub
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)
print(sentiment_sub)

# Write a regex that matches the pattern separating the words in sentiment_analysis, e.g. #newH
# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, ' ', sentiment_sub)
print(sentiment_final)
