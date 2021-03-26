# Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25
# Complete the for loop with a regex to find dates
# Complete the for loop with a regex to find dates
import re

# Crea date adeguate se vuoi usarlo.

for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w{2}\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))
