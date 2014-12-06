'''
By: Ben Weiss, Justin Lim, Anmol Raina

This file reads in an nba csv file and sanitizes it so we can
use it for our web app
'''
import sys

def createNewCSV(file):
    '''
    Creates a new csv file from a text file copied from our source website
    '''
    csvFile = open(file)
    listOfLines = csvFile.readlines()
    stringLines = ""
    
    # Cycle through each line of csv file and make changes
    # when appropriate
    for line in listOfLines:
        splitString = line.split(",")

        # If line begins with "Rk", delete the line from the file
        if splitString[0] == "Rk":
            continue
        else:
            # Delete all unused statistics in list
            splitString.pop(26)
            splitString.pop(21)
            splitString.pop(20)
            splitString.pop(18)
            splitString.pop(17)
            splitString.pop(16)
            splitString.pop(15)
            splitString.pop(14)
            splitString.pop(12)
            splitString.pop(11)
            splitString.pop(9)
            splitString.pop(8)
            splitString.pop(6)
            splitString.pop(5)
            splitString.pop(0)
        
        # Now make new comma delimted string with data to import into 
        # a new text file
        i = 0
        for item in splitString:
            if (len(splitString) - 1) == i:
                stringLines += item 
                i += 1
            else:
                stringLines += item + ","
                i += 1
    
    return stringLines

def printCSV(listOfLines):
    '''
    Print out the csv to standard output
    '''
    # Cycle through lines and print to output
    for row in listOfLines:
        for column in row:
            sys.stdout.write(column)
    print
    
def main():
    inputtedFile = sys.argv[1]
    listOfLines = createNewCSV(inputtedFile)
    printCSV(listOfLines)

main()
