import re
from typing import Tuple, List, Set, Dict
from collections import defaultdict

with open('input.txt', 'r') as input:
    cards: List[Tuple[Set[str], Set[str]]] = [
        (
            set(re.split(r'\s+', part[0].strip())),
            set(re.split(r'\s+', part[1].strip())),
        )
        for line in input
        for part in [line.split(':')[1].split('|')]
    ]

copies: Dict[int, int] = defaultdict(lambda: 1)

for i, (card, answers) in enumerate(cards):
    matchCount = len(card & answers)
    copies[i]
    for cardToCopy in range(i + 1, i + 1 + matchCount):
        copies[cardToCopy] += copies[i]

print(sum(copies.values()))
