#!/usr/bin/env python
# NondescriptBot
# by John Shutt (http://shutt.in)

import sys
import cmd
import json
import textwrap
from olapi import OpenLibrary
# secrets.py holds the login password, and is excluded from version control
from secrets import password

ol = OpenLibrary()

# Log in.
logged_in = False
print 'Trying to log in...'
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

# Define a command interpreter class, to get user input.
class NondescriptCmd(cmd.Cmd):
  prompt = '> '

  def do_exit(self, line):
    return True

  def do_get_by_olid(self, olid):
    work = ol.get("/works/" + olid)
    title = work["title"]
    print "Title:"
    print "\"" + title + "\""
    print "Author(s):"
    if work.has_key("authors"):
      authors = work["authors"]
      print authors
    elif work.has_key("author"):
      authors = work["author"]
      print authors
    else:
      print "No author for this work!"
    print "Description:"
    if work.has_key("description"):
      description = work["description"]
      print textwrap.fill(description)
    else:
      print "No description for this work!"

  def do_get_by_title(self, title):
    work = ol.query({"type": "/type/work", "title": title})
    for key in work:
      print key 


# Start the command interpreter up.
NondescriptCmd().cmdloop()

# Search Open Library for a book by name, and display its description, 
# or lack of description. Ask the user if they want to edit the 
# description.




# Search Wikipedia for the same book, and copy the first paragraph of the 
# Wikipedia article.




# Format the paragraph for Open Library by converting it to Markdown, 
# removing footnote indicators, and adding CC license information.





# Display the formatted description, and ask the user to confirm that it 
# is correct, and that they want to save it. If they answer yes, save the 
# updated description to Open Library.


