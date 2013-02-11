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
        print 'login successful'
        break
    except:
        print 'ol.login() error; retrying'
if not logged_in:
    sys.exit('Failed to log in.')

# Search Open Library for books that don't have descriptions yet.



# Search Wikipedia to find out which books in the list have entries.



# For the books that have Wikipedia entries, take the first paragraph of 
# the entry and make that their Open Library description.



# Save all of the new book descriptions.



