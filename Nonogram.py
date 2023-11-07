from SolveFunctions import *

yukaridanAsagiya = []
soldanSaga = []

config.PUZZLESIZE = int(input("Puzzle Boyutunu girin : "))

PUZZLE = [[' '] * config.PUZZLESIZE for _ in range(config.PUZZLESIZE)]

print("Yukaridan asagiya dogru doldurma degerlerini girin. (EX: 2,1,2) ")

for i in range(config.PUZZLESIZE):
    girdi = input(f"{i+1}. satiri girin : ")
    
    girdi_listesi = [int(x) for x in girdi.split(",")]
    
    # Girdi listesini ana liste içine ekle
    yukaridanAsagiya.append(girdi_listesi)

print("Soldan saga dogru doldurma degerlerini girin. (EX: 2,1,2) ")

for i in range(config.PUZZLESIZE):
    girdi = input(f"{i+1}. sutunu girin : ")
    
    girdi_listesi = [int(x) for x in girdi.split(",")]
    
    # Girdi listesini ana liste içine ekle
    soldanSaga.append(girdi_listesi)


possibilitiesList = []

while (not isFinished(PUZZLE)):
    for i in range(len(yukaridanAsagiya)):

        slot = [None] * (len(yukaridanAsagiya[i]) + 1)
        empty = 0
        for j in yukaridanAsagiya[i]:
            empty += j
        empty += len(yukaridanAsagiya[i]) - 1
        empty = config.PUZZLESIZE - empty

        calculatePossibleEmptySlots(slot,empty, 0, possibilitiesList)
        
        possibleSeries = calculatePossibleSeries(possibilitiesList, yukaridanAsagiya[i], PUZZLE[i])

        PUZZLE[i] = finalSerie(possibleSeries)

        possibilitiesList.clear()
        possibleSeries.clear()

        #input()
        #print("Yatay:" , i+1)
        #printPuzzle(PUZZLE)
    

    #print("----------------------\n\n")


    for i in range(len(soldanSaga)):

        slot = [None] * (len(soldanSaga[i]) + 1)
        empty = 0
        for j in soldanSaga[i]:
            empty += j
        empty += len(soldanSaga[i]) - 1
        empty = config.PUZZLESIZE - empty

        calculatePossibleEmptySlots(slot,empty, 0, possibilitiesList)

        possibleSeries = calculatePossibleSeries(possibilitiesList, soldanSaga[i], pickColumn(PUZZLE,i))

        fin = finalSerie(possibleSeries)

        for j in range(config.PUZZLESIZE):
            PUZZLE[j][i] = fin[j]

        possibilitiesList.clear()

        #input()
        #print("Dikey:" , i+1)
        #printPuzzle(PUZZLE)


print("\n\n\n\t" ,end="")
for i in range(config.PUZZLESIZE - 2):
    print("-",end="")
print("DONE", end="")
for i in range(config.PUZZLESIZE - 2):
    print("-",end="")
print()
printPuzzle(PUZZLE)

input("\nKapatmak icin bir tusa basin.")