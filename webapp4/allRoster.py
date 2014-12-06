#!/usr/bin/python
'''
By: Ben Weiss. Justin Lim. Anmol Raina
This file has been adapted from psycopg2-demo.py
from Jeff Ondich, 7 October 2013

This file implements the all teams function on our web page. 
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
import makeTable
import results
cgitb.enable()

def getCGIParameters():
    '''
    This function grabs the HTTP parameters we care about, sanitizes the
    user input, provides default values for each parameter is no parameters
    is provided by the incoming request, and returns the resulting values
    in a dictionary indexed by the parameter names.
    '''
    form = cgi.FieldStorage()
    parameters = {'team':'','year':''}
    if 'team' in form:
        parameters['team'] = form['team'].value
    if 'year' in form:
        parameters['year'] = form['year'].value
    return parameters
    
def sqlQueryGetTeam(team, year):
    '''
    This function grabs a new cursor with a query regarding one team, one year both
    entered as strings and returns the cursorList returned by the query. 
    '''
    # Make a new database and cursor list 
    database = DataSource()
    cursorList = database.getPlayersByTeam(team, year)
    return cursorList

def printPageAsHTML(team, year, templateFileName):
    '''
    This function prints out a main template of our web page in html format, taking
    in team and year as strings, and templateFileName as a file.
    '''
    tableString = ""
    # This if/else clause tests to see if the year the user entered is valid 
    if team and year:
        if results.testYearInput(year):
            sqlList = sqlQueryGetTeam(team, year)
            tableString = makeTable.makeTableFromQuery(sqlList)
        else:
            tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""

    # Once error catching is done, print out the html to standard output 
    outputText = ''
    try:
        f = open(templateFileName)
        templateText = f.read()
        f.close()
        outputText = templateText % (tableString)
    except Exception, e:
        outputText = 'Cannot read template file "%s".' % (templateFileName)
    print 'Content-type: text/html\r\n\r\n',
    print outputText

def main():
    parameters = getCGIParameters()
    printPageAsHTML(parameters['team'], parameters['year'], 'allRoster.html')

if __name__ == '__main__':
    main()
