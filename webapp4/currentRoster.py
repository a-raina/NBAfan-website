#!/usr/bin/python
'''
By: Ben Weiss. Justin Lim. Anmol Raina
This file has been adapted from psycopg2-demo.py
from Jeff Ondich, 7 October 2013

    This script outputs the roster at the end of the 2013 season for the team logo that 
    the user clicks on.
'''
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
    is provided by the incoming request, and returns the resulting values.
    '''
    form = cgi.FieldStorage()
    parameters = {'team':''}
    if 'team' in form:
        parameters['team'] = form['team'].value
    return parameters
    
def sqlQueryGetTeam(team, year):
    '''
    This function grabs a new cursor list associated with one team and then returns this 
    cursor list to parent function, taking in team and year as strings.
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
    # Check for errors. If the sqlList is empty return an error message.
    if team and year:
        sqlList = sqlQueryGetTeam(team, year)
        tableString = makeTable.makeTableFromQuery(sqlList)
    
    # Print html template along with inserted table to standard output 
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
    printPageAsHTML(parameters['team'],'2014' , 'currentRoster.html')

if __name__ == '__main__':
    main()
