with open('input.txt', 'r') as f:
    input = f.read().split('\n\n')

seeds = [int(i) for i in input[0].split(':')[1].strip().split(' ')]
maps = []
locations = []

for i in range(1, 8):
    mapRow = input[i].split(':')[1].strip().split('\n')
    maps.append([[int(v) for v in row.strip().split(' ')] for row in mapRow])

for seed in seeds:
    location = seed
    for map in maps:
        for row in map:
            dStart, sStart, span = row
            sEnd = sStart + span - 1
            if location >= sStart and location <= sEnd:
                offset = location - sStart
                location = dStart + offset
                break

    locations.append(location)

print(min(locations))
