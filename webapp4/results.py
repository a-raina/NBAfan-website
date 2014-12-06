#!/usr/bin/python
'''
results.py
By: Ben Weiss. Justin Lim. Anmol Raina
This file has been adapted from psycopg2-demo.py
from Jeff Ondich, 7 October 2013

    This file implements the player/search function on our home page. It returns a table of data
    for an entire year in the NBA, a single player, and an entire player's history of play. It
    also prints out the html to standard output.
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
cgitb.enable()

def getCGIParameters():
    '''
    This function grabs the HTTP parameters we care about, sanitizes the
     user input, provides default values for each parameter is no parameter
     is provided by the incoming request, and returns the resulting values
     in a dictionary indexed by the parameter names.
    '''
    form = cgi.FieldStorage()
    parameters = {'player':'', 'year':''}
    if 'player' in form:
        parameters['player'] = sanitizeUserInput(form['player'].value)
    if 'year' in form:
        parameters['year'] = sanitizeUserInput(form['year'].value)
    return parameters
    
def sanitizeUserInput(s):
    '''
    A simple function taken from Jeff Ondich to sanitize user input and prevent users from
    doing EVIL STUFF. s is a string which the user enters.
    '''
    charsToRemove = ';,\\/:\'"<>@'
    for ch in charsToRemove:
        s = s.replace(ch, '')
    return s

def sqlPlayerYearQuery(player, year):
    '''
    This function grabs a new resulting cursorList from a query regarding one player 
    and one year. Player and year are both strings.
    '''
    # Make a new database and cursor list 
    database = DataSource()
    cursorList = database.getPlayerByNameAndYear(player, year)
    return cursorList

def sqlYearQuery(year):
    '''
    This function grabs all data for one year, returning a list containing
    all information. Year is a string and refers to a nba season.
    '''
    # Make a new database and cursor List
    database = DataSource()
    cursorList = database.getAllYear(year)
    return cursorList

def sqlPlayerQuery(player):
    '''
    This function grabs all data for one player, returning a list containing
    all information. Player is a string and refers to the name of the player.
    '''
    # Make a new database and cursor List
    database = DataSource()
    cursorList = database.getPlayerByName(player)
    return cursorList
    
def printPageAsHTML(player, year, templateFileName):
    '''
    This function prints out a main template of our web page in html format. It also
    decides based on user input what type of search to run: get all players in one 
    year, get one specific player, or get the stats for one player over his entire career.
    The parameters are all strings. Player refers to the column for player name, year refers 
    to the nba year and templatheFileName is the html file we are printing to.
    '''
    tableString = ""
    outputText = ""
    # If player and year were entered, get one specific player
    if player and year:
        if testYearInput(year):
            sqlList = sqlPlayerYearQuery(player, year)
            tableString = makeTable.makeTableFromQuery(sqlList)
            if tableString is None:
                tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""

        else:
            tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""
    
    # Otherwise if only year was entered, get all player data for that year
    elif year != "":
        if testYearInput(year):
            sqlList = sqlYearQuery(year)
            tableString = makeTable.makeTableFromQuery(sqlList)
            if tableString is None:
                tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""
        else:
            tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""
    
    # If user only entered player, get all data concerning the player
    elif player != "":
        sqlList = sqlPlayerQuery(player)
        tableString = makeTable.makeTableFromQuery(sqlList)
        if tableString is None:
                tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""

# Open template file ("results.html")
    try:
        f = open(templateFileName)
        templateText = f.read()
        f.close()
        outputText += templateText % (tableString)
    except Exception, e:
        outputText = 'Cannot read template file "%s".' % (templateFileName)
    
    # Print out html to standard output
    print 'Content-type: text/html\r\n\r\n',
    print outputText

def testYearInput(year):
    '''
    Short function for error handling. Specifically, to see
    if user entered an integer between 2000 and 2014. year
    is  a string
    '''
    try: 
        integer = int(year)
        if integer in range(2000, 2015):
            return True
    except Exception, e:
        return False

def main():
    '''
    This is for testing purposes.
    '''
    parameters = getCGIParameters()
    printPageAsHTML(parameters['player'], parameters['year'], 'results.html')

if __name__ == '__main__':
    main()
