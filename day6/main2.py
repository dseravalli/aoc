with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    time = int(''.join(input[0].split()[1:]))
    distance = int(''.join(input[1].split()[1:]))
    winnings = []

    winning = 0
    for t in range(1, time):
        d = t * (time - t)
        if d > distance:
            winning += 1

    print(winning)
