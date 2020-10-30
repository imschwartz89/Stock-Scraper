import requests
import csv
import argparse
import os.path

##############################
# Author: Ian Schwartz
# Created: 7/14/2020
# Last Update: 10/30/2020
##############################

# returns the data for the given ticker from google
def getTicker(ticker):
    r = requests.get("https://google.com/search?q=" + ticker)
    #r = requests.get("https://www.google.com/search?client=firefox-b-1-e&q=" + ticker, stream=True)
    data = r.text
    return data

# returns the price of the ticker stock, using data given
## CURRENTLY USES SOMETHING THAT CHANGES, CURRENTLY WORKS RN
def getPrice(data, gibberish, ticker):
    #gibberish = "BNeawe iBp4i AP7Wnd" # THIS CHANGES!
    index = data.find(gibberish)
    if index == -1:
        print("WARNING 1001 - Stock (" + ticker + ") value not found. Using 0 for price..."
                + "\nIf this occurs for multiple stocks, there is a problem with the gibberish.\n")
        return 0
    shrunkData = data[index:index+100]
    index1 = shrunkData.find("\"><div><div class=\"" + gibberish + "\">")
    index2 = shrunkData.find(" <span")
    shrunkData = shrunkData[index1:index2]
    price = float(shrunkData[shrunkData.find(gibberish + "\">")+len(gibberish)+2:].replace(",", ""))
    return price

# returns list of lists, brings in data from csv file and stores data into list of lists
def getInfoCSV(filename):
    dataList = []
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            dataList.append(row)
    return dataList

# write price back to csv
def writeToCSV(filename, data):
    with open(filename, "w+", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for i in range(len(data)):
            writer.writerow(data[i])

# loop thru each in csv data get price
def getAllPrices(data):
    #updateData = data # shares same memory address
    updateData = [] # new memory location
    for i in range(len(data)):
        if data[i][0] != "Ticker":
            tickerData = getTicker(data[i][0])
            tickerPrice = getPrice(tickerData, data[0][-1], data[i][0])
            #updateData[i][2] = tickerPrice # when same memory address
            updateData.append([data[i][0], data[i][1], tickerPrice])
        else:
            updateData.append(data[i])
    return updateData

# prints all of the stocks nicely
def printAll(data):
    print("=============================")
    print("Stock |      Total Value")
    print("=============================")
    grandTotal = 0
    for i in range(len(data)):
        if data[i][0] != "Ticker":
            total = round(float(data[i][1]) * float(data[i][2]), 2)
            grandTotal += total
            print(f"{data[i][0]:5} | $" + f"{total:20,.2f}")

    print("=============================")
    print("Total | $" + f"{grandTotal:20,.2f}")
    print("=============================")

# method to print with change from last time
## NOTE: will only work if stock order has not changed and there is no new stocks
def printAllChange(lastData, newData):
    print("=================================================")
    print("Stock |      Total Value      |     Change")
    print("=================================================")
    grandTotal = 0
    lastGrandTotal = 0
    for i in range(len(newData)):
        if newData[i][0] != "Ticker":
            lastTotal = round(float(lastData[i][1]) * float(lastData[i][2]), 2)
            total = round(float(newData[i][1]) * float(newData[i][2]), 2)
            change = total - lastTotal
            lastGrandTotal += lastTotal
            grandTotal += total
            print(f"{newData[i][0]:5} | $" + f"{total:20,.2f} | " + f"{change:17,.2f}")

    totalChange = grandTotal - lastGrandTotal
    print("=================================================")
    print("Total | $" + f"{grandTotal:20,.2f} | " + f"{totalChange:17,.2f}")
    print("=================================================")

#prints all with change and sign
## NOTE: will only work if stock order has not changed and there is no new stocks
def printAllChangeSign(lastData, newData):
    print("=================================================")
    print("Stock |      Total Value      |     Change")
    print("=================================================")
    grandTotal = 0
    lastGrandTotal = 0
    for i in range(len(newData)):
        if newData[i][0] != "Ticker":
            lastTotal = round(float(lastData[i][1]) * float(lastData[i][2]), 2)
            total = round(float(newData[i][1]) * float(newData[i][2]), 2)
            change = total - lastTotal
            lastGrandTotal += lastTotal
            grandTotal += total
            charSign = ""
            if change < 0:
                change *= -1
                charSign = f"-({change:,.2f})"
            else:
                charSign = f"+({change:,.2f})"
            print(f"{newData[i][0]:5} | $" + f"{total:20,.2f} | " + f"{charSign:>17}")

    totalChange = grandTotal - lastGrandTotal
    charSign = ""
    if totalChange < 0:
        totalChange *= -1
        charSign = f"-({totalChange:,.2f})"
    else:
        charSign = f"+({totalChange:,.2f})"
    print("=================================================")
    print("Total | $" + f"{grandTotal:20,.2f} | " + f"{charSign:>17}")
    print("=================================================")

# argparse test function
def commandLineParse():
    parser = argparse.ArgumentParser(description="Determines value of stocks using Google")
    parser.add_argument("-i", "-input", help="input file name, expects CSV file")
    parser.add_argument("-o", "-output", help="output file name, expects CSV file")
    parser.add_argument("-io", help="input and output file name")
    parser.add_argument("-compare", "-comp", nargs="*", help="compares two files, expects CSV files")
    parser.add_argument("-p", "-P", default="", const="AAPL", nargs="?", help="prints the HTML return from requests for given ticker, default is AAPL")
    parser.add_argument("-c", "-C", default="", const="C", nargs="?", help="print with change amount")
    parser.add_argument("-s", "-S", default="", const="S", nargs="?", help="print with change amount and sign")
    parser.add_argument("-v", "-V", "--version", action="version", version="Version: 0.01")
    return parser.parse_args()

#compare the values from two CSV files that are passed as command line arguments under the flag -compare or -comp
def compare2CSV(args):
    if len(args.compare) != 2:
        print("ERROR 1003 - Not enough arguments passed to -compare\nExiting...")
        exit()
    else:
        if not os.path.isfile(args.compare[0]) or not os.path.isfile(args.compare[1]):
            print("ERROR 1004 - Files for -compare do not exist\nExiting...")
            exit()
        else:
            info0 = getInfoCSV(args.compare[0])
            info1 = getInfoCSV(args.compare[1])
            choosePrint(args, info0, info1)

#check if p flag is used
def checkPFlag(args):
    if args.p != "":
        dataHTML = getTicker(args.p)
        if args.o != None:
            with open(args.o, "w") as file:
                file.write(dataHTML)
                exit() #exit otherwise will create an overwriting of files
        else:
            print(dataHTML)
            exit() #exit is always desired because they did not specify a file

#choose the correct print based on the flags given
# if multiple flags are given it will choose -s, then -c, then none
def choosePrint(args, info, allPrices):
    if args.s != "":
        printAllChangeSign(info, allPrices)
    elif args.c != "":
        printAllChange(info, allPrices)
    else:
        printAll(allPrices)

#handles all of the command line arguments passed and gets all necessary data to make the correct print
# handles:
#   which file to get input from
#   which file to output to
#   which print style to use
#   whether to print the HTML return
#   whether to compare to CSV files
def runAll(args):
    info = []
    allPrices = []
    inFile = ""
    outFile = ""

    #check if compare flag is used
    if args.compare != None:
        compare2CSV(args)
        exit()

    #check if p flag is used
    checkPFlag(args)

    #check if input or input/output flag has a value
    if args.i == None and args.io == None:
        print("ERROR 1001 - No file given for -i or -io flag\nExiting...")
        exit()
    else:
        #determine what to set as inFile and outFile (only if writing to file will occur)
        if args.io != None:
            #read/write args.io
            inFile = args.io
            outFile = args.io
        elif args.o == None:
            #read args.i
            inFile = args.i
        else:
            #read args.i, write args.o
            inFile = args.i
            outFile = args.o

    #check that inFile exists
    if not os.path.isfile(inFile):  #args.i):
        print("ERROR 1002 - File does not exist\nExiting...")
        exit()

    #get information from the CSV file and then get all the current prices for each Ticker in the CSV file
    info = getInfoCSV(inFile)
    allPrices = getAllPrices(info)

    #check if writing to file is desired, and write to CSV file if yes
    if outFile != "":
        writeToCSV(outFile, allPrices)

    #choose print
    choosePrint(args, info, allPrices)


######################################################

### MAIN
if __name__ == '__main__':
    runAll(commandLineParse())

######################################################
