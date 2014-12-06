'''
By: Ben Weiss, Justin Lim, Anmol Raina

This file produces a variety of html tables to show our data.
'''

def makeTableFromQuery(cursorList):
    '''
    Produces a standard display table in html to show our data with all
    stats provided. Takes in the parameter cursorList as a list
    and returns a string formatted as a table in html.
    '''
    tableString = ""
    # This if/else clause tests to see if the query came up empty
    if not cursorList:
        tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""
    elif cursorList == None:
        tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""
    else:
        tableHeadings = """<div id = "tableHeaderDIV">
                    <table id = "dataTableHeader">
                    <tr = "dataTableHeader">
                    <th>Player</th>
                    <th>Pos</th>
                    <th>Age</th>
                    <th>Team</th>
                    <th>Min</th>
                    <th>FG%%</th>
                    <th>3P%%</th>
                    <th>FT%%</th>
                    <th>RPG</th>
                    <th>APG</th>
                    <th>SPG</th>
                    <th>BPG</th>
                    <th>PFG</th>
                    <th>PPG</th>
                    </tr>
                    </table>
                    </div>"""
        tableString += tableHeadings
    
        # We have a cursor associated with our datasource. Use it to print a table of results.
        tableString += '<div id = "tableDIV">'
        tableString += '<table id = "dataTable">'
        for row in cursorList:          
            for i in row:
                tableString += '<td>%s</td>'%i
            tableString += '<tr>\n</tr>'       
        tableString += "</table>"
        tableString += "</div>"
        return tableString

def makeSmallerTableFromQuery(cursorList, stat):
    '''
    Makes a smaller html display table in html to show data with only
    specified stat selected
    '''
    tableString = ""
    
    # This if/else clause tests to see if the query came up empty
    if not cursorList:
        tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""
    elif cursorList == None:
        tableString = """<p><font color="white">Invalid input or query was not resolved</font></p>"""
    else: 
        tableHeadings = """<div id = "tableHeaderDIV">
                    <table id = "dataTableHeader">
                    <tr = "dataTableHeader">
                    <th>Player</th>
                    <th>Pos</th>
                    <th>Age</th>
                    <th>{stat}</th>
                    </tr>
                    </table>
                    </div>""".format(stat = stat)
    
        tableString += tableHeadings
        # We have a cursor associated with our datasource. Use it to print a table of results.
        tableString += '<div id = "tableDIV">'
        tableString += '<table id = "dataTable">'
        for row in cursorList:          
            for i in row:
                tableString += '<td>%s</td>'%i
            tableString += '<tr>\n</tr>'       
        tableString += "</table>"
        tableString += "</div>"
        return tableString
