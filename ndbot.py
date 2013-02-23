#!/usr/bin/env python
# NondescriptBot
# by John Shutt (http://shutt.in)

import sys
from olapi import OpenLibrary
# secrets.py holds the login info, and is excluded from version control
from secrets import login_name, password

ol = OpenLibrary()

# Log in.
logged_in = False
print 'Trying to log in...'
for attempt in range(5):
    try:
        ol.login(login_name, password)
        logged_in = True
        print 'Login successful.'
        break
    except:
        print 'ol.login() error; retrying'
if not logged_in:
    sys.exit('Failed to log in.')
