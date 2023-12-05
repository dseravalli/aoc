import re

redMax = 12
greenMax = 13
blueMax = 14

input = open('input.txt', 'r')
sum = 0

for i, line in enumerate(input):
    gameNumber = i + 1
    possible = True

    selections = line.strip().split(':')[1].split(';')

    for selection in selections:
        colorSums = selection.strip().split(',')

        for colorSum in colorSums:
            m = re.match(r"(\d+) (\w+)", colorSum.strip())

            if m is not None:
                count = int(m.group(1))
                color = m.group(2)

                match color:
                    case 'red':
                        if count > redMax:
                            possible = False
                    case 'green':
                        if count > greenMax:
                            possible = False
                    case 'blue':
                        if count > blueMax:
                            possible = False
    if possible:
        sum += gameNumber

print(sum)
input.close()
