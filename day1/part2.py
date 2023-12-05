from typing import List
import re

def findNumbers(line: str) -> List:
    WORDS = enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    line = line.strip()
    matches = {}
    minIndex = len(line)
    maxIndex = 0

    for index, word in WORDS:
        contains = [i for i in range(len(line)) if line.startswith(word, i)]
        if len(contains) > 0:
            for match in contains:
                matches[match] = index + 1
                if match > maxIndex: maxIndex = match
                if match < minIndex: minIndex = match

    for m in re.finditer(r"\d", line):
        idx = m.start()
        matches[idx] = int(m.group(0))
        if idx > maxIndex: maxIndex = idx
        if idx < minIndex: minIndex = idx

    return [matches, minIndex, maxIndex]


input = open('input.txt', 'r')
sum = 0

for line in input:
    matches, minIndex, maxIndex = findNumbers(line)
    number = (matches[minIndex] * 10) + matches[maxIndex]
    sum += number

print(sum)
input.close()
