import re
input = open('input.txt', 'r')
sum = 0

for line in input:
    parts = line.split(':')[1].split('|')
    card = re.split(r'\s+', parts[0].strip())
    answers = re.split(r'\s+', parts[1].strip())
    cardSum = 0

    for number in card:
        if number in answers:
            if cardSum == 0:
                cardSum = 1
            else:
                cardSum = cardSum * 2

    sum += cardSum

print(sum)
