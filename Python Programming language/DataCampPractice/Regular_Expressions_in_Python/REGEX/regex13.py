"""
You want to extract the first part of the email. E.g. if you have the email marysmith90@gmail.com,
you are only interested in marysmith90.
You need to match the entire expression. So you make sure to extract only names present in emails.
Also, you are only interested in names containing upper (e.g. A,B, Z) or lowercase letters (e.g. a, d, z) and numbers.
"""

import re

sentiment_analysis = ['Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. '
                      'They have amazing prices',
                      'I should have paid more attention when we covered photoshop '
                      'in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.',
                      'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com'
                      ]

# Write a regex that matches email
regex_email = r"([a-zA-Z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))