'''
This is our Database Interface for CS 257. It contains a variety
of methods that help a user access an NBA database organized by players

By Ben Weiss, Justin Lim, and Anmom Raina
'''

import cgi
import psycopg2

class DataSource:
    '''	This class creates an object associated with all player data 
    from one year in the NBA.'''

    def __init__(self):
        pass

    def _getConnection(self):
        connection = None
        # Login to the database
        try:
            connection = psycopg2.connect(database='weissb', user='weissb', password='winter582tree')
            return connection
        # Otherwise print out error message
        except Exception, e:
            print 'Connection error: ', e
            return connection

    def getPlayerByNameAndYear(self, player, year):
        '''Search data table for player's name and return player's stats. This method takes a player name and year in the
        form of a string and returns a list.'''
        # Make new variable associated with an empty cursor
        connection = self._getConnection()
        cursorList = []
        # Try to initiate and start a query 
        try:
            cursor = connection.cursor();
            query = 'SELECT * FROM nba{year} WHERE UPPER(player) LIKE UPPER(\'%{player}%\')'.format(year = year, player = player)
            cursor.execute(query)

        # Otherwise print out error message
        except Exception, e:
            print 'Cursor error', e
        
        for row in cursor:
            cursorList.append(row)

        connection.close()
        return cursorList

    def getAllYear(self, year):
        '''Search data for age and return list of players who have
        same age. This method takes a year in the form of a string and returns a list.'''
    
        # Make new variable associated with an empty cursor
        connection = self._getConnection()
        cursorList = []
        # Try to initiate and start a query 
        try:
            cursor = connection.cursor();
            query = 'SELECT * FROM nba{year}'.format(year = year)
            cursor.execute(query)
            # Otherwise print out error message
        except Exception, e:
            print 'Cursor error', e
    
        for row in cursor:
            cursorList.append(row)
    
        connection.close()
        return cursorList

    def getPlayerByName(self, player):
        '''Search data for age and return list of players who have
        same age, taking in the parameter player which is entered as a string.'''
    
        # Make new variable associated with an empty cursor
        connection = self._getConnection()
        cursorList = []

        # Try to initiate and start a query 
        for i in range(2000,2015):
            try:
                year = str(i)
                cursor = connection.cursor();
                query = 'SELECT * FROM nba{year} WHERE UPPER(player) LIKE UPPER(\'%{player}%\')'.format(year = year, player = player)
                cursor.execute(query)
                
            # Otherwise print out error message
            except Exception, e:
                print 'Cursor error', e
    
            for row in cursor:
                cursorList.append(row)
        connection.close()
        return cursorList
    
    def getPlayersByTeam(self, team, year):
        '''Search data for team and return list of players who have same 
        team, taking in team and year as a string.'''
        
        # Make new variable associated with an empty cursor
        connection = self._getConnection()
        cursorList = []

        # Try to initiate and start a query 
        try:
            cursor = connection.cursor();
            query = 'SELECT * FROM nba{year} WHERE team = \'{team}\''.format(year = year, team = team)
            cursor.execute(query)
                
        # Otherwise print out error message
        except Exception, e:
            print 'Cursor error', e
    
        for row in cursor:
            cursorList.append(row)
        
        connection.close()
        return cursorList
    
    def sortBy(self, sortVariable, year, order):
        '''Sort table by sortVariable which could be any of the specifed
        stats indicated in our mockup (3P%, FG%, FT%, APG, RPG, PPG, SPG,
        BPG, Minutes Played). sortVariable, year and order are all entered
        in as strings'''
        # Make new variable associated with an empty cursor
        connection = self._getConnection()
        cursorList = []
        
        # Try to initiate and start a query 
        try:
            cursor = connection.cursor();
            query = 'SELECT player,position,age, MAX({stat}) as {stat} FROM nba{year} GROUP BY player,position,age ORDER BY {stat} {order}'.format(stat = sortVariable, year = year, order = order)
            cursor.execute(query)

        # Otherwise print out error message
        except Exception, e:
            print 'Cursor error', e                                                                                                                            
        
        for row in cursor:
            cursorList.append(row)

        connection.close()
        return cursorList
    
def main():
    database = DataSource()
    cursorList = database.sortBy("pointspg", "2013", "ASC")
    print cursorList

if __name__=='__main__':
    main()
