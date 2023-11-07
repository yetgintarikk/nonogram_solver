import config

EMPTY  = '-'
FILLED = '0'
CROSS  = 'X'


def isFinished(puzzle):
    for i in range(config.PUZZLESIZE):
        for j in range(config.PUZZLESIZE):
            if(puzzle[i][j] == ' ' or puzzle[i][j] == EMPTY):
                return False
    return True

def printLists(list):
    for i in list:
        print(i, end=" ")

def printPuzzle(puzzle):
    for i in range(config.PUZZLESIZE):
        print(end="\t")
        for j in range(config.PUZZLESIZE):
            print(puzzle[i][j] , end="|")
        print()
        print(end="\t")
        for k in range(config.PUZZLESIZE):
            print("--", end="")
        print()

def calculatePossibleEmptySlots(slot, empty, index, possibilitiesList):
    if index == len(slot):
        if empty == 0:
            possibilitiesList.append(slot.copy())
        return
    
    for i in range(empty + 1):
        slot[index] = i
        calculatePossibleEmptySlots(slot, empty - i, index + 1, possibilitiesList)


def calculatePossibleSeries(possibilitiesList, lineValues,serie):
    possibleSeries = []
    
    for i in range( len(possibilitiesList) ):
        tempList = []


        for j in range( len(lineValues) ):
            for k in range (possibilitiesList[i][j]):
                tempList.append(CROSS)
            for k in range (lineValues[j]):
                tempList.append(FILLED)
            tempList.append(CROSS)
        tempList.pop()
        for j in range(possibilitiesList[i][-1]):
            tempList.append(CROSS)

        if (isFit( serie, tempList)):
            possibleSeries.append(tempList)
    return possibleSeries

def pickColumn(arr,columnnumber):
    column = [satir[columnnumber] for satir in arr]
    return column

def isFit(serie, controlSerie):
    
    for i in range(config.PUZZLESIZE):
        if((serie[i] == FILLED and controlSerie[i] == CROSS) or (serie[i] == CROSS and controlSerie[i] == FILLED) ):
            return False
    return True


def finalSerie(possibleSeries):
    temp = possibleSeries[0]
    
    for i in range(config.PUZZLESIZE):
        for j in range(1, len(possibleSeries) ):
            if(temp[i] != possibleSeries[j][i]):
                temp[i] = EMPTY
                break
    
    return temp

