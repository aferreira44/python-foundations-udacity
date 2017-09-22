""" Search for curse words in a txt file """

import urllib

def read_text():
    """ Read the quotes from a txt file. """
    quotes = open("C:\Users\User\Documents\localdev\python-foundations-udacity\movie_quotes.txt")
    contents = quotes.read()
    #print contents
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    """ Search on a Google service for curse words """
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    #print output
    connection.close()
    if "true" in output:
        print "Profanity Alert!!"
    elif "false" in output:
        print "This document has no curse words!"
    else:
        print "Could not scan the document properly."

read_text()
