#!/usr/bin/env python
# NondescriptBot
# by John Shutt (http://shutt.in)

import sys
from olapi import OpenLibrary
# secrets.py holds the login password, and is excluded from version control
from secrets import password

ol = OpenLibrary()

# Log in.
logged_in = False
for attempt in range(5):
    try:
        ol.login('nondescriptbot', password)
        logged_in = True
        print 'Login successful.'
        break
    except:
        print 'ol.login() error; retrying'
if not logged_in:
    sys.exit('Failed to log in.')

# Search Open Library for a particular book, and display its description, 
# or lack of description. Ask the user if they want to edit the 
# description.




# Search Wikipedia for the same book, and copy the first paragraph of the 
# Wikipedia article.




# Format the paragraph for Open Library by converting it to Markdown, 
# removing footnote indicators, and adding CC license information.





# Display the formatted description, and ask the user to confirm that it 
# is correct, and that they want to save it. If they answer yes, save the 
# updated description to Open Library.


