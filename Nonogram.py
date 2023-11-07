from SolveFunctions import *

up_to_down = []
left_to_right = []

config.PUZZLESIZE = int(input("Enter Puzzle Size : ")) # "Puzzle Boyutunu girin"

PUZZLE = [[' '] * config.PUZZLESIZE for _ in range(config.PUZZLESIZE)]

print("Enter rows from up to down (EX: 2,1,2) ") # "Yukaridan asagiya dogru doldurma degerlerini girin."

for i in range(config.PUZZLESIZE):
    input_val = input(f"{i+1}. row : ")
    
    input_list = [int(x) for x in input_val.split(",")]
    
    # Girdi listesini ana liste içine ekle
    up_to_down.append(input_list)

print("Enter columns from left to right. (EX: 2,1,2) ")

for i in range(config.PUZZLESIZE):
    input_val = input(f"{i+1}. column : ")
    
    input_list = [int(x) for x in input_val.split(",")]
    
    # Girdi listesini ana liste içine ekle
    left_to_right.append(input_list)


possibilitiesList = []

while (not isFinished(PUZZLE)):
    for i in range(len(up_to_down)):

        slot = [None] * (len(up_to_down[i]) + 1)
        empty = 0
        for j in up_to_down[i]:
            empty += j
        empty += len(up_to_down[i]) - 1
        empty = config.PUZZLESIZE - empty

        calculatePossibleEmptySlots(slot,empty, 0, possibilitiesList)
        
        possibleSeries = calculatePossibleSeries(possibilitiesList, up_to_down[i], PUZZLE[i])

        PUZZLE[i] = finalSerie(possibleSeries)

        possibilitiesList.clear()
        possibleSeries.clear()

    for i in range(len(left_to_right)):

        slot = [None] * (len(left_to_right[i]) + 1)
        empty = 0
        for j in left_to_right[i]:
            empty += j
        empty += len(left_to_right[i]) - 1
        empty = config.PUZZLESIZE - empty

        calculatePossibleEmptySlots(slot,empty, 0, possibilitiesList)

        possibleSeries = calculatePossibleSeries(possibilitiesList, left_to_right[i], pickColumn(PUZZLE,i))

        fin = finalSerie(possibleSeries)

        for j in range(config.PUZZLESIZE):
            PUZZLE[j][i] = fin[j]

        possibilitiesList.clear()


print("\n\n\n\t" ,end="")
for i in range(config.PUZZLESIZE - 2):
    print("-",end="")
print("DONE", end="")
for i in range(config.PUZZLESIZE - 2):
    print("-",end="")
print()
printPuzzle(PUZZLE)

input("\nPress any key to exit.")