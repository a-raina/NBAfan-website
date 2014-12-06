#!/usr/bin/python
''' showsource.py taken directly from
    Jeff Ondich
    
    Used by: Ben Weiss, Justin Lim, Anmol Raina

    For all my web application samples, I want you to be able to execute
    the server-side code and to view its source. I was using an awkward
    system for providing access to the source code, so I'm going to try
    this simpler idea. We'll see if it's any easier to use.
'''

import cgi

def printFileAsPlainText(fileName):
    ''' Prints to standard output the contents of the specified file, preceded
        by a "Content-type: text/plain" HTTP header.
    '''
    text = ''
    try:
        f = open(fileName)
        text = f.read()
        f.close()
    except Exception, e:
        pass

    print 'Content-type: text/plain\r\n\r\n',
    print text

if __name__ == '__main__':
    # Not going to allow people to view just anything.
    allowedFiles = (
        'showsource.py',
        'template.html',
        'tinywebapp.py',
        'webapp.py',
        'webapp.html',
        'index.py',
        'index.html',
        'stats.py',
        'stats.html',
        'datasource.py',
        'ajax-sample.py',
        'jqplot-sample.py',
        'json-sample.py',
        'cookies.py',
    )

    # Really. Don't trust the user.
    form = cgi.FieldStorage()
    sourceFileName = 'showsource.py'
    if 'source' in form:
        sourceFileName = form['source'].value
    if sourceFileName not in allowedFiles:
        sourceFileName = 'showsource.py'

    # Print the file in question.
    printFileAsPlainText(sourceFileName)


