# Advent of Code 2025 - Day 4, Part 2

file_name = r'C:\Users\Ediku\Escritorio\MISC\CS Programming\Personal Projects\Github\SimpleCaci\advent-of-code-2025\day 4\input.txt'

with open(file_name) as f:
    grid = [list(line.strip()) for line in f]

rowSize = len(grid)
colSize = len(grid[0])

# Padding
newGrid = [['.' for _ in range(colSize+2)] for _ in range(rowSize+2)]
for r in range(rowSize):
    for c in range(colSize):
        newGrid[r+1][c+1] = grid[r][c]


def countOccupiedRoll(grid, row, col):
    occupiedCount = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    for dr, dc in directions:
        r = row + dr
        c = col + dc

        # only check immediate neighbors
        if grid[r][c] == '@':
            occupiedCount += 1

    return occupiedCount


moveable = 0

# must iterate in padded coordinates
for r in range(1, rowSize+1):
    for c in range(1, colSize+1):
        if newGrid[r][c] == '@':  # only rolls matter
            if countOccupiedRoll(newGrid, r, c) < 4:
                moveable += 1

print("Total Moveable Paper:", moveable)
