# Import template
from string import Template

answers = {'answer1': 'I really like the app. But there are some features that can be improved'}

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use .substitute() to replace identifiers
try:
    print(the_answers.substitute(answers))
except KeyError:
    print("Missing information")


# Use .safe_substitute() to replace identifiers
try:
    print(the_answers.safe_substitute(answers))                      # Restituisce in ogni caso una stringa.
except KeyError:
    print("Missing information")
