#!/usr/bin/python
'''
By: Ben Weiss. Justin Lim. Anmol Raina
This file has been adapted from psycopg2-demo.py
from Jeff Ondich, 7 October 2013

    This program gets a stat, year and the display order(ascending or descending)
    as the user input and uses it to output the max in that stat per player. Since
    in our data the max is already saved, we just use a sql query to find the max. 
    Therefore, even if a player has multiple entry we only get the max for that player
    by using group by.
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
     is provided by the incoming request, and returns the resulting values
    '''
    form = cgi.FieldStorage()
    parameters = {'year':'','stat':'', 'order':''}
    if 'stat' in form:
        parameters['stat'] = form['stat'].value
    if 'year' in form:
        parameters['year'] = form['year'].value
    if 'order' in form:
        parameters['order'] = form['order'].value
    return parameters
    
def sqlQuerySortBy(stat, year, order):
    '''
    This function grabs a new cursor with a query regarding one player and prints
    that player's stats in table form. stat, year and order are all strings obtained
    from drop down menus. stat refers to the stat user wants. Each stat is a column 
    in our table. Order can either be ascending or descending.
    '''
    # Make a new database and cursor list 
    database = DataSource()
    cursorList = database.sortBy(stat, year, order)
    return cursorList

def printPageAsHTML(stat, year, order, templateFileName):
    '''
    This function prints out a main template of our web page in html format.
    stat, year, order and templateFileName are all strings obtained from 
    drop down menus. templateFileName is the html file we print to.
    '''
    tableString = ""

    # Error handling. If all appropriate items are in parameters, execute query
    if stat and year and order:
        sqlList = sqlQuerySortBy(stat, year, order)
        tableString = makeTable.makeSmallerTableFromQuery(sqlList, stat)
    
    # Open template file
    outputText = ''
    try:
        f = open(templateFileName)
        templateText = f.read()
        f.close()
        outputText = templateText % (tableString)
    except Exception, e:
        outputText = 'Cannot read template file "%s".' % (templateFileName)
    
    # Print html to standard output
    print 'Content-type: text/html\r\n\r\n',
    print outputText

def main():
    '''
    This is for testing purposes only.
    '''
    parameters = getCGIParameters()
    printPageAsHTML(parameters['stat'], parameters['year'], parameters['order'], 'stats.html')

if __name__ == '__main__':
    main()
