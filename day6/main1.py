import math

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    times = [int(x) for x in input[0].split()[1:]]
    distances = [int(x) for x in input[1].split()[1:]]
    races = list(zip(times, distances))
    winnings = []

    for time, distance in races:
        winning = 0
        for t in range(1, time):
            d = t * (time - t)
            if d > distance:
                winning += 1
        winnings.append(winning)

    print(math.prod(winnings))
