import random

#  puzzle = [
        #  [0,0,0,0,0,0],
        #  [0,0,0,0,0,0],
        #  [0,0,0,0,0,0],
        #  [0,0,0,0,0,0],
        #  [0,0,0,0,0,0],
        #  [0,0,1,1,0,0]
#  ]
# this is the starting pos in the game
puzzle = [
        [0,1,0,0,1,1],
        [0,0,1,1,0,0],
        [0,1,1,1,0,1],
        [1,0,1,1,1,1],
        [0,1,1,0,0,0],
        [0,0,0,1,0,0]
]
# x axis goes down from top
# y axis goes right from left

BOARD_EXTENT = 6

clickedSquaresBitmask = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
]

def customPrint(puzzle):
    count = 0
    for row in puzzle:
        for pos in row:
            if pos == 1:
                count += 1
        print(row)
    print("^Printed puzzle with " + str(count) + " 1s")

def countOnes(puzzle):
    count = 0
    for row in puzzle:
        for pos in row:
            if pos == 1:
                count += 1
    return count

def clickOnLocation(x, y, puzzle):
    toggleSquare(x, y, puzzle)
    toggleSquare(x + 1, y, puzzle)
    toggleSquare(x - 1, y, puzzle)
    toggleSquare(x, y + 1, puzzle)
    toggleSquare(x, y - 1, puzzle)

def toggleSquare(x, y, puzzle):
    if 0 <= x < len(puzzle) and 0 <= y < len(puzzle[x]):
        puzzle[x][y] = invert(puzzle[x][y])
    #  else:
        #  print("x: " + str(x) + " y: " + str(y) + " out of range")

def invert(i):
    if i == 0:
        return 1
    return 0


customPrint(puzzle)

# click a random square on the board
lowestOnes = BOARD_EXTENT * BOARD_EXTENT
maxOnes = lowestOnes

for i in range(0, 10000000):
    x = random.randint(0, BOARD_EXTENT - 1)
    y = random.randint(0, BOARD_EXTENT - 1)
    #  print("clicking " + str(x) + ", " + str(y))
    #  if clickedSquaresBitmask[x][y] == 1:
        #  continue
    clickOnLocation(x, y, puzzle)
    toggleSquare(x, y, clickedSquaresBitmask)

    currentOnes = countOnes(puzzle)
    if currentOnes > maxOnes:
        clickOnLocation(x, y, puzzle)
        toggleSquare(x, y, clickedSquaresBitmask)
        continue

    if currentOnes < lowestOnes:
        customPrint(puzzle)
        customPrint(clickedSquaresBitmask)
        lowestOnes = currentOnes
        #  maxOnes = lowestOnes + 6 # got me to a 1 solution after a couple mins
        maxOnes = lowestOnes + 4 # got me to a FULL solution in like 10 seconds
        if currentOnes == 0:
            break







