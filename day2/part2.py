import re

input = open('input.txt', 'r')
sum = 0

for i, line in enumerate(input):
    minRed = 0
    minGreen = 0
    minBlue = 0

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
                        minRed = max(minRed, count)
                    case 'green':
                        minGreen = max(minGreen, count)
                    case 'blue':
                        minBlue = max(minBlue, count)

    sum += (minRed * minGreen * minBlue)

print(sum)
input.close()
