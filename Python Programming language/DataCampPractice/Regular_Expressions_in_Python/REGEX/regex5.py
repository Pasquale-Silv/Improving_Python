import re

sentiment_analysis = 'ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever'
print(sentiment_analysis)

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)
print(no_hashtag)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))
