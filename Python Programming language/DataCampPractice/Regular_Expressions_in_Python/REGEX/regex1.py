sentiment_analysis = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'

# Import the re module
import re

# Write the regex
regex = re.findall(r"\Wrobot\d\W", sentiment_analysis)

# Find all matches of regex
print(regex)

print("-------------------------")

# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))
