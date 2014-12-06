#!/usr/bin/python
'''
By: Ben Weiss. Justin Lim. Anmol Raina
This file has been adapted from psycopg2-demo.py
from Jeff Ondich, 7 October 2013

    This is the python script for our main web page. This is a relatively 
    simple program as it really just prints out our home page and connects
    to our web page's other features.
'''

# This part imports my database name, user name, host name, and
# especially my password from a file that Python is allowed to import,
# but that Apache is not allowed to access. So even though readers of
# this code could find my password if they were logged into my account,
# they can't do so via the web.
import sys
import psycopg2
import cgi
import cgitb
from datasource import DataSource
cgitb.enable()

def printPageAsHTML(templateFileName):
    '''
    This function takes in an html file as a file
    nd prints out a main template of our web page in html format.
    '''
    outputText = ''
    try:
        f = open(templateFileName)
        templateText = f.read()
        f.close()
        outputText = templateText
    except Exception, e:
        outputText = 'Cannot read template file "%s".' % (templateFileName)
    
    print 'Content-type: text/html\r\n\r\n',
    print outputText

def main():
    printPageAsHTML('index.html')

if __name__ == '__main__':
    main()
