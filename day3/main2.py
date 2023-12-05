from functools import reduce
from typing import Dict, Tuple, Set
from collections import defaultdict

with open('input.txt', 'r') as input:
    schematic = [list(line.strip()) for line in input]

m = len(schematic)
n = len(schematic[0])
gearsNumbers: Dict[Tuple[int, int], Set[int]] = defaultdict(set)
sum = 0


def findAdjacentGear(y: int, x1: int, x2: int) -> Tuple[int, int] | None:
    def isGear(s: str) -> bool: return s == '*'

    if y > 0:
        for j in range(x1, x2 + 1):
            if isGear(schematic[y - 1][j]):
                return (y -1, j)

    if y < m - 1:
        for j in range(x1, x2 + 1):
            if isGear(schematic[y + 1][j]):
                return (y + 1, j)

    if (x1 > 0 and isGear(schematic[y][x1 - 1])): return (y, x1 - 1)
    if (x2 < n - 1 and isGear(schematic[y][x2 + 1])): return (y, x2 + 1)
    if (y > 0 and x1 > 0 and isGear(schematic[y - 1][x1 - 1])): return (y - 1, x1 - 1)
    if (y > 0 and x2 < n - 1 and isGear(schematic[y - 1][x2 + 1])): return (y - 1, x2 + 1)
    if (y < m - 1 and x2 < n - 1 and isGear(schematic[y + 1][x2 + 1])): return (y + 1, x2 + 1)
    if (y < m - 1 and x1 > 0 and isGear(schematic[y + 1][x1 - 1])): return (y + 1, x1 - 1)

    return None


def findOtherNumber(gearPosition: Tuple[int, int], num1x1: int, num1x2: int) -> int | None:
    y, x = gearPosition

    for row in range(y - 1, y + 2):
        for col in range(x - 1, x + 2):
            if row == y and col == x: continue
            if row < 0 or row >= m or col < 0 or col >= n: continue

            cell = schematic[row][col]
            if cell.isdigit():
                num2x1 = col
                num2x2 = col
                while num2x1 > 0 and schematic[row][num2x1 - 1].isdigit(): num2x1 -= 1
                while num2x2 < n - 1 and schematic[row][num2x2 + 1].isdigit(): num2x2 += 1

                if num2x1 == num1x1 and num2x2 == num1x2:
                    return reduce(lambda acc, val: 10 * acc + val, [int(schematic[row][j]) for j in range(num2x1, num2x2 + 1)], 0)

    return None


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
                number1 = reduce(lambda acc, val: 10 * acc + val, numBuffer, 0)

                x1 = numStart
                x2 = numStart + len(numBuffer) - 1
                gearPosition = findAdjacentGear(row, x1, x2)

                if gearPosition is not None:
                    gearsNumbers[gearPosition].add(number1)

                    number2 = findOtherNumber(gearPosition, x1, x2)
                    if number2 is not None:
                        gearsNumbers[gearPosition].add(number2)

                numBuffer = []
                numStart = -1
            processBuffer = False

for gearPosition, numbers in gearsNumbers.items():
    if len(numbers) == 2:
        sum += numbers.pop() * numbers.pop()

print(sum)
