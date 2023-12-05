import re

input = open('input.txt', 'r')
sum = 0

for line in input:
    arr = list(line)
    first = None
    last = None

    for char in arr:
        if re.match(r"\d", char):
            first = int(char)
            break

    for i in range(1, len(arr) + 1):
        char = arr[-i]
        if re.match(r"\d", char):
            last = int(char)
            break

    if first and last:
        number = (first * 10) + last
        sum += number

input.close()
print(sum)
