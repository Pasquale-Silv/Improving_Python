"""
You write down some specifiers to help you:
%d(day),
%B (month name),
%m (month number),
%Y(year),
%H (hour)
%M(minutes)
"""

# Import datetime
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()
print(get_date)

# Add named placeholders with format specifiers
# Complete the string message by adding placeholders named today and the format specifiers to format the date as:
# month_name, day, year and time as hour:minutes.
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Format date
print(message.format(today=get_date))

print("{:%d %m %Y}".format(get_date))
print("{:%d-%m-%Y}".format(get_date))
