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

# Search Wikipedia for book entries, excluding books that have already 
# been crawled, copy the first paragraph from the description of each 
# book, and convert the text to the correct format for Open Library.





# Search Open Library for each of the books from the Wikipedia crawl, 
# check if they have descriptions, and add the descriptions from Wikipedia 
# if they don't.





# Save all of the new book descriptions.


