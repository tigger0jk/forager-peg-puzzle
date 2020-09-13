puzzle = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,1,0,0]
]
# x axis goes down from top
# y axis goes right from left

def customPrint(puzzle):
    count = 0
    for row in puzzle:
        for pos in row:
            if pos == 1:
                count += 1
        print(row)
    print("^Printed puzzle with " + str(count) + " 1s")

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

clickOnLocation(5, 2, puzzle)

customPrint(puzzle)

# state:
# current puzzle board
# clickedSquares
# running total of 1s?

# keep a "clickedSquares" array, never click the same space twice
# look at all 36 positions
