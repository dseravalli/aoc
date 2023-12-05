from functools import reduce

with open('input.txt', 'r') as input:
    schematic = [list(line.strip()) for line in input]

m = len(schematic)
n = len(schematic[0])
sum = 0

def isSymbol(s: str) -> bool: return not s.isdigit() and s != '.'

def symbolAdjacent(y: int, x1: int, x2: int) -> bool:
    if y > 0:
        for j in range(x1, x2 + 1):
            if isSymbol(schematic[y - 1][j]):
                return True

    if y < m - 1:
        for j in range(x1, x2 + 1):
            if isSymbol(schematic[y + 1][j]):
                return True

    if (
        x1 > 0 and isSymbol(schematic[y][x1 - 1])
        or x2 < n - 1 and isSymbol(schematic[y][x2 + 1])
        or y > 0 and x1 > 0 and isSymbol(schematic[y - 1][x1 - 1])
        or y > 0 and x2 < n - 1 and isSymbol(schematic[y - 1][x2 + 1])
        or y < m - 1 and x2 < n - 1 and isSymbol(schematic[y + 1][x2 + 1])
        or y < m - 1 and x1 > 0 and isSymbol(schematic[y + 1][x1 - 1])
    ):
        return True

    return False


for row in range(m):
    numBuffer = []
    numStart = -1
    processBuffer = False

    for col in range(n):
        cell = schematic[row][col]

        if cell.isdigit():
            numBuffer.append(int(cell))
            if numStart == -1: numStart = col
        else:
            processBuffer = True

        if col == n - 1 or processBuffer:
            if len(numBuffer) > 0:
                number = reduce(lambda acc, val: 10 * acc + val, numBuffer, 0)

                if symbolAdjacent(row, numStart, numStart + len(numBuffer) - 1):
                    sum += number

                numBuffer = []
                numStart = -1
            processBuffer = False

print(sum)
